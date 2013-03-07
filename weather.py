import re
import feedparser
import subprocess

filename = 'voice.txt'
f = open(filename, 'w')
j = re.compile('\'(.*?)\'', re.IGNORECASE)
d = feedparser.parse('http://weather.yahooapis.com/forecastrss?w=2444988')
condition = j.findall(str((d['items'][0]['yweather_condition'])))
forecast =  j.findall(str((d['items'][0]['yweather_forecast'])))

f.write("Here is the weather for Mansfield Pennsylvania.\n")
f.write("Currently: " + condition[3] + " and " + condition[7] + " degrees.\n")
f.write("Forecast: " + forecast[3] + " and " + forecast[7] + " degrees.\n")
f.close()
#subprocess.call('espeak -ven+m1 -f voice.txt', shell=True)
subprocess.call('festival --tts voice.txt', shell=True)
