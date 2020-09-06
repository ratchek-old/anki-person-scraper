import wikipedia
from bs4 import BeautifulSoup
import requests
from my_exception import *


IMGS_LOCATION ="/home/tomek/TOMEK/0-new/anki bio project/imgs/"
MAX_FILE_NAME_LENGTH = 40
def get_info(name):
    full_name, img_source, info = "","",""
    try:
    	page = wikipedia.page(wikipedia.search(name)[0])
    except:
    	raise
    else:
        soup = BeautifulSoup(page.html(), 'lxml')
        vbox =  soup.find('table', {'class':'infobox'})
        if not vbox:
            raise noVboxError("{} does not have a vbox on his wiki page".format(name))
        try:
            img_source = "https:" + vbox.findAll('img')[0]['src']
        except:
            raise noPicError("Can't find a picture in the infobox of {}".format(name))
        else:
            info = page.summary.split("\n")[0]
            full_name = page.title

    return (full_name, img_source, info)

def download_pic(url):
	response = requests.get(url)
	name = url.split("/")[-1][0:MAX_FILE_NAME_LENGTH]
	file = open(IMGS_LOCATION + name, "wb")
	file.write(response.content)
	file.close()
	return name
