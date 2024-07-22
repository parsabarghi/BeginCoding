# COVID-19 Data Analysis

This repository contains SQL queries for analyzing COVID-19 data related to cases, deaths, and vaccinations. The data is sourced from the `CovidProject` database, which includes two main tables: `CovidDeaths` and `CovidVaccinations`.

## Overview

The SQL scripts perform various analyses, such as:
•  Retrieving COVID-19 death records and ordering them by date and location.

•  Calculating the death percentage as `(total_deaths/total_cases)*100`.

•  Filtering data for specific countries or states using a wildcard search.

•  Comparing total cases against the population to find the infection percentage.

•  Identifying countries with the highest infection rates and death counts.

•  Handling null values in the continent field and aggregating data at a global level.

•  Joining the deaths and vaccinations tables to analyze vaccination rates.

•  Using Common Table Expressions (CTE) and temporary tables for advanced data manipulation.


## Queries

### Basic Data Retrieval
```sql
-- Retrieve all death records and order by location and date
SELECT * FROM CovidProject..CovidDeaths ORDER BY 3, 4;

Death Percentage Calculation
-- Calculate the death percentage and order by location and date
SELECT location, date, population, (total_deaths/total_cases)*100 AS deaths_percentage 
FROM CovidProject..CovidDeaths ORDER BY 1, 2;

Infection Rate Analysis
-- Calculate the total infection rate as a percentage
SELECT location, date, total_cases, new_cases, total_deaths, population,
(total_cases/population)*100 AS total_infection
FROM CovidProject..CovidDeaths
WHERE location LIKE '%state%'
ORDER BY 1, 2;

Vaccination Analysis
-- Analyze vaccination rates using a CTE
WITH PopVsVac (continent, location, population, date, new_vaccinations, SumVacPerDay) AS
(
SELECT CCD.continent, CCD.location, CCD.population, CCD.date, CCV.new_vaccinations,
SUM(CONVERT(int, CCV.new_vaccinations)) OVER
(PARTITION BY CCD.location ORDER BY CCD.location, CCD.date, CCD.population) AS SumVac 
FROM CovidProject..CovidDeaths CCD
JOIN CovidProject..CovidVaccinations CCV
ON CCD.location = CCV.location
AND CCD.date = CCV.date
WHERE CCD.continent IS NOT NULL
)
SELECT *, (SumVacPerDay/population)*100 
FROM PopVsVac
WHERE new_vaccinations IS NOT NULL
ORDER BY date;

Views and Temporary Tables
The scripts also include the creation of views and temporary tables for more complex analyses and visualizations.

Usage
To run these queries, you will need access to the CovidProject database with the CovidDeaths and CovidVaccinations tables populated with relevant data.
