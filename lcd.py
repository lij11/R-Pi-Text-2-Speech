#!/usr/bin/pythonhttp://raspberrypi.local/editor

#
# based on code from lrvick and LiquidCrystal
# lrvic - https://github.com/lrvick/raspi-hd44780/blob/master/hd44780.py
# LiquidCrystal - https://github.com/arduino/Arduino/blob/master/libraries/LiquidCrystal/LiquidCrystal.cpp
#

from subprocess import *
from time import sleep
from Adafruit_LCDPlate import Adafruit_CharLCD
from Adafruit_MCP230xx import Adafruit_MCP230XX
import smbus
import string
import pywapi
import subprocess

mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)

lcd = Adafruit_CharLCD(15, 13, [12,11,10,9], 14)
lcd.clear()
lcd.backlight(lcd.GREEN)
lcd.message("A TEAM\nTXT2VOICE")
sleep(2)
cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd2 = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd3 = "sudo shutdown -h now"
cmd4 = "sudo reboot"
cmd5 = 'date +"%r"'
cmd6 = 'date +"%m-%d-%y"'

def run_cmd(cmd):
  p = Popen(cmd, shell=True, stdout=PIPE)
  output = p.communicate()[0]
  return output

sleep(1)
count = 0

while 1:
  if (not mcp.input(lcd.LEFT)):
		lcd.backlight(lcd.RED)
		lcd.clear()
		wipaddr = run_cmd(cmd)
		eipaddr = run_cmd(cmd2)
		if(wipaddr == '' and eipaddr != ''):
			lcd.message('Ethernet IP\n%s' % (eipaddr))
		if(wipaddr != '' and eipaddr == ''):
			lcd.message('Wireless IP\n%s' % (wipaddr))
		if(wipaddr == '' and eipaddr == ''):
			lcd.message('No connection')

	if (not mcp.input(lcd.UP)):
		lcd.clear()
		lcd.backlight(lcd.BLUE)
		lcd.message("NPR Headlines")
		subprocess.call("python headlines.py", shell=True)		

	if (not mcp.input(lcd.DOWN)):
		lcd.backlight(lcd.GREEN)
		lcd.clear()
		lcd.message("Shutdown? Select\nReboot? Down")
		select = 1
		while (select == 1):
			if (not mcp.input(lcd.SELECT)):
				lcd.backlight(lcd.RED)
				lcd.clear()
				lcd.message("Goodbye!")
				sleep(3)
				lcd.clear()
				lcd.backlight(lcd.OFF)
				lcd.noDisplay()
				sleep(2)
				test = run_cmd(cmd3)
			if (not mcp.input(lcd.UP)):
				select = 0
			if (not mcp.input(lcd.DOWN)):
				lcd.backlight(lcd.RED)
				lcd.clear()
				lcd.message("See you soon!")
				sleep(3)
				lcd.backlight(lcd.OFF)
				lcd.clear()
				test = run_cmd(cmd4)
			
	
	if (not mcp.input(lcd.RIGHT)):
		lcd.clear()
		lcd.backlight(lcd.GREEN)
		lcd.message("MU Weather")
		subprocess.call("python weather.py",shell=True)

	if (not mcp.input(lcd.SELECT)):
		lcd.backlight(lcd.GREEN)
		lcd.clear()
		lcd.message("A TEAM\nTXT2VOICE")
