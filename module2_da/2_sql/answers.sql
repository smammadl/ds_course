-------------------------------------------- AGGREGATE FUNCTIONS --------------------------------------------
-- Database: World

-- Question 1: How many official languages are there?
-- Table: countrylanguage
-- Result: 238
select count(countrycode) from countrylanguage
where isofficial = true;

-- Question 2: What is the average life expectancy in the world?
-- Table: country
-- Result: 66.48603611164265
select avg(lifeexpectancy) from country;

-- Question 3: What is the average population for cities in the netherlands?
-- Table: city
-- Result: 185001
select AVG(population) from city
where countrycode = 'NLD';

-------------------------------------------- COMPARISON OPERATORS --------------------------------------------

-- How many female customers do we have from the state of Oregon (OR)?
-- Database: Store
-- Table: Customers
-- Result: 106
SELECT COUNT(firstName)
FROM customers
WHERE gender = 'F' and state = 'OR';

-- Who over the age of 44 has an income of 100 000 or more? (excluding 44)
-- Database: Store
-- Table: Customers
-- Result: 2497
SELECT COUNT(income)
FROM customers
WHERE age > 44 and income >= 100000;

SELECT customerid, firstname, lastname, age, income 
FROM customers
WHERE age > 44 and income >= 100000;

-- Who between the ages of 30 and 50 has an income less than 50 000? (include 30 and 50 in the results)
-- Database: Store
-- Table: Customers
-- Result: 2362
SELECT COUNT(income)
FROM customers
WHERE age >= 30 and age <= 50 AND income < 50000;

SELECT customerid, firstname, lastname, age, income 
FROM customers
WHERE age >= 30 and age <= 50 AND income < 50000;

-- What is the average income between the ages of 20 and 50? (Excluding 20 and 50)
-- Database: Store
-- Table: Customers
-- Result: 59409.926240780098
SELECT AVG(income)
FROM customers
WHERE age > 20 and age < 50;

-------------------------------------------- IN --------------------------------------------

/*
* DB: Store
* Table: orders
* Question: How many orders were made by customer 7888, 1082, 12808, 9623
*/
SELECT COUNT(orderid)
FROM orders
WHERE customerid IN (7888, 1082, 12808, 9623)


/*
* DB: World
* Table: city
* Question: How many cities are in the district of Zuid-Holland, Noord-Brabant and Utrecht?
*/
SELECT COUNT(id)
FROM city
WHERE district IN ('Zuid-Holland', 'Noord-Brabant', 'Utrecht');

-------------------------------------------- BETWEEN AND --------------------------------------------

-- Who between the ages of 30 and 50 has an income less than 50 000? (include 30 and 50 in the results)
-- Database: Store
-- Table: Customers
SELECT customerid, firstname, lastname, age, income 
FROM customers
WHERE age BETWEEN 30 AND 50 AND income < 50000;

-- What is the average income between the ages of 20 and 50? (Including 20 and 50)
-- Database: Store
-- Table: Customers
SELECT AVG(income) 
FROM customers 
WHERE age BETWEEN 20 AND 50;

-------------------------------------------- DISTINCT --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: How many unique birth dates are there?
*/
SELECT COUNT(DISTINCT birth_date)
FROM employees;

/*
* DB: World
* Table: country
* Question: Can I get a list of distinct life expectancy ages (Make sure there are no nulls)
*/
SELECT DISTINCT lifeexpectancy 
FROM country
WHERE lifeexpectancy IS NOT NULL
ORDER BY lifeexpectancy;

-------------------------------------------- ORDER BY --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: Sort employees by first name ascending and last name descending
*/
SELECT * 
FROM employees
ORDER BY first_name ASC, last_name DESC;

/*
* DB: Employees
* Table: employees
* Question: Sort employees by birth_date
*/
SELECT * 
FROM employees
ORDER BY birth_date;

/*
* DB: Employees
* Table: employees
* Question: Sort employees who's name starts with a "k" by hire_date
*/
SELECT * 
FROM employees
WHERE first_name ILIKE 'k%'
ORDER BY hire_date;

