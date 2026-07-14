-- ==========================================
-- Orders Table
-- ==========================================

CREATE TABLE orders (

    order_id SERIAL PRIMARY KEY,

    customer_id INT NOT NULL,

    employee_id INT NOT NULL,

    date_key INT NOT NULL,

    payment_method VARCHAR(30) NOT NULL,

    sales_channel VARCHAR(30) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_orders_employee
        FOREIGN KEY(employee_id)
        REFERENCES employees(employee_id),

    CONSTRAINT fk_orders_date
        FOREIGN KEY(date_key)
        REFERENCES date_dimension(date_key)
);