import scrapy
import re
import os
import sqlite3

from ..database_helper import DatabaseHelper
from ..config import DB_FILEPATH
from ..items import JournalInfoItem

class SpringerJournal(scrapy.Spider):

	name = "springerjournal"

	def start_requests(self):
		DatabaseHelper.create_db(DB_FILEPATH)

		urls = [
			'https://www.springer.com/gp/computer-science/all-journals-in-computer-science',
		]

		for url in urls:

			yield scrapy.Request(url=url, callback=self.parse)


		# set corpus for names
		with open("names.txt", encoding="utf8", errors='ignore') as f1:
			for line in f1:
				name = line[:-1]
				DatabaseHelper.addCorpus(DB_FILEPATH, "names", name)

		# set corpus for universities
		with open("university.txt", encoding="utf8", errors='ignore') as f2:
			for line in f2:
				university = line[:-1]
				DatabaseHelper.addCorpus(DB_FILEPATH, "university", university)

		# set corpus for surnames
		f = open("surnames.txt", "r")
		for line in f:
			surname = line[:-1].lower()
			if surname != " ":
				DatabaseHelper.addCorpus(DB_FILEPATH, "surname", surname)

	def parse(self, response):

		page = response.url.split("/")[-2]

		filename = 'AllJournals-%s.html' % page

		with open(filename, 'wb') as f:
			self.log('Saved file %s' % filename)

		alljournals = response.xpath('//div[contains(@class, "product-information")]')

		counter = 0
		while counter < len(alljournals):
			str_target = alljournals[counter].get()
			str_temp = re.split('com/', str_target)[1]
			journal_code = re.split('"', str_temp)[0]
			url = 'https://www.springer.com/journal/'+journal_code+'/editors'
			str_temp = re.split("</a></h3>", str_target)[0] 
			title = re.split(">", str_temp)[-1]

			DatabaseHelper.addJournal(JournalInfoItem(title=title, publisher="Springer", url=url), DB_FILEPATH)
			
			counter = counter + 1

		os.system("rm "+filename)
