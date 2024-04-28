from fastapi import FastAPI
from src.config.configuration import ConfigurationManager
import joblib
import os
from src.utils.column_mapping import mapping


app = FastAPI()


def load_artifacts() -> None:
    global ENCODER
    global MODEL

    config = ConfigurationManager()

    encoder_config = config.get_data_transformation_config()
    ENCODER = joblib.load(os.path.join(
        encoder_config.root_dir, encoder_config.encoder_name))

    model_config = config.get_model_trainer_config()
    MODEL = joblib.load(os.path.join(
        model_config.root_dir, model_config.model_name))


def transform_data(data: dict) -> list[int]:
    new_data = {key: mapping[key][value.lower()] for key, value in data.items()}
    return ENCODER.transform(new_data.values())


@app.post("/predict")
def predict_edibility(features: dict) -> str:
    load_artifacts()
    transformed_features = transform_data(features)
    return "Poisonous" if MODEL.predict([transformed_features])[0] else "Edible"