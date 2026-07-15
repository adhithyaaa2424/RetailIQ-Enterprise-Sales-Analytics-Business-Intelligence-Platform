"""
RetailIQ Validators

Contains reusable validation functions
for RetailIQ datasets.
"""

import pandas as pd
from datetime import date

def validate_missing_values(df: pd.DataFrame) -> None:
    """
    Check for missing values in every column.
    """

    print("=" * 50)
    print("Missing Value Report")
    print("=" * 50)

    print(df.isnull().sum())
    
    
def validate_duplicate_emails(df: pd.DataFrame) -> None:
    """
    Check for duplicate email addresses.
    """

    duplicates = df["email"].duplicated().sum()

    print("=" * 50)
    print("Duplicate Email Report")
    print("=" * 50)

    if duplicates == 0:
       print("✅ No duplicate emails found.")
    else:
       print(f"❌ Duplicate Emails Found: {duplicates}")
       


def validate_age_range(df: pd.DataFrame) -> None:
    """
    Validate customer ages.
    Age must be between 18 and 70.
    """

    invalid_ages = df[
        (df["age"] < 18) |
        (df["age"] > 70)
    ]

    print("=" * 50)
    print("Age Validation Report")
    print("=" * 50)

    if invalid_ages.empty:
        print("✅ All customer ages are valid.")
    else:
        print(f"❌ Invalid Ages Found: {len(invalid_ages)}")
        print()
        print(invalid_ages[["first_name", "last_name", "age"]])
        
        
        
def validate_gender(df: pd.DataFrame) -> None:
    """
    Validate gender values.
    """

    valid_genders = ["Male", "Female"]

    invalid_gender = df[
        ~df["gender"].isin(valid_genders)
    ]

    print("=" * 50)
    print("Gender Validation Report")
    print("=" * 50)

    if invalid_gender.empty:
        print("✅ All gender values are valid.")
    else:
        print(f"❌ Invalid Gender Records: {len(invalid_gender)}")
        print()
        print(invalid_gender[["first_name", "last_name", "gender"]])
        
        

def validate_future_join_dates(df: pd.DataFrame) -> None:
    """
    Check whether any customer join_date is in the future.

    Business Rule:
        join_date must not be greater than today's date.
    """

    print("=" * 50)
    print("Checking Future Join Dates...")

    today = pd.Timestamp(date.today())

    invalid_dates = df[df["join_date"] > today]

    if invalid_dates.empty:
        print("No Future Join Dates Found.")
    else:
        print("Future Join Dates Found!")
        print(invalid_dates)
        
        
def run_customer_validations(df: pd.DataFrame) -> None:
    """
    Run all customer validation checks.

    Parameters:
        df (pd.DataFrame): Customer dataset.
    """

    print("\n" + "=" * 50)
    print("Running Customer Validation Pipeline")
    print("=" * 50)

    validate_missing_values(df)
    validate_duplicate_emails(df)
    validate_age_range(df)
    validate_gender(df)
    validate_future_join_dates(df)

    print("=" * 50)
    print("Customer Validation Pipeline Completed")
    print("=" * 50)