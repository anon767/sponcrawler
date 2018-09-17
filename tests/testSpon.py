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
        crawler.add_visitor(ArticleIntroVisitor())
        articleIntros = crawler.parse()
        self.assertGreater(len(articleIntros), 0, "Should atleast return one result")

    def test_title(self):
        try:
            crawler = crawl.SponCrawler()
            crawler.add_visitor(ArticleIntroVisitor())
            crawler.parse()
        except BaseException:
            self.fail("No Exception should be thrown when retrieving title")

    def test_all(self):
        try:
            crawler = crawl.SponCrawler()
            crawler.add_visitor(ArticleIntroVisitor())
            crawler.add_visitor(ParagraphsVisitor())
            crawler.add_visitor(TimeVisitor())
            crawler.add_visitor(TitleIntroVisitor())
            crawler.add_visitor(TitleVisitor())
            crawler.parse()
        except BaseException:
            self.fail("No Exception should be thrown when retrieving all")

    def test_single_url(self):
        crawler = crawl.SponCrawler()
        crawler.add_visitor(TitleVisitor())
        sample_url = "http://www.spiegel.de/gesundheit/diagnose/eingeimpft-peter-aaby-was-sind-unspezifische-effekte-von-impfungen-a-1225184.html"
        result = crawler.parse_url(sample_url)
        self.assertEqual(result["TitleVisitor"][0], "Wie eine provokante These\xa0die Sicht aufs Impfen ändern könnte")
