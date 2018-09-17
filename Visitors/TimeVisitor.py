from Visitors.BaseVisitor import BaseVisitor


class TimeVisitor(BaseVisitor):
    def parse(self, content):
        date = content.find('time', attrs={'class': 'timeformat'})
        if date is not None:
            date = date.get('datetime')
        return date
