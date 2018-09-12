from bs4 import BeautifulSoup
from urllib.request import urlopen


class SponCrawler():
    start_url = "http://spiegel.de"
    articles = []

    def __init__(self):
        self.page = urlopen(self.start_url)
        self.soup = BeautifulSoup(self.page, 'html.parser')
        all_articles = self.soup.find_all('h2', attrs={'class': 'article-title'})
        for x in all_articles:
            self.parse(x.find('a').get('href'))

    def parse(self, url):
        if not str.startswith(url, "http://"):
            url = self.start_url + url

        print(url)

        article_soup = BeautifulSoup(urlopen(url), 'html.parser')
        main = article_soup.find('div', attrs={'class': 'spArticleContent'})
        if main is None:
            return

        title_intro = main.find('span', attrs={'class': "headline-intro"})
        if title_intro is not None:
            title_intro = title_intro.contents

        title = main.find('span', attrs={'class': "headline"})
        if title is not None:
            title = title.contents

        article_intro = main.find('p', attrs={'class': 'article-intro'}).find('strong')
        if article_intro is not None:
            article_intro = article_intro.contents

        paragraphs = []
        paragraphs_raw = main.find('div', attrs={'class': 'article-section'})
        if paragraphs_raw is not None:
            paragraphs_raw = paragraphs_raw.find_all('p')
            for paragraph in paragraphs_raw:
                paragraphs.append(paragraph.contents)

        date = main.find('time', attrs={'class': 'timeformat'})
        if date is not None:
            date = date.get('datetime')

        self.articles.append([date, title_intro, title, article_intro, paragraphs])
