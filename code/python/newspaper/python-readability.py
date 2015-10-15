from readability.readability import Document
import urllib
html = urllib.urlopen(url).read()
readable_article = Document(html).summary()
readable_title = Document(html).short_title()
