# Python-Scripts

 xkcd.py
 
* This python program can be used from the terminal of your operating system. It will download all the comics from xkcd.com and save them locally in a folder 'xkcd-comics' in your current directory. 

* I have used requests module for getting the url and the Beautiful Soup to properly crawl through the data. I have defined two functions, one to check whether the name of comics can be used as a file name or not, if not then it replaces the invalid Characters with '-'. The other function gets the latest comic number. There is also a third function for showing progress of download, that code has been taken from vladignatyev/progress.py
