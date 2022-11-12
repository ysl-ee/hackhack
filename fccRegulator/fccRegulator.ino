#include <rgb_lcd.h>

#include <Wire.h>

rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 0;

int curseCounter = 0;
bool safeHarbor = TRUE;
int allowedCurse = 0;
int checks[4];
int currTime;
int grLED = 2;
int grButt = 3;
int rLED = 5;
int yLED = 6;
int gLED = 7;
int rButt = 9;

void setup() {
  // grove LED
  pinMode(grLED, OUTPUT);
  // grove button
  pinMode(grButt, INPUT);
  // red LED
  pinMode(rLED, OUTPUT);
  // yellow LED
  pinMode(yLED, OUTPUT);
  // green LED
  pinMode(gLED, OUTPUT);
  // breadboard button
  pinMode(rButt, INPUT_PULLUP);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.display();
  if (safeHarbor) {
    allowedCurse = 3;
  } else {
    allowedCurse = 0;
  }
}

void printStats() {
  if (safeHarbor) {
    lcd.setCursor(0, 0);
    lcd.print("Safe Harbor: ON ");
  } else {
    lcd.setCursor(0, 0);
    lcd.print("Safe Harbor: OFF");
  }
  lcd.setCursor(0, 1);
  lcd.print("Cur:");
  lcd.setCursor(5, 1);
  lcd.print(curseCounter);
  lcd.setCursor(8, 1);
  lcd.print("Alw:");
  lcd.setCursor(13, 1);
  lcd.print(allowedCurse);
}

void goodLEDs() {
  digitalWrite(gLED, HIGH);
  digitalWrite(yLED, LOW);
  digitalWrite(rLED, LOW);
}

void watchOutLEDs() {
  digitalWrite(gLED, LOW);
  digitalWrite(yLED, HIGH);
  digitalWrite(rLED, LOW);
}

void badLEDs() {
  digitalWrite(gLED, LOW);
  digitalWrite(yLED, LOW);
  digitalWrite(rLED, HIGH);
}

void loop() {
  /* if (digitalRead(rButt) == HIGH) {
    safeHarbor = !safeHarbor;
    delay(200);
  } */
  if (safeHarbor) {
    if (curseCounter <= allowedCurse && curseCounter != 0) {
      currTime = millis();
      if ((currTime - checks[0]) / 1000 >= 5) {
        curseCounter--;
        for (int i = 0; i < allowedCurse; i++) {
          checks[i] = checks[i + 1];
        }
      }
    }
    if (curseCounter == 0) {
      goodLEDs();
    }
    if (curseCounter > 0 && curseCounter <= allowedCurse) {
      watchOutLEDs();
    }
    if (curseCounter > allowedCurse) {
      badLEDs();
    }
  } else {
    allowedCurse = 0;
    if (curseCounter != 0) {
      badLEDs();
    } else {
      goodLEDs();
    }
  }
  if (digitalRead(grButt) == HIGH) {
    digitalWrite(grLED, HIGH);
    checks[curseCounter] = millis();
    curseCounter++;
    delay(200);
    digitalWrite(grLED, LOW);
  }
  printStats();
}