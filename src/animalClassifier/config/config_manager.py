from src.animalClassifier.constants import *
#we don't need to reference common file as it did in the init file
from src.animalClassifier.utils import read_yaml, create_directories
from src.animalClassifier.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        #config and file path were written in init file in constant
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        #defined in config file to create directory for model and data as artifact
        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self):
        #from config file to list all ingestion directories
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        #creating output directories
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config