# Real-Time ESP32 Sensor Dashboard (High-Speed 100 FPS Visualization)

A complete real-time control system demonstrating embedded sensor acquisition, WiFi TCP streaming, and high-frequency desktop visualization. The ESP32 collects sensor readings (LDR + Joystick), computes an error signal, drives a servo, and streams telemetry to a Python dashboard built with PyQtGraph.

This project showcases embedded programming, networking, signal processing, and real-time data visualization — ideal for engineering/quant/embedded portfolios.

---

# 🎥 Demonstration Video
A short example of the system running in real time:

**[demo_video.mp4](media/demo_video.mp4)**

---

# System Overview

### **What the ESP32 Does**
- Reads **LDR** and **joystick** values through ADC  
- Computes:  
  `error = ldr_normalized - joystick_normalized`  
- Maps the error to a servo angle  
- Streams a high-frequency JSON packet (200+ Hz) over WiFi  
- Sends:  
  ```json
  {"ldr": ..., "joy": ..., "error": ..., "servo": ...}
  ```

### **What the Python Dashboard Does**
- Opens a TCP socket to the ESP32  
- Parses incoming newline-delimited JSON  
- Updates four real-time plots at **100 FPS** using PyQtGraph  
- Shows:
  - LDR sensor waveform  
  - Joystick input  
  - Error signal  
  - Servo output in degrees  

---

# Hardware

### **Components Used**
- **ESP32 Dev Module**  
- **LDR + 10kΩ resistor** (voltage divider)  
- **Joystick module**  
- **SG90 / MG90S servo motor**  
- Breadboard + jumper wires  
- Micro-USB cable  

### **Wiring Summary**
| Component | ESP32 Pin | Notes |
|----------|-----------|-------|
| LDR (voltage divider output) | GPIO 32 | ADC1 channel |
| Joystick X-axis | GPIO 34 | ADC1 channel |
| Servo signal | GPIO 4 | PWM capable |
| Servo VCC | 5V | External supply recommended if load applied |
| Servo GND | GND | Must share ground with ESP32 |

The servo *may make noise even with no load attached* — that's normal for SG90s due to idle PWM jitter.

---

# Repository Structure

```
realtime-sensor-dashboard/
│
├── esp32/  
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

---

# ESP32 Firmware (Included)

Full firmware is located here:  
**[esp32_realtime.ino](esp32/esp32_realtime.ino)**  

It contains:
- WiFi connection  
- ADC sampling  
- Servo mapping  
- JSON streaming  
- 200+ Hz loop timing  

---

# Python Real-Time Dashboard

PC side tool is at:  
**[dashboard_realtime.py](pc_dashboard/dashboard_realtime.py)**

### Install dependencies:
```
pip install -r pc_dashboard/requirements.txt
```

### Run:
```
python pc_dashboard/dashboard_realtime.py
```

Edit these two lines to match your ESP32:

```python
ESP32_IP = "YOUR.IP.HERE"
PORT = 8080
```

---

# Technical Highlights

- High-frequency analog sampling  
- Real-time control loop  
- WiFi TCP communication  
- Non-blocking sockets  
- JSON telemetry protocol  
- PyQtGraph 100 FPS visualization  
- Embedded-to-host data pipeline  

---

# Skills Demonstrated

- ESP32 firmware development  
- Sensor calibration & normalization  
- Control systems fundamentals  
- Real-time Python visualization  
- Socket programming  
- Efficient data buffering (deque)  
- Embedded/desktop system integration  
- High-performance GUI programming  

---

# License
MIT License


