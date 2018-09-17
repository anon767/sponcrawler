from Visitors.BaseVisitor import BaseVisitor


class ParagraphsVisitor(BaseVisitor):
    def parse(self, content):
        paragraphs = []
        paragraphs_raw = content.find('div', attrs={'class': 'article-section'})
        if paragraphs_raw is not None:
            paragraphs_raw = paragraphs_raw.find_all('p')
            for paragraph in paragraphs_raw:
                paragraphs.append(paragraph.contents)
        return paragraphs
