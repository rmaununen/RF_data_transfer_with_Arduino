//Transmit from here
String inBytes;
void setup() {
Serial.begin(9600);
pinMode(6,1);
}

void loop() {
if (Serial.available()>0){
  inBytes = Serial.readStringUntil('\n');
  if (inBytes == "1"){
    digitalWrite(6,1);
    Serial.println("1 is sent");
  }
  else if (inBytes == "0"){
    digitalWrite(6,0);
    Serial.println("0 is sent");
  }
  else{
    Serial.println("Invalid information");
  }
}
}
