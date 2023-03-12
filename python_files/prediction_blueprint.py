from flask import Blueprint, Flask, request
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input

from keras.applications import VGG16

import cv2 as cv
import numpy as np
import json, requests
import logging

prediction_blueprint = Blueprint('prediction_blueprint', __name__)

vgg16Model = VGG16(weights="imagenet")


@prediction_blueprint.route('/predict', methods=['POST'])
def index():
    image = request.get_json().get('image')

    pro_image = preprocess_image('uploads/' + image)

    pred = vgg16Model.predict(pro_image)

    output = decode_predictions(pred)

    logging.warning(output[0][0])

    resultTuple = output[0][0]

    return {
        "success" : True,
        "message" : {
            "category" : resultTuple[0],
            "name" : resultTuple[1],
            "prob" : str(resultTuple[2])
        }
    }


def preprocess_image(address):
    img = cv.imread(address)
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    final_image = cv.resize(rgb_img, (224, 224))
    final_image = np.asarray(final_image)

    input_sample = np.expand_dims(final_image, axis=0)
    samples = preprocess_input(input_sample)

    return samples
