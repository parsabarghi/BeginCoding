# Cleaning the World Layoffs Data in MySQL

In this project, we use SQL to clean up our data. Below are the steps we followed:

![image](https://media.licdn.com/dms/image/C4D12AQF3S7kI48k2MQ/article-cover_image-shrink_600_2000/0/1603125120540?e=2147483647&v=beta&t=npj6zBS0cK2tfoxgRz-_fVv_kaFgiLxj0jwZAaEcFyY)

## What We Do in This Project
1. **Removing Duplicated Values**
2. **Standardizing the Data**
3. **Handling Null or Blank Values**
4. **Removing Unnecessary Columns or Rows**

### Removing Duplicated Values
In the first step, we use a Common Table Expression (CTE) to find duplicated values. We then create a new column named `row_num` to count our duplicated rows. Typically, we create a new table to make changes. One important thing to note is the `SQL_SAFE_UPDATE` setting, which we need to turn off to update our table.

### Standardizing the Data
In this step, we identify issues in our data and fix them. We start by analyzing the data. For example, we replace erroneous values in rows, such as correcting "Crypto" entries and removing whitespace. A crucial task is changing the date format (dtype) from text (or string) to integer.

### Handling Null or Blank Values
Here, we use the JOIN method to replace incorrect data in our rows or columns with the correct form.

### Removing Unnecessary Columns or Rows
Finally, we remove any useless rows or columns using `ALTER TABLE` and `DROP COLUMN`.
