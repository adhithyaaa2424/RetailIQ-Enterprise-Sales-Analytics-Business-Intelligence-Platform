-- ==========================================
-- RetailIQ Indexes
-- ==========================================

CREATE INDEX idx_orders_customer
ON orders(customer_id);

CREATE INDEX idx_orders_employee
ON orders(employee_id);

CREATE INDEX idx_orders_date
ON orders(date_key);

CREATE INDEX idx_order_items_order
ON order_items(order_id);

CREATE INDEX idx_order_items_product
ON order_items(product_id);

CREATE INDEX idx_inventory_product
ON inventory(product_id);