#! python 3

import pyperclip, sys, webbrowser

if len(sys.argv)>1:
	addr=' '.join(sys.argv[1:] )
else:
	addr=pyperclip.paste()

webbrowser.open('https:google.com/maps/place/'+addr)

#   Chandrapura Bokaro
