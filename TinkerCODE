// C++ code
//
int sensor = 0;

int IncJANUS = 0;

int prevJANUS = 0;

int newJANUS = 0;

int i = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(13, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop()
{
  sensor = analogRead(A0);
  if (sensor == 466) {
    digitalWrite(13, HIGH);
  } else {
    digitalWrite(13, LOW);
  }
  if (sensor == 466) {
    digitalWrite(4, HIGH);
  } else {
    digitalWrite(4, LOW);
  }
  newJANUS = analogRead(A0);
  if (newJANUS > prevJANUS) {
    digitalWrite(8, HIGH);
  }
  if (newJANUS <= prevJANUS) {
    digitalWrite(8, LOW);
  }
  if (1 == 1) {
    if (newJANUS < prevJANUS) {
      if (newJANUS > 466) {
        digitalWrite(1, LOW);
      }
    }
    if (newJANUS < prevJANUS) {
      digitalWrite(9, HIGH);
    }
    if (newJANUS > prevJANUS) {
      digitalWrite(9, LOW);
    }
  }
  if (sensor == 466) {
    digitalWrite(4, HIGH);
  } else {
    digitalWrite(4, LOW);
  }
  if (sensor == 466) {
    analogWrite(3, 0);
  }
  if (newJANUS < prevJANUS) {
    digitalWrite(1, LOW);
  }
  prevJANUS = newJANUS;
  delay(10); // Delay a little bit to improve simulation performance
}
