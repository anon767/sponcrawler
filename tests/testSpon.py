import unittest

import crawl


class TestCrawl(unittest.TestCase):

    def test_crawl(self):
        crawler = crawl.SponCrawler()
        self.assertGreater(len(crawler.articles), 0, "Should atleast return one result")

    def test_crawl_content(self):
        try:
            crawler = crawl.SponCrawler()
            print(crawler.articles)
        except BaseException:
            self.fail("crawling and printing should not raise exception")
