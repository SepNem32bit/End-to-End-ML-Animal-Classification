from src.animalClassifier.config import ConfigurationManager
from src.animalClassifier.components import DataIngestion
from src.animalClassifier import logger


class DataIngestionPipeline():
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()