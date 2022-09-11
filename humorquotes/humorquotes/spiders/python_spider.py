import scrapy
from humorquotes.items import PythonPostItems


class PythonPostSpider(scrapy.Spider):

    name = "python_posts"
    allowed_domains = "https://www.reddit.com/r/Python/"
    start_urls = ['https://www.reddit.com/r/Python/']

    def parse(self, response):
        post_div = 'div[data-testid="post-container"]'
        all_posts = response.css(post_div)

        for post in all_posts:
            yield self.get_post_item(response, post)

    def get_post_item(self, response, post):
        post_item = PythonPostItems()

        title_div = post.css('div[data-adclicklocation="title"]')

        post_item['title'] = title_div.css('div h3::text').get()
        post_item['post_link'] = self.get_post_link(title_div, response)
        post_item['post_type'] = title_div.css(
            'div div:first-child span::text').get()

        post_item['votes'] = post.css(
            'button[aria-label="upvote"] + div::text').get()
        post_item['comments_count'] = post.css(
            'a[data-click-id="comments"] span::text').re(r'(\d+)')

        post_item['post_text'] = self.get_post_text(post)
        return post_item

    def get_post_text(self, post):
        html_posts_list = post.css(
            'a[data-click-id="body"] div[data-click-id="text"] div p::text')
        post_list = html_posts_list.getall()

        if post_list is None:
            return ""

        return "".join(post_list)

    def get_post_link(self, title_div, response):
        post_link = title_div.css(
            'div div:nth-child(2) > a[data-click-id="body"]::attr(href)').get()

        if post_link is None:
            return ""

        return response.urljoin(post_link)
