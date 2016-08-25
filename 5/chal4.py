import urllib
import re

page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827")

print "Nothing #1:"
result = page.read()

result_split = re.findall(r"\d+", result)
print result_split


urlprefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#nothing = 12345 #FIRST SET OF NOTHINGS
#nothing = 8022 #SECOND SET OF NOTHINGS
nothing = 63579 #THIRD SET OF NOTHINGS

while True:
	url = urlprefix + str(nothing)
	print url
	page = urllib.urlopen(url)
	result = page.read()
	result_split = re.findall(r"\d+", result)
	print "Next nothing is %s" %result_split[0]
	nothing = result_split[0]
