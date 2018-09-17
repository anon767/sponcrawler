from Visitors.BaseVisitor import BaseVisitor


class TitleVisitor(BaseVisitor):
    def parse(self, content):
        title = content.find('span', attrs={'class': "headline"})
        if title is not None:
            title = title.contents
        return title
