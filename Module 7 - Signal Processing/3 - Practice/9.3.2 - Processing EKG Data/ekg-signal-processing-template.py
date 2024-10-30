import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = np.loadtxt(signal_filepath, delimiter=',', skiprows=2)
first_lead = signal[:3600,1]
second_lead = signal[:3600,2]

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

"""
Step 3: Pass data through weighted differentiator
"""

# Weighted differentiator
weighted_data_first = np.diff(first_lead)
weighted_data_second = np.diff(second_lead)
"""
Step 4: Square the results of the previous step
"""

squared_first = np.square(weighted_data_first)
squared_second = np.square(weighted_data_second)

"""
Step 5: Pass a moving filter over your data
"""

# Moving average filter
window_size = 10
moving_first = np.convolve(squared_first, np.ones(window_size) / window_size, mode='valid')
moving_second = np.convolve(squared_second, np.ones(window_size) / window_size, mode='valid')

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Signal Processing')
#plt.plot(first_lead, label='Original Signal for Lead 1')
#plt.plot(second_lead, label='Original Signal for Lead 2')
#plt.plot(weighted_data_first, label='Lead 1: Weighted')
#plt.plot(weighted_data_second, label='Lead 2: Weighted')
#plt.plot(squared_first, label='Lead 1: Squared')
#plt.plot(squared_second, label='Lead 2: Squared')
plt.plot(moving_first, label='Lead 1: Moving')
plt.plot(moving_second, label='Lead 2: Moving')
plt.xlabel('Sample #')
plt.ylabel('Voltage (mV)')
plt.legend()
plt.show()

