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
    new_data: dict = {key: mapping[key][value.lower()]
                      for key, value in data.items()}

    encoded_list: list = []
    for key, value in new_data.items():
        if key in ENCODER:
            le = ENCODER[key]
            encoded_list.append(le.transform([value]))

    labeled_list: list = [x[0] for x in encoded_list]

    return labeled_list


@app.post("/predict")
async def predict_edibility(features: dict):
    try:
        load_artifacts()
        transformed_features: list = transform_data(features)
        return "Poisonous" if MODEL.predict([transformed_features])[0] else "Edible"

    except Exception as e:
        raise e


if __name__ == '__main__':
    load_artifacts()
    # for i in ENCODER:
    #     print(ENCODER[i].classes_)

    d = {
        "cap-shape": "Bell",
        "cap-surface": "Smooth",
        "cap-color": "Brown",
        "bruises": "Yes",
        "odor": "Pungent",
        "gill-attachment": "Free",
        "gill-spacing": "Close",
        "gill-size": "Narrow",
        "gill-color": "Black",
        "stalk-shape": "Enlarging",
        "stalk-root": "Equal",
        "stalk-surface-above-ring": "Smooth",
        "stalk-surface-below-ring": "Smooth",
        "stalk-color-above-ring": "White",
        "stalk-color-below-ring": "White",
        "veil-type": "Partial",
        "veil-color": "White",
        "ring-number": "One",
        "ring-type": "Pendant",
        "spore-print-color": "Black",
        "population": "Scattered",
        "habitat": "Urban"
    }

    print(transform_data(d))