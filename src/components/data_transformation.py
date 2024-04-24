import os
from src import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.entity.config_entity import (DataTransformationConfig)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self) -> None:
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2)

        train.to_csv(os.path.join(
            self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitting data into Training and Test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
