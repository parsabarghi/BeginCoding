-- Looking at both table 
select * from CovidProject..CovidDeaths
order by 3, 4
-- select * from CovidProject..CovidVaccinations

-- select the data that we will use in our procces
select location, date, total_cases, new_cases, total_deaths, population
from CovidProject..CovidDeaths
order by 1, 2

-- total cases vs total deaths
-- deaths percentage 
-- deaths percentage new columns
select location, date, population, (total_deaths/total_cases)*100 as deaths_percentage 
from CovidProject..CovidDeaths
order by 1, 2

-- use tools to get information about a country (like usa, qatar or...)
select location, date, total_cases, new_cases, total_deaths, population, (total_deaths/total_cases)*100 as deaths_percentage
from CovidProject..CovidDeaths
where location like '%state%'
order by 1, 2

-- total cases vs population
-- infection percentage  new columns
-- use tools to get information about a country (like usa, qatar or...)
select location, date, total_cases, new_cases, total_deaths, population,
(total_cases/population)*100 as total_infection
from CovidProject..CovidDeaths
where location like '%state%'
order by 1, 2
-- show the total infection rate as a percentage with two decimal places
--SELECT location, date, total_cases, new_cases, total_deaths, population, 
--FORMAT((CAST(total_cases AS FLOAT)/population)*100, 'N2') AS total_infection
--FROM CovidProject..CovidDeaths
--WHERE location LIKE '%state%'
--ORDER BY 1, 2;

-- find the country that have highest total_infection
select location, date, max(total_cases), population,
max((total_cases)/population)*100 as maximum_total_infection
from CovidProject..CovidDeaths
group by location, date, population, total_cases
order by maximum_total_infection desc

-- find the country that have highest total deaths
select location, max(cast(total_deaths as int)) as most_deaths, population
from CovidProject..CovidDeaths
group by location, total_deaths, population
order by total_deaths desc

-- showing the null in continent
select * 
from CovidProject..CovidDeaths
where continent is null
order by 3, 4

-- find the continent that have highest total deaths
select continent, max(cast(total_deaths as int)) as most_deaths
from CovidProject..CovidDeaths
where continent is not null
group by continent
order by most_deaths desc

-- showing death count in world
select location, max(cast(total_deaths as int)) as most_deaths
from CovidProject..CovidDeaths
where continent is null
group by location
order by most_deaths desc

-- showing some global information
select 'Global' as location,
SUM(cast(total_cases as float)) as total_cases,
SUM(cast(total_deaths as float)) as total_deaths,
SUM(cast(total_deaths as float))/SUM(cast(total_cases as float))*100 as death_percentage
from CovidProject..CovidDeaths
where continent is not null
-- second global table
select 'Global' as location,
SUM(cast(new_cases as float)) as total_cases,
SUM(cast(new_deaths as float)) as total_deaths,
SUM(cast(new_deaths as float))/SUM(cast(new_cases as float))*100 as death_percentage
from CovidProject..CovidDeaths
where continent is not null

-- joining the second table
select *
from CovidProject..CovidDeaths CCD
join CovidProject..CovidVaccinations CCV
	on CCD.location = CCV.location
	and CCD.date = CCV.date

-- total vaccination vs population 
-- vaccinate rate on each country
-- search a country...
-- USE CTE
with PopVsVac (continent, location, population, date, new_vaccinations, SumVacPerDay)
as
(
select CCD.continent, CCD.location, CCD.population, CCD.date, CCV.new_vaccinations,
sum(convert(int, CCV.new_vaccinations)) over
(partition by CCD.location order by CCD.location, CCD.date, CCD.population) as SumVac 
from CovidProject..CovidDeaths CCD
join CovidProject..CovidVaccinations CCV
	on CCD.location = CCV.location
	and CCD.date = CCV.date
where CCD.continent is not null --and CCD.location like '%iran%%'
)

Select *, (SumVacPerDay/population)*100 
from PopVsVac
where new_vaccinations is not null
order by date 

-- temp table
drop table if exists #VaccinationPercentage
create table #VaccinationPercentage
(
continent nvarchar(255),
location nvarchar(255),
population numeric,
date datetime,
new_vaccinations numeric,
SumVac numeric
)
insert into #VaccinationPercentage
select CCD.continent, CCD.location, CCD.population, CCD.date, CCV.new_vaccinations,
sum(convert(int, CCV.new_vaccinations)) over
(partition by CCD.location order by CCD.location, CCD.date, CCD.population) as SumVac 
from CovidProject..CovidDeaths CCD
join CovidProject..CovidVaccinations CCV
	on CCD.location = CCV.location
	and CCD.date = CCV.date
where CCD.continent is not null --and CCD.location like '%iran%%'

Select *, (SumVac/population)*100 
from #VaccinationPercentage
-- where new_vaccinations is not null
-- order by date 

--creating view for later(visualization)

create view VaccinationPercentage as
select CCD.continent, CCD.location, CCD.population, CCD.date, CCV.new_vaccinations,
sum(convert(int, CCV.new_vaccinations)) over
(partition by CCD.location order by CCD.location, CCD.date, CCD.population) as SumVac 
from CovidProject..CovidDeaths CCD
join CovidProject..CovidVaccinations CCV
	on CCD.location = CCV.location
	and CCD.date = CCV.date
where CCD.continent is not null --and CCD.location like '%iran%%'

select * 
from VaccinationPercentage