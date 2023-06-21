# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SandboxscraperItem(scrapy.Item):
    name = scrapy.Field()
    product_title = scrapy.Field()
    product_brand = scrapy.Field()
    product_description  = scrapy.Field()
    product_current_price = scrapy.Field()
    product_original_price = scrapy.Field()
    product_availability = scrapy.Field()
    images_urls = scrapy.Field()
    product_unique_id = scrapy.Field()
    available_colors = scrapy.Field()
    available_sizes = scrapy.Field()
