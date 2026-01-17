-------------------------------------------- AGGREGATE FUNCTIONS --------------------------------------------
-- Database: World

-- Question 1: How many official languages are there?
-- Table: countrylanguage
-- Result: 238

-- ...

-- Question 2: What is the average life expectancy in the world?
-- Table: country
-- Result: 66.48603611164265

-- ...

-- Question 3: What is the average population for cities in the netherlands?
-- Table: city
-- Result: 185001

-- ...

-------------------------------------------- COMPARISON OPERATORS --------------------------------------------

-- How many female customers do we have from the state of Oregon (OR)?
-- Database: Store
-- Table: Customers
-- Result: 106

-- ...

-- Who over the age of 44 has an income of 100 000 or more? (excluding 44)
-- Database: Store
-- Table: Customers
-- Result: 2497

-- ...

-- Who between the ages of 30 and 50 has an income less than 50 000? (include 30 and 50 in the results)
-- Database: Store
-- Table: Customers
-- Result: 2362

-- ...

-- What is the average income between the ages of 20 and 50? (Excluding 20 and 50)
-- Database: Store
-- Table: Customers
-- Result: 59409.926240780098

-- ...

-------------------------------------------- IN --------------------------------------------

/*
* DB: Store
* Table: orders
* Question: How many orders were made by customer 7888, 1082, 12808, 9623
*/

-- ...

/*
* DB: World
* Table: city
* Question: How many cities are in the district of Zuid-Holland, Noord-Brabant and Utrecht?
*/

-- ...

-------------------------------------------- BETWEEN AND --------------------------------------------

-- Who between the ages of 30 and 50 has an income less than 50 000? (include 30 and 50 in the results)
-- Database: Store
-- Table: Customers

-- ...

-- What is the average income between the ages of 20 and 50? (Including 20 and 50)
-- Database: Store
-- Table: Customers

-- ...

-------------------------------------------- DISTINCT --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: How many unique birth dates are there?
*/

-- ...

/*
* DB: World
* Table: country
* Question: Can I get a list of distinct life expectancy ages (Make sure there are no nulls)
*/

-- ...

-------------------------------------------- ORDER BY --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: Sort employees by first name ascending and last name descending
*/

-- ...

/*
* DB: Employees
* Table: employees
* Question: Sort employees by birth_date
*/

-- ...

/*
* DB: Employees
* Table: employees
* Question: Sort employees who's name starts with a "k" by hire_date
*/

-- ...

-------------------------------------------- LIKE --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: How many people's name start with A and end with R?
* Expected output: 1846
*/

-- ...

/*
* DB: Store
* Table: customers
* Question: How many people's zipcode have a 2 in it?.
* Expected output: 4211 
*/

-- ...

/*
* DB: Store
* Table: customers
* Question: How many people's zipcode start with 2 with the 3rd character being a 1.
* Expected output: 109 
*/

-- ...

-------------------------------------------- OPERATOR PRECEDENCE (comparison operators) --------------------------------------------

/*
* DB: Store
* Table: Customers
* Question: 
* Select people either under 30 or over 50 with an income above 50000
* Include people that are 50
* that are from either Japan or Australia
*/

-- ...

/*
* DB: Store
* Table: Orders
* Question: 
* What was our total sales in June of 2004 for orders over 100 dollars?
*/

-- ...

-------------------------------------------- DATA FILTERING --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: Get me all the employees above 60, use the appropriate date functions
*/

-- ...

/*
* DB: Employees
* Table: employees
* Question: How many employees where hired in February?
*/

-- ...

/*
* DB: Employees
* Table: employees
* Question: How many employees were born in november?
*/

-- ...

/*
* DB: Employees
* Table: employees
* Question: What is the age of the oldest employee?
*/

-- ...

/*
* DB: Store
* Table: orders
* Question: How many orders were made in January 2004?
*/

-- ...

-------------------------------------------- JOINS --------------------------------------------

/*
* DB: Store
* Table: orders
* Question: Get all orders from customers who live in Ohio (OH), New York (NY) or Oregon (OR) state ordered by orderid
*/

-- ...

/*
* DB: Store
* Table: products
* Question: Show me the inventory for each product
*/

-- ...

/*
* DB: Employees
* Table: employees
* Question: Show me for each employee which department they work in
*/

-- ...

/*
*  Show me all the employees that work in the department development and the from and to date.
*  Database: Employees
*/

-- ...

-------------------------------------------- GROUP BY --------------------------------------------

/*
*  How many people were hired on did we hire on any given hire date?
*  Database: Employees
*  Table: Employees
*/

-- ...

