import numpy as np
from train import trainModel

input_path = "data/final_dataset.csv"
target_path = "data/salary_final.csv"

test_input_path = "data/final_dataset.csv"
test_target_path = "data/salary_final.csv"

param_grid = {
            #  'reg__max_depth': np.arange(4, 16, 4),
            #  'reg__n_estimators': np.arange(20, 100, 20)
              }

# Model names:
#   - XGBRegressor ...............'XGBoost'
#   - RandomForestRegressor ......'RandomForest'
trainModel(input_path, target_path, test_input_path, test_target_path, grid=param_grid, model_name='LinearRegression',
           min_cut=100, max_cut=700000, cv=4, eval=True)
