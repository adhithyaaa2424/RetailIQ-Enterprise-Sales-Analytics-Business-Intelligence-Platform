-- ==========================================
-- RetailIQ Customer Analytics
-- ==========================================


-- ==========================================
-- Total Customers
-- ==========================================

SELECT

COUNT(*) AS total_customers

FROM retail.customers;



-- ==========================================
-- Top 10 Customers By Revenue
-- ==========================================

SELECT

c.customer_id,

c.first_name || ' ' || c.last_name AS customer_name,


SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS total_revenue


FROM retail.customers c


JOIN retail.orders o

ON c.customer_id = o.customer_id


JOIN retail.order_items oi

ON o.order_id = oi.order_id


GROUP BY

c.customer_id,
c.first_name,
c.last_name


ORDER BY total_revenue DESC


LIMIT 10;



-- ==========================================
-- Customer Lifetime Value (CLV)
-- ==========================================

SELECT

c.customer_id,

c.first_name || ' ' || c.last_name AS customer_name,


SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS lifetime_value


FROM retail.customers c


JOIN retail.orders o

ON c.customer_id = o.customer_id


JOIN retail.order_items oi

ON o.order_id = oi.order_id


GROUP BY

c.customer_id,
c.first_name,
c.last_name


ORDER BY lifetime_value DESC;



-- ==========================================
-- Repeat Customers
-- Customers with more than one order
-- ==========================================

SELECT

c.customer_id,

c.first_name || ' ' || c.last_name AS customer_name,


COUNT(DISTINCT o.order_id) AS total_orders


FROM retail.customers c


JOIN retail.orders o

ON c.customer_id = o.customer_id


GROUP BY

c.customer_id,
c.first_name,
c.last_name


HAVING COUNT(DISTINCT o.order_id) > 1


ORDER BY total_orders DESC;



-- ==========================================
-- Customer Purchase Frequency
-- ==========================================

SELECT

c.customer_id,

c.first_name || ' ' || c.last_name AS customer_name,


COUNT(DISTINCT o.order_id) AS purchase_frequency


FROM retail.customers c


JOIN retail.orders o

ON c.customer_id = o.customer_id


GROUP BY

c.customer_id,
c.first_name,
c.last_name


ORDER BY purchase_frequency DESC;



-- ==========================================
-- Customer Segmentation
-- ==========================================
-- High Value:
-- Revenue > 10000
-- Medium Value:
-- Revenue 5000-10000
-- Low Value:
-- Revenue < 5000
-- ==========================================


SELECT

customer_id,

customer_name,

lifetime_value,


CASE

WHEN lifetime_value > 10000
THEN 'High Value'


WHEN lifetime_value BETWEEN 5000 AND 10000
THEN 'Medium Value'


ELSE 'Low Value'


END AS customer_segment


FROM

(

SELECT

c.customer_id,

c.first_name || ' ' || c.last_name AS customer_name,


SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS lifetime_value


FROM retail.customers c


JOIN retail.orders o

ON c.customer_id=o.customer_id


JOIN retail.order_items oi

ON o.order_id=oi.order_id


GROUP BY

c.customer_id,
c.first_name,
c.last_name

) customer_value


ORDER BY lifetime_value DESC;