-- ==========================================
-- Employees Table
-- ==========================================

CREATE TABLE employees (

    employee_id SERIAL PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,

    last_name VARCHAR(50) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    phone VARCHAR(20) UNIQUE,

    branch VARCHAR(50) NOT NULL,

    designation VARCHAR(50) NOT NULL,

    manager_name VARCHAR(100) NOT NULL,

    hire_date DATE NOT NULL,

    is_active BOOLEAN DEFAULT TRUE
);