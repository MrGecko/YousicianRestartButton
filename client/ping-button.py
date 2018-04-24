import sys
from json import JSONDecodeError
from queue import Queue

import requests
import pyautogui
import time

CONFIG = {
    "BASE_URL":"https://api.particle.io/v1/devices",
    "ACCESS_TOKEN": "",
    "DEVICE_ID": ""
}


def curl_var(var_name):
    url = "{BASE_URL}/{DEVICE_ID}/{VAR_NAME}?access_token={ACCESS_TOKEN}".format(**CONFIG, VAR_NAME=var_name)
    data = requests.get(url)

    response = None

    try:
        j = data.json()
        if "result" in j:
            response = j["result"]
    except JSONDecodeError:
        pass

    return response


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise ValueError("./ping-button.py {DEVICE_ID} {ACCESS_TOKEN}")

    CONFIG["DEVICE_ID"] = sys.argv[1]
    CONFIG["ACCESS_TOKEN"] = sys.argv[2]

    MIN_DELAY_BETWEEN_STROKES = 3
    start_time = time.time()

    event_queue = Queue()

    while True:

        button_state = curl_var("resBtnState")

        if button_state is not None:

            event_queue.put(int(button_state) == 1)
            t = time.time()

            if (t - start_time) > MIN_DELAY_BETWEEN_STROKES:
                if not event_queue.empty() and event_queue.get():
                    pyautogui.press('r')
                    event_queue = Queue()
                    start_time = t

        time.sleep(0.1)