
int sensor_pin = A0;

int output_value;
int led = 7;

void setup()
{
   Serial.begin(9600);

   Serial.println("Reading From the Sensor ...");
   pinMode(led, OUTPUT);
       delay(2000);
}

void loop()
{
   output_value = analogRead(sensor_pin);

   output_value = map(output_value, 550, 0, 0, 100);

   Serial.print("Mositure : ");
   if (output_value == -86)//hypothatical value....
   {
      digitalWrite(led, HIGH);
      Serial.println("if condition");//debugging  purpose
   }
   else
   {
      Serial.println("else condition");
   }
   digitalWrite(led, LOW);

   Serial.print(output_value);

   Serial.println("%");

   delay(1000);
}
