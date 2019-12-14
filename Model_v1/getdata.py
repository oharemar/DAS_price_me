import numpy as np
from sklearn.model_selection import train_test_split


# loads data from path and return train, test samples
# input_path...relative path to the input data
# target_path...relative path to the target values
def GetData(input_path, target_path, size=0.15):
    print(".....Loading input data from: ", input_path)
    inpt = np.load(input_path)
    print(".....Loading targets from: ", target_path)
    target = np.load(target_path)
    print(".....Getting training and testing samples.")
    X_train, X_test, y_train, y_test = train_test_split(inpt, target, test_size=size, random_state=666)
    print("Done.")
    return X_train, X_test, y_train, y_test


# cuts X input set and y output set for y in (min,max)
# X.....input data
# y.....target
# min...min value for y
# max...max value for y
def Cuts(X, y, min_cut=300, max_cut=500000):
    print(".....Applying cuts from {min} to {max}.".format(min=min_cut, max=max_cut))
    print(".....Original shape: ", X.shape, y.shape)
    X = X[y < max_cut]
    y = y[y < max_cut]
    X = X[y > min_cut]
    y = y[y > min_cut]
    print(".....New shape: ", X.shape, y.shape)
    return X, y
