import scrapy
from scrapy.loader import ItemLoader
from humorquotes.items import PythonPostItems


class PythonPostSpider(scrapy.Spider):
    name = "python_posts"
    allowed_domains = "https://www.reddit.com/r/Python/"
    start_urls = [
         'https://www.reddit.com/r/Python/'
    ]


    def parse(self, response):
        post_div = 'div[data-testid="post-container"]'
        all_posts = response.css(post_div)

        for post in all_posts:
            yield self.get_post_item(response, post)
            
    
    def get_post_item(self, response, post):
        post_item = PythonPostItems()

        title_div = post.css('div[data-adclicklocation="title"]')


        post_item['title'] = title_div.css('div h3::text').get()
        post_item['post_link'] = response.urljoin(title_div.css('div div:nth-child(2) > a[data-click-id="body"]::attr(href)').get())
        post_item['post_type'] = title_div.css('div div:first-child span::text').get()

        post_item['votes'] = post.css('button[aria-label="upvote"] + div::text').get()
        post_item['comments_count'] = post.css('a[data-click-id="comments"] span::text').re(r'(\d+)')

        post_item['post_text'] = self.get_post_text(post)
        return post_item


    def get_post_text(self, post):
        post_text_list = post.css('a[data-click-id="body"] div[data-click-id="text"] div p::text').getall()

        if post_text_list is None:
            return ""

        return "".join(post_text_list)

            


            




