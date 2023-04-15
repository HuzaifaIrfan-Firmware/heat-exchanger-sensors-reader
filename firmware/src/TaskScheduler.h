#ifndef TaskScheduler_h
#define TaskScheduler_h

#include "Arduino.h"

#include "TaskManagerIO.h"


#include "SerialCom.h"

#include "TemperatureSensors.h"

#include "PressureSensors.h"

#include "FlowSensors.h"




void schedulerSetup(){

serialComSetup();

temperatureSensorsSetup();
pressureSensorsSetup();
flowSensorsSetup();


 taskManager.scheduleFixedRate(1000, [] {
   temperatureSensorsLoop();
serialComLoop();
});

 taskManager.scheduleFixedRate(1000, [] {
   pressureSensorsLoop();
});

 taskManager.scheduleFixedRate(1000, [] {
   flowSensorsLoop();
});







// taskManager.scheduleFixedRate(10, [] {
//       serialComLoop();
//   });



}


void schedulerLoop(){
  taskManager.runLoop();
}

#endif
