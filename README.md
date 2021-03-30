# News

Get headline news from popular news sources

### Get headlines 

```python
headlines = News().get_headlines()

for headline in headlines:
    # Source name, ABC, CNN, etc
    headline.source
    
    headline.article.title

    # First 200 characters of the article
    headline.article.snippet

    headline.article.url
```


### Get articles from specified source

```python
count = 3
articles = News().get_from_source("cnn", count)

for article in articles:
    article.title
    article.snippet
    article.url
```

### Using the commandline interface
```sh
# Get headlines
python news.py

# Get from specified source
python news.py -s "bbc"

# Get from source with count
python news.py -s "npr" -c 3
```

### Available Sources
- ABC
- BBC
- CNN
- NPR
