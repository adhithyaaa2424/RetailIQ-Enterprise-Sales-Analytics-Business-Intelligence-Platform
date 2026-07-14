-- ==========================================
-- RetailIQ - Customers Table
-- ==========================================

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,

    gender VARCHAR(10)
        CHECK (gender IN ('Male', 'Female', 'Other')),

    age INT
        CHECK (age >= 18 AND age <= 100),

    email VARCHAR(100) UNIQUE NOT NULL,

    phone VARCHAR(20) UNIQUE,

    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,

    join_date DATE NOT NULL
);



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