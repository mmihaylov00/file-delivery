import json
import subprocess
import time

import socketio

with open('config.json', 'r') as f:
    data = json.load(f)

ip = data["ip"]
port = data["port"]
fileName = data["fileName"]
clientName = data["clientName"]
scriptName = data["scriptName"]

sio = socketio.Client()
running = False


@sio.event
def disconnect():
    sio.disconnect()


@sio.on('start')
def on_start():
    global running
    if running:
        return
    running = True

    print('Started the process')
    process = subprocess.Popen(["sh", scriptName])
    process.wait()
    file = open(fileName, "r")
    sio.emit("file", {'data': file.read(), 'client': clientName, 'file': fileName})
    print("DONE")
    running = False


while True:
    try:
        print("Connecting to {}:{}...".format(ip, port))
        sio.connect("{}:{}".format(ip, port))
        print("Connected!")
    except Exception as e:
        print(e)
    else:
        sio.wait()
    time.sleep(3)
