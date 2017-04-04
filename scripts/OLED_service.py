#!/usr/bin/env python

# imports all of the required modules

import time

import sys
import socket
import fcntl
import struct
# from time import sleep

import tsl2591
import cPickle as pickle
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

# This function grabs the IP address of eth0 and wlan0
def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,	# SIOCGIFADDR
		struct.pack('256s', ifname[:15])
	    )[20:24])

for i in range (0,17280):
	TextLuxHeader = "Lux:"
	TextFullHeader = "Full:"
	TextIRHeader = "IR:"

	try:
		tsl = tsl2591.Tsl2591()
		full, ir = tsl.get_full_luminosity()
		lux = tsl.calculate_lux(full, ir)
		with open('/home/pi/sensor/sensor.pickle', 'w') as f:
			pickle.dump([lux, full, ir], f)
		lux = "{} LX".format(lux)
		full = "{} FULL".format(full)
		ir = "{} IR".format(ir)
	except:
		lux = ('N/A')
		full = ('N/A')
		ir = ('N/A')

	try:
		TEXTwlan = get_ip_address('wlan0')
	except IOError:
		TEXTwlan = ('NO NETWORK')

	try:
		TEXTlan = get_ip_address('eth0')
	except IOError:
		TEXTlan = ('NO NETWORK')


# Initialize library.
	disp.begin()

# Clear display.
# disp.clear()
# disp.display()

# Create blank image for drawing
	width = disp.width
	height = disp.height
	image = Image.new('1', (width, height))

# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)

# Load Font
	font1 = ImageFont.truetype('FreeSans.ttf', 13)
	font2 = ImageFont.truetype('FreeSans.ttf', 14)

	draw.text((1, 1),TextLuxHeader, font=font2, fill=255)
	draw.text((45, 1), lux, font=font2, fill=255) 
	draw.text((1, 14), TextFullHeader, font=font2, fill=255)
	draw.text((45, 14), full, font=font2, fill=255)
	draw.text((1, 27),TextIRHeader, font=font2, fill=255)
	draw.text((45, 27), ir, font=font2, fill=255)

	ipWLAN = 'WLAN:'
	ipLAN = 'LAN:'
	draw.text((45, 41),TEXTwlan, font=font1, fill=255)
	draw.text((45, 52),TEXTlan, font=font1, fill=255)
	draw.text((1, 41),ipWLAN, font=font1, fill=255)
	draw.text((1, 52),ipLAN, font=font1, fill=255)


# Display image.
	disp.image(image)
	disp.display()

	time.sleep(5)
