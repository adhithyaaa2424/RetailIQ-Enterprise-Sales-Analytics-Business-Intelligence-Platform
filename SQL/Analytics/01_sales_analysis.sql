-- ==========================================
-- RetailIQ Sales Analytics
-- ==========================================


-- ==========================================
-- Total Orders
-- ==========================================

SELECT
COUNT(*) AS total_orders
FROM retail.orders;



-- ==========================================
-- Total Revenue
-- ==========================================

SELECT

SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS total_revenue

FROM retail.order_items oi;



-- ==========================================
-- Average Order Value
-- ==========================================

SELECT

AVG(order_total) AS average_order_value

FROM
(
    SELECT

    o.order_id,

    SUM(
        oi.quantity *
        oi.unit_price *
        (1 - oi.discount)
    ) AS order_total


    FROM retail.orders o


    JOIN retail.order_items oi

    ON o.order_id = oi.order_id


    GROUP BY o.order_id

) x;



-- ==========================================
-- Monthly Revenue Trend
-- ==========================================

SELECT

DATE_TRUNC(
    'month',
    o.created_at
) AS month,


SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS revenue


FROM retail.orders o


JOIN retail.order_items oi

ON o.order_id = oi.order_id


GROUP BY month


ORDER BY month;



-- ==========================================
-- Revenue By Category
-- ==========================================

SELECT

p.category,


SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS revenue


FROM retail.order_items oi


JOIN retail.products p

ON oi.product_id = p.product_id


GROUP BY p.category


ORDER BY revenue DESC;



-- ==========================================
-- Revenue By Brand
-- ==========================================

SELECT

p.brand,


SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS revenue


FROM retail.order_items oi


JOIN retail.products p

ON oi.product_id = p.product_id


GROUP BY p.brand


ORDER BY revenue DESC;



-- ==========================================
-- Total Quantity Sold
-- ==========================================

SELECT

SUM(quantity) AS total_quantity_sold

FROM retail.order_items;



-- ==========================================
-- Highest Revenue Orders
-- ==========================================

SELECT

o.order_id,


SUM(
    oi.quantity *
    oi.unit_price *
    (1 - oi.discount)
) AS order_value


FROM retail.orders o


JOIN retail.order_items oi

ON o.order_id = oi.order_id


GROUP BY o.order_id


ORDER BY order_value DESC


LIMIT 10;