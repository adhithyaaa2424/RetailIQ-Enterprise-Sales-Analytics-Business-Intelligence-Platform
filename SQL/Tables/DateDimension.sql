-- ==========================================
-- Date Dimension Table
-- ==========================================

CREATE TABLE date_dimension (

    date_key INT PRIMARY KEY,

    full_date DATE UNIQUE NOT NULL,

    year INT NOT NULL,

    quarter INT
        CHECK (quarter BETWEEN 1 AND 4),

    month INT
        CHECK (month BETWEEN 1 AND 12),

    month_name VARCHAR(20) NOT NULL,

    week INT
        CHECK (week BETWEEN 1 AND 53),

    day INT
        CHECK (day BETWEEN 1 AND 31),

    day_name VARCHAR(20) NOT NULL,

    is_weekend BOOLEAN NOT NULL
);