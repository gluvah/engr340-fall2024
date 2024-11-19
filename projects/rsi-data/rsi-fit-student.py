import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""

file_path = '/Users/michaelglover/Documents/GitHub/repoengr340/data/drop-jump/all_participant_data_rsi.csv'
data = pd.read_csv(file_path)

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')
# Step 1: Calculate the mean (mu) and standard deviation (std) for each
force_plate = data['force_plate_rsi']
accelerometer = data['accelerometer_rsi']
mu_fp, std_fp = np.mean(force_plate),np.std(force_plate)
mu_acc, std_acc = np.mean(accelerometer),np.std(accelerometer)
print(f"Force Plate - Mean: {mu_fp:.3f}, Std Dev: {std_fp:.3f}")
print(f"Accelerometer - Mean: {mu_acc:.3f}, Std Dev: {std_acc:.3f}")
# Step 2: Generate x-values for plotting the normal distribution
x_fp = np.linspace(mu_fp - 4 * std_fp, mu_fp + 4 * std_fp, 1000)
x_acc = np.linspace(mu_acc - 4 * std_acc, mu_acc + 4 * std_acc, 1000)
#This will ensure +- 4 std dev. from the mean
# Step 3: Use scipy to generate the normal distribution curve for each
y_fp = norm.pdf(x_fp, mu_fp, std_fp)
y_acc = norm.pdf(x_acc, mu_acc, std_acc)
# Step 4: Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_fp, y_fp, label='Force Plate RSI', color='blue')
plt.plot(x_acc, y_acc, label='Accelerometer RSI', color='red')
plt.xlabel('RSI Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution Fit for RSI Data (Force Plate vs Accelerometer)')
plt.legend()
plt.grid(True)
plt.show()
"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')
bins = np.linspace(0, 2, 10)
bins = np.concatenate(([-np.inf], bins, [np.inf]))
alpha = 0.05
"""
Acceleration
"""
### YOUR CODE HERE


"""
Force Plate
"""
### YOUR CODE HERE

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE

"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE