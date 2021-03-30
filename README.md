# News

Get headline news from popular news sources

### Usage

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
