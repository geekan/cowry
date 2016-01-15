from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'

article = Article(url)
article.download()
article.parse()
print(article.authors)
print(article.publish_date)
print(article.text)
print(article.top_image)
print(article.movies)

article.nlp()
print(article.keywords)
print(article.summary)
