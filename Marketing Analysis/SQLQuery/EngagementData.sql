-- General Looking

Select * 
From dbo.engagement_data;


-- Query to clean and normalize the data

Select 
	EngagementID,
	ContentID,
	CampaignID,
	ProductID,
	Upper(Replace(ContentType, 'Socialmedia', 'Social Media')) As ContentType, 
	Left(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined) - 1) As Views,
	Right(ViewsClicksCombined, Len(ViewsClicksCombined) - CHARINDEX('-', ViewsClicksCombined)) As Clicks,
	Likes,
	Format(Convert(DATE, EngagementDate), 'dd.MM.yyyy') As EngagmentDate
From 
	dbo.engagement_data
Where
	ContentType != 'Newsletter';