

#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino

// 11 12 10 8 7 6 4 5
// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire0(5);
OneWire oneWire1(4);
OneWire oneWire2(6);
OneWire oneWire3(7);

OneWire oneWire4(8);
OneWire oneWire5(10);
OneWire oneWire6(12);
OneWire oneWire7(11);

// Pass our oneWire reference to Dallas Temperature.
DallasTemperature tempSensors0(&oneWire0);
DallasTemperature tempSensors1(&oneWire1);
DallasTemperature tempSensors2(&oneWire2);
DallasTemperature tempSensors3(&oneWire3);

DallasTemperature tempSensors4(&oneWire4);
DallasTemperature tempSensors5(&oneWire5);
DallasTemperature tempSensors6(&oneWire6);
DallasTemperature tempSensors7(&oneWire7);


void temperatureSensorsSetup(){

 tempSensors0.begin();
 tempSensors1.begin();
 tempSensors2.begin();
 tempSensors3.begin();
 
 tempSensors4.begin();
 tempSensors5.begin();
 tempSensors6.begin();
 tempSensors7.begin();


}


uint8_t findDevices(int pin)
{
  OneWire ow(pin);

  uint8_t address[8];
  uint8_t count = 0;


  if (ow.search(address))
  {
    Serial.print("\nuint8_t pin");
    Serial.print(pin, DEC);
    Serial.println("[][8] = {");
    do {
      count++;
      Serial.println("  {");
      for (uint8_t i = 0; i < 8; i++)
      {
        Serial.print("0x");
        if (address[i] < 0x10) Serial.print("0");
        Serial.print(address[i], HEX);
        if (i < 7) Serial.print(", ");
      }
      Serial.println("  },");
    } while (ow.search(address));

    Serial.println("};");
    Serial.print("// nr devices found: ");
    Serial.println(count);
  }

  return count;
}



void temperatureSensorsLoop(){


  tempSensors0.requestTemperatures();
  tempSensors1.requestTemperatures();
  tempSensors2.requestTemperatures();
  tempSensors3.requestTemperatures();

  tempSensors4.requestTemperatures();
  tempSensors5.requestTemperatures();
  tempSensors6.requestTemperatures();
  tempSensors7.requestTemperatures();

  transmitStruct.temp0 =tempSensors0.getTempCByIndex(0);
  transmitStruct.temp1 =tempSensors1.getTempCByIndex(0);
  transmitStruct.temp2 =tempSensors2.getTempCByIndex(0);
  transmitStruct.temp3 =tempSensors3.getTempCByIndex(0);

  transmitStruct.temp4 =tempSensors4.getTempCByIndex(0);
  transmitStruct.temp5 =tempSensors5.getTempCByIndex(0);
  transmitStruct.temp6 =tempSensors6.getTempCByIndex(0);
  transmitStruct.temp7 =tempSensors7.getTempCByIndex(0);

  // Serial.print(tempSensors0.getTempCByIndex(0));
  // Serial.print(",");
  // Serial.print(tempSensors1.getTempCByIndex(0));
  // Serial.print(",");
  // Serial.print(tempSensors2.getTempCByIndex(0));
  // Serial.print(",");
  // Serial.print(tempSensors3.getTempCByIndex(0));
  // Serial.print(",");

  // Serial.print(tempSensors4.getTempCByIndex(0));
  // Serial.print(",");
  // Serial.print(tempSensors5.getTempCByIndex(0));
  // Serial.print(",");
  // Serial.print(tempSensors6.getTempCByIndex(0));
  // Serial.print(",");
  // Serial.println(tempSensors7.getTempCByIndex(0));


  // Serial.print("Temperature for the device 1 (index 0) is: ");
  // Serial.println(sensors.getTempCByIndex(0));
  // Serial.println("//\n// Start oneWireSearch.ino \n//");

  // for (uint8_t pin = 2; pin < 13; pin++)
  // {
  //   findDevices(pin);
  // }
  // Serial.println("\n//\n// End oneWireSearch.ino \n//");


}