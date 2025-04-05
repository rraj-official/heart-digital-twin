#!/usr/bin/env python3
"""
WSGI entry point for the Heart Digital Twin application
Used for production deployments with Gunicorn
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

# Import app and initialize it
from digital_twins.app import app, init_ecg_data, register_routes

# Initialize ECG data
init_ecg_data(record_name='100', window_seconds=5)

# Register all routes
register_routes(app)

# Application variable for gunicorn
application = app

# For local testing
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port) 