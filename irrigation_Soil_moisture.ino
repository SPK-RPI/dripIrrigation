
int sensor_pin = A0;

int output_value;
int led = 7;//this represent the motor output.....
int onboardLed=13;
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
   if (output_value == -80 ||output_value==-82||output_value==-83||output_value==-85||output_value==-79 )//hypothatical value.... need to fine tune according tho the plants requirements

   {
      digitalWrite(led, HIGH);
       digitalWrite(onboardLed, LOW);
      Serial.println("if condition");//debugging  purpose
   }
   else
   {
      Serial.println("else condition");//debugging purpose
       digitalWrite(onboardLed, HIGH);
        digitalWrite(led, LOW);
   }
  

   Serial.print(output_value);

   Serial.println("%");

   delay(1000);
}
