"""
RetailIQ Data Generators

This module contains reusable functions
for generating synthetic retail datasets.
"""

from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker("en_IN")  # Indian locale


# ==========================================================
# Customer Generator
# ==========================================================

def generate_customers(count: int) -> pd.DataFrame:
    """
    Generate synthetic customer data.

    Parameters
    ----------
    count : int
        Number of customers to generate.

    Returns
    -------
    pd.DataFrame
        Customer dataset.
    """

    customers = []

    for _ in range(count):

        customer = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender": random.choice(["Male", "Female"]),
            "age": random.randint(18, 70),
            "email": fake.unique.email(),
            "phone": fake.phone_number(),
            "city": fake.city(),
            "state": fake.state(),
            "country": "India",
            "join_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),
        }

        customers.append(customer)

    customers_df = pd.DataFrame(customers)
    customers_df["join_date"] = pd.to_datetime(customers_df["join_date"])

    return customers_df


# ==========================================================
# Product Configuration
# ==========================================================

PRODUCT_CATALOG = {

    "Electronics": {
        "brands": ["Apple", "Samsung", "Sony", "Dell", "HP"],
        "products": [
            "Laptop",
            "Smartphone",
            "Monitor",
            "Tablet",
            "Smartwatch",
            "Headphones",
        ],
        "price_range": (10000, 150000),
    },

    "Furniture": {
        "brands": ["IKEA", "Godrej", "Nilkamal"],
        "products": [
            "Office Chair",
            "Dining Table",
            "Wardrobe",
            "Bookshelf",
            "Study Desk",
        ],
        "price_range": (2000, 80000),
    },

    "Clothing": {
        "brands": ["Nike", "Adidas", "Puma", "Levi's"],
        "products": [
            "T-Shirt",
            "Jeans",
            "Jacket",
            "Sneakers",
            "Hoodie",
        ],
        "price_range": (500, 8000),
    },

    "Groceries": {
        "brands": ["Amul", "Nestle", "Britannia"],
        "products": [
            "Milk",
            "Bread",
            "Coffee",
            "Butter",
            "Biscuits",
        ],
        "price_range": (20, 2000),
    },

    "Books": {
        "brands": ["Penguin", "Pearson", "O'Reilly"],
        "products": [
            "Python Programming",
            "SQL Fundamentals",
            "Data Science",
            "Machine Learning",
            "Business Analytics",
        ],
        "price_range": (150, 3000),
    },
}


SKU_PREFIX = {
    "Electronics": "ELE",
    "Furniture": "FUR",
    "Clothing": "CLO",
    "Groceries": "GRO",
    "Books": "BOO",
}


# ==========================================================
# Product Generator
# ==========================================================

def generate_products(count: int) -> pd.DataFrame:
    """
    Generate synthetic product data.

    Parameters
    ----------
    count : int
        Number of products to generate.

    Returns
    -------
    pd.DataFrame
        Product dataset.
    """

    products = []

    for i in range(1, count + 1):

        # Select category
        category = random.choice(list(PRODUCT_CATALOG.keys()))
        category_info = PRODUCT_CATALOG[category]

        # Brand & Product
        brand = random.choice(category_info["brands"])
        product_name = random.choice(category_info["products"])

        # Pricing
        min_price, max_price = category_info["price_range"]

        unit_price = round(
            random.uniform(min_price, max_price),
            2,
        )

        cost_price = round(
            unit_price * random.uniform(0.70, 0.90),
            2,
        )

        # Inventory
        stock_quantity = random.randint(0, 500)
        reorder_level = random.randint(10, 50)

        # Product Status
        status = (
            "Active"
            if stock_quantity > 0
            else "Out of Stock"
        )

        # SKU
        sku = f"{SKU_PREFIX[category]}-{i:06d}"

        # Product Record
        product = {
            "product_id": i,
            "sku": sku,
            "product_name": product_name,
            "category": category,
            "brand": brand,
            "unit_price": unit_price,
            "cost_price": cost_price,
            "stock_quantity": stock_quantity,
            "reorder_level": reorder_level,
            "status": status,
        }

        products.append(product)

    return pd.DataFrame(products)



# ==========================================================
# Inventory Configuration
# ==========================================================

WAREHOUSES = [
    "Chennai Warehouse",
    "Bengaluru Warehouse",
    "Mumbai Warehouse",
    "Hyderabad Warehouse",
    "Delhi Warehouse",
]


# ==========================================================
# Inventory Generator
# ==========================================================

