
Logging and persist data
=====
* scrapy crawl dmoz.org --set FEED_URI=items.json --set FEED_FORMAT=json
* print repr(item).decode("unicode-escape")
* write data directly to file
```
   def parse(self, response):  
       filename = response.url.split("/")[-2]  
       open(filename, 'wb').write(response.body)  
```
