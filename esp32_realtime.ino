#include <WiFi.h>
#include <Servo.h>

const char* ssid     = "YOUR_WIFI";
const char* password = "YOUR_PASS";

WiFiServer server(8080);
Servo myservo;

// Pins
int LDR_PIN = 32;
int JOY_PIN = 34;
int SERVO_PIN = 4;

// Values
int ldr_val, joy_val, error_val, servo_angle;

void setup() {
  Serial.begin(115200);

  pinMode(LDR_PIN, INPUT);
  pinMode(JOY_PIN, INPUT);

  myservo.attach(SERVO_PIN, 500, 2400);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(300);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (!client) return;

  while (client.connected()) {
    // read sensors
    ldr_val = analogRead(LDR_PIN);      // 0–4095
    joy_val = analogRead(JOY_PIN);      // 0–4095

    // normalize joystick to ~center
    int joy_norm = joy_val / 8;         // ~0–512
    int ldr_norm = ldr_val / 4;         // ~0–1023
    
    error_val = ldr_norm - joy_norm;

    servo_angle = map(error_val, -400, 400, 0, 180);
    servo_angle = constrain(servo_angle, 0, 180);

    myservo.write(servo_angle);

    // send JSON
    String packet = "{";
    packet += "\"ldr\":" + String(ldr_norm) + ",";
    packet += "\"joy\":" + String(joy_norm) + ",";
    packet += "\"error\":" + String(error_val) + ",";
    packet += "\"servo\":" + String(servo_angle);
    packet += "}\n";

    client.print(packet);

    delay(5);   // ~200 Hz update
  }
}
