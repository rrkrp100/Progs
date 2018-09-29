#! Python 3

import pyperclip
from selenium import webdriver

anime=pyperclip.paste()
if len(anime)==0:
	print('Please Copy a valid name and relaunch')
	exit()
	
link ="http://animeheaven.eu/i.php?a="+anime

browser= webdriver.Firefox()
browser.get(link)

ep=browser.find_elements_by_class_name('infovanr')
if len(ep)==0:
	ep=browser.find_elements_by_class_name('infovan')

if len(ep)==0:
	print("Could not Find "+anime+"'s latest episode")
	exit()

eplink= ep[0].get_attribute('href')

browser.get(eplink)

FDlink=browser.find_elements_by_link_text('Force Download')

if len(FDlink)!=0:
	ulink=FDlink[0].get_attribute('href')
	
elif len(FDlink)==0:
	FDlink=browser.find_elements_by_class_name('an')
	if len(FDlink)==0:
		print("Could not Find "+anime+"'s latest episode")
		exit()
	ulink=FDlink[1].get_attribute('href')
	
browser.get(ulink)

