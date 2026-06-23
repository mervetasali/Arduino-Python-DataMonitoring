int simulatorCounter = 0;

void setup() {
  Serial.begin(9600); //Starts serial communication at 9600 baud

  randomSeed(analogRead(A0)); //Prevents the random function from producing the same sequence on every startup
  
}

void loop() {
  int temperature = random(0,150); //Generates random temperature values
  
  simulatorCounter = simulatorCounter + 1;

  if (simulatorCounter < 5){
    Serial.print("TEMP: ");
    Serial.println(temperature);    
  }
  else if (simulatorCounter == 5){
    Serial.print("TEMP: ");
    Serial.println();
  }
  else if (simulatorCounter == 6){
    Serial.print("PRESSURE: ");
    Serial.println(temperature);
  }
  else if (simulatorCounter == 7){
    Serial.print("TEMP");
    Serial.println(temperature);
  }
  else if (simulatorCounter == 8){
    Serial.print("TEMP:");
    Serial.println("ab");

    simulatorCounter = 0;
  }
  

  delay(1000);

}
