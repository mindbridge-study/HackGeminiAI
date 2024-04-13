import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Since the preview indicates a structured format, let's attempt to parse the data accordingly.
# We'll skip the initial metadata lines and parse the EEG data, focusing on one channel for simplicity.

# Define a function to parse the EEG data file
def parse_eeg_data(file_path):
    # Skip initial metadata lines
    data = pd.read_csv(file_path, delim_whitespace=True, comment='#', header=None, names=['Trial', 'Channel', 'Sample', 'Amplitude'])
    return data

# Parse the data
eeg_data = parse_eeg_data(file_path)

# For simplicity, let's plot the data for the first channel found in the dataset
first_channel = eeg_data['Channel'].unique()[0]
channel_data = eeg_data[eeg_data['Channel'] == first_channel]

# Plotting the amplitude of the first channel over its samples
plt.figure(figsize=(10, 6))
plt.plot(channel_data['Sample'], channel_data['Amplitude'], label=first_channel)
plt.xlabel('Sample')
plt.ylabel('Amplitude (uV)')
plt.title(f'EEG Data - Channel: {first_channel}')
plt.legend()
plt.grid(True)

# Save the plot to a file
plot_path = '/mnt/data/eeg_data_plot.png'
plt.savefig(plot_path)
plt.close()

plot_path
