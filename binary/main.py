import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/d/dd/Bucovina_Sheepdog.jpg').read()
fhand = open('cover.jpg', 'wb')
fhand.write(img)
fhand.close()