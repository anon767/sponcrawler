import unittest

import crawl
from Visitors.ArticleIntroVisitor import ArticleIntroVisitor
from Visitors.ParagraphsVisitor import ParagraphsVisitor
from Visitors.TimeVisitor import TimeVisitor
from Visitors.TitleIntroVisitor import TitleIntroVisitor
from Visitors.TitleVisitor import TitleVisitor


class TestCrawl(unittest.TestCase):

    def test_crawl(self):
        crawler = crawl.SponCrawler()
        crawler.addVisitor(ArticleIntroVisitor())
        articleIntros = crawler.parse()
        self.assertGreater(len(articleIntros), 0, "Should atleast return one result")

    def test_title(self):
        try:
            crawler = crawl.SponCrawler()
            crawler.addVisitor(ArticleIntroVisitor())
            crawler.parse()
        except BaseException:
            self.fail("No Exception should be thrown when retrieving title")

    def test_all(self):
        try:
            crawler = crawl.SponCrawler()
            crawler.addVisitor(ArticleIntroVisitor())
            crawler.addVisitor(ParagraphsVisitor())
            crawler.addVisitor(TimeVisitor())
            crawler.addVisitor(TitleIntroVisitor())
            crawler.addVisitor(TitleVisitor())
            crawler.parse()
        except BaseException:
            self.fail("No Exception should be thrown when retrieving title")

    def test_single_url(self):
        crawler = crawl.SponCrawler()
        crawler.addVisitor(TitleVisitor())
        sample_url = "http://www.spiegel.de/gesundheit/diagnose/eingeimpft-peter-aaby-was-sind-unspezifische-effekte-von-impfungen-a-1225184.html"
        result = crawler.parseUrl(sample_url)
        self.assertEqual(result["TitleVisitor"][0], "Wie eine provokante These\xa0die Sicht aufs Impfen ändern könnte")
