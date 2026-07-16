-- ==========================================
-- Products Table
-- ==========================================

CREATE TABLE products (

    product_id INT PRIMARY KEY,

    sku VARCHAR(50) UNIQUE NOT NULL,

    product_name VARCHAR(150) NOT NULL,

    category VARCHAR(50) NOT NULL,

    brand VARCHAR(50) NOT NULL,

    unit_price NUMERIC(10,2)
        CHECK (unit_price >= 0),

    cost_price NUMERIC(10,2)
        CHECK (cost_price >= 0),

    stock_quantity INT
        CHECK (stock_quantity >= 0),

    reorder_level INT
        CHECK (reorder_level >= 0),

    status VARCHAR(20) NOT NULL
);