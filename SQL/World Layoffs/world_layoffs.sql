-- Data Cleaning Using MySql

Select * 
From layoffs;

-- Create New Table For Our Analysis
Create Table layoffs_new
Like layoffs;

-- Insert Everything Into Our New Table That Called lyoffs_new!
Select * 
From layoffs_new;

Insert layoffs_new
Select *
From layoffs;

-- 1. Find duplicate value and then Remove them

With dup_cte as
(
Select *, 
Row_Number() Over(
Partition By company, location, industry, total_laid_off, percentage_laid_off, 'date',
 stage, country, funds_raised_millions) as row_num
From layoffs_new
)
Select * 
From dup_cte 
Where row_num > 1;

Select *
From layoffs_new
Where company = 'Oda';

-- Start deleting duplicated

CREATE TABLE `layoffs_new2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

Select *
From layoffs_new2
Where row_num > 1;

INSERT INTO layoffs_new2
SELECT *,
ROW_NUMBER() Over(
PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, date,
stage, country, funds_raised_millions
ORDER BY some_column) AS row_num
FROM layoffs_new;


SET SQL_SAFE_UPDATES = 0;
Delete 
From layoffs_new2
Where row_num > 1;

SET SQL_SAFE_UPDATES = 1;
Select *
From layoffs_new2
Where row_num > 1;

Select *
From layoffs_new2;

-- 2. Standardizing Data (find issuse and fixing that)
SET SQL_SAFE_UPDATES = 0;

-- We should delete null or empty values!!
Select Distinct Company
From layoffs_new2;

Update layoffs_new2
Set company = Trim(company);
-- Also we should change Crypto in our industry column

Select Distinct industry
From layoffs_new2
Order By 1;

Update layoffs_new2
Set industry = 'Crypto'
Where industry Like 'Crypto%';

Select *
From layoffs_new2
Where industry Like 'Crypto%'; 

Select Distinct country
From layoffs_new2
Order By 1;
-- we have a period at end of 'United States' sp we should change that
Select Distinct country, Trim(Trailing '.' From country)
From layoffs_new2
Order by 1;

Update layoffs_new2
Set country = Trim(Trailing '.' From country)
Where country Like 'United States%';

Select Distinct country 
From layoffs_new2
Where country Like 'United States%';

-- Now we should change our date(Text) to date(date) column 
Select `date`,
STR_TO_DATE(`date`, '%m/%d/%y')
From layoffs_new2;

UPDATE layoffs_new2
SET `date` = STR_TO_DATE(`date`, '%m/%d/%Y');

Select `date`
From layoffs_new2
Order BY 1;

Alter Table layoffs_new2
Modify column `date` Date;

-- 3. Working with null and blank values

Select *
From layoffs_new2
Where total_laid_off is Null
And percentage_laid_off is Null; 

Select * 
From layoffs_new2
Where industry is Null 
Or industry = '';

Select *
From layoffs_new2
Where company = 'Airbnb' ;

Select t1.industry, t2.industry
From layoffs_new2 t1
Join layoffs_new2 t2
	On t1.company = t2.company 
    And t1.location = t2.location
Where (t1.industry is Null Or t1.industry = '') 
And t2.industry is not Null;

Update layoffs_new2
Set industry = Null
Where industry = '';

Update layoffs_new2 t1
Join layoffs_new2 t2
	On t1.company = t2.company 
    And t1.location = t2.location
Set t1.industry = t2.industry
Where (t1.industry is Null Or t1.industry = '') 
And t2.industry is not Null;

Select * 
From layoffs_new2
Where industry is Null 
Or industry = '';

Select *
From layoffs_new2
Where company = "Bally's Interactive" ;


Select *
From layoffs_new2
Where total_laid_off is Null
And percentage_laid_off is Null; 

Delete 
From layoffs_new2
Where total_laid_off is Null
And percentage_laid_off is Null; 

Alter Table layoffs_new2
Drop Column row_num;

Select *
From layoffs_new2;

