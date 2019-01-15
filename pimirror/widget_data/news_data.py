import feedparser
from random import randint
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import re

class News(QtCore.QObject):
    """News articles using RSS

    Returns:
        list -- List containing self.headline_count number of news dict
    """


    current_headlines = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self.news_sources = ['https://www.nbcnewyork.com/news/tech/?rss=y']
        self.headline_count = 3
        self.update_time = 900 # 15 minutes recommended (900)
        self.duplicates = True

    def add_source(self, source : str):
        """Add an RSS feed to the widget

        Arguments:
            source {str} -- RSS URL
        """

        self.news_sources.append(source)

    @staticmethod
    def clean_html(raw):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw)
        return cleantext

    @QtCore.pyqtSlot()
    def update_headlines(self):
        while True:
            updated_headlines = []
            selected_sources = []
            for source in range(self.headline_count):
                next_source = self.news_sources[randint(0, len(self.news_sources)-1)]
                if self.duplicates:
                    selected_sources.append(next_source)
                else:
                    if not next_source in selected_sources:
                        selected_sources.append(next_source)

            for source in selected_sources:
                data = feedparser.parse(source)
                entry = data.entries[randint(0, len(data.entries)-1)]
                try:
                    content = {
                        "source": data.feed.title,
                        "title": entry.title,
                        "summary": entry.summary,
                        "author": entry.author,
                        "content": self.clean_html(entry.content[0]["value"])
                    }
                except AttributeError:
                    content = {
                        "source": data.feed.title,
                        "title": entry.title,
                        "summary": entry.summary,
                        "author": entry.author,
                        "content": "N/A"
                    }

                updated_headlines.append(content)
            self.current_headlines.emit(updated_headlines)
            sleep(self.update_time)

