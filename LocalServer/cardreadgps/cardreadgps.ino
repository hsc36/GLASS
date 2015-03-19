#include <Wire.h>
#include <Adafruit_NFCShield_I2C.h>
#include "SoftwareSerial.h"

// Define the GPS by its inputs to the Arduino, similar to a Serial Port
SoftwareSerial gps(4,5);

// Variables used for compiling the incoming data
char im[80];          // A buffer for storing an entire incoming message
char im_char = 0;     // A particular character of the incoming message
int im_position = 0;  // The position in the incoming message buffer for the character to be placed

// Variable used for storing the processed data in a useable format
float lat_deg;  // Latitude
float lat_min;
char lat_direc; // Latitudinal Direction
float lng_deg;  // Longitude
float lng_min;
char lng_direc; // Longitudinal Direction
float time;     // Time to receive incoming message


#define IRQ   (2)
#define RESET (3)  // Not connected by default on the NFC Shield

Adafruit_NFCShield_I2C nfc(IRQ, RESET);

void setup() {
  // Set the Bauderates
  gps.begin(4800);
  Serial.begin(9600);
  //Serial.println("Hello!");
  //pinMode(led, OUTPUT); 
  nfc.begin();
  
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    Serial.print("Didn't find PN53x board");
    while (1); // halt
  }
  nfc.SAMConfig();
    
}



void loop() {
    
  uint8_t success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID
  uint8_t uidLength;                        // Length of the UID (4 or 7 bytes depending on ISO14443A card type)
  
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
  
  if(gps.available() > 0){
    im_char = gps.read();
    // A '$' means that the GPS is ready (the line has been completed and is ready to be parsed)
    if(im_char == 36){ 
      // The sequence, [G, P, G, G, A], means that that the data is in the correct format
      if(im[0] == 'G' && im[1] == 'P' && im[2] == 'G' && im[3] == 'G' && im[4] == 'A'){
        // Send the data over the serial
        //Serial.println(im);
      }
      // Reset the position for the character of the incomming message, back to the beginning of the buffer
      im_position = 0;
    }else{
      // Fill in a character for the incomming message, then move to the next place in the buffer
      im[im_position] = im_char;
      im_position++;
    }
  }
      
  if(success){
    // Display some basic information about the card
    //Serial.print("  UID Length: ");Serial.print(uidLength, DEC);Serial.println(" bytes");
    //Serial.print("  UID Value: ");
    //Serial.println("--");
    //nfc.PrintHex(uid, uidLength);
    //Serial.println("--");
    Serial.println(im);
    Serial.println("end gps");
    //Serial.println("");
  }
  
  
  
  
}
