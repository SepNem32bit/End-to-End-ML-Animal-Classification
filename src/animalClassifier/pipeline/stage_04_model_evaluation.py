from src.animalClassifier.config import ConfigurationManager
from src.animalClassifier.components import Evaluation
from src.animalClassifier import logger

class ModelEvaluationPipeline:
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()