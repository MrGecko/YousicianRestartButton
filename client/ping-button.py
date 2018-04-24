import sys
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
    j = data.json()
    if "result" in j:
        return j["result"]
    else:
        #raise ValueError("Cannot fetch value for variable '{0}': {1}".format(var_name, j))
        return None


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
                    print(button_state)

        time.sleep(0.1)