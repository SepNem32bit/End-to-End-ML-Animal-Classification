# Flask: The web framework used to create a web application.
# request: Used to handle incoming HTTP requests (e.g., POST requests with image data).
# jsonify: Converts Python objects (like dictionaries) into JSON format for API responses.
# render_template: Renders HTML pages (e.g., index.html).
# CORS: Handles Cross-Origin Resource Sharing (CORS) to allow frontend applications to communicate with this API.

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.animalClassifier.utils import decodeImage
from src.animalClassifier.pipeline.stage_prod_prediction import AnimalPredict

#Ensures that the system uses UTF-8 encoding to handle special characters correctly.
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

#Initializing Flask Application
app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        #The image filename is set to a default value.
        self.filename = "inputImage.jpg"
        self.classifier = AnimalPredict(self.filename)



#It listens for GET requests at the root URL (/).
#When someone visits http://localhost:8080/, it renders an HTML file called index.html.
#This file is expected to be in a templates folder inside the project.
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    #The function render_template() searches for an HTML file in the templates directory.
    return render_template('index.html')


#When a request is sent to /train, the script triggers the training pipeline by running main.py.
@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    #run the main.py for triggering the pipeline
    os.system("python main.py")
    return "Training done successfully!"




@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    # Receives an image as a base64 string from a POST request.
    image = request.json['image']
    # Decodes the image and saves it using decodeImage().
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    # Returns the prediction as a JSON response.
    return jsonify(result)

#Runs the application on all available network interfaces (0.0.0.0) so it can be accessed externally.
#Uses port 8080.
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)