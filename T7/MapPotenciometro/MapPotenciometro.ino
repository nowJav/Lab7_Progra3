#define led1 8
#define led2 9
#define led3 10
#define pot A1


void setup()
{
  Serial.begin(9600);
  pinMode(pot,INPUT);
  for(int i=led1;i<=led3;i++)
  {
    pinMode(i,OUTPUT);
  }
}

void loop()
{
  int val = analogRead(pot);
  int m = map(val,0,1023,0,100);
  Serial.print("Valor PWM: ");
  Serial.println(m);
  for(int i=led1;i<=led3;i++)
  {
    if(m>=50)
    {
     digitalWrite(i,HIGH);
     
    }
    else
    {
     digitalWrite(i,LOW);
     
    }
    //Envio de datos
    
    delay(50);
  }

}
