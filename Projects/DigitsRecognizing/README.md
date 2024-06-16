# Digits Recognizing

## Introduction
This project is about recognizing handwritten digits using the Support Vector Machine (SVM) classifier from the scikit-learn library. It utilizes the popular MNIST dataset to train and test the SVM model for digit classification.

## Project Structure
The code is structured as follows:
•  Importing necessary libraries

•  Loading the digits dataset from scikit-learn

•  Analyzing and visualizing the dataset

•  Preprocessing the data for the SVM model

•  Splitting the data into training and testing sets

•  Training the SVM model

•  Predicting digit labels with the model

•  Visualizing the predictions

•  Evaluating the model's performance using metrics and a confusion matrix


## Dependencies
•  NumPy

•  Pandas

•  Matplotlib

•  scikit-learn


## Usage
To run this project, you will need to install the above dependencies. The main script can be executed in a Python environment that supports Jupyter Notebooks or converted into a standalone Python script.

## Model Details
The SVM classifier is configured with a gamma value of 0.001 and a C value of 100. These hyperparameters were chosen to provide a balance between model complexity and training time.

## Dataset
The dataset used is the `load_digits` dataset from scikit-learn, which contains 8x8 pixel images of digits.

## Visualization
The project includes visualization of the digits from the dataset as well as the predictions made by the model.

## Metrics
Model performance is evaluated using a classification report and a confusion matrix.