-------------------------------------------- LIKE --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: How many people's name start with A and end with R?
* Expected output: 1846
*/
SELECT count(emp_no) 
FROM employees
WHERE first_name ILIKE 'A%R';

/*
* DB: Store
* Table: customers
* Question: How many people's zipcode have a 2 in it?.
* Expected output: 4211 
*/
SELECT count(customerid) 
FROM customers
WHERE zip::text LIKE '%2%';


/*
* DB: Store
* Table: customers
* Question: How many people's zipcode start with 2 with the 3rd character being a 1.
* Expected output: 109 
*/
SELECT count(customerid) 
FROM customers
WHERE zip::text LIKE '2_1%';

-------------------------------------------- OPERATOR PRECEDENCE (comparison operators) --------------------------------------------

/*
* DB: Store
* Table: Customers
* Question: 
* Select people either under 30 or over 50 with an income above 50000
* Include people that are 50
* that are from either Japan or Australia
*/
SELECT firstname, income, age, country 
FROM customers
WHERE income > 50000 AND (age < 30 OR age >= 50) and (country = 'Japan' OR country = 'Australia')

-- alternative --
SELECT firstname, income, age, country
FROM customers
WHERE (age < 30 or (income > 50000 AND age >= 50)) and (country = 'Japan' OR country = 'Australia')


/*
* DB: Store
* Table: Orders
* Question: 
* What was our total sales in June of 2004 for orders over 100 dollars?
*/
SELECT SUM(totalamount) 
FROM orders
WHERE (orderdate >= '2004-06-01' AND orderdate <= '2004-06-30') AND totalamount > 100

-- alternative --
SELECT SUM(totalamount) 
FROM orders
WHERE orderdate BETWEEN '2004-06-01' AND '2004-06-30' AND totalamount > 100

-------------------------------------------- DATA FILTERING --------------------------------------------

/*
* DB: Employees
* Table: employees
* Question: Get me all the employees above 60, use the appropriate date functions
*/
SELECT 
	*,  
	AGE(birth_date), 
	EXTRACT (YEAR FROM AGE(birth_date)) as "year"
FROM employees
WHERE (
   EXTRACT (YEAR FROM AGE(birth_date))
) > 60 ;

-- alternative --
SELECT * 
FROM employees
WHERE birth_date < now() - interval '61 years' -- 61 years before the current date

/*
* DB: Employees
* Table: employees
* Question: How many employees where hired in February?
*/
SELECT count(emp_no) 
FROM employees
WHERE EXTRACT (MONTH FROM hire_date) = 2;

/*
* DB: Employees
* Table: employees
* Question: How many employees were born in november?
*/
SELECT COUNT(emp_no) 
FROM employees
WHERE EXTRACT (MONTH FROM birth_date) = 11;

/*
* DB: Employees
* Table: employees
* Question: What is the age of the oldest employee?
*/
SELECT MAX(AGE(birth_date)) FROM employees;

/*
* DB: Store
* Table: orders
* Question: How many orders were made in January 2004?
*/
SELECT COUNT(orderid)
FROM orders
WHERE DATE_TRUNC('month', orderdate) = date '2004-01-01';

-- alternative --
SELECT COUNT(orderid)
FROM orders
WHERE orderdate BETWEEN '2004-01-01' AND '2004-01-31';

-- alternative --
SELECT COUNT(orderid)
FROM orders
WHERE EXTRACT (MONTH FROM orderdate) = 1 AND EXTRACT (YEAR FROM orderdate) = 2004;

-------------------------------------------- JOINS --------------------------------------------

/*
* DB: Store
* Table: orders
* Question: Get all orders from customers who live in Ohio (OH), New York (NY) or Oregon (OR) state ordered by orderid
*/
SELECT c.firstname, c.lastname, o.orderid, c.state
FROM orders AS o
    RIGHT JOIN customers AS c 
        ON o.customerid = c.customerid
WHERE c.state IN ('NY', 'OH', 'OR')
ORDER BY o.orderid;


