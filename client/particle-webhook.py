import sys
from json import JSONDecodeError
from flask import Flask, request, jsonify
import pyautogui
import time

from client.config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)
app.start_time = time.time()


def react(event, react_callback):
    data = request.get_json()
    if "event" in data and data["event"] == event:
        t = time.time()
        if (t - app.start_time) > AppConfig.MIN_DELAY_BETWEEN_STROKES:
            react_callback()
            app.start_time = t
    return jsonify(data)


@app.route('/restart', methods=['POST'])
def restart():
    return react(AppConfig.RESTART_EVENT, lambda: pyautogui.press('r'))


@app.route('/pause', methods=['POST'])
def pause():
    return react(AppConfig.PAUSE_EVENT, lambda: pyautogui.press('space'))


@app.route('/', methods=['GET'])
def hello_world_get():
    return 'Hello, GET World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=AppConfig.PORT, debug=True)
