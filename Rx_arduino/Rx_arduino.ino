//Receive here
String inBytes = "0";
bool waiting = true;
int Voltage;

void setup() {
  Serial.begin(9600);
  pinMode(A0,0);
  pinMode(13,1);

}

void loop() {
  while(waiting){
    digitalWrite(13,1);
    if (Serial.available()>0){
      inBytes = Serial.readStringUntil('\n');
      if (inBytes == "1"){
        waiting = false;
        digitalWrite(13,0);
        Serial.println("START RECEIVING DATA");
      }
    }
    delay(5);
  }
  
  Voltage = analogRead(A0);
  Serial.println(Voltage);
  
  if (Serial.available()>0){
      inBytes = Serial.readStringUntil('\n');
      if (inBytes == "0"){
        Serial.println("STOP RECEIVING DATA\n");
        waiting = true;
        digitalWrite(13,0);
        delay(500);
      }
    }
  
  delay(50);


}
