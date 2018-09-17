from bs4 import BeautifulSoup
from urllib.request import urlopen

class SponCrawler():
    start_url = "http://spiegel.de"
    articles = {}
    visitors = []

    def __init__(self):
        """Grep all current Article URLs"""
        self.page = urlopen(self.start_url)
        self.soup = BeautifulSoup(self.page, 'html.parser')

    def addVisitor(self, visitor):
        """Adds Visitor"""
        self.visitors.append(visitor)

    def parse(self):
        """Parses all urls"""
        all_articles = self.soup.find_all('h2', attrs={'class': 'article-title'})
        for x in all_articles:
            url = x.find('a').get('href')
            if not str.startswith(url, "http"):
                url = self.start_url + url
            self.articles[url] = self.parseUrl(url)
        return self.articles

    def parseUrl(self, url):
        """Parses URL and calls Spon Visitors and creates new Object"""

        print(url)

        article_soup = BeautifulSoup(urlopen(url), 'html.parser')
        main = article_soup.find('div', attrs={'class': 'spArticleContent'})
        if main is None:
            return

        object = {}
        for x in self.visitors:
            object[type(x).__name__] = (x.parse(main))
        object["url"] = url

        return object
