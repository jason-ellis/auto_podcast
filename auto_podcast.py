"""Main module to download and/or add to RSS any podcasts defined in config.ini
"""

from urllib.request import urlopen
import json
import datetime
import download
import constants
from rss import Rss


def main():
    # Download server response, format as JSON, and convert to Python object
    page = urlopen(constants.URL)
    json_data = page.read()
    json_data = str(json_data)
    json_data = json_data.replace("<br \\\\/>", "")
    json_data = json_data.replace('\\', '')
    json_data = json_data.split('"results":')
    json_data = json_data[1]
    json_data = json_data.rsplit(',"page_data":')
    json_data = json_data[0]
    podcast_list = json.loads(json_data)

    rss = Rss()
    podcasts = {}

    # Create Python object of desired podcasts
    for podcast in podcast_list:
        if 'artist' in podcast and podcast['artist'].lower() in constants.PODCAST_TITLES:
            podcast_artist =        podcast['artist']
            podcast_title =         podcast['title']
            podcast_date_str =      podcast_title.split('- ')
            podcast_date_str =      podcast_date_str[len(podcast_date_str)-1]
            podcast_date =          datetime.datetime.strptime(podcast_date_str, '%m/%d/%Y')
            podcast_mp3 =           podcast['mp3']
            podcast_filename =      "%s - %s.mp3" % (podcast_date_str.replace('/', '-'),
                                                     podcast_artist)
            podcast_feed_filename = podcast_artist.replace(' ', '_')

            podcasts[podcast_title] = {
                'title':            podcast_title,
                'artist':           podcast_artist,
                'date':             podcast_date,
                'date_string':      podcast_date_str,
                'mp3':              podcast_mp3,
                'filename':         podcast_filename,
                'feed_filename':    podcast_feed_filename
            }

    if constants.RSS is True:
        for podcast in podcasts:
            rss.add_rss(podcasts[podcast])

    if constants.DOWNLOAD is True:
        for podcast in podcasts:
            download.download_podcast(podcasts[podcast])

if __name__ == "__main__":
    main()