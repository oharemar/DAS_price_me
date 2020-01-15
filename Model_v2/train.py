from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from getdata import GetTrainData, GetTestData,Cuts
from sklearn.model_selection import train_test_split
import pickle
import math
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

def real_output(y_norm, coef_path):
    coefs = pd.read_csv(coef_path, sep=';')
    coefs = coefs['Coef'].values
    y_pred = y_norm * coefs

    return y_pred

def evaluate_model(model, test_input_path, test_target_path, model_name = 'XGB'):

    X_test, country, y_test = GetTestData(test_input_path, test_target_path)
    y_pred_norm = model.predict(X_test)
    y_pred = real_output(y_pred_norm, test_target_path)
    plt.hist2d(y_pred, y_test.values, 50, cmin=5)
    x = np.arange(y_test.values.min(), y_test.values.max())
    plt.plot(x, x, color='red')
    plt.xlabel("estimated salary")
    plt.ylabel("true salary")
    plt.axis('scaled')
    print(".....Saving {img}.....".format(img='{model}_2dhist.png'))
    plt.savefig('{model}_2dhist.png'.format(model=model_name))
    print("..... RMSE = ", math.sqrt(mse(y_pred, y_test.values)))
    print("..... MAE  = ", mae(y_pred, y_test.values))
    print("Done.")


def trainModel(input_path, target_path, test_input_path, test_target_path, grid, model_name='XGBoost', min_cut=0, max_cut=99999999, cv=3, eval = False):

    if model_name=='XGBoost':
        model = XGBRegressor(objective='reg:squarederror')
    elif model_name=='RandomForest':
        model = RandomForestRegressor()
    else:
        print("... Unknown model name ...")
        return 0

    inpt, target, target_norm = GetTrainData(input_path, target_path)
    col_num = ['Years Coding', 'Years Coding professional', 'Career Satisfaction', 'Age']
    cat_feature_cols = list(inpt)
    for c in col_num:
        cat_feature_cols.remove(c)

    column_transformer = ColumnTransformer(
        [
        #('imputer_num', SimpleImputer(missing_values=np.nan, strategy='median'), col_num),
        #('imputer_cat', SimpleImputer(missing_values=np.nan, strategy='most_frequent'), cat_feature_cols),
         ('onehot', OneHotEncoder(handle_unknown='ignore'), cat_feature_cols)], remainder='passthrough')

    pipeline_steps = [('col_trans', column_transformer), ('reg', model)]
    pipe = Pipeline(pipeline_steps)

    X_train, X_test, y_train, y_test = train_test_split(inpt, target_norm, test_size=0.00, random_state=666)
    #X_train, y_train = Cuts(X_train, y_train, min_cut, max_cut)
    print(".....Training {m} on {t} training samples.".format(m=model_name, t=y_train.size))
    print(".....Applying GridSearchCV on {m} with grid {g}.".format(m=model_name, g=grid))

    model_full0 = GridSearchCV(pipe, grid, scoring='neg_mean_squared_error', cv=cv,
                               iid=False, verbose=10).fit(X_train, y_train)
    print(".....Best params ...", model_full0.best_params_)

    with open('encoder.pickle', 'wb') as f:
        pickle.dump(column_transformer, f)

    model_final = model_full0.best_estimator_
    print(".....Saving {m}.".format(m=model_name))
    pickle.dump(model_final, open("model_price_me.dat", "wb"))

    if eval:
        evaluate_model(model_final, test_input_path, test_target_path, model_name='XGB')
    else:
        print("Done.")


