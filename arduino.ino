// C++ code
//
//int IdrPin=A0;

//int sensorValue;
//void setup()
//{

//  Serial.begin(9600);
//}

//void loop()
//{
 //sensorValue=analogRead(IdrPin);
  //Serial.println(sensorValue);
  //delay(500);
  
//}

int IdrPin = A0;        // Broche du capteur
int potPin = A1;        // Broche du potentiomètre

int sensorValue;
int potValue;
int delayTime;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  // Lire la valeur du capteur (IDR)
  sensorValue = analogRead(IdrPin);

  // Lire la valeur du potentiomètre
  potValue = analogRead(potPin);

  // Mapper la valeur du potentiomètre pour obtenir un délai entre 200ms et 2000ms
  delayTime = map(potValue, 0, 1023, 200, 2000);

  // Afficher les valeurs dans le Moniteur Série sur une nouvelle ligne
  Serial.println(sensorValue);

  // Attendre le temps calculé avant la prochaine lecture
  delay(delayTime);
}

