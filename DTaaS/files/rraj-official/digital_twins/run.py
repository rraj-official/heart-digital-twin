#!/usr/bin/env python3
"""
This file provides backward compatibility with the original structure.
It simply imports and runs the main function from app.py.
"""
import os
import sys

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Initialize the data directory
print("Initializing data directory...")
from data.initialize import ensure_data_directory
data_dir = ensure_data_directory()
print(f"Data directory initialized: {data_dir}")

from app import main

if __name__ == "__main__":
    main()
