import scrapy

from yandere.items import PostItem


class PostSpider(scrapy.Spider):
    """
    Post List Spider
    limit: How many posts you want to retrieve. There is a hard limit of 100 posts per request.
    page: The page number.
    tags: The tags to search for.
    """
    name = 'post'
    allowed_domains = ['yande.re']

    def __init__(self, limit=100, page=1, tags='', username='', vote=3, **kwargs):
        super().__init__(**kwargs)
        start_url = f'https://yande.re/post.json?limit={limit}&page={page}&tags={tags}'
        if username and vote:
            start_url += f' vote:{vote}:{username}'
        self.start_urls = [start_url]

    def parse(self, response, **kwargs):
        posts = response.json()
        for post in posts:
            item = PostItem()
            item['file_url'] = post['file_url']
            yield item
