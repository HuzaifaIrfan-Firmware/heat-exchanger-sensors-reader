
#include "SerialTransfer.h"


SerialTransfer myTransfer;

struct __attribute__((packed)) STRUCT {
  char z;
  double y;
} transmitStruct;




void serialComSetup(){

  Serial.begin(115200);
  myTransfer.begin(Serial);

  transmitStruct.z = '$';
  transmitStruct.y = 4.5;

}


void serialComLoop(){

    // uint16_t sendSize = 0;
    // ///////////////////////////////////////// Stuff buffer with struct
    // sendSize = myTransfer.txObj(transmitStruct, sendSize);
    // ///////////////////////////////////////// Send buffer
    // myTransfer.sendData(sendSize);

}