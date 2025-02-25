import os
import tensorflow as tf
from dataclasses import dataclass
from pathlib import Path

from src.animalClassifier.config import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
    
    def train_valid_generator(self):


        #we will use this dictionary as an argument
        #kwargs stands for keyword arguments in Python. It allows functions to accept an arbitrary number of named arguments as a dictionary.
        datagenerator_kwargs = dict(
            #Raw image pixel values range from 0 to 255 (for 8-bit images).
            #By multiplying by 1./255, the values are scaled to the [0,1] range.
            rescale = 1./255,
            #Splits the dataset into training (80%) and validation (20%).
            validation_split=0.20
        )

        
        dataflow_kwargs = dict(
            #Resize images
            #224x224
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            #Resampling method for resizing
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs)

        #loading validation data
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            # No shuffling for validation
            shuffle=False,
            **dataflow_kwargs
        )
          



        #if augumentatio is True  
        #all augumnetation settings
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs)
        else:
            #it is used again to load the training data from the same directory as the validation set
            train_datagenerator = valid_datagenerator


       #Creating Training Data Generator
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            #we will shuffle the training data
            shuffle=True,
            **dataflow_kwargs)




    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self, callback_list: list):
        #This divides and calculates the number of batches (or "steps") in one epoch. 
        #It's computed as the total number of training samples divided by the batch size of self.train_generator.
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            #Defines how many batches of validation data will be processed in each epoch.
            #Limits the number of validation batches per epoch.
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )