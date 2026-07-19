-- =====================================================
-- RetailIQ Employee Analytics
-- File: 04_employee_analysis.sql
-- =====================================================


-- =====================================================
-- 1. Total Employees
-- =====================================================

SELECT
    COUNT(*) AS total_employees
FROM retail.employees;



-- =====================================================
-- 2. Employee Order Count
-- =====================================================

SELECT
    e.employee_id,
    e.first_name,
    e.last_name,

    COUNT(o.order_id) AS total_orders

FROM retail.employees e

JOIN retail.orders o
ON e.employee_id = o.employee_id

GROUP BY
    e.employee_id,
    e.first_name,
    e.last_name

ORDER BY total_orders DESC;



-- =====================================================
-- 3. Employee Revenue Ranking
-- =====================================================

SELECT

    e.employee_id,

    e.first_name,
    e.last_name,

    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        2
    ) AS total_revenue


FROM retail.employees e


JOIN retail.orders o
ON e.employee_id = o.employee_id


JOIN retail.order_items oi
ON o.order_id = oi.order_id


GROUP BY

    e.employee_id,
    e.first_name,
    e.last_name


ORDER BY total_revenue DESC;



-- =====================================================
-- 4. Top 10 Performing Employees
-- =====================================================

SELECT

    e.employee_id,

    CONCAT(
        e.first_name,
        ' ',
        e.last_name
    ) AS employee_name,


    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        2
    ) AS revenue


FROM retail.employees e


JOIN retail.orders o
ON e.employee_id = o.employee_id


JOIN retail.order_items oi
ON o.order_id = oi.order_id


GROUP BY

    e.employee_id,
    employee_name


ORDER BY revenue DESC

LIMIT 10;



-- =====================================================
-- 5. Average Order Value Per Employee
-- =====================================================

SELECT

    e.employee_id,

    CONCAT(
        e.first_name,
        ' ',
        e.last_name
    ) AS employee_name,


    ROUND(

        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        )
        /
        COUNT(DISTINCT o.order_id),

        2

    ) AS average_order_value


FROM retail.employees e


JOIN retail.orders o
ON e.employee_id = o.employee_id


JOIN retail.order_items oi
ON o.order_id = oi.order_id


GROUP BY

    e.employee_id,
    employee_name


ORDER BY average_order_value DESC;



-- =====================================================
-- 6. Sales Channel Performance
-- =====================================================

SELECT

    o.sales_channel,


    COUNT(DISTINCT o.order_id)
    AS total_orders,


    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        2
    ) AS revenue


FROM retail.orders o


JOIN retail.order_items oi
ON o.order_id = oi.order_id


GROUP BY o.sales_channel


ORDER BY revenue DESC;



-- =====================================================
-- 7. Employee Monthly Sales Trend
-- =====================================================

SELECT

    e.employee_id,

    CONCAT(
        e.first_name,
        ' ',
        e.last_name
    ) AS employee_name,


    DATE_TRUNC(
        'month',
        o.created_at
    ) AS month,


    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        2
    ) AS monthly_revenue


FROM retail.employees e


JOIN retail.orders o
ON e.employee_id = o.employee_id


JOIN retail.order_items oi
ON o.order_id = oi.order_id


GROUP BY

    e.employee_id,
    employee_name,
    month


ORDER BY month;



-- =====================================================
-- 8. Employee Ranking
-- =====================================================

WITH employee_sales AS
(
    SELECT

        e.employee_id,

        CONCAT(
            e.first_name,
            ' ',
            e.last_name
        ) AS employee_name,


        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ) AS revenue


    FROM retail.employees e


    JOIN retail.orders o
    ON e.employee_id = o.employee_id


    JOIN retail.order_items oi
    ON o.order_id = oi.order_id


    GROUP BY

        e.employee_id,
        employee_name
)


SELECT

    employee_name,

    ROUND(revenue,2) AS revenue,


    RANK() OVER(
        ORDER BY revenue DESC
    ) AS employee_rank


FROM employee_sales;