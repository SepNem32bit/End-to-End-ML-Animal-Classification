from src.animalClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.animalClassifier import logger

STAGE_NAME="data ingestion stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nEnd of the Stage")
except Exception as e:
        logger.exception(e)
        raise e
