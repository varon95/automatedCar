
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
String commandString = "";
int forward = 5;
int back = 4;
int left = 6;
int right = 3;

void setup() {

pinMode(forward, OUTPUT);
pinMode(back, OUTPUT);
pinMode(left, OUTPUT);
pinMode(right, OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:



if(stringComplete)
{
  stringComplete = false;
  getCommand();
  
  if(commandString.equals("FWRD")){
      digitalWrite(forward, HIGH);}
  if(commandString.equals("BACK")){
      digitalWrite(back, HIGH);}
  if(commandString.equals("LEFT")){
      digitalWrite(left, HIGH);}
  if(commandString.equals("RGHT")){
      digitalWrite(right, HIGH);}

  if(commandString.equals("FWR0")){
      digitalWrite(forward, LOW);}
  if(commandString.equals("BAC0")){
      digitalWrite(back, LOW);}
  if(commandString.equals("LEF0")){
      digitalWrite(left, LOW);}
  if(commandString.equals("RGH0")){
      digitalWrite(right, LOW);}

  inputString = "";
}
}

void getCommand()
{
  if(inputString.length()>0)
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
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
