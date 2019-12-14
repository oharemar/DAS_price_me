from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from getdata import GetData, Cuts
import pickle
import math
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from matplotlib import pyplot as plt
import numpy as np


def trainModel(input_path, target_path, grid, model_name='XGBoost', min_cut=300, max_cut=500000, cv=3, eval = False):

    if model_name=='XGBoost':
        model = XGBRegressor(objective='reg:squarederror')
    elif model_name=='RandomForest':
        model = RandomForestRegressor()
    else:
        print("... Unknown model name ...")
        return 0

    X_train, X_test, y_train, y_test = GetData(input_path, target_path, size=0.10)
    X_train, y_train = Cuts(X_train, y_train, min_cut, max_cut)
    print(".....Training {m} on {t} training samples.".format(m=model_name, t=y_train.size))
    print(".....Applying GridSearchCV on {m} with grid {g}.".format(m=model_name, g=grid))
    model_full0 = GridSearchCV(model, grid, scoring='neg_mean_squared_error', cv=cv,
                               iid=False, verbose=10).fit(X_train, y_train)
    print(".....Best params ...", model_full0.best_params_)

    model_final = model_full0.best_estimator_
    print(".....Saving {m}.".format(m=model_name))
    pickle.dump(model_final, open("model_price_me.dat", "wb"))

    if eval:
        plt.hist2d(model_final.predict(X_test), y_test, 15, cmin=5)
        x = np.arange(min(y_test), max(y_test))
        plt.plot(x, x, color='red')
        plt.xlabel("estimated salary")
        plt.ylabel("true salary")
        plt.axis('scaled')
        print(".....Saving {img}.....".format(img='{model}_2dhist.png'))
        plt.savefig('{model}_2dhist.png'.format(model=model_name))
        print("..... RMSE = ", math.sqrt(mse(model_final.predict(X_test), y_test)))
        print("..... MAE  = ", mae(model_final.predict(X_test), y_test))
        print("Done.")
    else:
        print("Done.")
