import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class AnimalPredict():
    def __init__(self,filename):
        self.filename =filename

    def predictiondogcat(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        #loading a new image for classification
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        #Deep learning models in Keras expect batched input, even when predicting on a single image. Most models are trained on batches of images
        #Since Keras models expect a batch of images, we need to expand the dimensions to include a batch size of 1, resulting in:
        # (1, height, width, channels)  # e.g., (1, 224, 224, 3)
        test_image = np.expand_dims(test_image, axis = 0)
        #model predicition 
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'dog'
            return [{ "image" : prediction}]
        else:
            prediction = 'cat'
            return [{ "image" : prediction}]