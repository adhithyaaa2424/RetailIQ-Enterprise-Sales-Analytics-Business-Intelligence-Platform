-- =====================================================
-- RetailIQ - Reporting Views
-- Database : RetailIQ
-- Schema   : retail
-- =====================================================

-- =====================================================
-- 1. Sales Summary View
-- =====================================================

CREATE OR REPLACE VIEW retail.vw_sales_summary AS
SELECT
    o.order_id,
    o.created_at,
    o.date_key,

    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    c.city,
    c.state,
    c.country,

    e.employee_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.branch,
    e.designation,

    p.product_id,
    p.sku,
    p.product_name,
    p.category,
    p.brand,

    oi.quantity,
    oi.unit_price,
    oi.discount,

    (oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue,

    o.payment_method,
    o.sales_channel

FROM retail.orders o

JOIN retail.customers c
ON o.customer_id = c.customer_id

JOIN retail.employees e
ON o.employee_id = e.employee_id

JOIN retail.order_items oi
ON o.order_id = oi.order_id

JOIN retail.products p
ON oi.product_id = p.product_id;




-- =====================================================
-- 2. Customer Analysis View
-- =====================================================

CREATE OR REPLACE VIEW retail.vw_customer_analysis AS

SELECT

    c.customer_id,

    c.first_name || ' ' || c.last_name AS customer_name,

    c.gender,

    c.age,

    c.city,

    c.state,

    c.country,

    COUNT(DISTINCT o.order_id) AS total_orders,

    COALESCE(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ), 0
    ) AS total_revenue,

    COALESCE(
        ROUND(
            SUM(
                oi.quantity *
                oi.unit_price *
                (1 - oi.discount)
            )
            /
            NULLIF(COUNT(DISTINCT o.order_id),0),
            2
        ),
        0
    ) AS average_order_value,

    MIN(o.created_at) AS first_purchase,

    MAX(o.created_at) AS last_purchase

FROM retail.customers c

LEFT JOIN retail.orders o
ON c.customer_id = o.customer_id

LEFT JOIN retail.order_items oi
ON o.order_id = oi.order_id

GROUP BY

    c.customer_id,
    c.first_name,
    c.last_name,
    c.gender,
    c.age,
    c.city,
    c.state,
    c.country;




-- =====================================================
-- 3. Product Performance View
-- =====================================================

CREATE OR REPLACE VIEW retail.vw_product_performance AS

SELECT

    p.product_id,

    p.sku,

    p.product_name,

    p.category,

    p.brand,

    p.unit_price,

    p.cost_price,

    p.stock_quantity,

    p.reorder_level,

    p.status,

    COALESCE(SUM(oi.quantity), 0) AS quantity_sold,

    COALESCE(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        0
    ) AS total_revenue,

    COALESCE(
        ROUND(AVG(oi.unit_price), 2),
        0
    ) AS average_selling_price,

    COALESCE(
        SUM(
            (oi.unit_price - p.cost_price) *
            oi.quantity
        ),
        0
    ) AS estimated_profit

FROM retail.products p

LEFT JOIN retail.order_items oi
ON p.product_id = oi.product_id

GROUP BY

    p.product_id,
    p.sku,
    p.product_name,
    p.category,
    p.brand,
    p.unit_price,
    p.cost_price,
    p.stock_quantity,
    p.reorder_level,
    p.status;




-- =====================================================
-- 4. Employee Performance View
-- =====================================================

CREATE OR REPLACE VIEW retail.vw_employee_performance AS

SELECT

    e.employee_id,

    e.first_name || ' ' || e.last_name AS employee_name,

    e.branch,

    e.designation,

    e.manager_name,

    e.hire_date,

    e.is_active,

    COUNT(DISTINCT o.order_id) AS total_orders,

    COALESCE(
        SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount)
        ),
        0
    ) AS total_revenue,

    COALESCE(
        ROUND(
            SUM(
                oi.quantity *
                oi.unit_price *
                (1 - oi.discount)
            )
            /
            NULLIF(COUNT(DISTINCT o.order_id),0),
            2
        ),
        0
    ) AS average_order_value

FROM retail.employees e

LEFT JOIN retail.orders o
ON e.employee_id = o.employee_id

LEFT JOIN retail.order_items oi
ON o.order_id = oi.order_id

GROUP BY

    e.employee_id,
    e.first_name,
    e.last_name,
    e.branch,
    e.designation,
    e.manager_name,
    e.hire_date,
    e.is_active;



-- =====================================================
-- 5. Inventory Status View
-- =====================================================

CREATE OR REPLACE VIEW retail.vw_inventory_status AS

SELECT

    i.inventory_id,

    p.product_id,

    p.product_name,

    p.category,

    p.brand,

    i.warehouse,

    i.stock_quantity,

    i.reorder_level,

    CASE
        WHEN i.stock_quantity <= i.reorder_level
            THEN 'Low Stock'
        ELSE 'In Stock'
    END AS stock_status,

    p.unit_price,

    (i.stock_quantity * p.unit_price) AS inventory_value,

    i.last_stock_update,

    i.is_active

FROM retail.inventory i

JOIN retail.products p
ON i.product_id = p.product_id;