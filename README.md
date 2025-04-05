# Heart Digital Twin

A real-time ECG visualization and 3D beating heart model powered by the INTO-CPS Digital Twin as a Service (DTaaS) platform.

## Introduction

The Heart Digital Twin is an interactive simulation tool that provides real-time visualization of electrocardiogram (ECG) data alongside a synchronized 3D heart model. This application demonstrates the power of digital twin technology in medical visualization by combining:

- Real-time ECG signal processing and visualization
- Interactive 3D heart model with synchronized beating animation
- Configurable parameters to explore different patient records and ECG leads

Built on the INTO-CPS DTaaS platform, this application showcases how digital twins can provide insights into complex physiological systems, enabling better understanding and analysis of cardiac data.

## Screenshot

![Heart Digital Twin Screenshot](/DTaaS/screenshot.png)

## Hosted Demo

You can access a hosted demo of this application at: [Link](https://heart-digital-twin-deployed.onrender.com)

Note: We are using a free deployment service so it might take 10-15 seconds to load the heart model.

## Running the Application

### Prerequisites

- WSL (Windows Subsystem for Linux) or Linux environment
- Docker and Docker Compose
- Git
- A GitLab account

### Installation and Setup

Follow these steps to install and run the Heart Digital Twin application:

#### 1. Platform Installation (WSL or Linux)

1. Clone the repository and navigate to the project directory

2. Make the initialization script executable:
   ```bash
   chmod +x init.sh
   ```

3. Run the initialization script:
   ```bash
   ./init.sh
   ```
   - You will be prompted for your GitLab username
   - Enter the username associated with your GitLab account

4. Make the start script executable:
   ```bash
   chmod +x start.sh
   ```

5. Start the DTaaS platform:
   ```bash
   ./start.sh
   ```
   - This will initialize the Docker containers for the DTaaS platform
   - Wait until all services have started successfully

#### 2. Accessing the DTaaS Platform

1. Open your web browser and navigate to:
   ```
   http://localhost
   ```

2. Sign in using the same GitLab account you provided during initialization

3. After logging in, navigate to the "Digital Twins" tab

#### 3. Running the Heart Digital Twin

1. In the DTaaS interface, select "Open Tool → Terminal"

2. Navigate to the digital_twins directory under /DTaas/files/your-gitlab-username/digital_twins and activate the virtual environment:
   ```bash
   cd digital_twins
   source venv/bin/activate
   cd ..
   ```

3. Run the Heart Digital Twin application:
   ```bash
   python3 run.py
   ```

4. The Flask application (Heart Digital Twin) will start and be accessible through the DTaaS platform

5. Interact with the ECG visualization and 3D heart model through the provided interface

#### 4. Stopping the Application

1. To stop the Flask application, press `Ctrl+C` in the terminal window

2. To stop the DTaaS platform, run:
   ```bash
   ./stop.sh
   ```

## Features

- Real-time ECG visualization using data from the MIT-BIH Arrhythmia Database
- Interactive 3D beating heart model synchronized with ECG data
- Configurable ECG display parameters (record selection, lead selection, time window)
- Simulation controls (pause/resume, reset position)
- Automatic download and processing of ECG records

## Technical Details

This application is built using:
- Python with Flask for the backend server
- WebGL for 3D heart model visualization
- Matplotlib for ECG signal plotting
- WFDB library for ECG data processing
- The INTO-CPS DTaaS platform for hosting and integration

## License

This project is licensed under the MIT License - see the LICENSE file for details. 