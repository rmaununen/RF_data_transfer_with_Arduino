//Transmit from here
byte inBytes;
void setup() {
Serial.begin(9600);
pinMode(13,1);
}

void loop() {
if (Serial.available()>0){
  inBytes = Serial.read();
  if (inBytes == 1){
    digitalWrite(13,1);
    Serial.write("1 is sent");
  }
  if (inBytes == 0){
    digitalWrite(13,0);
    Serial.write("0 is sent");
  }
  else{
    Serial.write("Invalid information");
  }
}
}
