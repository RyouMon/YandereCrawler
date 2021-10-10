import scrapy

from yandere.items import PostPageItem


class PostSpider(scrapy.Spider):
    """
    Post List Spider
    limit: How many posts you want to retrieve. There is a hard limit of 100 posts per request.
    page: The page number.
    tags: The tags to search for.
    """
    name = 'post'
    allowed_domains = ['yande.re']

    def __init__(self, limit=100, page=1, tags='', **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://yande.re/post.json?limit={limit}&page={page}&tags={tags}']

    def parse(self, response, **kwargs):
        posts = response.json()
        for post in posts:
            item = PostPageItem()
            item['file_url'] = post['file_url']
            yield item
