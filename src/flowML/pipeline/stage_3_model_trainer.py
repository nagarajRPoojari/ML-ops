from flowML.config.configuration import ConfigurationManager
from flowML.components.model_trainer import Training
from flowML import logger

STAGE_NAME= "STAGE-03 model training "

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self)-> None:
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



