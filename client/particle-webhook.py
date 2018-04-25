import sys
from json import JSONDecodeError
from flask import Flask, request, jsonify

import pyautogui
import time


class AppConfig:
    MIN_DELAY_BETWEEN_STROKES = 1.5
    EVENT_NAME = "restartButton"


app = Flask(__name__)
app.config.from_object(AppConfig)
app.start_time = time.time()

@app.route('/', methods=['POST'])
def hello_world_post():
    data = request.get_json()
    if "event" in data and data["event"] == AppConfig.EVENT_NAME:
        t = time.time()
        if (t - app.start_time) > AppConfig.MIN_DELAY_BETWEEN_STROKES:
            pyautogui.press('r')
            app.start_time = t
    return jsonify(data)

@app.route('/', methods=['GET'])
def hello_world_get():
    return 'Hello, GET World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5100, debug=True)
