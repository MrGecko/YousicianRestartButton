import sys
from json import JSONDecodeError
from flask import Flask, request, jsonify
from config import AppConfig
import pyautogui
import time



app = Flask(__name__)
app.config.from_object(AppConfig)
app.start_time = time.time()

@app.route('/restart', methods=['POST'])
def restart():
    data = request.get_json()
    if "event" in data and data["event"] == AppConfig.RESTART_EVENT:
        t = time.time()
        if (t - app.start_time) > AppConfig.MIN_DELAY_BETWEEN_STROKES:
            pyautogui.press('r')
            app.start_time = t
    return jsonify(data)

@app.route('/pause', methods=['POST'])
def pause():
    data = request.get_json()
    if "event" in data and data["event"] == AppConfig.RESTART_EVENT:
        t = time.time()
        if (t - app.start_time) > AppConfig.MIN_DELAY_BETWEEN_STROKES:
            pyautogui.press('space')
            app.start_time = t
    return jsonify(data)

@app.route('/', methods=['GET'])
def hello_world_get():
    return 'Hello, GET World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=AppConfig.PORT, debug=True)
