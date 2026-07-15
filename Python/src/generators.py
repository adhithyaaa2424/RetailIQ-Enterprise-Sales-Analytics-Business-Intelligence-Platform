"""
RetailIQ Data Generators

This module contains reusable functions
for generating synthetic retail datasets.
"""

from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")   # Indian locale


def generate_customers(count: int) -> pd.DataFrame:
    
    """
    Generate synthetic customer data.

    Parameters:
        count (int): Number of customers to generate.

    Returns:
        pd.DataFrame: Customer dataset.
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
            )
        }

        customers.append(customer)
    
    customers_df = pd.DataFrame(customers)

    customers_df["join_date"] = pd.to_datetime(customers_df["join_date"])

    return customers_df

