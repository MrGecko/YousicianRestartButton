

int d1Pin = D1;
int d2Pin = D2;
int d3Pin = D3;
int led = D7;

int d1State = 0;
int d2State = 0;
int d3State = 0;


void setup()
{
   pinMode(d1Pin, INPUT_PULLUP);
   pinMode(d2Pin, INPUT_PULLUP);
   pinMode(d3Pin, INPUT_PULLUP);

   pinMode(led, OUTPUT);

   Particle.function("led", ledToggle);
   Particle.variable("d1State", &d1State, INT);
   Particle.variable("d2State", &d2State, INT);
   Particle.variable("d3State", &d3State, INT);

   digitalWrite(led, LOW);
}


void loop()
{
    d1State = digitalRead(d1Pin) == LOW;
    d2State = digitalRead(d2Pin) == LOW;
    d3State = digitalRead(d3Pin) == LOW;

    if (d1State == HIGH) {
      Particle.publish("d1Button", PRIVATE);
    }
    if (d2State == HIGH) {
      Particle.publish("d2Button", PRIVATE);
    }
    if (d3State == HIGH) {
      Particle.publish("d3Button", PRIVATE);
    }

    if (d1State || d2State || d3State) {
      digitalWrite(led, HIGH);
      delay(500);
    }
    else {
      digitalWrite(led, LOW);
    }
}



int ledToggle(String command) {

    if (command=="on") {
        digitalWrite(led,HIGH);
        return 1;
    }
    else if (command=="off") {
        digitalWrite(led,LOW);
        return 0;
    }
    else {
        return -1;
    }
}
