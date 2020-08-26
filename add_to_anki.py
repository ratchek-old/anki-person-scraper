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
  			fields=[img_name, info[0], info[2]]
			)

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
genanki.Package(my_deck).write_to_file('output.apkg')
