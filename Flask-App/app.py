from __future__ import division, print_function
from flask.templating import render_template
from flask import Flask
# coding=utf-8
import sys
import json
import os
import glob
import re
import base64
import time
import pathlib
# Flask utils
from flask import Flask, redirect, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
app = Flask(__name__,template_folder='D:/Project_2/templates',static_folder='D:/Project_2/static')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        print("Got a Request!!")
        json_data=request.get_json();
        data_audio=json_data['file_1']
        data_audio=data_audio[data_audio.index(","):]
        decoded_data_audio=base64.b64decode((data_audio))
        audio_file = open('D:/Project_2/input/audio_1.wav', 'wb')
        audio_file.write(decoded_data_audio)
        audio_file.close()
        print("File Saved!!")
        # Model will runned and dialect will be shown.
        print("File encoding done!!")
        #time.sleep(10)
        return jsonify({'b64':'Hindi'})
    return None

if __name__=="__main__":
    app.run(debug=True)