from Visitors.BaseVisitor import BaseVisitor


class ArticleIntroVisitor(BaseVisitor):
    def parse(self, content):
        article_intro = content.find('p', attrs={'class': 'article-intro'}).find('strong')
        if article_intro is not None:
            article_intro = article_intro.contents
        return article_intro
