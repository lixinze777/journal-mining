from pathlib import Path

# Set arbitrary browser agent in header since certain sites block against crawlers
REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

# Filepath directory for saved DBs of scraped conferences
file_name = 'all_files'
curr_dir = Path().parent.resolve()

CRAWL_FILEPATH = Path.joinpath(curr_dir.parent, 'crawls/{}/'.format(file_name))
DB_FILEPATH = Path.joinpath(CRAWL_FILEPATH, "{}.db".format(file_name))
LOG_FILEPATH = Path.joinpath(CRAWL_FILEPATH, '{}.log'.format(file_name))