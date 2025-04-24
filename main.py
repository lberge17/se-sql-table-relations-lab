# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
SELECT firstName, lastName
FROM employees
JOIN offices
    USING(officeCode)
WHERE city = 'Boston'
""", conn)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
SELECT
    o.officeCode,
    o.city,
    COUNT() AS n_employees
FROM offices AS o
JOIN employees AS e
    USING(officeCode)
GROUP BY officeCode
HAVING n_employees = 0
;
""", conn)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT firstName, lastName, city, state
FROM employees
LEFT JOIN offices
    USING(officeCode)
ORDER BY firstName, lastName
;
""", conn)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
SELECT
    contactFirstName,
    contactLastName,
    phone,
    salesRepEmployeeNumber
FROM customers
LEFT JOIN orders
    USING(customerNumber)
WHERE orderNumber is NULL
ORDER BY contactLastName
;
""", conn)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
SELECT
    contactFirstName,
    contactLastName,
    CAST(amount as REAL) as paymentamount,
    paymentDate
FROM customers
JOIN payments
    USING(customerNumber)
ORDER BY paymentamount DESC
;
""", conn)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""
SELECT
    employeeNumber,
    firstName,
    lastName,
    COUNT(customerNumber) AS numCustomers
FROM employees AS e
JOIN customers As c
    ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY employeeNumber
HAVING AVG(creditLimit) > 90000
ORDER BY numCustomers DESC
;
""", conn)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
SELECT
    productName,
    COUNT(orderNumber) AS numberorders,
    SUM(quantityOrdered) AS totalunits
FROM products
JOIN orderdetails
    USING (productCode)
GROUP BY productName
ORDER BY totalunits DESC
;
""", conn)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
SELECT productName, productcode, COUNT(DISTINCT customerNumber) AS numpurchasers
FROM products
JOIN orderdetails
    USING(productCode)
JOIN orders
    USING(orderNumber)
GROUP BY productName
ORDER BY numPurchasers DESC
;
""", conn)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""SELECT
    o.officeCode,
    o.city,
    COUNT(c.customerNumber) AS n_customers
FROM offices AS o
JOIN employees AS e
    USING(officeCode)
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY officeCode
;
""", conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
SELECT
    Distinct(employeenumber),
    firstName,
    lastName,
    o.city,
    officeCode
FROM employees AS e
JOIN offices AS o
    USING(officeCode)
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
WHERE productCode IN (
    SELECT productCode
    FROM products
    JOIN orderdetails
        USING(productCode)
    JOIN orders
        USING(orderNumber)
    GROUP BY productCode
    HAVING COUNT(DISTINCT customerNumber) < 20
)
ORDER BY lastName
;
""", conn)

conn.close()