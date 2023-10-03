import numpy as np
import pywt
from scipy.io import loadmat

def calculate_entropy():
    pass 

def calculate_statistics(list_values):
    # get the 0th, 5th, 25th, 50th, 75th, and 95th percentiles
    n0 = np.nanpercentile(list_values, 0)
    n05 = np.nanpercentile(list_values, 5)
    n25 = np.nanpercentile()
    median = np.nanpercentile(list_values, 50)
    n75 = np.nanpercentile(list_values, 75)
    n95 = np.nanpercentile(list_values, 95)
    n100 = np.nanpercentile(list_values, 100)
    mean = np.nanmean(list_values)
    std = np.nanstd(list_values)
    var = np.nanstd(list_values)
    rms = np.nanmean(np.sqrt(list_values**2))
    return (n0, n05, n25, median, n75, n95, n100, mean, std, var, rms)

def calculate_crossings(list_values):
    zero_crossings = (np.diff(np.sign(list_values[list_values!=0]))!=0).sum()
    mean_diff = list_values - np.nanmean(list_values)
    mean_crossings = (np.diff(np.sign(mean_diff[mean_diff!=0]))!=0).sum()
    return (zero_crossings, mean_crossings)

def get_features():
    pass 

# read the ECG file 
filename = 'ECGData/ECGData.mat'
raw_data = loadmat(filename)
# raw data of size 162x65536
list_signals = raw_data['ECGData'][0][0][0]
# convert the labels into a list, 162 labels
list_labels = list(map(lambda x: x[0][0], raw_data['ECGData'][0][0][1]))
print(f"signals = {list_signals}")
print(f"signals shape = {list_signals.shape}")
print(f"labels = {list_labels}")
print(f"labels shape = {len(list_labels)}")



'''
a = [1, 2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7, -10]
a = [1, 2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7]
a = [2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7, -10]
zero_crossings = a[1:] * a[:-1]
'''