import pyshorteners

link = input("\nEntrez votre lien : ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("\nLe lien court est : " + x)