#!/usr/bin/env python3
"""
Heart Digital Twin - ECG Visualization with Flask
This script runs a Flask server displaying a live ECG from the MIT-BIH Arrhythmia Database
"""
import sys
import os
import platform

# Import the setup module
from functions.setup import install_dependencies

try:
    import numpy as np
    # Check NumPy version
    np_version = np.__version__
    if tuple(map(int, np_version.split('.'))) < (1, 20, 3):
        print(f"NumPy version {np_version} is too old. Upgrading...")
        install_dependencies()
        # Reload NumPy after installation
        import importlib
        importlib.reload(np)
    
    # Now try to import the other dependencies
    import wfdb
    import matplotlib.pyplot as plt
    from flask import Flask
    
except ImportError as e:
    print(f"Error importing required libraries: {e}")
    install_dependencies()
    # Import the libraries again after installation
    import numpy as np
    import wfdb
    import matplotlib.pyplot as plt
    from flask import Flask

# Import application components
from functions.ecg_handler import init_ecg_data
from functions.routes import register_routes

# Get the absolute path to the static folder
current_dir = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(current_dir, 'static')
print(f"Using static folder: {static_folder}")

# Create Flask app with the static folder set to digital_twins/static
app = Flask(__name__, static_url_path='/static', static_folder=static_folder)

def main():
    # Initialize ECG data
    if not init_ecg_data(record_name='100', window_seconds=5):
        print("Failed to initialize ECG data. Exiting.")
        return
    
    # Register all routes
    register_routes(app)
    
    # Run the Flask server
    print("Starting Flask server...")
    host = '0.0.0.0'  # Listen on all interfaces
    port = 5000
    print(f"Server running at http://localhost:{port}")
    print(f"If running in WSL, access from Windows at http://localhost:{port} or http://<WSL-IP-address>:{port}")
    app.run(host=host, port=port, debug=False, threaded=True)

if __name__ == "__main__":
    main() 