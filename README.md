# 3D_Scanner

**Files and Settings for 3D scanner HAT**

Note that updated version of FreeLSS (Version 1.22) is available and works under Raspbian BUSTER. Updated FreeLSS version also permits use of higher pin designations (e.g. for lighting). After installing FreeLSS, ensure that PIN settings specific to 3D scanner board are correct and that steps/rotation are correct (depending on how the board is jumpered). For proper scanning, the motor should rotate counter-clockwise during scanning!  

**This 3D Scanner is based upon two open-source 3D scanning projects**: 

     FreeLSS Atlas 3D Scanner by Uriah Liggett: http://www.freelss.org/ and https://www.kickstarter.com/projects/1545315380/atlas-3d-the-3d-scanner-you-print-and-build-yourse/description 

-and- 

     Ciclop 3D Scanner by BqLabs http://diwo.bq.com/en/tag/ciclop/ and http://www.thingiverse.com/thing:740357.  

  The Atlas 3D Scanner allowed one to 3D print the majority of the components to build the scanner and ran on a Raspberry Pi and an interface board to control the lasers and turntable. The software, FreeLSS runs an HTTP server which can be accessed from any computer on your home or office network. Images acquisition is through the fixed-focus 5MP Raspberry Pi camera. In contrast, the BqLabs Ciclops 3D Scanner runs on an Arduino Uno and an interface board that requires a direct connection to a PC and utilizes a Logitech USB webcam. 
  
  The Piclop 3D Scanner (http://www.thingiverse.com/thing:754003) combines features of both projects to create a more customizable set of hardware.  The 3D Scanner HAT, conforms to the Raspberry Pi specification for HATs with a user-programmable EEPROM, cut-outs for the camera and display interface, 11 mm spacing between the HAT and the Raspberry Pi, and a 3.5 amp polyfuse for over-current protection.  An earlier version of this HAT also incorporated back-power protection, however it is no longer present in the current board version.  The board has a standard Pololu stepper driver socket (low-voltage DRV8834), jumpers to select for microstepping depending on the choice of stepper motor (0.9 or 1.8 degrees).  There are several additional connectors for: 

1. Two LED arrays
2. I2C interface for OLED displays and digital luminosity sensors (tsl2561 and tsl2591), e.g. https://www.adafruit.com/products/1980
3. Serial communication through a USB-TTL Serial interface, e.g. https://www.adafruit.com/product/954
4. Breakout for additional sensors
5. DC power connector for a 5V, 4A power supply
6. Screw terminal for power switch, e.g. https://www.adafruit.com/products/915
  
**Default settings in FreeLSS for this board**

1. Right Laser - 4
2. Left Laser  - 0
3. Steps       - 6400
4. Motor En    - 1
5. Motor Step  - 2
6. Motor Dir   - 3
7. Lighting - 21 or 22 - In Older version of the FreeLSS software, max pin number was set to 7.  FreeLESS is configured for 1 LED currently.  

*Note: This can be changed by increasing 7 to 22 in line 42 of file HttpServer.cpp (/freelss/src). You will need to make clean and recompile after changing this value.  This does not need to be done in the most recent release, version 1.22

8. All other settings stay the same. 

9. If you enable autostart "make startup", these setttings will not be present at boot.

*Note: This may not be an issue with the most recent release, version 1.22

     The TSL2591 is implemented as a systemd process that runs at boot to output digital luminosity readings to an OLED display. Preference may be to have information displayed in FreeLSS software but has not been implemented.  

Fun alternative - with a LDR input: controlling output of Darlington through either LS1/LS2 or LED1/LED2 output: https://youtu.be/d3qYswq6j8c

**Additional Notes**: Under Raspbian STRETCH through BUSTER the OLED does not initialize when RST pin is set to GPIO24 and should use GPIO4. For V1 scanner boards, this would correspond to the GPIO breakout for header # J1. In the V2 Scanner boards, GPIO4 breakout has been moved to header J11 next to SDA/SCL pinout (header J12). Voltage output at header J11 has also been changed to provide 3.3V output. Please note changes in script files for OLED display.

** You can now purchase PCBs for the 3D scanner HAT from OSH Park.  See https://oshpark.com/shared_projects/FvgkGJDE **
