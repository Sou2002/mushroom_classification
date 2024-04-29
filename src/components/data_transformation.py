import os
from src import logger
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from src.entity.config_entity import (DataTransformationConfig)
import joblib


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_path)

    def label_encoding(self) -> None:
        label_encoders: dict = {}

        for col in self.data.columns:
            le = LabelEncoder()
            self.data[col] = le.fit_transform(self.data[col])
            label_encoders[col] = le

        joblib.dump(label_encoders, os.path.join(
            self.config.root_dir, self.config.encoder_name))

    def train_test_splitting(self) -> None:
        train, test = train_test_split(self.data, test_size=0.2)

        train.to_csv(os.path.join(
            self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitting data into Training and Test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
