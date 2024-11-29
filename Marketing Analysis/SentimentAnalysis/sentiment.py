import warnings
import pandas as pd
import pyodbc
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer (VADER)
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment score using VADER
def calculate_sentiment(review_text: str) -> float:
    """
    Calculates the sentiment score of a review text using VADER sentiment analysis.
    Args:
        review_text (str): The review text.
    Returns:
        float: Sentiment score of the review.
    """
    return sia.polarity_scores(review_text)['compound']

# Function to categorize sentiment based on sentiment score and rating
def categorize_sentiment(sentiment_score: float, rating: int) -> str:
    """
    Categorizes sentiment based on sentiment score and rating.
    Args:
        sentiment_score (float): The sentiment score of the review.
        rating (int): The rating given by the customer (1 to 5).
    Returns:
        str: Sentiment category ('Positive', 'Neutral', 'Negative').
    """
    if sentiment_score > 0.05 or rating >= 4:
        return 'Positive'
    elif sentiment_score < -0.05 or rating <= 2:
        return 'Negative'
    else:
        return 'Neutral'

# Function to bucket sentiment scores into defined ranges
def sentiment_bucket(sentiment_score: float) -> str:
    """
    Buckets sentiment scores into defined ranges.
    Args:
        sentiment_score (float): The sentiment score of the review.
    Returns:
        str: Sentiment bucket ('Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive').
    """
    if sentiment_score <= -0.6:
        return 'Very Negative'
    elif sentiment_score <= -0.2:
        return 'Negative'
    elif sentiment_score <= 0.2:
        return 'Neutral'
    elif sentiment_score <= 0.6:
        return 'Positive'
    else:
        return 'Very Positive'

def get_sql_data() -> pd.DataFrame:
    """
    Connects to SQL Server and retrieves customer reviews data from the database.
    
    Returns:
        DataFrame: A Pandas DataFrame containing ReviewText and Rating.
    """
    # Suppress warnings
    warnings.filterwarnings("ignore")

    # Database connection
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'Server=;'
        'Database=;'
        'Trusted_Connection=yes;'
    )

    query = """
    SELECT 
    ReviewID, CustomerID, ProductID, ReviewDate, Rating, 
    REPLACE(ReviewText, '  ', ' ') AS ReviewText 
    FROM 
    dbo.customer_reviews
    """

    # Fetch data into DataFrame
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df

def analyze_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes sentiment of reviews using VADER and assigns sentiment categories and buckets.
    
    Args:
        df (DataFrame): The DataFrame containing customer reviews.
        
    Returns:
        DataFrame: The DataFrame with sentiment scores, categories, and buckets added.
    """
    # Apply sentiment analysis to calculate sentiment scores for each review
    df['SentimentScore'] = df['ReviewText'].apply(calculate_sentiment)

    # Apply sentiment categorization using both text and rating
    df['SentimentCategory'] = df.apply(
        lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1
    )

    # Apply sentiment bucketing to categorize scores into defined ranges
    df['SentimentBucket'] = df['SentimentScore'].apply(sentiment_bucket)

    return df

def plot_sentiment_distribution(df: pd.DataFrame):
    """
    Plots the sentiment distribution of the reviews.
    
    Args:
        df (DataFrame): The DataFrame containing sentiment labels.
    """
    # Plot the sentiment distribution
    sns.countplot(x='SentimentCategory', data=df, palette='coolwarm')
    plt.title('Sentiment Distribution of Customer Reviews')
    plt.show()

# Main process
if __name__ == "__main__":
    # Step 1: Get the data from SQL Server
    customer_reviews_df = get_sql_data()

    # Step 2: Analyze sentiment of reviews
    customer_reviews_df = analyze_sentiment(customer_reviews_df)

    # Step 3: Print the DataFrame with sentiment scores, categories, and buckets
    print(customer_reviews_df[['ReviewID', 'ReviewText', 'Rating', 'SentimentScore', 'SentimentCategory', 'SentimentBucket']].head())

    # Step 4: Plot the sentiment distribution
    plot_sentiment_distribution(customer_reviews_df)

    # Step 5: Save the DataFrame with sentiment scores, categories, and buckets to a new CSV file
    customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)
