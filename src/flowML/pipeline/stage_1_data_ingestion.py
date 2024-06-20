from flowML.config.configuration import ConfigurationManager
from flowML.components.data_ingestion import DataIngestion
from flowML import logger

STAGE_NAME= "STAGE-01 Data ingestion "

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    def main(self)-> None:
        try:
            config= ConfigurationManager()
            data_ingestion_config= config.get_data_ingestion_config()
            data_ingestion= DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e