# Sponspooder 

A super simple Spiegel Online Crawler in python

See tests for example usages

# Requirements

```
pip install beautifulsoup4
```

# Usage

Get all recent Articles with their Titles and corresponding publish timestamp:

```python
import crawl
from Visitors.TimeVisitor import TimeVisitor
from Visitors.TitleVisitor import TitleVisitor

crawler = crawl.SponCrawler()
crawler.add_visitor(TitleVisitor())
crawler.add_visitor(TimeVisitor())
result = crawler.parse()
print(result)
```