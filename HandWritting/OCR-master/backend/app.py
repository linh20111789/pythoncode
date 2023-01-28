from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json

from ocr.ocr import save_file, predict
from ocr.test import predict_crnn

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import requests
import tensorflow.compat.v1.keras.backend as K


# All the 1000 imagenet classes
class_labels = 'imagenet_classes.json'

# Read the json
# with open('imagenet_classes.json', 'r') as fr:
# 	json_classes = json.loads(fr.read())

app = Flask(__name__)

# Allow 
CORS(app)

# Path for uploaded images
UPLOAD_FOLDER = 'data/'

# Allowed file extransions
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello():
	return "Hello World!"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		print("request data", request.data)
		print("request files", request.files)

		# check if the post request has the file part
		if 'file' not in request.files:
			return "No file part"
		file = request.files['file']
		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			
			_, temp = filename.split("_")
			model, temp = temp.split(".")
			print(model)
			print(filename)
			if(model=="transformer"):
			# Send uploaded image for prediction
				predicted_image_class = predict_img(UPLOAD_FOLDER+filename)
				print("predicted_image_class", predicted_image_class)
			else:
				predicted_image_class = predict_crnn()				
				print("predicted_image_class", predicted_image_class)
			test = "Cleaning image data"
			print(test)
			remove_file('./data')
	
	return json.dumps(predicted_image_class)

def predict_img(img_path):
	output = './test'
	lines = predict('data/img_transformer.png', output)
	print(img_path)
	print("out", lines)
	save_file('./result/result.txt', lines)
	save_file('../frontend/src/result/result.txt', lines)

	return lines

def remove_file(path):
	for f in os.listdir(path):
		os.remove(os.path.join(path,f))


if __name__ == "__main__":
	app.run(debug=True, threaded=False)