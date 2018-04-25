

int btn = D2;
int led = D7;

int btnState = 0;


void setup()
{
   pinMode(btn, INPUT_PULLUP);
   pinMode(led, OUTPUT);

   Particle.function("led", ledToggle);
   Particle.variable("resBtnState", &btnState, INT);

   digitalWrite(led, LOW);
}


void loop()
{
    btnState = digitalRead(btn) == LOW;
    if (btnState == HIGH) {
      digitalWrite(led, HIGH);
      Particle.publish("restartButton", PRIVATE);
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