def generate_inventory(products_df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate synthetic inventory data.

    Parameters
    ----------
    products_df : pd.DataFrame
        Product dataset.

    Returns
    -------
    pd.DataFrame
        Inventory dataset.
    """

    inventory = []

    for _, product in products_df.iterrows():

        stock_quantity = random.randint(0, 500)

        reorder_level = random.randint(10, 50)

        inventory_record = {

            "product_id": product["product_id"],

            "warehouse": random.choice(WAREHOUSES),

            "stock_quantity": stock_quantity,

            "reorder_level": reorder_level,

            "last_stock_update": fake.date_between(
                start_date="-1y",
                end_date="today"
            ),

            "is_active": stock_quantity > 0,

            "created_at": fake.date_time_between(
                start_date="-1y",
                end_date="-30d"
            ),

            "updated_at": fake.date_time_between(
                start_date="-30d",
                end_date="now"
            ),
        }

        inventory.append(inventory_record)

    inventory_df = pd.DataFrame(inventory)

    inventory_df["last_stock_update"] = pd.to_datetime(
        inventory_df["last_stock_update"]
    )

    inventory_df["created_at"] = pd.to_datetime(
        inventory_df["created_at"]
    )

    inventory_df["updated_at"] = pd.to_datetime(
        inventory_df["updated_at"]
    )

    return inventory_df



# ==========================================================
# Employee Configuration
# ==========================================================

BRANCHES = [
    "Chennai",
    "Bengaluru",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Coimbatore",
]

DESIGNATIONS = [
    "Sales Executive",
    "Cashier",
    "Inventory Executive",
    "Store Manager",
    "Branch Manager",
    "HR Executive",
    "Regional Manager",
]

MANAGERS = [
    "Ravi Kumar",
    "Priya Sharma",
    "Arjun Nair",
    "Sneha Reddy",
    "Karthik Raj",
]



# ==========================================================
# Employee Generator
# ==========================================================

def generate_employees(count: int) -> pd.DataFrame:
    """
    Generate synthetic employee data.

    Parameters
    ----------
    count : int
        Number of employees to generate.

    Returns
    -------
    pd.DataFrame
        Employee dataset.
    """

    employees = []

    for _ in range(count):

        first_name = fake.first_name()
        last_name = fake.last_name()

        employee = {

            "first_name": first_name,

            "last_name": last_name,

            "email": (
                f"{first_name.lower()}."
                f"{last_name.lower()}."
                f"{random.randint(100,999)}"
                "@retailiq.com"
            ),

            "phone": fake.unique.msisdn()[:10],

            "branch": random.choice(BRANCHES),

            "designation": random.choice(DESIGNATIONS),

            "manager_name": random.choice(MANAGERS),

            "hire_date": fake.date_between(
                start_date="-10y",
                end_date="today"
            ),

            "is_active": random.choices(
                [True, False],
                weights=[90, 10],
                k=1
            )[0],
        }

        employees.append(employee)

    employees_df = pd.DataFrame(employees)

    employees_df["hire_date"] = pd.to_datetime(
        employees_df["hire_date"]
    )

    return employees_df



import pandas as pd


def generate_date_dimension(
    start_date: str,
    end_date: str
) -> pd.DataFrame:
    """
    Generate a Date Dimension table.
    """

    dates = pd.date_range(
        start=start_date,
        end=end_date,
        freq="D"
    )

    date_df = pd.DataFrame({
        "full_date": dates
    })

    date_df["date_key"] = (
        date_df["full_date"]
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    date_df["year"] = date_df["full_date"].dt.year

    date_df["quarter"] = date_df["full_date"].dt.quarter

    date_df["month"] = date_df["full_date"].dt.month

    date_df["month_name"] = date_df["full_date"].dt.month_name()

    date_df["week"] = (
        date_df["full_date"]
        .dt.isocalendar()
        .week
        .astype(int)
    )

    date_df["day"] = date_df["full_date"].dt.day

    date_df["day_name"] = date_df["full_date"].dt.day_name()

    date_df["is_weekend"] = (
        date_df["full_date"]
        .dt.dayofweek >= 5
    )

    return date_df[
        [
            "date_key",
            "full_date",
            "year",
            "quarter",
            "month",
            "month_name",
            "week",
            "day",
            "day_name",
            "is_weekend",
        ]
    ]
    
    

# ==========================================================
# Orders Configuration
# ==========================================================

NUM_ORDERS = 10000

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Cash",
]

SALES_CHANNELS = [
    "Online",
    "Store",
    "Mobile App",
]

    
    
def generate_orders(
    customers_df,
    employees_df,
    date_dimension_df,
):
    """
    Generate synthetic orders for RetailIQ.
    """

    orders = []

    customer_ids = customers_df["customer_id"].tolist()
    employee_ids = employees_df["employee_id"].tolist()
    date_keys = date_dimension_df["date_key"].tolist()

    for _ in range(NUM_ORDERS):

        orders.append(
            {
                "customer_id": random.choice(customer_ids),
                "employee_id": random.choice(employee_ids),
                "date_key": random.choice(date_keys),
                "payment_method": random.choice(PAYMENT_METHODS),
                "sales_channel": random.choice(SALES_CHANNELS),
            }
        )

    orders_df = pd.DataFrame(orders)

    print(f"Generated {len(orders_df)} orders successfully.")

    return orders_df



def generate_order_items(
    orders_df,
    products_df
):
    order_items = []

    item_id = 1

    product_ids = products_df["product_id"].tolist()

    for _, order in orders_df.iterrows():

        num_items = random.randint(1, 5)

        selected_products = random.sample(
            product_ids,
            num_items
        )

        for product_id in selected_products:

            product = products_df[
                products_df["product_id"] == product_id
            ].iloc[0]

            quantity = random.randint(1, 3)

            unit_price = product["unit_price"]

            order_items.append(
               {
                    "order_item_id": item_id,
                    "order_id": order["order_id"],
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "discount": round(random.uniform(0, 0.20), 2),
                    "created_at": datetime.now()
                }
            )

            item_id += 1

    return pd.DataFrame(order_items)