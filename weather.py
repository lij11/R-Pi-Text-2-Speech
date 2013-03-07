#Jason O'Donnell and Justin Walrath - Text to Voice Robot for Raspberry Pi
import re
import feedparser
import subprocess

filename = 'voice.txt'
f = open(filename, 'w')
#re = regex.  Since the parse comes back as a bunch of nonsense, we filter
#out words between ' '
j = re.compile('\'(.*?)\'', re.IGNORECASE)

#Parse weather from rss feed
d = feedparser.parse('http://weather.yahooapis.com/forecastrss?w=2444988')
condition = j.findall(str((d['items'][0]['yweather_condition'])))
forecast =  j.findall(str((d['items'][0]['yweather_forecast'])))

#Write the weather to the text file.
f.write("Here is the weather for Mansfield Pennsylvania.\n")
f.write("Currently: " + condition[3] + " and " + condition[7] + " degrees.\n")
f.write("Forecast: " + forecast[3] + " and " + forecast[7] + " degrees.\n")
f.close()
#Call a linux console command.  Not sure what voice program I like more yet.

#subprocess.call('espeak -ven+m1 -f voice.txt', shell=True)
subprocess.call('festival --tts voice.txt', shell=True)
