# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonPostItems(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    post_type = scrapy.Field()
    post_link = scrapy.Field()
    votes = scrapy.Field()
    post_text = scrapy.Field()
    comments_count = scrapy.Field()
