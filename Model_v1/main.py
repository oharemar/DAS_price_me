import numpy as np
from train import trainModel

input_path = 'mirek_data_2/2019_instances_version_2.npy'
target_path = 'mirek_data_2/2019_labels_version_2.npy'

param_grid = {
              'reg__max_depth': np.arange(5, 20, 5),
              'reg__n_estimators': np.arange(40, 120, 10)
              }

# Model names:
#   - XGBRegressor ...............'XGBoost'
#   - RandomForestRegressor ......'RandomForest'
trainModel(input_path, target_path, grid=param_grid, model_name='XGBoost', min_cut=300, max_cut=20000000, cv=3, eval=True)
