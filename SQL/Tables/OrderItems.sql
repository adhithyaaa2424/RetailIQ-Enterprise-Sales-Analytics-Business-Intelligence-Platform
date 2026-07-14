-- ==========================================
-- Order Items Table
-- ==========================================

CREATE TABLE order_items (

    order_item_id SERIAL PRIMARY KEY,

    order_id INT NOT NULL,

    product_id INT NOT NULL,

    quantity INT
        CHECK(quantity > 0),

    unit_price NUMERIC(10,2)
        CHECK(unit_price >= 0),

    discount NUMERIC(5,2)
        DEFAULT 0
        CHECK(discount >= 0),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_orderitems_order
        FOREIGN KEY(order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_orderitems_product
        FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);