import ipaddress
import json
import os
import ssl
import time

import adafruit_requests
import socketpool
import wifi
from src.draw import draw

TIME_URL = "https://timekeeper-py.onrender.com/timekeeper/time"
TIME_URL2 = "https://time.now/developer/api/timezone/America/Denver"


def main():
    nets = wifi.radio.start_scanning_networks()
    print(
        json.dumps(
            list(
                {"ssid": network.ssid, "rssi": network.rssi, "auth": network.authmode}
                for network in nets
            )
        )
    )

    print("Connecting to WiFi")

    #  connect to your SSID
    SSID = os.getenv("CIRCUITPY_WIFI_SSID")
    wifi.radio.connect(SSID, os.getenv("CIRCUITPY_WIFI_PASSWORD"))

    print("Connected to WiFi: ", SSID)

    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())

    #  prints MAC address to REPL
    print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

    #  prints IP address to REPL
    print("My IP address is", wifi.radio.ipv4_address)

    # Every N * 60 seconds
    draw_each_min = 10
    while True:
        try:
            # response = requests.get(url=TIME_URL).json()
            # the_time = response.get("datetime", "")
            timenow = requests.get(url=TIME_URL2).json()
            the_time = timenow["datetime"].replace("T", ".").split(".")
            draw(the_time[0] + " " + the_time[1])
        except Exception as e:
            print(str(e))
        time.sleep(draw_each_min * 60)
