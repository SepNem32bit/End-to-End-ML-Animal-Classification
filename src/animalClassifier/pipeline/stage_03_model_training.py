from src.animalClassifier.config import ConfigurationManager
from src.animalClassifier.components import PrepareCallback, Training
from src.animalClassifier import logger

class ModelTrainingPipeline():
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        #checkpoint model and tensorboard callabcks
        #to see the logs: tensorboard --logdir "directory"
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callback_list) #using the created callbacks
