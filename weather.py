#Jason O'Donnell - RSS Weather Parser for Yahoo Weather
import feedparser

d = feedparser.parse('http://weather.yahooapis.com/forecastrss?w=2444988')
print (d['items'][0]['yweather_condition'])
print (d['items'][0]['yweather_forecast'])
