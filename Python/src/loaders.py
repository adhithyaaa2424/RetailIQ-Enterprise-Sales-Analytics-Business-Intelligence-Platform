"""
RetailIQ Data Loaders

Contains reusable ETL loading functions.
"""

import pandas as pd

from src.database import get_engine


def load_dataframe(
    df: pd.DataFrame,
    table_name: str,
    schema: str = "retail",
    if_exists: str = "append",
) -> None:
    """
    Load a DataFrame into PostgreSQL.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to load.

    table_name : str
        Target table name.

    schema : str
        Database schema.

    if_exists : str
        append / replace / fail
    """

    engine = get_engine()

    df.to_sql(
        name=table_name,
        schema=schema,
        con=engine,
        if_exists=if_exists,
        index=False,
        method="multi",
    )

    print(f"✅ Loaded {len(df)} rows into {schema}.{table_name}")