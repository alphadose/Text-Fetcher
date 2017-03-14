#!/usr/bin/python3

from urllib import request
import sys
import _thread
import threading

with open(sys.argv[1],"r") as f:
	lines=f.readlines()		
words=0
m=1
flag=1		
def download(link, filelocation):
		global words
		global m
		global flag
		response=request.urlopen(link)
		text=response.read()
		text=text.decode('utf-8')
		text=str(text)
		text2=text.split('\\n')
		fw=open(filelocation,"w")
		for j in text2:
			fw.write(j + "\n")
			words=words+len(j.split(" "))
		fw.close()
		if(m==200):
			print(words)
		else:
			m=m+1
		

		

def createNewDownloadThread(link, filelocation):
	download_thread = threading.Thread(target=download, args=(link,filelocation))
	try:
		download_thread.start()
	except(KeyboardInterrupt,SystemExit):
		print("\n Exiting")
		sys.exit()	

for i in range(0,210):
		save_link=sys.argv[2]+str(i+1)+".txt"
		createNewDownloadThread(lines[i], save_link)	

	




