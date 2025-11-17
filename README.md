# Real-Time ESP32 Sensor Dashboard (100 FPS)

This project implements a high-performance real-time sensor dashboard using an ESP32 microcontroller and a Python-based desktop visualization tool. The ESP32 continuously samples sensor data (LDR and joystick), computes an error value, drives a servo motor accordingly, and streams all measurements to a host computer over WiFi using a lightweight JSON protocol.  

A Python/PyQtGraph application receives the stream and renders four synchronized plots at 100 frames per second.  

---

## Repository Structure

```
realtime-sensor-dashboard/
│
├── esp32/
│   └── esp32_realtime.ino
│
├── pc_dashboard/
│   ├── dashboard_realtime.py
│   └── requirements.txt
│
├── media/
│   └── demo_video.mp4
│
└── README.md
```

### Direct Links  
ESP32 firmware:  
- [esp32_realtime.ino](esp32/esp32_realtime.ino)

Python dashboard:  
- [dashboard_realtime.py](pc_dashboard/dashboard_realtime.py)  
- [requirements.txt](pc_dashboard/requirements.txt)

Media:  
- [demo_video.mp4](media/demo_video.mp4)

---

## System Overview

### Microcontroller (ESP32)

The ESP32 performs the following operations in a continuous control and streaming loop:

1. Samples two analog sensors:  
   • LDR (light intensity)  
   • Joystick (X-axis)

2. Normalizes and scales readings to usable ranges.

3. Computes a real-time error signal:  
   `error = ldr_normalized - joystick_normalized`

4. Maps the error signal to a servo angle using linear transformation.

5. Drives a servo motor using PWM based on computed error.

6. Packages the data as a one-line JSON object containing:  
   - ldr  
   - joy  
   - error  
   - servo  

7. Streams ~200 Hz JSON packets to the host computer via TCP.

### Desktop Application (Python)

The Python visualization tool:

1. Establishes a TCP connection to the ESP32.  
2. Receives newline-delimited JSON packets.  
3. Parses and stores values in bounded deques.  
4. Uses PyQtGraph to render four real-time plots at 100 FPS:  
   - LDR intensity  
   - Joystick position  
   - Error signal  
   - Servo output angle  
5. Maintains consistent timing and smooth frame rate via a QTimer loop.  
6. Provides high-frequency, low-latency visualization.

---

## Hardware Overview

### Components
- ESP32 Dev Module  
- LDR + 10kΩ resistor (voltage divider)  
- Joystick module  
- SG90 or MG90S servo motor  
- Breadboard, jumper wires  
- USB power/programming cable  

### Wiring
- LDR → ADC pin (e.g., GPIO32)  
- Joystick X-axis → ADC pin (e.g., GPIO34)  
- Servo signal → PWM pin (e.g., GPIO4)  
- Use common GND between ESP32 and servo (5V may require external source depending on load)

---

## Firmware

Full ESP32 firmware is located here:  
[esp32_realtime.ino](esp32/esp32_realtime.ino)

This code implements sensor sampling, error computation, servo control, JSON construction, and high-speed TCP streaming.

---

## Python Dashboard

The real-time visualization tool is here:  
[dashboard_realtime.py](pc_dashboard/dashboard_realtime.py)

### Installing dependencies
```
pip install -r pc_dashboard/requirements.txt
```

### Running the dashboard
```
python pc_dashboard/dashboard_realtime.py
```

Ensure the ESP32 IP address and port match your local network configuration.

---

## Demonstration Video

A short demonstration showing real-time sensor input, servo response, and dashboard output is available here:  
[demo_video.mp4](media/demo_video.mp4)

The video displays:
- Changes to LDR and joystick inputs  
- Live error response  
- Real-time servo behavior  
- Smooth 100 FPS dashboard performance  

---

## Technical Highlights

- Embedded systems firmware in C++  
- Analog sensor acquisition at high sample rates  
- WiFi networking and TCP data streaming  
- Lightweight JSON telemetry protocol  
- Real-time visualization using PyQtGraph  
- High-frequency plotting at 100 FPS  
- Non-blocking sockets and deque-based buffering  
- Real-world control loop implementation  
- Efficient mapping between sensor error and servo output  

---

## Skills Demonstrated

- ESP32 development (Arduino framework)  
- Real-time data processing  
- Python GUI development  
- Network socket programming  
- Control systems and signal mapping  
- High-frequency plotting  
- Multithreaded timing and buffering strategies  
- Embedded-to-host communication architecture  

---

## License

This repository is distributed under the MIT License.