/*
* DB: Store
* Table: products
* Question: Show me the inventory for each product
*/
SELECT p.prod_id, i.quan_in_stock
FROM products as p
    LEFT JOIN inventory AS i 
        ON p.prod_id = i.prod_id 

/*
* DB: Employees
* Table: employees
* Question: Show me for each employee which department they work in
*/
SELECT e.first_name, dp.dept_name
FROM 
    employees AS e 
    INNER JOIN dept_emp AS de 
        ON de.emp_no = e.emp_no

    INNER JOIN departments AS dp 
        ON dp.dept_no = de.dept_no


/*
*  Show me all the employees that work in the department development and the from and to date.
*  Database: Employees
*/
SELECT e.emp_no, de.from_date, de.to_date
FROM employees as e JOIN dept_emp AS de USING(emp_no)
WHERE de.dept_no = 'd005'  -- d005 is development department
-- GROUP BY e.emp_no, de.from_date, de.to_date
ORDER BY e.emp_no, de.to_date;


-------------------------------------------- GROUP BY --------------------------------------------

/*
*  How many people were hired on did we hire on any given hire date?
*  Database: Employees
*  Table: Employees
*/
SELECT hire_date, COUNT(emp_no) as "amount"
FROM employees
GROUP BY hire_date
-- ORDER BY "amount" DESC
ORDER BY hire_date;

/*
*  Show me all the employees, hired after 1991 and count the amount of positions they've had
*  Database: Employees
*/
SELECT e.emp_no, count(t.title) as "amount of titles"
FROM employees as e JOIN titles as t USING(emp_no)
WHERE EXTRACT (YEAR FROM e.hire_date) > 1991
GROUP BY e.emp_no
ORDER BY e.emp_no;

/*
-- How many employees were hired in each year?
-- Database: Employees
-- Table: Employees
*/
SELECT EXTRACT (YEAR FROM hire_date), COUNT(emp_no)
FROM employees
GROUP BY EXTRACT (YEAR FROM hire_date)
ORDER BY EXTRACT (YEAR FROM hire_date);

-- Find the employee numbers and names of employees who work in the 'Sales' department.
-- Database: Employees
-- Table: Employees, Dept_emp, Departments
select e.emp_no, e.first_name, e.last_name, d.dept_name, de.to_date  
-- select * 
from employees as e 
	join dept_emp as de on e.emp_no = de.emp_no 
	join departments as d on d.dept_no = de.dept_no 
where d.dept_name ilike 'sales' and de.to_date >= now() 
order by e.emp_no;

/*
-- Count the number of employees who were hired each month.
-- Database: Employees
-- Table: Employees
*/
SELECT EXTRACT (YEAR FROM hire_date), EXTRACT (MONTH FROM hire_date), COUNT(emp_no)
FROM employees
GROUP BY EXTRACT (YEAR FROM hire_date), EXTRACT (MONTH FROM hire_date) 
ORDER BY EXTRACT (YEAR FROM hire_date), EXTRACT (MONTH FROM hire_date);

-------------------------------------------- HAVING --------------------------------------------

/*
*  Show me all the employees, hired after 1991, that have had more than 2 titles
*  Database: Employees
*/
SELECT e.emp_no, count(t.title) as "amount of titles"
FROM employees as e JOIN titles as t USING(emp_no)
WHERE EXTRACT (YEAR FROM e.hire_date) > 1991
GROUP BY e.emp_no
HAVING count(t.title) > 2
ORDER BY e.emp_no;

/*
*  Show me all the employees that have had more than 15 salary changes that work in the department development
*  Database: Employees
*/
SELECT e.emp_no, count(s.from_date) as "amount of raises"
FROM employees as e
	JOIN salaries as s USING(emp_no)
	JOIN dept_emp AS de USING(emp_no)
WHERE de.dept_no = 'd005'
GROUP BY e.emp_no
HAVING count(s.from_date) > 15
ORDER BY e.emp_no;

-- alternative --
select e.emp_no, count(s.salary) as "num salary changes" 
from employees as e left join dept_emp as de on e.emp_no = de.emp_no
	left join departments as d on de.dept_no = d.dept_no 
	left join salaries as s on e.emp_no = s.emp_no 
