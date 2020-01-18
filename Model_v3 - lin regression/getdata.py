import numpy as np
import pandas as pd

# loads data from path and return train, test samples
# input_path...relative path to the input data
# target_path...relative path to the target values
def GetTrainData(input_path, target_path):
    print(".....Loading input data from: ", input_path)
    inpt = pd.read_csv(input_path, sep= ';')
    inpt = inpt.drop(columns=['Country'])
    print(".....Loading targets from: ", target_path)
    target = pd.read_csv(target_path, sep= ';')
    target_norm = target['Normalized']
    target = target['Salary']
    print("Done.")
    return inpt, target, target_norm


# loads data from path and return train, test samples
# input_path...relative path to the input data
# target_path...relative path to the target values
def GetTestData(test_input_path, test_target_path):
    print(".....Loading input data from: ", test_input_path)
    inpt = pd.read_csv(test_input_path, sep= ';')
    country = inpt['Country']
    inpt = inpt.drop(columns=['Country'])
    print(".....Loading targets from: ", test_target_path)
    target = pd.read_csv(test_target_path, sep= ';')
    target = target['Salary']
    print("Done.")
    return inpt, country, target


# cuts X input set and y output set for y in (min,max)
# X.....input data
# y.....target
# min...min value for y
# max...max value for y
def Cuts(X, y, target, min_cut=300, max_cut=950000):
    print(".....Applying cuts from {min} to {max}.".format(min=min_cut, max=max_cut))
    print(".....Original shape: ", X.shape, y.shape)
    X = X[target < max_cut]
    y = y[target < max_cut]
    X = X[target > min_cut]
    y = y[target > min_cut]
    print(".....New shape: ", X.shape, y.shape)
    return X, y

