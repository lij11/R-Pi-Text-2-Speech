#Jason O'Donnell and Justin Walrath   Text to Voice Robot
#World New Headlines
import feedparser
import subprocess

#Parse feed
d = feedparser.parse('http://www.npr.org/rss/rss.php?id=1001')

#Need to keep string sizes down or get errors.
headline0 = './speech.sh Heres the current world news:'
headline1 = (d['items'][0]['title'])
headline2 = (d['items'][1]['title'])
headline3 = (d['items'][2]['title'])
headline4 = (d['items'][3]['title'])
headlineBreak = ":"

head1 = "./speech.sh Heres the current world news: " + headline1 
head2 = "./speech.sh " + headlineBreak + headline2 
head3 = "./speech.sh " + headlineBreak + headline3 
head4 = "./speech.sh " + headlineBreak + headline4 

#Call linux command - Using Google Translate now.  Wayyyy better.
subprocess.call(head1, shell=True)
subprocess.call(head2, shell=True)
subprocess.call(head3, shell=True)
subprocess.call(head4, shell=True)
