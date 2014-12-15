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

# Podcasts to process
PODCAST_TITLES = config.get('PODCASTS', 'PODCAST_TITLES')
if VERBOSE:
    print(PODCAST_TITLES)
PODCAST_TITLES = PODCAST_TITLES.splitlines()
# remove empty items from list
PODCAST_TITLES = [x for x in PODCAST_TITLES if x]
if VERBOSE:
    print(PODCAST_TITLES)

# RSS configuration
RSS_DIR = config.get('LOCAL', 'RSS_DIR')
RSS_BASE_URL = config.get('RSS', 'BASE_URL')
RSS_FOLDER_ID = config.get('RSS', 'FOLDER_ID')
RSS_URL = '{0:s}{1:s}'.format(RSS_BASE_URL, RSS_FOLDER_ID)
RSS_DESCRIPTION = config.get('RSS', 'RSS_DESCRIPTION')