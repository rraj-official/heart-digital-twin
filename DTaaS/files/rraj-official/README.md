# Heart Digital Twin Application

A real-time ECG visualization and 3D heart model application for Digital Twin as a Service (DTaaS).

## Project Structure

The application is organized into the following modules:

- **common**: Configuration, constants, and utilities
- **data**: Data handling for ECG records - all records from MIT-BIH database are stored here
- **digital_twins**: Main application, Flask routes, and UI components
- **functions**: Core functionality implementations
- **models**: 3D model files
- **tools**: Helper functions for specific tasks

## Features

- Real-time ECG visualization using data from the MIT-BIH Arrhythmia Database
- Interactive 3D beating heart model
- Configurable ECG display parameters (record selection, lead selection, time window)
- Simulation controls (pause/resume, reset position)

## Data Storage

The application automatically downloads ECG records from the MIT-BIH Arrhythmia Database and stores them in the `data` folder. These records consist of:

- `.dat` files: Binary signal data
- `.hea` files: Header information

For more information about the MIT-BIH Arrhythmia Database, see: https://physionet.org/content/mitdb/

## Running the Application

To run the application, execute the `run.py` script in the root directory:

```bash
python run.py
```

The application will be accessible at http://localhost:5000.

## Requirements

The application will automatically install the required dependencies when first run:

- Python 3.6 or higher
- NumPy 1.20.3 or higher
- Pandas 1.3.0 or higher
- Matplotlib 3.4.0 or higher
- WFDB 4.1.0 or higher
- Flask 2.0.0 or higher 