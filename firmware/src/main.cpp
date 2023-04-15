#include <Arduino.h>
#include <SPI.h>
#include <Wire.h>

#include "TaskScheduler.h"

void setup() {
  // put your setup code here, to run once:
  schedulerSetup();
}

void loop() {
  // put your main code here, to run repeatedly:
   schedulerLoop();
}