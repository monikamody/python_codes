from bs4 import BeautifulSoup
import requests
url=raw_input("enter website")
r=requests.get("http://"+url)
data=r.text #stores the text in variable data 
#print data
soup=BeautifulSoup(data)# beautifulsoup helps in extracting data
for link in soup.find_all('img'): #get all image links .
	print link.get('src')
	print link.get('title')

