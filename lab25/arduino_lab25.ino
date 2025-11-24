void setup() {

}

Serial.begin(9600);

void loop() {

if

(Serial.available() > 0) { String msg = Serial.readStringUntil('\n'); Serial.println("Received: " + msg);

}
}