"""
RetailIQ Export Utilities
-------------------------
Reusable functions for exporting DataFrames to CSV files.
"""

from pathlib import Path
import pandas as pd


def export_to_csv(
    df: pd.DataFrame,
    file_name: str,
    output_dir: Path
) -> None:
    """
    Export a DataFrame to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to export.

    file_name : str
        Name of the CSV file.

    output_dir : Path
        Directory where the CSV file will be saved.
    """

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create full file path
    file_path = output_dir / file_name

    # Export DataFrame
    df.to_csv(file_path, index=False)

    print("=" * 60)
    print("✅ Dataset exported successfully!")
    print(f"📁 File Name : {file_name}")
    print(f"📂 Location  : {file_path.resolve()}")
    print("=" * 60)