




void pressureSensorsSetup(){

}


void pressureSensorsLoop(){
    transmitStruct.analog0=analogRead(0);
    transmitStruct.analog1=analogRead(1);
    transmitStruct.analog2=analogRead(2);
    transmitStruct.analog3=analogRead(3);

    Serial.print(analogRead(0));
    Serial.print(",");
    Serial.print(analogRead(1));
    Serial.print(",");
    Serial.print(analogRead(2));
    Serial.print(",");
    Serial.println(analogRead(3));

}