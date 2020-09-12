
void setup() {
  Serial.begin(9600);

}

void loop() {
  if(analogRead(A0)>500) Serial.println('A');
  else if(analogRead(A1)>500) Serial.println('B');
  else if(analogRead(A2)>500) Serial.println('C');
  else if(analogRead(A3)>500) Serial.println('D');
  else if(analogRead(A4)>500) Serial.println('Q');
  else if(analogRead(A5)>500) Serial.println('F');
  else Serial.println('0');
  delay(11);
}
