
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
String commandString = "";
int forward = 5;
int back = 4;
int left = 6;
int right = 3;

bool fwd = false;
bool bck = false;
bool changer = true;
bool changer2 = true;

long previousMillis = 0;        // will store last time LED was updated
long previousMillis2 = 0; 
int interval = 100;           // interval at which to blink (milliseconds)
int interval2 = 100; 
int intervalPau = 50;
int intervalFwd = 45;
int intervalBck = 75;

String newInterval = "";

void setup() {

pinMode(forward, OUTPUT);
pinMode(back, OUTPUT);
pinMode(left, OUTPUT);
pinMode(right, OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis();

  //staccato forward
  if(currentMillis - previousMillis > interval) {
      // save the last time you blinked the LED 
      previousMillis = currentMillis;
      if(changer){interval = intervalFwd;}
      if(!changer){interval = intervalPau;}
      
      if(changer && fwd){
        digitalWrite(forward, HIGH);
      }
      else{
         digitalWrite(forward, LOW);       
      }

      if (changer){
        changer = false;}
      else{
        changer = true;}
  }   

  //staccato backward
  if(currentMillis - previousMillis2 > interval2) {
      // save the last time you blinked the LED 
      previousMillis2 = currentMillis;
      if(changer2){interval2 = intervalBck;}
      if(!changer2){interval2 = intervalPau;}
      
      if (changer2 && bck){
        digitalWrite(back, HIGH);
      }
      else{
         digitalWrite(back, LOW);        
      }

      if (changer2){
        changer2 = false;}
      else{
        changer2 = true;}
  }    

  if(stringComplete)
  {
    stringComplete = false;
    getCommand();
    
    if(commandString.equals("FWRD")){
      fwd = true;
     //digitalWrite(forward, HIGH);
     }
    if(commandString.equals("BACK")){
      bck = true;
      //digitalWrite(back, HIGH);
      }
    if(commandString.equals("FWR0")){
        fwd = false;
        digitalWrite(forward, LOW);}
    if(commandString.equals("BAC0")){
        bck = false;
        digitalWrite(back, LOW);}
    if(commandString.equals("LEFT")){
        digitalWrite(left, HIGH);}
    if(commandString.equals("RGHT")){
        digitalWrite(right, HIGH);}
    if(commandString.equals("LEF0")){
        digitalWrite(left, LOW);}
    if(commandString.equals("RGH0")){
        digitalWrite(right, LOW);}

    if(newInterval.length()>1){        
        if(commandString.equals("INTF")){intervalFwd = newInterval.toInt();}
        if(commandString.equals("INTB")){intervalBck = newInterval.toInt();}
        }
    newInterval = "";
  
    inputString = "";
  }
}

void getCommand()
{
  if(inputString.length()>2)
  {
     commandString = inputString.substring(1,5);
  }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;

  
    if(isDigit(inChar)){
        newInterval += inChar;}
    
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
