import wikipedia
from bs4 import BeautifulSoup
import time
from get_data import *
import genanki


def create_note(name):
	my_note = False

	try:
		info = get_info(name)
	except noVboxError:
		SKIPPED.append(name)
	else:
		img_name = download_pic(info[1])
		my_note = genanki.Note(
  			model=FACES_MODEL,
  			fields=['<img src="{}">'.format(img_name), info[0], info[2]]
			)
		IMGS.append("{}/{}".format(IMGS_LOCATION, img_name))

	return my_note

def create_model():
	faces_model = genanki.Model(
  		1607392318,
  		'Faces Model',
  		fields=[
    		{'name': 'Pic'},
    		{'name': 'Name'},
    		{'name': 'Description'},
  		],
  		templates=[
    		{
      		'name': 'Card 1',
      		'qfmt': '{{Pic}}',
      		'afmt': '{{FrontSide}}<hr id=answer><b>{{Name}}</b><br><br>{{Description}}',
    		},
		]
	)
	return faces_model


FACES_MODEL = create_model()
SKIPPED = []
IMGS = []

my_deck = genanki.Deck(
  2059400109,
  'Faces')


for person in ["donald trump", "kosciuszko", "obama", "chopin", "marie curie"]:
	print("Scraping", person)
	note = create_note(person)
	if note:
		print("Adding note for", person)
		my_deck.add_note(note)

print ("Skipped = {}".format(SKIPPED))

print ("Writing to file")
my_package = genanki.Package(my_deck)
my_package.media_files = IMGS
my_package.write_to_file('output.apkg')
