-- =====================================================
-- RetailIQ Product Analytics
-- File: 03_product_analysis.sql
-- =====================================================


-- =====================================================
-- 1. Total Products
-- =====================================================

SELECT
    COUNT(*) AS total_products
FROM retail.products;



-- =====================================================
-- 2. Best Selling Products By Quantity
-- =====================================================

SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.brand,
    SUM(oi.quantity) AS total_quantity_sold
FROM retail.products p
JOIN retail.order_items oi
ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category,
    p.brand
ORDER BY total_quantity_sold DESC
LIMIT 10;



-- =====================================================
-- 3. Product Revenue Ranking
-- =====================================================

SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.brand,

    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        2
    ) AS total_revenue

FROM retail.products p

JOIN retail.order_items oi
ON p.product_id = oi.product_id

GROUP BY
    p.product_id,
    p.product_name,
    p.category,
    p.brand

ORDER BY total_revenue DESC
LIMIT 10;



-- =====================================================
-- 4. Category Revenue Analysis
-- =====================================================

SELECT
    p.category,

    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        2
    ) AS category_revenue

FROM retail.products p

JOIN retail.order_items oi
ON p.product_id = oi.product_id

GROUP BY p.category

ORDER BY category_revenue DESC;



-- =====================================================
-- 5. Brand Performance
-- =====================================================

SELECT
    p.brand,

    COUNT(DISTINCT p.product_id) AS product_count,

    ROUND(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        2
    ) AS brand_revenue

FROM retail.products p

JOIN retail.order_items oi
ON p.product_id = oi.product_id

GROUP BY p.brand

ORDER BY brand_revenue DESC;



-- =====================================================
-- 6. Product Revenue Contribution %
-- =====================================================

WITH product_sales AS
(
    SELECT

        p.product_id,
        p.product_name,

        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ) AS revenue

    FROM retail.products p

    JOIN retail.order_items oi
    ON p.product_id = oi.product_id

    GROUP BY
        p.product_id,
        p.product_name
)

SELECT

    product_name,

    ROUND(revenue,2) AS revenue,

    ROUND(
        revenue * 100 /
        SUM(revenue) OVER(),
        2
    ) AS revenue_percentage

FROM product_sales

ORDER BY revenue DESC;



-- =====================================================
-- 7. Low Performing Products
-- =====================================================

SELECT

    p.product_id,
    p.product_name,
    p.category,
    p.brand,

    COALESCE(
        SUM(oi.quantity),
        0
    ) AS units_sold


FROM retail.products p

LEFT JOIN retail.order_items oi

ON p.product_id = oi.product_id


GROUP BY

    p.product_id,
    p.product_name,
    p.category,
    p.brand


ORDER BY units_sold ASC

LIMIT 10;



-- =====================================================
-- 8. Average Selling Price By Product
-- =====================================================

SELECT

    p.product_id,
    p.product_name,
    p.category,

    ROUND(
        AVG(oi.unit_price),
        2
    ) AS average_selling_price


FROM retail.products p

JOIN retail.order_items oi

ON p.product_id = oi.product_id


GROUP BY

    p.product_id,
    p.product_name,
    p.category


ORDER BY average_selling_price DESC

LIMIT 10;



-- =====================================================
-- 9. Category Quantity Analysis
-- =====================================================

SELECT

    p.category,

    SUM(oi.quantity) AS total_units_sold


FROM retail.products p

JOIN retail.order_items oi

ON p.product_id = oi.product_id


GROUP BY p.category


ORDER BY total_units_sold DESC;