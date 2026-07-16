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
    
    
    
def validate_product_missing_values(df: pd.DataFrame) -> None:
    """
    Check for missing values in the product dataset.
    """

    print("=" * 50)
    print("Product Missing Value Validation")
    print("=" * 50)

    missing = df.isnull().sum()

    if missing.sum() == 0:
        print("✅ No missing values found.")
    else:
        print("❌ Missing values detected:")
        print(missing[missing > 0])

    print()
    


def validate_duplicate_sku(df):
    """
    Check duplicate SKU values.
    """

    print("=" * 50)
    print("Checking Duplicate SKU")

    duplicates = df[df["sku"].duplicated()]

    if len(duplicates) > 0:
        print("❌ Duplicate SKU found")
        print(duplicates)

    else:
        print("✅ No duplicate SKU found")

    print("=" * 50)
    
    
    
def validate_duplicate_product_id(df):
    """
    Check duplicate product IDs.
    """

    print("=" * 50)
    print("Checking Duplicate Product ID")

    duplicates = df[df["product_id"].duplicated()]

    if len(duplicates) > 0:
        print("❌ Duplicate product_id found")
        print(duplicates)

    else:
        print("✅ No duplicate product_id found")

    print("=" * 50)
    
    
def validate_price_columns(df):
    """
    Validate product pricing rules.
    Cost price should be less than unit price.
    """

    print("=" * 50)
    print("Checking Price Validation")

    invalid_prices = df[df["cost_price"] >= df["unit_price"]]

    if len(invalid_prices) > 0:
        print("❌ Invalid price relationship found")
        print(invalid_prices)

    else:
        print("✅ All prices are valid")

    print("=" * 50)
    
    
def validate_categories(df):
    """
    Validate product categories.
    """

    print("=" * 50)
    print("Checking Product Categories")

    allowed_categories = [
        "Electronics",
        "Furniture",
        "Clothing",
        "Groceries",
        "Books"
    ]

    invalid_categories = df[
        ~df["category"].isin(allowed_categories)
    ]

    if len(invalid_categories) > 0:
        print("❌ Invalid categories found")
        print(invalid_categories)

    else:
        print("✅ All categories are valid")

    print("=" * 50)
    
    
    
def validate_status(df):
    """
    Validate product status based on stock quantity.
    """

    print("=" * 50)
    print("Checking Product Status")

    invalid_status = df[
        (
            (df["stock_quantity"] > 0) &
            (df["status"] != "Active")
        )
        |
        (
            (df["stock_quantity"] == 0) &
            (df["status"] != "Out of Stock")
        )
    ]

    if len(invalid_status) > 0:
        print("❌ Invalid status found")
        print(invalid_status)

    else:
        print("✅ All statuses are valid")

    print("=" * 50)
    
    
def validate_stock(df):
    """
    Validate stock quantity and reorder level.
    """

    print("=" * 50)
    print("Checking Stock Validation")

    invalid_stock = df[
        (df["stock_quantity"] < 0) |
        (df["reorder_level"] < 0)
    ]

    if len(invalid_stock) > 0:
        print("❌ Invalid stock values found")
        print(invalid_stock)

    else:
        print("✅ All stock values are valid")

    print("=" * 50)
    
    
    
def run_product_validations(df):
    """
    Run complete product validation pipeline.
    """

    print("\n")
    print("#" * 60)
    print("PRODUCT VALIDATION PIPELINE STARTED")
    print("#" * 60)

    validate_product_missing_values(df)

    validate_duplicate_sku(df)

    validate_duplicate_product_id(df)

    validate_price_columns(df)

    validate_categories(df)

    validate_status(df)

    validate_stock(df)

    print("#" * 60)
    print("PRODUCT VALIDATION PIPELINE COMPLETED")
    print("#" * 60)
    
    
    
def run_product_validations(df):
    """
    Run complete product validation pipeline.
    """

    print("\n" + "=" * 60)
    print("PRODUCT VALIDATION PIPELINE STARTED")
    print("=" * 60)

    validate_product_missing_values(df)

    validate_duplicate_sku(df)

    validate_duplicate_product_id(df)

    validate_price_columns(df)

    validate_categories(df)

    validate_status(df)

    validate_stock(df)

    print("\n" + "=" * 60)
    print("PRODUCT VALIDATION PIPELINE COMPLETED")
    print("=" * 60)
    
    
# ==========================================================
# Inventory Validators
# ==========================================================

def validate_inventory_missing_values(df):
    """
    Check for missing values in the inventory dataset.
    """

    print("=" * 50)
    print("Inventory Missing Value Validation")
    print("=" * 50)

    missing = df.isnull().sum()

    if missing.sum() == 0:
        print("✅ No missing values found.")
    else:
        print("❌ Missing values detected:")
        print(missing[missing > 0])

    print()


def validate_inventory_stock(df):
    """
    Validate stock quantity and reorder level.
    """

    print("=" * 50)
    print("Checking Inventory Stock")

    invalid = df[
        (df["stock_quantity"] < 0) |
        (df["reorder_level"] < 0)
    ]

    if len(invalid) == 0:
        print("✅ Inventory stock is valid.")
    else:
        print("❌ Invalid inventory records found.")
        print(invalid)

    print("=" * 50)


def run_inventory_validations(df):
    """
    Run complete inventory validation pipeline.
    """

    print("\n" + "=" * 60)
    print("INVENTORY VALIDATION PIPELINE STARTED")
    print("=" * 60)

    validate_inventory_missing_values(df)
    validate_inventory_stock(df)

    print("\n" + "=" * 60)
    print("INVENTORY VALIDATION PIPELINE COMPLETED")
    print("=" * 60)
    
    

def validate_employee_missing_values(employees_df):
    """
    Check for missing values in employee data.
    """

    missing = employees_df.isnull().sum()

    if missing.sum() > 0:
        print("\n❌ Missing Values Found")
        print(missing[missing > 0])
    else:
        print("✅ No missing values found.")
        
        
        
def validate_employee_duplicate_emails(employees_df):
    """
    Check duplicate employee emails.
    """

    duplicates = employees_df["email"].duplicated().sum()

    if duplicates > 0:
        print(f"❌ Duplicate emails found: {duplicates}")
    else:
        print("✅ No duplicate emails found.")
        
        
        
def validate_employee_duplicate_phones(employees_df):
    """
   Check duplicate phone numbers.
    """

    duplicates = employees_df["phone"].duplicated().sum()

    if duplicates > 0:
        print(f"❌ Duplicate phone numbers found: {duplicates}")
    else:
        print("✅ No duplicate phone numbers found.")
        
        
        
from datetime import datetime

def validate_employee_hire_dates(employees_df):
    """
    Check hire dates.
    """

    invalid = employees_df[
        employees_df["hire_date"] > pd.Timestamp.today()
    ]

    if len(invalid) > 0:
        print(f"❌ Invalid hire dates: {len(invalid)}")
    else:
        print("✅ Hire dates are valid.")
        
        
        
def run_employee_validations(employees_df):
    """
    Run all employee validations.
    """

    print("\nRunning Employee Validations...\n")

    validate_employee_missing_values(employees_df)
    validate_employee_duplicate_emails(employees_df)
    validate_employee_duplicate_phones(employees_df)
    validate_employee_hire_dates(employees_df)

    print("\n✅ Employee validation completed.")