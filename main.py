import numpy as np
import pywt
from scipy.io import loadmat
from scipy.stats import entropy 
from sklearn.model_selection import train_test_split 

def calculate_entropy(list_values):
    _, count = np.unique(list_values, return_counts=True)
    probabilities = count / np.len(list_values)
    entropy_of_list = entropy(probabilities)
    return [entropy_of_list]

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

def get_features(list_values):
    entropy_features = calculate_entropy(list_values) 
    statistical_features = calculate_statistics(list_values)
    crossings_features = calculate_crossings(list_values)
    return entropy_features + statistical_features + crossings_features

def get_ecg_features(ecg_data, ecg_labels, waveletname):
    list_features = [] 
    list_unique_labels = list(set(ecg_labels))
    list_labels = [list_unique_labels.index(elem) for elem in ecg_labels]
    for signal in ecg_data:
        list_coeff = pywt.wavedec(signal, waveletname)
        features = [] 
        for coeff in list_coeff:
            features += get_features(coeff)
        list_features.append(features)
    return list_features, list_labels

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
x_train, x_test, y_train, y_test = train_test_split(list_signals, list_labels, test_size=0.2, shuffle=True)
print(f"training size={len(x_train)}")
print(f"testing size={len(x_test)}")


'''
a = [1, 2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7, -10]
a = [1, 2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7]
a = [2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7, -10]
zero_crossings = a[1:] * a[:-1]
'''