/*
*  Show me all the employees, hired after 1991 and count the amount of positions they've had
*  Database: Employees
*/

-- ...

/*
-- How many employees were hired in each year?
-- Database: Employees
-- Table: Employees
*/

-- ...

-- Find the employee numbers and names of employees who work in the 'Sales' department.
-- Database: Employees
-- Table: Employees, Dept_emp, Departments

-- ...

/*
-- Count the number of employees who were hired each month.
-- Database: Employees
-- Table: Employees
*/

-- ...

-------------------------------------------- HAVING --------------------------------------------

/*
*  Show me all the employees, hired after 1991, that have had more than 2 titles
*  Database: Employees
*/

-- ...

/*
*  Show me all the employees that have had more than 15 salary changes that work in the department development
*  Database: Employees
*/

-- ...

/*
*  Show me all the employees that have worked for multiple departments
*  Database: Employees
*/

-- ...

-------------------------------------------- ROLLUP, CUBE, GROUPING SETS --------------------------------------------

/*
*  Calculate the total amount of employees per department using grouping sets
*  Database: Employees
*  Table: Employees
*/

-- ...

/*
*  Calculate the total average salary per department and the total using grouping sets
*  Database: Employees
*  Table: Employees
*/

-- ...

-------------------------------------------- WINDOW FUNCTIONS --------------------------------------------

-- Find the average income for each position
-- Database: Employees

-- ...

-- Find the average price for each category and then subtract the item’s price from its category’s price 
-- Database: Store

-- ...

-- Find the percentage of the world's population that lives on each continent.
-- Database: World
-- Table: Country

-- ...

/*
*  Show the population per continent
*  Database: World
*  Table: Country
*/

-- ...

/*
*  To the previous query add on the ability to calculate the percentage of the world population
*  What that means is that you will divide the population of that continent by the total population and multiply by 100 to get a percentage.
*  Make sure you convert the population numbers to float using `population::float` otherwise you may see zero pop up
*
*  Database: World
*  Table: Country
*/

-- ...

-------------------------------------------- RANK()/ROW_NUMBER()/DENSE_RANK() --------------------------------------------

-- Find the first three hired employees for each department

-- ...


-- Find the 3 highest salaries for each position

-- ...


-- Find the most expensive product for each category

-- ...

-------------------------------------------- LEAD() LAG() FIRST_VALUE() LAST_VALUE() --------------------------------------------

-- Task: For each employee's title record, show the current title and the next title. If there is no next title, show NULL.
-- Database: Employees

-- ...


-- Task: For each employee's department record, show the current department,  the previous department, 
-- the next department, and  the last recorded department for that employee. show NULL.
-- Database: Employees

-- ...


--Task: For each employee, calculate the number of days between their hire date and the hire date of the previous employee based on the emp_no order. 
-- If there is no previous employee, show NULL
-- Database: Employees

-- ...


-- Task: Assign a sequential number to each employee based on their hire date within each gender.
-- Additionally, mark whether the employee is in the top half or bottom half of their gender group based on their hire date.
-- Database: Employees

-- ...

-- Task: Assign a dense rank to each employee's title based on the from_date within each employee. 
-- Additionally, mark the first title each employee received
-- Database: Employees

-- ...

-------------------------------------------- UNION --------------------------------------------

/*
*  Calculate the total average salary per department and the total
*  Database: Employees
*  Table: Employees
*/

-- ...

-------------------------------------------- CONDITIONAL STATEMENTS --------------------------------------------

/*
* Database: Store
* Table: products
* Create a case statement that's named "price class" where if a product is over 20 dollars you show 'expensive'
* if it's between 10 and 20 you show 'average' 
* and of is lower than or equal to 10 you show 'cheap'.
*/

-- ...

/*
* DB: World
* Table: Countries
* Calculate the total area of countries that have a population of over 50 million 
*/

-- ...

-------------------------------------------- VIEWS --------------------------------------------
/*
*  Create a view "90-95" that:
*  Shows me all the employees, hired between 1990 and 1995
*  Database: Employees
*/

-- ...

/*
*  Create a view "bigbucks" that:
*  Shows me all employees that have ever had a salary over 80000
*  Database: Employees
*/

-- ...


-------------------------------------------- SUBQUERIES --------------------------------------------

/* TRY TO WRITE THESE AS JOINS FIRST */
/*
* DB: Store
* Table: orders
* Question: Get all orders from customers who live in Ohio (OH), New York (NY) or Oregon (OR) state
* ordered by orderid
*/

-- ...

/*
* DB: Employees
* Table: employees
* Question: Filter employees who have emp_no 110183 as a manager
*/

-- ...

-- Written with JOIN --

-- ...