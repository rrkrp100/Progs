#! Python 3
# Downloads the youtube videos who's link is already copied

import pyperclip, os, bs4, webbrowser, requests

ulink  = pyperclip.paste();

if len(ulink)==0:
	print('Please copy a valid url\n The downloader will now Exit\n');
	#time.sleep(3)
	exit()


print("The link given is: " + ulink + "\n")

ulink = "https://www.gen" + ulink[12:]


print("Searching the for the requested file\n")

res = requests.get(ulink);	
soup= bs4.BeautifulSoup(res.text,features='html5lib')

elems= soup.select('a[data-itag="22"]')

if len(elems)==0:
	print("Sorry, the 720p downloadable file is missing\n playing the 360p file\n")
	elems= soup.select('a[data-itag="18"]')

if len(elems)==0:
	print("Sorry, could not find the downloadable files for your request\n The downloader will now exit\n")
	#time.sleep(3)
	exit()
	
webbrowser.open(elems[0].get('href'))

print("Commencing the download via Browser\n PLEASE SELECT SAVE AS \n THANK YOU")

