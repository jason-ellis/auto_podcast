# Auto Podcast

**What is Auto Podcast?**

This is a Python module to help me create my own RSS feed and download podcasts.

**Why does Auto Podcast exist?**

I'm a fan of a local sports radio station in Dallas and I like to listen everyday. Some other loyal listeners created a website that archives all audio from the sports and they serve it up on their website. For a period of time, they made the audio available via podcast streams. This was very convenient, but it also greatly increased their bandwidth usage, so they discontinued the RSS feeds associated with the audio.

Following the discontinuation of the podcasts, I had to manually download the audio I wanted to listen to. Downloading the audio on a phone frequently timed out before the download completed. THe other option was to download on a computer and transfer it to the phone. Either way, I would also need to move the audio files to a special folder for my podcasting app.

There HAS to be a better way!

![infomercial gif](http://i.imgur.com/0Z0M3Vl.gif)

**What does Auto Podcast do?**

This module was built for my specific need. I made it extensible and reusable where I was able, but some of what it does won't apply to most use cases. You're welcome to build on it and make it work for you!

I approached this project with the intent of making it a scraper. Unfortunately, that was not possible because the information I need (file information and URLs) is served up inside a player that is populated by AJAX after the page loads. Because of this, I've employed the strategy below.

1. Looks at config.ini to gather specifications including:
    - Podcasts to search for (date, name)
    - Whether to download the podcast files to a local directory
    - Whether to add the podcasts to a RSS feed
    - Where to store the RSS feed (I recommend Dropbox)
2. Queries a server (PHP in my case) that returns a JSON response.
3. Converts the JSON data to a Python object.
4. If specified, adds all search results to a RSS XML file locally.
    - If you specified a Dropbox folder for the RSS feed XML, the module converts the share link to one that allows direct access to the file (without Dropbox's viewing UI).
5. If specified, downloads all results matching date to a local destination.

I run this module on my home server with Windows Task Scheduler at defined times throughout the day when I know the newest audio files will become available. If you plan to do the same on Windows 8.1, the following tips I picked up while troubleshooting may be helpful:

- If running whether user is logged on or not, run the script with highest privileges
- As your Action, Program/script should be your Python.exe. 
- Set Arguments to the location of auto_podcast.py, surrounded in quotes if the location contains any spaces. 
- Set Start in as the location of auto_podcast, but DO NOT include any quotes, even if the location contains spaces.

**How can I, the inquisitive reader, use this?**

You can use it however you'd like. As I said, this was made for my specific need, but you're free to modify it as you'd like to make it work for you. It's possible that you may just need to change the SOURCE in config.ini and then modify the JSON manipulation in the first few lines of auto_podcast.main() in auto_podcast.py.

If you have questions about making this work for you, feel free to send me an email.