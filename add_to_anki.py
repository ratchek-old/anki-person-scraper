import wikipedia
from bs4 import BeautifulSoup
import time
from get_data import *

def get_info(name):
	page = wikipedia.page(name)
	soup = BeautifulSoup(page.html(), 'lxml')
	vbox =  soup.find('table', {'class':'infobox'})
	img_source = "https:" + vbox.findAll('img')[0]['src']
	info = page.summary.split("\n")[0]
	full_name = page.title
	
	return (full_name, img_source, info)


def create_note(info):
	download_pic(info[1])


def create_model():




for person in ["trump", "kosciuszko", "obama", "chopin", "marie curie"]:
	try:
		src = get_info(person)

	except:
		print()
		print("========== ERROR for {} ===============".format(person))
		print()
	else:
		file_name = download_pic(src[1])
		print (src)
		print ()
		print ("filename = ", file_name)
