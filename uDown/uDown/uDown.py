#! Python 3
# Downloads the youtube videos who's link is already copied

import pyperclip, os, bs4, webbrowser, requests

ulink  = pyperclip.paste();

if len(ulink)==0:
	print('Please copy a valid url\n The downloader will now Exit\n');
	#time.sleep(3)
	exit()


print("The link given is: " + ulink + "\n")

dlink=ulink
ulink = "https://www.gen" + ulink[12:]


print("Searching the for the requested file\n")

res = requests.get(ulink);	
soup= bs4.BeautifulSoup(res.text,features='html5lib')

elems= soup.select('a[data-itag="22"]')

if len(elems)!=0:
	webbrowser.open(elems[0].get('href'))

if len(elems)==0:
	print("Sorry, the 720p downloadable file is missing from the Gen repository\n Opening the Save from net website\n")
	import pyperclip
	from selenium import webdriver

	dlink= "https://www.ss"+ dlink[12:]
	browser= webdriver.Firefox()
	browser.get(dlink)

	link = browser.find_elements_by_link_text('Download')

	if len(link)==0:
		print("Downloadable file NOT FOUND, \nExiting... \n")
		exit()
	
	link[0].click()

print("Commencing the download via Browser\n PLEASE SELECT SAVE AS \n THANK YOU")




