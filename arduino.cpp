#include <SoftwareSerial.h>

SoftwareSerial bluetooth(10, 11); // RX, TX

int vibrationSensor = A5; // Vibration sensor connected to A5
int presentCondition = 0; // Current state of vibration sensor

void setup() {
    pinMode(vibrationSensor, INPUT);
    bluetooth.begin(9600); // Start Bluetooth communication
}

void loop() {
    presentCondition = digitalRead(vibrationSensor); // Read vibration sensor

    if (presentCondition == HIGH) { // If vibration is detected
        bluetooth.println("vibration detected"); // Send message via Bluetooth
        delay(1000); // Delay to avoid multiple messages for one vibration event
    }
}
