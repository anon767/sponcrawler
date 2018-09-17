from Visitors.BaseVisitor import BaseVisitor


class TitleIntroVisitor(BaseVisitor):
    def parse(self, content):
        title_intro = content.find('span', attrs={'class': "headline-intro"})
        if title_intro is not None:
            title_intro = title_intro.contents
        return title_intro
