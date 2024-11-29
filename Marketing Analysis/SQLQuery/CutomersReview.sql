-- General Looking

Select * 
From dbo.customer_reviews;


-- We have double spacing instead one space so we should handle that

Select 
	ReviewID,
	CustomerID,
	ProductID,
	ReviewDate,
	Rating,
	REPLACE(ReviewText, '  ', ' ') As ReviewText -- Replace double space with the one space
From 
	dbo.customer_reviews;