where d.dept_name = 'Development'
group by e.emp_no 
having count(s.salary) > 15

/*
*  Show me all the employees that have worked for multiple departments
*  Database: Employees
*/
SELECT e.emp_no, count(de.dept_no) as "worked for # departments"
FROM employees as e JOIN dept_emp AS de USING(emp_no) 
GROUP BY e.emp_no
HAVING count(de.dept_no) > 1
ORDER BY e.emp_no;

-------------------------------------------- GROUPING SETS --------------------------------------------

/*
*  Calculate the total amount of employees per department using grouping sets
*  Database: Employees
*  Table: Employees
*/
select 
    grouping(e.dept_no), e.dept_no, COUNT(e.emp_no)
FROM public.dept_emp as e
GROUP BY
	GROUPING SETS ((e.dept_no), ())
order by e.dept_no

/*
*  Calculate the total average salary per department and the total using grouping sets
*  Database: Employees
*  Table: Employees
*/
select 
    grouping(de.dept_no), de.dept_no, AVG(e.salary)
FROM public.salaries as e JOIN public.dept_emp as de USING (emp_no)
GROUP BY
	GROUPING SETS ((de.dept_no), ())
order by de.dept_no

-------------------------------------------- WINDOW FUNCTIONS --------------------------------------------

-- Find the average income for each position
-- Database: Employees
select 
	distinct t.title, 
	avg(s.salary) over w1
from titles as t join salaries as s on t.emp_no = s.emp_no
window w1 as (partition by t.title);

-- alternative --
select 
	distinct t.title, 
	avg(s.salary) over (partition by t.title)
from titles as t join salaries as s on t.emp_no = s.emp_no

-- Find the average price for each category and then subtract the item’s price from its category’s price 
-- Database: Store
select 
	category,  
	avg(price) over w1 as "cat. avg price",
	prod_id,
	price, 
	price - (avg(price) over w1) as "price diff"
from products 
window w1 as (partition by category)


-- alternative --
select 
	category,  
	avg(price) over (partition by category) as "cat. avg price",
	prod_id,
	price, 
	price - (avg(price) over (partition by category)) as "price diff"
from products 

-- Find the percentage of the world's population that lives on each continent.
-- Database: World
-- Table: Country
select 
	distinct continent, 
	sum(population) over (partition by continent) as "continent population", 
	sum(population) over () as "total population", 
	concat(
		round(
			(sum(population::decimal) over (partition by continent) / sum(population::decimal) over ()) * 100
		), '%'
	) as "percentage of population"
from country

/*
*  Show the population per continent
*  Database: World
*  Table: Country
*/

SELECT
  DISTINCT continent,
  SUM(population) OVER w1 as"continent population"
FROM country 
WINDOW w1 AS( PARTITION BY continent );

-- alternative --
SELECT
  DISTINCT continent,
  SUM(population) OVER (PARTITION BY continent) as"continent population"
FROM country 

-- alternative --
select continent, sum(population)  
from country
group by continent

/*
*  To the previous query add on the ability to calculate the percentage of the world population
*  What that means is that you will divide the population of that continent by the total population and multiply by 100 to get a percentage.
*  Make sure you convert the population numbers to float using `population::float` otherwise you may see zero pop up
*
*  Database: World
*  Table: Country
*/

SELECT
  DISTINCT continent,
  SUM(population) OVER w1 as"continent population",
  CONCAT( 
      ROUND( 
          ( 
            SUM( population::float4 ) OVER w1 / 
            SUM( population::float4 ) OVER() 
          ) * 100    
      ),'%' ) as "percentage of population"
FROM country 
WINDOW w1 AS( PARTITION BY continent );

-------------------------------------------- RANK()/ROW_NUMBER()/DENSE_RANK() --------------------------------------------

-- Find the first three hired employees for each department
with rank_table as 
	(select 
		de.dept_no, 
		e.emp_no, 
		e.hire_date, 
		rank() over (partition by de.dept_no order by e.hire_date asc) as "rank"
	from employees as e JOIN dept_emp as de ON e.emp_no=de.emp_no)
