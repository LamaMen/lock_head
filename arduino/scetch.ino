#include <Wire.h>

int door_1 = 7;
int door_2 = 6;
int door_3 = 5;
int door_4 = 4;

bool isNeedClose = false;
int currentDoor = -1;

void setup() { 
  Serial.begin(9600);
  Wire.begin(0x8);
  Wire.onReceive(receiveEvent);
  
  pinMode(door_1, OUTPUT);
  pinMode(door_2, OUTPUT);
  pinMode(door_3, OUTPUT);
  pinMode(door_4, OUTPUT);
} 

 
void receiveEvent(int howMany) {
  while (Wire.available()) {
    int c = Wire.read();
    switch (c) {
      case 1:
        currentDoor = door_1;
        openDoor();
        break;
      case 2:
        currentDoor = door_2;
        openDoor();
        break;
      case 3:
        currentDoor = door_3;
        openDoor();
        break;
      case 4:
        currentDoor = door_4;
        openDoor();
        break;
    }
  }
}

void loop() {
  if (isNeedClose && currentDoor != -1) {
    delay(5000);
    Serial.println("Close");
    digitalWrite(currentDoor, LOW);
    isNeedClose = false;
  }
}

void openDoor() {
  Serial.println("Open");
  digitalWrite(currentDoor, HIGH);
  isNeedClose = true;
}
