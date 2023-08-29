// C++ code
//
int incomingByte = 0;
bool run = false;// for incoming serial data
void setup()
{
  pinMode(11, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop()
{
   if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
     if (incomingByte==49){
     	run = true;
     } else {
     	run=false;
     }
    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
  }
  if (run){
  	digitalWrite(11,HIGH);
    delay(10000);
  } 
}