#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

const char* ssid = "colddsam";
const char* password = "give_up_on_your_dreams_and_die";

String serverName="http://127.0.0.1:8000/connection/";

void setup() {
  // put your setup code here, to run once:'
  Serial.begin(115200);
  WiFi.begin(ssid,password);
  Serial.println('Wifi Started to Connecting.......');
  while(WiFi.status()!=WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println('Wifi connected ');
  Serial.println(WiFi.localIP());

  if(WiFi.status()== WL_CONNECTED){
    WiFiClient client;
    HTTPClient http;
    String serverPath = serverName + "?data=24.37";
    http.begin(client, serverPath.c_str());

    int httpResponseCode = http.GET();

    if (httpResponseCode>0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
      String payload = http.getString();
      Serial.println(payload);
    }
    else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
  }


}

void loop() {


}
