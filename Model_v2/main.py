import numpy as np
from train import trainModel

input_path = "data/final_dataset.csv"
target_path = "data/salary_final.csv"

test_input_path = "data/final_dataset.csv"
test_target_path = "data/salary_final.csv"

param_grid = {
              'reg__max_depth': np.arange(6, 8, 2),
              'reg__n_estimators': np.arange(20, 30, 10)
              }

# Model names:
#   - XGBRegressor ...............'XGBoost'
#   - RandomForestRegressor ......'RandomForest'
trainModel(input_path, target_path, test_input_path, test_target_path, grid=param_grid, model_name='XGBoost',
           min_cut=300, max_cut=20000000, cv=2, eval=True)
