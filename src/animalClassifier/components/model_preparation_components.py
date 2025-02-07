import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from src.animalClassifier.entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        #not the config file
        #retreiving all params and config from the config method
        self.config = config

    #download and save the base model with the defined configuration
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)

    
    #it won't be considered as class method and won't need self
    @staticmethod
    def _prepare_updated_model(model, classes, freeze_all, freeze_till, learning_rate):
        #If freeze_all is True, it means we do not want to train any layers in the pretrained model.
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        #When using a pretrained model (like ResNet, VGG, or MobileNet), the last layer usually outputs a multi-dimensional feature map. 
        # However, for classification tasks, we typically need a 1D vector that can be fed into a fully connected (Dense) layer. 
        # The Flatten() layer helps us do this transformation.
        #converts the multidimensional output into a 1D vector so it can be fed into a dense layer.
        flatten_in = tf.keras.layers.Flatten()(model.output)
        #adding layers to customize to our data
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model



    def update_base_model(self):
        self.full_model = self._prepare_updated_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)