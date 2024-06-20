from flowML.config.configuration import ConfigurationManager
from flowML.components.model_evaluation import Evaluation
from flowML import logger

STAGE_NAME= "STAGE-04 model evaluation "

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self)-> None:
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()

        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = Evaluation()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

