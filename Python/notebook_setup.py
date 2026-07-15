"""
RetailIQ Notebook Setup

Initializes the notebook environment.
"""

import sys
from pathlib import Path

project_python = Path(__file__).resolve().parent

if str(project_python) not in sys.path:
    sys.path.insert(0, str(project_python))

print("✅ RetailIQ environment initialized.")
print(f"Project Path: {project_python}")