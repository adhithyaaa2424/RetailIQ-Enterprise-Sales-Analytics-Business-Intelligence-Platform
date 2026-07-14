-- ==========================================
-- Products Table
-- ==========================================

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,

    product_name VARCHAR(150) NOT NULL,

    category VARCHAR(50) NOT NULL,

    sub_category VARCHAR(50) NOT NULL,

    brand VARCHAR(50) NOT NULL,

    cost_price NUMERIC(10,2)
        CHECK (cost_price >= 0),

    selling_price NUMERIC(10,2)
        CHECK (selling_price >= cost_price),

    is_active BOOLEAN DEFAULT TRUE
);