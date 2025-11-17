import socket
import json
from collections import deque
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore

# --------------------------
# QT APPLICATION
# --------------------------
app = QtWidgets.QApplication([])

# --------------------------
# CONFIG
# --------------------------
ESP32_IP = "192.168.1.129"
PORT = 8080

BUFFER = ""
MAX_POINTS = 500

ldr = deque(maxlen=MAX_POINTS)
joy = deque(maxlen=MAX_POINTS)
err = deque(maxlen=MAX_POINTS)
servo = deque(maxlen=MAX_POINTS)

# --------------------------
# TCP SOCKET
# --------------------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP32_IP, PORT))
sock.setblocking(False)

# --------------------------
# WINDOW + LAYOUT
# --------------------------
win = pg.GraphicsLayoutWidget(show=True, title="Real-Time Control Dashboard")
win.resize(1500, 1200)

plots = []
curves = []
titles = ["LDR Sensor", "Joystick", "Error (LDR - Joystick)", "Servo Angle"]

for title in titles:
    p = win.addPlot(title=title)
    p.showGrid(x=True, y=True)
    c = p.plot(pen=pg.mkPen(width=2))
    plots.append(p)
    curves.append(c)
    win.nextRow()

# --------------------------
# UPDATE LOOP
# --------------------------
def update():
    global BUFFER

    try:
        data = sock.recv(1024).decode()
        if data:
            BUFFER += data
    except BlockingIOError:
        pass

    while "\n" in BUFFER:
        line, BUFFER = BUFFER.split("\n", 1)
        line = line.strip()
        if not line:
            continue

        try:
            obj = json.loads(line)
        except:
            continue

        ldr.append(obj["ldr"])
        joy.append(obj["joy"])
        err.append(obj["error"])
        servo.append(obj["servo"])

    datasets = [ldr, joy, err, servo]

    for curve, data in zip(curves, datasets):
        curve.setData(list(data))

# --------------------------
# TIMER 100FPS
# --------------------------
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

# --------------------------
# RUN APP
# --------------------------
app.exec()
