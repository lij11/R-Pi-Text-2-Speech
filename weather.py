#Jason O'Donnell and Justin Walrath - Text to Voice Robot for Raspberry Pi
import re
import feedparser
import subprocess

#re = regex.  Since the parse comes back as a bunch of nonsense, we filter
#out words between ' '
j = re.compile('\'(.*?)\'', re.IGNORECASE)

#Parse weather from rss feed
d = feedparser.parse('http://weather.yahooapis.com/forecastrss?w=2444988')
condition = j.findall(str((d['items'][0]['yweather_condition'])))
forecast =  j.findall(str((d['items'][0]['yweather_forecast'])))

weather = "./speech.sh Here is the weather for Mansfield Pennsylvania."
current = "./speech.sh Currently: " + condition[3] + " and " + condition[7] + " degrees."
forecast = "./speech.sh Forecast: " + forecast[3] + " and " + forecast[7] + " degrees."


#Call a linux console command.  Using Google Translate
subprocess.call(weather, shell=True)
subprocess.call(current, shell=True)
subprocess.call(forecast, shell=True)

