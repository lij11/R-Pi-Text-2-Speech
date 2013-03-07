#Jason O'Donnell and Justin Walrath   Text to Voice Robot
#World New Headlines
import re
import feedparser
import subprocess

filename = 'headlines.txt'
f = open(filename, 'w')
#Parse feed
d = feedparser.parse('http://www.npr.org/rss/rss.php?id=1001')

headline1 = (d['items'][0]['title'])
headline2 = (d['items'][1]['title'])
headline3 = (d['items'][2]['title'])
headline4 = (d['items'][3]['title'])

#Write headlines to file
f.write("Here is the current world news.:\n")
f.write(headline1+":\n")
f.write(headline2+":\n")
f.write(headline3+":\n")
f.write(headline4+":\n")
f.close()

#Call linux command
#subprocess.call('espeak -ven+m1 -f headlines.txt', shell=True)
subprocess.call('festival --tts headlines.txt', shell=True)
