


byte sensor0InterruptPin = 0; 
byte sensor0Pin       = 2;

double sensor0InterruptRate;    //This is the value we intend to calculate.
volatile int sensor0InterruptCount; //This integer needs to be set as volatile to ensure it updates correctly during the interrupt process.


byte sensor1InterruptPin = 1; 
byte sensor1Pin       = 3;

double sensor1InterruptRate;    //This is the value we intend to calculate.
volatile int sensor1InterruptCount; //This integer needs to be set as volatile to ensure it updates correctly during the interrupt process.



/*
Insterrupt Service Routine
 */
void sensor0ISR()
{
sensor0InterruptCount++;
}

void sensor1ISR()
{
sensor1InterruptCount++;
}


void flowSensorsSetup(){

     pinMode(sensor0Pin, INPUT);
   digitalWrite(sensor0Pin, HIGH); // Optional Internal Pull-Up

 attachInterrupt(sensor0InterruptPin, sensor0ISR, RISING); // Setup Interrupt

 
     pinMode(sensor1Pin, INPUT);
   digitalWrite(sensor1Pin, HIGH); // Optional Internal Pull-Up

 attachInterrupt(sensor1InterruptPin, sensor1ISR, RISING); // Setup Interrupt

 noInterrupts(); //Disable the interrupts on the Arduino




}


void flowSensorsLoop(){

  sensor0InterruptCount=0;
  sensor1InterruptCount=0;

  interrupts();   //Enables interrupts on the Arduino
  delay(1000);   //Wait 1 second
  noInterrupts(); //Disable the interrupts on the Arduino

  transmitStruct.interruptRate0=sensor0InterruptCount;
  transmitStruct.interruptRate1=sensor1InterruptCount;

}