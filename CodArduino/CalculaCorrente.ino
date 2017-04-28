#include "EmonLib.h"// Include Emon Library
#include "Thermistor.h"


EnergyMonitor emon1;             // Create an instance
Thermistor temp(0);
float currentM = 0;

void setup()
{  
  Serial.begin(9600);
  
  
  emon1.voltage(2, 234.26, 1.7);  // Voltage: input pin, calibration, phase_shift
  emon1.current(1, 25);       // Current: input pin, calibration.
  //emon1.current(1, 111.1);       // Current: input pin, calibration.
  
}

void loop()
{
  emon1.calcVI(20,2000);    // Calculate all. No.of wavelengths, time-out
  float Irms = emon1.Irms;    //extract Irms into Variable
  int temperature = temp.getTemp();   //Serial.println(realPower);

  //emon1.serialprint();           // Print out all variables
  //float realPower       = emon1.realPower;        //extract Real Power into variable
  //float apparentPower   = emon1.apparentPower;    //extract Apparent Power into variable
  //float powerFActor     = emon1.powerFactor;      //extract Power Factor into Variable
  //float supplyVoltage   = emon1.Vrms;             //extract Vrms into Variable

  if((Irms - 0.1) == currentM || (Irms - 0.1) < currentM){
      
      Serial.println("Queda de Energia");
      Serial.flush();
      
  }
  else{
      
      Serial.print("Corrente aproximada: ");
      Serial.print(Irms);
      
      Serial.print(" |  Temperatura no Sensor: ");
      Serial.print(temperature);
      Serial.println("*C");
      Serial.flush();
  }
      
}