select * 
from rank_table 
where rank <= 3


-- Find the 3 highest salaries for each position
with rank_table as 
(
select 
	t.title , 
	s.salary, 
	rank() over (partition by t.title order by salary desc) as "rank", 
	s.emp_no 
from titles as t join salaries as s on t.emp_no = s.emp_no 
)
select *
from rank_table 
where rank<=3


-- Find the most expensive product for each category
with price_rank_table as 
(
	select 
		category,  
		rank() over (partition by category order by price desc) as "rank", 
		prod_id, 
		price 
	from products 
)
select * 
from price_rank_table 
where rank=1

-------------------------------------------- LEAD() LAG() FIRST_VALUE() LAST_VALUE() --------------------------------------------

-- Task: For each employee's title record, show the current title and the next title. If there is no next title, show NULL.
-- Database: Employees
select 
		e.emp_no, 
		t.title, 
		t.from_date, 
		t.to_date, 
		LEAD(title) OVER w1 AS next_title,
		LEAD(from_date) OVER w1 AS next_from_date,
		LEAD(to_date) OVER w1 AS next_to_date
from employees as e JOIN titles as t ON e.emp_no = t.emp_no 
window w1 as (partition by e.emp_no order by t.from_date) 
order by e.emp_no, t.from_date


-- Task: For each employee's department record, show the current department,  the previous department, 
-- the next department, and  the last recorded department for that employee. show NULL.
-- Database: Employees

select 
		e.emp_no, 

		de.dept_no, 
		de.from_date, 
		de.to_date, 

		LAG(de.dept_no) OVER w1 AS previous_department,
		-- LAG(de.from_date) OVER w1 AS previous_from_date,
		-- LAG(de.to_date) OVER w1 AS previous_to_date,

		LEAD(de.dept_no) OVER w1 AS next_department,
		-- LEAD(de.from_date) OVER w1 AS next_from_date,
		-- LEAD(de.to_date) OVER w1 AS next_to_date,

		LAST_VALUE(de.dept_no) OVER w2 AS last_recorded_department
		-- LAST_VALUE(de.from_date) OVER w2 AS last_recorded_from_date,
		-- LAST_VALUE(de.to_date) OVER w2 AS last_recorded_to_date

