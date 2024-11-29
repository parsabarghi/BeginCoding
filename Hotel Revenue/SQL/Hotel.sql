-- 1. Make general checking on our Data.

Select * 
From hotelrevenue.2018;

Select * 
From hotelrevenue.2019;

Select * 
From hotelrevenue.2020;


-- 2. Change them to the one big table using Union
Use hotelrevenue;
Create Table hoteldata as
Select * 
From hotelrevenue.2018
union
Select * 
From hotelrevenue.2019
union
Select * 
From hotelrevenue.2020

select * from hoteldata;

-- 3. Is our Hotel growing?
-- Exploratory Data Analysis or EDA

Select 
arrival_date_year,
hotel,
Round(Sum((stays_in_week_nights+stays_in_weekend_nights)*adr), 2) as revenue 
From hotelrevenue.hoteldata
group by arrival_date_year, hotel;

-- 4. Change table and use market segment and meal cost

Select * 
From hoteldata
left join hotelrevenue.market_segment
on hoteldata.market_segment = market_segment.market_segment

Select * 
From hoteldata
left join hotelrevenue.meal_cost
on meal_cost.meal = hoteldata.meal