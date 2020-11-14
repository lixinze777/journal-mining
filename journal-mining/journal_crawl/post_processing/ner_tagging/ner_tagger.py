import sys
sys.path.append("../../journal_crawl")

import database_helper
import config
import items

from flair.models import SequenceTagger
from flair.data import Sentence

class NER_Tagger:

	def __init__(self):
		# load the model you trained
		self.model = SequenceTagger.load('../data_augmentation/resources/taggers/bpe/best-model.pt')

	def tag_sentences(self, publisher):

		lines = database_helper.DatabaseHelper.getLines(config.DB_FILEPATH, publisher)

		counter = 0

		for title, sentence in lines:
			sentence = Sentence(sentence)
			self.model.predict(sentence)
			predicted = sentence.to_tagged_string()
			database_helper.DatabaseHelper.addTaggedLine(items.TaggedLineItem(publisher=publisher, title=title, line=predicted), config.DB_FILEPATH)
			counter = counter + 1
			
		print(str(counter)+" rows predicted")

if __name__ == "__main__":
	tagger = NER_Tagger()
	tagger.tag_sentences("Springer")