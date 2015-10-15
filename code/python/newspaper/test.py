from newspaper import Article
url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'

def quick_analyse(url):
    fields = ['authors', 'publish_date', 'top_image', 'movies', 'keywords', 'summary']

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    print(len(article.html))
    for f in fields:
        print(f + ': ' + str(getattr(article, f)))

    return article

article = quick_analyse(url)
import pdb; pdb.set_trace()
