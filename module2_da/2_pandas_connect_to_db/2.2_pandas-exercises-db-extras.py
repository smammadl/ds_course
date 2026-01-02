#----------------------------------------------------------------------------------------

#-- Database: world

#-- Question 1: How many official languages are there?
#-- Table: countrylanguage

#-- Question 2: What is the average life expectancy in the world?
#-- Table: country

#-- Question 3: What is the average population for cities in the netherlands?
#-- Table: city

#----------------------------------------------------------------------------------------

#-- How many female customers do we have from the state of Oregon (OR)?
#-- Database: store
#-- Table: customers

#-- Who over the age of 44 has an income of 100 000 or more? (excluding 44)
#-- Database: store
#-- Table: customers

#-- Who between the ages of 30 and 50 has an income less than 50 000? (include 30 and 50 in the results)
#-- Database: store
#-- Table: customers

#-- What is the average income between the ages of 20 and 50? (Excluding 20 and 50)
#-- Database: store
#-- Table: customers

#----------------------------------------------------------------------------------------

#-- Question: How many orders were made by customer 7888, 1082, 12808, 9623
#-- DB: store
#-- Table: orders

#-- Question: How many cities are in the district of Zuid-Holland, Noord-Brabant and Utrecht?
#-- DB: world
#-- Table: city

#----------------------------------------------------------------------------------------

#-- Who between the ages of 30 and 50 has an income less than 50 000? (include 30 and 50 in the results)
#-- DB: store
#-- Table: customers

#-- What is the average income between the ages of 20 and 50? (Including 20 and 50)
#-- DB: store
#-- Table: customers

#----------------------------------------------------------------------------------------

#--Question: Can I get a list of distinct life expectancy ages (Make sure there are no nulls)
#--DB: world
#--Table: country

#----------------------------------------------------------------------------------------

#--Question: How many people's zipcode have a 2 in it?.
#--DB: store
#--Table: customers

#--Question: How many people's zipcode start with 2 with the 3rd character being a 1.
#--DB: store
#--Table: customers

#----------------------------------------------------------------------------------------

#--Question: Select people either under 30 or over 50 with an income above 50000
#--Include people that are 50
#--that are from either Japan or Australia
#--DB: store
#--Table: customers

#-- Question: What was our total sales in June of 2004 for orders over 100 dollars?
#-- DB: store
#-- Table: orders

#----------------------------------------------------------------------------------------

#-- Question: How many orders were made in January 2004?
#-- DB: store
#-- Table: orders

#----------------------------------------------------------------------------------------

#-- Question: Get all orders from customers who live in Ohio (OH), New York (NY) or Oregon (OR) state ordered by orderid
#-- DB: store
#-- Table: orders

#-- Question: Show me the inventory for each product
#-- DB: store
#-- Table: products

#----------------------------------------------------------------------------------------

#-- Find the average price for each category and then subtract the item’s price from its category’s price 
#-- Database: store

#-- Find the percentage of the world's population that lives on each continent.
#-- Database: world
#-- Table: country

#-- Show the population per continent
#-- Database: world
#-- Table: country

#-- To the previous query add on the ability to calculate the percentage of the world population
#-- What that means is that you will divide the population of that continent by the total population and multiply by 100 to get a percentage.
#-- Make sure you convert the population numbers to float using `population::float` otherwise you may see zero pop up
#-- Database: world
#-- Table: country

#----------------------------------------------------------------------------------------

#-- Find the most expensive product for each category

#----------------------------------------------------------------------------------------

#-- Create a case statement that's named "price class" where if a product is over 20 dollars you show 'expensive'
#-- if it's between 10 and 20 you show 'average' 
#-- and of is lower than or equal to 10 you show 'cheap'.
#-- Database: store
#-- Table: products

#-- Calculate the total area of countries that have a population of over 50 million 
#-- DB: world
#-- Table: countries

#----------------------------------------------------------------------------------------

#-- Question: Get all orders from customers who live in Ohio (OH), New York (NY) or Oregon (OR) state
#-- ordered by orderid
#-- DB: store
#-- Table: orders