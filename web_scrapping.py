from bs4 import BeautifulSoup
import requests
url=raw_input("enter website")
r=requests.get("http://"+url)
data=r.text #stores the text in variable data 
#print data
soup=BeautifulSoup(data)# beautifulsoup helps in extracting data
for link in soup.find_all('a'): #get all anchor links .
	print link.get('href')

