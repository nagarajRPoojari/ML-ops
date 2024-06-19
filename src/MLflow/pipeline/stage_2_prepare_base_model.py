from MLflow.config.configuration import ConfigurationManager
from MLflow.components.base_model import PrepareBaseModel
from MLflow import logger

STAGE_NAME= "STAGE-02 Preparing base model "

class PrepareBaseModelPipeline:
    def __init__(self) -> None:
        pass
    def main(self)-> None:
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModel()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e