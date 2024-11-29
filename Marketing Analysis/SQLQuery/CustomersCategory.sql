-- General looking to the Data

Select *
From dbo.customers

Select *
From dbo.geography


-- Sql code to join two table 

Select 
	c.CustomerID,
	c.CustomerName,
	c.Email,
	c.Gender,
	c.Age,
	g.Country,
	g.City
From 
	dbo.customers as c
Left Join 
	dbo.geography as g
On
	c.GeographyID = g.GeographyID