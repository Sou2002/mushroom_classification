from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src import logger


STAGE_NAME = "Model Evaluation stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_evaluation_config = config.get_model_evaluation_config()
        data_evaluation = ModelEvaluation(config=data_evaluation_config)
        data_evaluation.save_results()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {
                    STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
