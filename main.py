from src.animalClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.animalClassifier.pipeline.stage_02_model_preparation import ModelPreparationPipeline
from src.animalClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.animalClassifier import logger

STAGE_NAME="Data Ingestion Stage 1"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nEnd of the Stage")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Model Preparation Stage 2"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_preparation = ModelPreparationPipeline()
   model_preparation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nEnd of the Stage")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME="Model Training Stage 3"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_training = ModelTrainingPipeline()
   model_training.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nEnd of the Stage")
except Exception as e:
        logger.exception(e)
        raise e