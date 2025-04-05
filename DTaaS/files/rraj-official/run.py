#!/usr/bin/env python3
"""
Heart Digital Twin - Main Entry Point
Run this script to start the Heart Digital Twin application
"""
import os
import sys

# Add the current directory to the path so that modules can be imported
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Initialize the data directory
print("Initializing data directory...")
from data.initialize import ensure_data_directory
data_dir = ensure_data_directory()
print(f"Data directory initialized: {data_dir}")

# Import the main app from digital_twins module
from digital_twins.app import main

if __name__ == "__main__":
    print("Starting Heart Digital Twin Application...")
    main() 