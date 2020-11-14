import sqlite3
from typing import List


class DatabaseHelper:

    @staticmethod
    def create_db(dbpath):
        """ Create the necessary tables for the journal database
        """
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS journalInfo (\
            title TEXT NOT NULL UNIQUE,\
            publisher TEXT NOT NULL,\
            url TEXT PRIMARY KEY\
        );")

        cur.execute("CREATE TABLE IF NOT EXISTS corpus (\
            type TEXT NOT NULL,\
            content TEXT NOT NULL UNIQUE\
        );")

        cur.execute("CREATE TABLE IF NOT EXISTS journalLine (\
	        publisher TEXT NOT NULL,\
            title TEXT NOT NULL,\
            _line TEXT NOT NULL UNIQUE\
        );")

        cur.execute("CREATE TABLE IF NOT EXISTS taggedLine (\
            publisher TEXT NOT NULL,\
            title TEXT NOT NULL,\
            _line TEXT NOT NULL UNIQUE\
        );")

        cur.execute("CREATE TABLE IF NOT EXISTS crawled (\
            publisher TEXT NOT NULL,\
            title TEXT NOT NULL,\
            role  TEXT NOT NULL,\
            name  TEXT NOT NULL,\
            affiliation TEXT NOT NULL\
        );")

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def addJournal(journal_info: 'JournalInfoItem', dbpath:str):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO journalInfo\
            (title, publisher, url)\
            VALUES(?,?,?)",
            (
            str(journal_info['title']),
            str(journal_info['publisher']),
            str(journal_info['url']),
            )
        )

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def addLine(journal_line: 'JournalLineItem', dbpath:str):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO journalLine\
            (publisher, title, _line)\
            VALUES(?,?,?)",
            (
	        str(journal_line['publisher']),
            str(journal_line['title']),
            str(journal_line['line']),
            )
        )

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def addTaggedLine(tagged_line: 'TaggedLineItem', dbpath:str):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO taggedLine\
            (publisher, title, _line)\
            VALUES(?,?,?)",
            (
            str(tagged_line['publisher']),
            str(tagged_line['title']),
            str(tagged_line['line']),
            )
        )

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def addCrawledItem(crawled: 'CrawledItem', dbpath:str):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO crawled\
            (publisher, title, role, name, affiliation)\
            VALUES(?,?,?,?,?)",
            (
            str(crawled['publisher']),
            str(crawled['title']),
            str(crawled['role']),
            str(crawled['name']),
            str(crawled['affiliation']),
            )
        )

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def addCorpus(dbpath, _type, _content):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO corpus\
            (type, content)\
            VALUES(?,?)",
            (
            _type,
            _content
            )
        )

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def getJournalUrls(dbpath, _publisher):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        url = cur.execute("SELECT url FROM journalInfo WHERE publisher == '" + _publisher + "'").fetchall()

        conn.commit()
        cur.close()
        conn.close()

        return url


    @staticmethod
    def getLines(dbpath, _publisher):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        lines = cur.execute("SELECT title, _line FROM journalLine WHERE publisher == '" + _publisher + "'").fetchall()

        conn.commit()
        cur.close()
        conn.close()

        return lines


    @staticmethod
    def getTaggedLines(dbpath, _publisher):
        conn = sqlite3.connect('/home/wing.nus/xinze/journal-mining/journal_crawl/crawls/all_files/all_files.db')
        cur = conn.cursor()
        lines = cur.execute("SELECT title, _line FROM taggedLine WHERE publisher == '" + _publisher + "'").fetchall()

        conn.commit()
        cur.close()
        conn.close()

        return lines