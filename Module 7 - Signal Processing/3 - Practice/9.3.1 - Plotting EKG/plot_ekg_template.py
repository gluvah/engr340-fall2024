import matplotlib.pyplot as plt
import numpy as np

# Import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# Load data in matrix from CSV file; skip first two rows
data = np.loadtxt(path, delimiter=',', skiprows=2)

# Extract time and lead data
time = data[:, 0]
lead1 = data[:, 1]
lead2 = data[:, 2]

# Plot Lead 1 and Lead 2 against Time
plt.figure(figsize=(10, 6))
plt.plot(time, lead1, label='Lead 1', color='b')
plt.plot(time, lead2, label='Lead 2', color='r')

# Add titles and labels
plt.title("EKG Leads Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (mV)")
plt.legend()
plt.grid(True)


plt.show()