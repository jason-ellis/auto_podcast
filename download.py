"""Module to download podcasts if required in config.ini
"""
from os.path import isfile
from urllib.request import urlretrieve
import constants


def download_podcast(podcast):
    """ Download a podcast passed to it.
    """
    if podcast['date_string'] != constants.DOWNLOAD_DATE and constants.DOWNLOAD_DATE is not '':
        if constants.VERBOSE:
            print("{0:s} found but not downloaded because of date.".format(podcast['title']))
    elif isfile(constants.PODCAST_DIR + podcast['filename']):
        if constants.VERBOSE:
            print("{0:s} already exists. Download skipped".format(podcast['title']))
    else:
        if constants.VERBOSE:
            print('Downloading ' + podcast['title'])
        urlretrieve(podcast['mp3'], constants.PODCAST_DIR + podcast['filename'])
        if constants.VERBOSE:
            print('Finished downloading ' + podcast['title'])