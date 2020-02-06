import urllib.request #so we can request url stuff
import time # gonna use this to set up scraping intervals
import datetime # for time stamping file names
import os # for making folder

if not os.path.exists("html_files"):
	os.mkdir("html_files")


for i in range(5):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S') # make time stamp
	print(current_time_stamp)
	f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb") # to write a file we need to open it. w means we are gonna write it, b is binary
	response = urllib.request.urlopen('https://coinmarketcap.com/')
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(30) #note, the 5 means 5 seconds. DO NOT DO THIS IN REAL LIFE. make the time sleep longer
	

