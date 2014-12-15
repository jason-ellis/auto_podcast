"""Rss object to create an XML file in podcast RSS format if none exists and populate
the file with all podcast results provided.
"""

from os.path import isfile
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import parse

import constants


class Rss(object):

    def create_xml(self, podcast):
        """Create XML file with RSS podcast structure
        """

        # <rss>
        rss_xml = Element('rss')
        ElementTree.register_namespace('atom', 'http://www.w3.org/2005/Atom')
        rss_xml.set("version", "2.0")

        # <rss><channel>
        channel_xml = SubElement(rss_xml, 'channel')

        # <rss><channel><title>
        title_xml = SubElement(channel_xml, 'title')
        title_xml.text = podcast['artist']

        #<rss><channel><atom:link>
        atom_xml = SubElement(channel_xml, '{http://www.w3.org/2005/Atom}link')
        atom_xml.set('href', constants.RSS_URL + podcast['feed_filename'])
        atom_xml.set('rel', 'self')
        atom_xml.set('type', 'application/rss+xml')

        # <rss><channel><link>
        link_xml = SubElement(channel_xml, 'link')
        link_xml.text = constants.RSS_URL + podcast['feed_filename']

        # <rss><channel><language>
        language_xml = SubElement(channel_xml, 'language')
        language_xml.text = 'en-us'

        # <rss><channel><description>
        description_xml = SubElement(channel_xml, 'description')
        description_xml.text = constants.RSS_DESCRIPTION

        output_file = open(constants.RSS_DIR + podcast['feed_filename'], 'w')
        output_file.write('<?xml version="1.0" encoding="UTF-8"?>')
        output_file.write(ElementTree.tostring(rss_xml, encoding="unicode"))
        output_file.close()

    def add_rss(self, podcast):
        """Add podcast to XML file. Fire create_xml if the file doesn't exist.
        """

        # If a XML file doesn't exist for this podcast, create one
        if not isfile(constants.RSS_DIR + podcast['feed_filename']):
            self.create_xml(podcast)

        # Load XML data for parsing and create list of episodes for comparison
        xml_tree = parse(constants.RSS_DIR + podcast['feed_filename'])
        xml_channel = xml_tree.find('channel')
        xml_titles = []
        for node in xml_channel.findall('item/title'):
            xml_titles.append(node.text)

        if podcast['title'] not in xml_titles:
            if constants.VERBOSE:
                print(podcast['title'] + " added to RSS")
            item_xml = SubElement(xml_channel, 'item')
            title_xml = SubElement(item_xml, 'title')
            title_xml.text = podcast['title']
            enclosure_xml = SubElement(item_xml, 'enclosure')
            enclosure_xml.set('url', podcast['mp3'])
            enclosure_xml.set('type', 'audio/mpeg')
            enclosure_xml.set('length', '1')
            pubdate_xml = SubElement(item_xml, 'pubDate')
            pubdate_xml.text = podcast['date'].strftime('%a, %d %b %Y 00:00:00 -0600')
            guid_xml = SubElement(item_xml, 'guid')
            guid_xml.text = podcast['mp3']
            xml_tree.write(constants.RSS_DIR + podcast['feed_filename'])

        else:
            if constants.VERBOSE:
                print(podcast['title'] + ' NOT added to RSS')