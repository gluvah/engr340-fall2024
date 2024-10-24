
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
data = np.loadtxt(path, delimiter = ',',skiprows=2)



# save each vector as own variable
num_rows = data.shape[0]
vectors = [data[i, :] for i in range(num_rows)]
# use matplot lib to generate a single

### Your code here ###
for i in range(num_rows):  # Plot the first 5 rows (or all rows if less than 5)
    plt.plot(vectors[i:2], label=f'Row {i+1}')

plt.title("First few rows of data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.legend()
plt.show()

for vec in vectors:
    time = vec[0]
    lead1 = vec[1]
    lead2 = vec[2]

    # For each row, plot lead1 and lead2 against time
    plt.plot(time, lead1, 'b.', label='Lead 1' if vectors.index(vec) == 0 else "")
    plt.plot(time, lead2, 'r.', label='Lead 2' if vectors.index(vec) == 0 else "")

# Add titles and labels
plt.title("ECG Leads Over Time (row by row)")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (mV)")  