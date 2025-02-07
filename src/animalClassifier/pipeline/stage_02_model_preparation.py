from src.animalClassifier.config import ConfigurationManager
from src.animalClassifier.components import PrepareBaseModel
from src.animalClassifier import logger


class ModelPreparationPipeline():
    def main(self):
        config = ConfigurationManager()
        model_preparation_config = config.get_prepare_base_model_config()
        model_preparation = PrepareBaseModel(config=model_preparation_config)
        model_preparation.get_base_model()
        model_preparation.update_base_model()
