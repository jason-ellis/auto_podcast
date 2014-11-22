"""constants.py processes the config data in config.ini and makes it available
to other modules. Global variable changes should be done in config.ini.
"""

import configparser
import datetime

# Set configuration according to config.ini
config = configparser.ConfigParser()
config.read('config.ini')

VERBOSE = config.getboolean('SETTINGS', 'VERBOSE')
DOWNLOAD_DATE = config.get('SETTINGS', 'DOWNLOAD_DATE')
if DOWNLOAD_DATE == 'CURRENT_DATE':
    DOWNLOAD_DATE = datetime.date.today().strftime('%m/%d/%Y')
DOWNLOAD = config.getboolean('SETTINGS', 'DOWNLOAD')
RSS = config.getboolean('SETTINGS', 'RSS')
if VERBOSE:
    print("DOWNLOAD_DATE = {0:s}".format(DOWNLOAD_DATE))
    print("DOWNLOAD = {0:b}".format(DOWNLOAD))
    print("RSS = {0:b}".format(RSS))

# Local download location
PODCAST_DIR = config.get('LOCAL', 'PODCAST_DIR')

# Construct URL from config.ini
URL = ''
for string in config['SOURCE']:
    URL = URL + config.get('SOURCE', string)
if VERBOSE:
    print("URL = {0:s}".format(URL))

# Podcasts to download
PODCAST_TITLES = config.get('PODCASTS', 'PODCAST_TITLES')
print(PODCAST_TITLES)
PODCAST_TITLES = PODCAST_TITLES.split('\n')
PODCAST_TITLES = [x for x in PODCAST_TITLES if x]
for string in PODCAST_TITLES:
    string = string.strip(' \n')
print(PODCAST_TITLES)

# RSS configuration
RSS_DIR = config.get('LOCAL', 'RSS_DIR')
RSS_FILENAME = config.get('LOCAL', 'RSS_FILENAME')
if config.get('RSS', 'DROPBOX_LINK') is not None:
    dropbox_url = config.get('RSS', 'DROPBOX_LINK')
    dropbox_url = dropbox_url.replace('www.dropbox.com', 'dl.dropboxusercontent.com')
    head, sep, tail = dropbox_url.partition(RSS_FILENAME)
    RSS_URL = head + RSS_FILENAME
else:
    RSS_BASE_URL = config.get('RSS', 'BASE_URL')
    RSS_FOLDER_ID = config.get('RSS', 'FOLDER_ID')
    RSS_URL = '{0:s}{1:s}{2:s}'.format(RSS_BASE_URL, RSS_FOLDER_ID, RSS_FILENAME)
RSS_TITLE = config.get('RSS', 'RSS_TITLE')
RSS_DESCRIPTION = config.get('RSS', 'RSS_DESCRIPTION')