import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=None)

# Average CV score on the training set was: 0.8394679030404459
exported_pipeline = XGBClassifier(learning_rate=0.01, max_depth=8, min_child_weight=20, n_estimators=100, nthread=1, subsample=0.45)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