from employees as e JOIN dept_emp as de ON e.emp_no = de.emp_no 
window 
	w1 as (partition by e.emp_no order by de.from_date), 
	w2 as (PARTITION BY e.emp_no ORDER BY de.from_date RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
order by e.emp_no, de.from_date


--Task: For each employee, calculate the number of days between their hire date and the hire date of the previous employee based on the emp_no order. 
-- If there is no previous employee, show NULL
-- Database: Employees

SELECT 
    emp_no,
    hire_date, 
    LAG(hire_date) OVER (ORDER BY emp_no) as "previous hire date", 
	case 
		when LAG(hire_date) OVER (ORDER BY emp_no) is not null
			then LAG(hire_date) OVER (ORDER BY emp_no) - hire_date
		else null
	end as "days between hire dates"
FROM  employees 
ORDER BY emp_no;


-- Task: Assign a sequential number to each employee based on their hire date within each gender.
-- Additionally, mark whether the employee is in the top half or bottom half of their gender group based on their hire date.
-- Database: Employees
select 
	emp_no,
	gender, 
	hire_date, 
	row_number () over w1, 
	count(*) over w2, 
	case 
		when row_number () over w1 < count(*) over w2 / 2 
			then 'ilk ishe alinanlar' 
		else 
			'son ishe alinanlar'
	end 
from employees 
window 
	w1 as (partition by gender order by hire_date), 
	w2 as (partition by gender)

-- Task: Assign a dense rank to each employee's title based on the from_date within each employee. 
-- Additionally, mark the first title each employee received
-- Database: Employees

select 
	emp_no, 
	title, 
	from_date, 
	rank() over w1, 
	case 
		when rank() over w1 = 1
			then 'ilk ish'
		else 
			null
	end as "is first title"
from titles 
window w1 as (partition by emp_no order by from_date)
order by emp_no; 

-- alternative --
select 
	emp_no, 
	title, 
	from_date, 
	rank() over w1, 
	title = (NTH_VALUE(title, 1) OVER w1 ) as "is first title"
from titles 
window w1 as (partition by emp_no order by from_date)
order by emp_no; 



-------------------------------------------- UNION --------------------------------------------

/*
*  Calculate the total average salary per department and the total
*  Database: Employees
*  Table: Employees
*/

SELECT
	de.dept_no, 
	avg(s.salary)
from dept_emp as de join salaries as s on de.emp_no = s.emp_no
group by de.dept_no

UNION ALL

SELECT
	null, 
	avg(s.salary)
from salaries as s



-------------------------------------------- CONDITIONAL STATEMENTS --------------------------------------------

/*
* Database: Store
* Table: products
* Create a case statement that's named "price class" where if a product is over 20 dollars you show 'expensive'
* if it's between 10 and 20 you show 'average' 
* and of is lower than or equal to 10 you show 'cheap'.
*/

SELECT prod_id, title, price, 
    CASE   
      WHEN  price > 20 THEN 'expensive'
      WHEN  price <= 10 THEN  'cheap'
      WHEN  price BETWEEN 10 and 20  THEN 'average'
    END AS "price class"
FROM products

/*
* DB: World
* Table: Countries
* Calculate the total area of countries that have a population of over 50 million 
*/

select 
	sum(case when population > 50000000 then surfacearea else 0 end) as "total area"
from country

-- alternative --
SELECT SUM(surfacearea) as "total area"
FROM country
WHERE population > 50000000

-------------------------------------------- VIEWS --------------------------------------------
/*
*  Create a view "90-95" that:
*  Shows me all the employees, hired between 1990 and 1995
*  Database: Employees
*/

CREATE VIEW "90-95" AS
SELECT *
FROM employees as e
WHERE EXTRACT (YEAR FROM e.hire_date) BETWEEN 1990 AND 1995
ORDER BY e.emp_no;

/*
*  Create a view "bigbucks" that:
*  Shows me all employees that have ever had a salary over 80000
*  Database: Employees
*/

CREATE VIEW "bigbucks" AS
SELECT e.emp_no, s.salary
FROM employees as e
JOIN salaries as s USING(emp_no)
WHERE s.salary > 80000
ORDER BY s.salary;


-------------------------------------------- SUBQUERIES --------------------------------------------

/* TRY TO WRITE THESE AS JOINS FIRST */
/*
* DB: Store
* Table: orders
* Question: Get all orders from customers who live in Ohio (OH), New York (NY) or Oregon (OR) state
* ordered by orderid
*/

select * 
from orders 
where customerid in 
	(select customerid 
	from customers 
	where state in ('OH', 'NY', 'OR'))

select * 
from 
	orders as o, 
	(select *   
	from customers 
	where state in ('OH', 'NY', 'OR')) as c
where o.customerid = c.customerid


SELECT c.firstname, c.lastname, o.orderid 
FROM orders AS o, (
    SELECT customerid, state, firstname, lastname
    FROM customers
) AS c
WHERE  o.customerid = c.customerid AND 
c.state IN ('NY', 'OH', 'OR')
ORDER BY o.orderid;

/*
* DB: Employees
* Table: employees
* Question: Filter employees who have emp_no 110183 as a manager
*/

SELECT emp_no, first_name, last_name
FROM employees
WHERE emp_no IN (
    SELECT emp_no
    FROM dept_emp
    WHERE dept_no = (
        SELECT dept_no 
        FROM dept_manager
        WHERE emp_no = 110183
    )
)
ORDER BY emp_no

-- Written with JOIN --
SELECT e.emp_no, first_name, last_name, dm.emp_no 
FROM employees as e
JOIN dept_emp as de USING (emp_no)
JOIN dept_manager as dm USING (dept_no)
WHERE dm.emp_no = 110183