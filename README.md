# 3D_Scanner
Files and Settings for 3D scanner HAT 

This 3D Scanner is based upon two open-source 3D scanning projects: 
FreeLSS Atlas 3D Scanner by Uriah Liggett: http://www.freelss.org/ and https://www.kickstarter.com/projects/1545315380/atlas-3d-the-3d-scanner-you-print-and-build-yourse/description and 
Ciclops 3D Scanner by BqLabs http://diwo.bq.com/en/tag/ciclop/ and http://www.thingiverse.com/thing:740357.  

  The Atlas 3D Scanner allowed one to 3D print the majority of the components to build the scanner and ran on a Raspberry Pi and an interface board to control the lasers and turntable.  The software, FreeLSS runs an HTTP server which can be accessed from any computer on your home or office network.  Images aquisition is through the fixed-foucs 5MP Raspberry Pi camera.  In contrast, the BqLabs Ciclops 3D Scanner runs on an Arduino Uno and an interface board that requires a direct connection to a PC and utilizes a Logitech USB webcam. 
  
  The Piclop 3D Scanner (http://www.thingiverse.com/thing:754003) combines features of both projects to create a more customizable set of hardware.  The 3D Scanner HAT, conforms to the Raspberry Pi specification for HATS with a user-programmable EEPROM, cut-outs for the camera and display interface, and a 3.5 amp polyfuse for over-current protection.  The board has a standard Pololu stepper driver socket (low-voltage DRV8834), jumpers to select for microstepping depending on the choice of stepper motor (0.9 or 1.8 degrees).  There are several additional connectors for: 

1. Two LED arrays
2. I2C interface for OLED displays and digital luminosity sensors (tsl2561 and tsl2591), e.g. https://www.adafruit.com/products/1980
3. Serial communcation through a USB-TTL Serial interface, e.g. https://www.adafruit.com/product/954
4. Breakout for additional sensors
5. DC power connector
6. Screw terminal for power switch, e.g. https://www.adafruit.com/products/915
  
Default settings in FreeLSS for this board 

Right Laser - 4
Left Laser  - 0
Steps       - 6400
Motor En    - 1
Motor Step  - 2
Motor Dir   - 3
Lighting    - 21 or 22 - The FreeLSS software is not configured for more than 1 array

  The TSL2591 is implemented as a systemd process that runs at boot to output digital luminosity readings to an OLED display.  Preference may be to have information displayed in FreeLSS software.  
