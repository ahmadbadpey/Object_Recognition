from flask import Blueprint, Flask, request
import cv2 as cv
import numpy as np
import json, requests

prediction_blueprint = Blueprint('prediction_blueprint', __name__)


@prediction_blueprint.route('/predict', methods=['POST'])
def index():
    image = request.get_json().get('image')


    return {
        "success": True,
        "message": {}
    }
