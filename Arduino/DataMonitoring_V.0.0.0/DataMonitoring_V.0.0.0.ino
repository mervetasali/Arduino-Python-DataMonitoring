void setup() {
  Serial.begin(9600); //Starts serial communication at 9600 baud

  randomSeed(analogRead(A0)); //Prevents the random function from producing the same sequence on every startup

}

void loop() {
  int temperature = random(0,150); //Generates random temperature values

  Serial.print("TEMP: ");
  Serial.println(temperature);

  delay(1000);

}
