import urllib.request
from bs4 import BeautifulSoup
import requests
import re # Regular Expressions
import os
import sys
import time

#Creating xkcd-comics folder.
current_path = os.getcwd()
path = current_path+"\\xkcd-comics"
try:
	os.mkdir(path)
except FileExistsError as e:
	print("Folder Already Exists.")

# Progress Bar, From vladignatyev/progress.py
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

# For proper Title of the Image File
def properTitle( title):
	invalidChars = "\/:?\"<>|*"
	for char in invalidChars:
		title = title.replace(char,"-")
	return title

def getLatestPageNo():
	main_page = ("https://xkcd.com/")
	r = requests.get(main_page)
	soup = BeautifulSoup(r.text,"html5lib")
	text = soup.get_text()
	index = text.find("xkcd.com/")+9
	latestPageNo = int(text[index:index+4])
	#print(latestPageNo)
	return latestPageNo


latestPageNo = getLatestPageNo() # Or Set it manually.

path = path + "\\"
for pageNo in range(latestPageNo,0,-1):
	try:
		url = ("https://xkcd.com/"+ str(pageNo) + "/")
		r = requests.get(url)
		soup = BeautifulSoup(r.text, "html5lib")
		title = str(soup.title)
		title = title[13:len(title)-8]
		title = properTitle(title)
		#print(pageNo, end="")
		#print(" -> "+title)
		progress(latestPageNo-pageNo, latestPageNo, status='Downloading Comics')
		time.sleep(0.5)  # emulating long-playing job
		for link in soup.find_all('img'):
			imgSource = link.get('src')
			#print(imgSource)
			if "comics" in imgSource:
				try:
					urllib.request.urlretrieve("https:"+imgSource, path+title+".png")
				except HTTPError as err:
					print("Problem with the HTTP :(")  # Something wrong with url
				except FileNotFoundError :
					print("Problem with the filename :(")
			
	except UnicodeEncodeError:
		print("Character error at comic no. "+ str(pageNo))
