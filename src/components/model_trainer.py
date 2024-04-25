import pandas as pd
import os
from src import logger
from src.entity.config_entity import (ModelTrainerConfig)
from sklearn.ensemble import RandomForestClassifier
import joblib


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)

        train_x = train_data.drop([self.config.TARGET_COLUMN], axis=1)
        train_y = train_data[[self.config.TARGET_COLUMN]]

        clf = RandomForestClassifier(n_estimators=self.config.n_estimators)
        clf.fit(train_x, train_y)

        joblib.dump(clf, os.path.join(
            self.config.root_dir, self.config.model_name))
