#include <HTTPClient.h>
#include <WiFi.h>


//----------------------------------------------------------------------------Wifi-----------------------------------------------------------------------------------------------------------
const char* ssid = "MG45";
const char* password =  "quintosur18";
//-------------------------------------------------------------------------Pines de la Escala------------------------------------------------------------------------------------------------
const int ledPin = 5;
const int val0 = 23;
const int val1 = 22; 
const int val2 = 18;
const int val3 = 19; 
//-------------------------------------------------------------------------Pines de Grupo----------------------------------------------------------------------------------------------------
const int button = 14;
//------------------------------------------------------------------------Values---------------------------------------------------------------------------------------------------------------
int scala = 0;
int aux = 0; 
int currentID = 0;
//-------------------------------------------------------------------------Numeros de grupo---------------------------------------------------------------------------------------------------------------
int X = 4;
int Y = 0;
int grupo =  8; 
void setup() {
 
  Serial.begin(115200);


  pinMode (ledPin, OUTPUT);
  pinMode (val0, INPUT);
  pinMode (val1, INPUT); 
  pinMode (val2, INPUT);
  pinMode (val3, INPUT); 
  pinMode (button, INPUT); 
  
  delay(4000);   //Delay needed before calling the WiFi.begin
 
  WiFi.begin(ssid, password); 
 
  while (WiFi.status() != WL_CONNECTED) { //Check for the connection
    delay(1000);
    Serial.println("Connecting to WiFi..");
    digitalWrite(ledPin, HIGH); 
  }
  digitalWrite(ledPin, LOW); 
  delay(1000); 
  Serial.println("Connected to the WiFi network");
 
}
 
void loop() {

  getScale();

  if ((WiFi.status() == WL_CONNECTED)) { //Check the current connection status
 
    HTTPClient http;
 
    //http.begin("http://jsonplaceholder.typicode.com/comments?id=8"); //Specify the URL
    //http.begin("http://10.200.78.26:3000/");
    Serial.println("http://computerarchitecture.us-3.evennode.com/main/rasp?X="+String(X)+"&Y="+String(Y)+"&Grupo="+String(grupo)+"&Valor="+String(scala)); 
    http.begin("http://computerarchitecture.us-3.evennode.com/main/rasp?X="+String(X)+"&Y="+String(Y)+"&Grupo="+String(grupo)+"&Valor="+String(scala));;
    int httpCode = http.GET();                                        //Make the request
 
    if (httpCode > 0) { //Check for the returning code
 
        String payload = http.getString();
        Serial.println(httpCode);
        Serial.println(payload);
        currentID++;
      }
 
    else {
      Serial.println("Error on HTTP request");
      Serial.println(String(httpCode)); 
    }
 
    http.end(); //Free the resources
  }
 
  delay(10000);
}

void getScale(){
    while(digitalRead(button) != HIGH){
      digitalWrite (ledPin, HIGH);
      Serial.println("No entra");
    }
    digitalWrite(ledPin, LOW); 
    delay(1000); 
    aux = digitalRead(val0); 
    scala = aux;
    aux = digitalRead(val1); 
    scala += aux*2;
    aux = digitalRead(val2); 
    scala += aux*2*2;
    aux = digitalRead(val3); 
    scala += aux*2*2*2; 
    Serial.println(String(scala)); 
}
