import joblib
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('../../artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction
    

if __name__ == '__main__':
    obj = PredictionPipeline()
    print(obj.predict([[2,2,2,0,7,1,0,1,0,1,0,2,1,6,7,0,2,1,0,7,4,4]]))