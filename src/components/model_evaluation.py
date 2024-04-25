import os
import pandas as pd
from sklearn.metrics import classification_report
from src.utils.common import save_json
import joblib
from src.entity.config_entity import (ModelEvaluationConfig)
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def save_results(self) -> None:
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        predictions = model.predict(test_x)

        eval_report = classification_report(
            test_y, predictions, output_dict=True)

        save_json(path=Path(self.config.metric_file_name), data=eval_report)
