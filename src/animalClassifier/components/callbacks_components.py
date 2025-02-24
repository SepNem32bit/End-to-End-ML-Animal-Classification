from src.animalClassifier.config import PrepareCallbacksConfig

import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    #this decorator makes this method as a hidden method which doesn't need () when it's called
    #tensorboard callback
    @property
    def _create_tb_callbacks(self):
        #it will create a timestamp where all logs are stored
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        #it creates a path including particular timestamp
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    #checkpoint model callabck
    @property
    def _create_ckpt_callbacks(self):
        checkpoint_path = str(self.config.checkpoint_model_filepath)
        #saved model path callback
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path,
            #only save the best model
            save_best_only=True
        )


    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]