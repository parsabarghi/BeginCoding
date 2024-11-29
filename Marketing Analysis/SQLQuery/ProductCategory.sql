-- 1. Make some general checking on the Data
Select * 
From dbo.products

-- 2. Query to make categorized using price
SELECT 
    ProductID, 
    ProductName, 
    Price,
	-- Category
    CASE 
        WHEN Price < 50 THEN 'low'
        WHEN Price BETWEEN 50 AND 200 THEN 'medium'
        ELSE 'high'
    END AS PriceCategory
FROM dbo.products;
