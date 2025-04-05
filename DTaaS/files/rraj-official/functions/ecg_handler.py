#!/usr/bin/env python3
"""
ECG Handler module for Heart Digital Twin
Manages the ECG data processing functions
"""
import os
import io
import base64
from threading import Lock
import numpy as np
import wfdb
import matplotlib.pyplot as plt

# Set the backend before importing matplotlib
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-interactive saving

# Import data handling functions
from data.record_loader import download_record, get_record_path

# Global variables to store ECG data
record_data = {}
current_position = 0
data_lock = Lock()  # Lock for thread safety

def init_ecg_data(record_name='100', window_seconds=5):
    """Initialize the ECG data from the specified record"""
    global record_data, current_position
    
    # Download the record if needed, stores in data folder
    if not download_record(record_name):
        print(f"Failed to download record {record_name}")
        return False
    
    # Get the record path in the data folder
    record_path = get_record_path(record_name)
    
    # Read the record
    print(f"Reading record {record_name} from {record_path}...")
    try:
        record = wfdb.rdrecord(record_path)
    except Exception as e:
        print(f"Error reading record: {e}")
        return False
    
    fs = record.fs  # Sampling frequency
    signal = record.p_signal  # The signal data
    
    # Get lead/channel names from the record
    channel_names = []
    print(f"Record signal names: {record.sig_name}")
    
    lead_descriptions = {
        'MLII': 'Modified Limb Lead II (MLII)',
        'V1': 'Precordial Lead V1',
        'V2': 'Precordial Lead V2',
        'V3': 'Precordial Lead V3',
        'V4': 'Precordial Lead V4',
        'V5': 'Precordial Lead V5',
        'V6': 'Precordial Lead V6',
        'aVR': 'Augmented Vector Right (aVR)',
        'aVL': 'Augmented Vector Left (aVL)',
        'aVF': 'Augmented Vector Foot (aVF)',
        'I': 'Lead I',
        'II': 'Lead II',
        'III': 'Lead III'
    }
    
    for i, sig_name in enumerate(record.sig_name):
        if sig_name in lead_descriptions:
            lead_description = f"Channel {i}: {lead_descriptions[sig_name]}"
        else:
            lead_description = f"Channel {i}: {sig_name}"
        
        channel_names.append(lead_description)
        print(f"Added channel: {lead_description}")
    
    with data_lock:
        record_data = {
            'signal': signal,
            'fs': fs,
            'n_samples': signal.shape[0],
            'window_size': int(fs * window_seconds),
            'channel': 0,  # Use first channel by default
            'channel_names': channel_names,  # Store channel names
            'record_name': record_name  # Store the record name
        }
        current_position = 0
    
    print(f"Record loaded: {record_data['n_samples']} samples, {signal.shape[1]} channels, {fs} Hz sampling rate")
    print(f"Available channels: {', '.join(channel_names)}")
    return True

def generate_plot():
    """Generate a plot for the current window of ECG data"""
    global current_position, record_data
    
    try:
        with data_lock:
            if not record_data or 'signal' not in record_data:
                print("No ECG data available for plotting")
                return None
                
            # Get the current window
            start = current_position
            window_size = record_data['window_size']
            end = start + window_size
            
            # Ensure we don't exceed the data length
            if end > record_data['n_samples']:
                end = record_data['n_samples']
                start = max(0, end - window_size)
                # Reset to beginning if we've reached the end
                if end == record_data['n_samples']:
                    current_position = 0
                else:
                    current_position = start
            else:
                # Move the window for next time
                current_position += int(window_size * 0.1)  # Overlap windows by 90%
            
            # Extract data for the current window
            channel = record_data['channel']
            data = record_data['signal'][start:end, channel]
            fs = record_data['fs']
            xdata = np.arange(start, end) / fs  # Time axis in seconds
            
            # Get current channel name for the title
            current_channel_name = "ECG Lead"
            if 'channel_names' in record_data and len(record_data['channel_names']) > channel:
                channel_name = record_data['channel_names'][channel]
                # Extract the part after the colon (if present)
                if ': ' in channel_name:
                    current_channel_name = channel_name.split(': ', 1)[1]
                else:
                    current_channel_name = channel_name
                print(f"Using channel name: {current_channel_name}")
            
            # Get record name
            record_name = record_data.get('record_name', 'Unknown')
        
        # Generate the plot with enhanced styling - use default fonts
        plt.rcParams.update({'font.size': 10})
        # Don't specify font family to use system defaults
        fig, ax = plt.subplots(figsize=(10, 4), dpi=100)
        
        # Plot the ECG with a better style
        ax.plot(xdata, data, color='#1a75ff', lw=1.5)
        
        # Add a grid that resembles ECG paper
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='#ff9999', alpha=0.3)
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='#ffcccc', alpha=0.2)
        ax.minorticks_on()
        
        # Customize appearance
        ax.set_facecolor('#f8f9fa')
        fig.patch.set_facecolor('#f8f9fa')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#dddddd')
        ax.spines['bottom'].set_color('#dddddd')
        
        # Add labels and title
        ax.set_xlabel("Time (s)", fontsize=10, color='#444444')
        ax.set_ylabel("Amplitude (mV)", fontsize=10, color='#444444')
        ax.set_title(f"DTaaS Heart Digital Twin - Record {record_name}, {current_channel_name}", fontsize=12, color='#333333', fontweight='bold')
        
        # Add time range information
        time_info = f"Time window: {xdata[0]:.1f}s - {xdata[-1]:.1f}s"
        ax.annotate(time_info, xy=(0.02, 0.97), xycoords='axes fraction', 
                   fontsize=8, color='#666666', verticalalignment='top')
        
        # Convert plot to PNG image with higher quality
        img = io.BytesIO()
        plt.tight_layout()
        fig.savefig(img, format='png', dpi=100, bbox_inches='tight')
        plt.close(fig)
        img.seek(0)
        
        return base64.b64encode(img.getvalue()).decode('utf-8')
        
    except Exception as e:
        print(f"Error in generate_plot: {e}")
        return None

def update_parameters(params):
    """Update the ECG display parameters"""
    global record_data, current_position
    
    try:
        with data_lock:
            if not record_data:
                return False, "No ECG data loaded"
                
            if 'channel' in params:
                channel = int(params['channel'])
                if 0 <= channel < record_data['signal'].shape[1]:
                    record_data['channel'] = channel
                else:
                    return False, f"Invalid channel. Must be 0-{record_data['signal'].shape[1]-1}"
            
            if 'window_seconds' in params:
                window_seconds = float(params['window_seconds'])
                if 1 <= window_seconds <= 60:
                    record_data['window_size'] = int(record_data['fs'] * window_seconds)
                else:
                    return False, "Window size must be between 1-60 seconds"
            
            if 'reset' in params and params['reset']:
                current_position = 0
                
            # Return current information
            return True, {
                "current_channel": record_data.get('channel', 0),
                "channel_names": record_data.get('channel_names', [])
            }
            
    except Exception as e:
        print(f"Error updating parameters: {e}")
        return False, str(e)

def get_current_info():
    """Get current record and channel information"""
    with data_lock:
        if not record_data:
            return False, "No ECG data loaded", {}
        
        return True, "Success", {
            "current_record": record_data.get('record_name', '100'),
            "current_channel": record_data.get('channel', 0),
            "channel_names": record_data.get('channel_names', [])
        } 