-- ==========================================
-- Inventory Table
-- ==========================================

CREATE TABLE inventory (

    inventory_id SERIAL PRIMARY KEY,

    product_id INT NOT NULL,

    warehouse VARCHAR(100) NOT NULL,

    stock_quantity INT
        CHECK (stock_quantity >= 0),

    reorder_level INT
        CHECK (reorder_level >= 0),

    last_stock_update DATE NOT NULL,

    is_active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_inventory_product
        FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);