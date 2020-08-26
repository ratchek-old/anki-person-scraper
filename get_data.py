import wikipedia
from bs4 import BeautifulSoup
import requests
from my_exception import *
 

IMGS_LOCATION ="/home/tomek/TOMEK/0-new/anki bio project/imgs/"

def get_info(name):
	page = wikipedia.page(wikipedia.search(name)[0])
	soup = BeautifulSoup(page.html(), 'lxml')
	vbox =  soup.find('table', {'class':'infobox'})
	if not vbox:
		raise noVboxError("{} does not have a vbox on his wiki page".format(name))
	img_source = "https:" + vbox.findAll('img')[0]['src']
	info = page.summary.split("\n")[0]
	full_name = page.title

	return (full_name, img_source, info)

def download_pic(url):
	response = requests.get(url)
	name = url.split("/")[-1]
	file = open(IMGS_LOCATION + name, "wb")
	file.write(response.content)
	file.close()
	return name
