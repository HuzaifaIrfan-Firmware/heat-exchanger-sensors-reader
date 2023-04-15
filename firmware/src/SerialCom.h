
#include "SerialTransfer.h"


SerialTransfer myTransfer;

struct __attribute__((packed)) STRUCT {
  float temp0;
  float temp1;
  float temp2;
  float temp3;

  float temp4;
  float temp5;
  float temp6;
  float temp7;

  float analog0;
  float analog1;
  float analog2;
  float analog3;

  float interruptRate0;
  float interruptRate1;


} transmitStruct;






void serialComSetup(){

  Serial.begin(115200);
  myTransfer.begin(Serial);



}


void serialComLoop(){

    uint16_t sendSize = 0;
    ///////////////////////////////////////// Stuff buffer with struct
    sendSize = myTransfer.txObj(transmitStruct, sendSize);
    ///////////////////////////////////////// Send buffer
    myTransfer.sendData(sendSize);

}