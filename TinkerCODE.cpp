//I made everything in BLOCK code and couldnt figure out how to delete 
//so there are some useless pins which I hv mentioned
int sensor = 0;//Of force sensor

int prevJANUS = 0;//Brownie pts for taking these names for Variable???

int newJANUS = 0;//So prevJANUS contains the previous value of the current and newJANUS stores the latest value as it reads A0 Analog pin of sensor

void setup()
{
  pinMode(A0, INPUT);
  pinMode(13, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(1, OUTPUT);//useless
  pinMode(9, OUTPUT);
  pinMode(3, OUTPUT);//useless
}

void loop()
{
  sensor = analogRead(A0);
  if (sensor == 466) {//The 466 is maximum value SERIAL MONItOR was readin so I used it everywhere
    digitalWrite(13, HIGH);//Yellow Pin when max is reached
  } else {
    digitalWrite(13, LOW);
  }
  if (sensor == 466) {
    digitalWrite(4, HIGH);//This is for that PIEZO buzzer
  } else {
    digitalWrite(4, LOW);
  }
  newJANUS = analogRead(A0);
  if (newJANUS > prevJANUS) {//This is condition for the green light that it turns on only if the next value is greater than previous i.e The "BOMB" is ascending 
    digitalWrite(8, HIGH);
  }
  if (newJANUS <= prevJANUS) {
    digitalWrite(8, LOW);
  }
  if (1 == 1) {//See here I couldnt delete the prev condition I made bcz all blocks were moving on selecting it so 
    if (newJANUS < prevJANUS) {//I made this condition which is always True
      if (newJANUS > 466) {
        digitalWrite(1, LOW);//This whole section is useless but I dont want to change code bcz I am short of time 
      }                      //and wont be able to correct anything
    }
    if (newJANUS < prevJANUS) {
      digitalWrite(9, HIGH);//This is condition for red just opposite of blue
    }
    if (newJANUS > prevJANUS) {
      digitalWrite(9, LOW);
    }
  }
  if (sensor == 466) {//Already above the PIEZO BUZZER
    digitalWrite(4, HIGH);
  } else {
    digitalWrite(4, LOW);
  }
  if (sensor == 466) {/Uselss
    analogWrite(3, 0);
  }
  if (newJANUS < prevJANUS) {
    digitalWrite(1, LOW);
  }
  prevJANUS = newJANUS;//Added this so that at the end of each loop prevJanus starts with the latest value
  delay(10); // Delay a little bit to improve simulation performance(THIS COMMENT WAS ALREADY BY TINKERCAD)
}

