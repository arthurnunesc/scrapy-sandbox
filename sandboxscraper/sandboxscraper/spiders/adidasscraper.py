import scrapy
from typing import List


class AdidasScraper(scrapy.Spider):
    name = "adidas_scraper"
    base_url = "https://www.adidas.es"
    start_urls = [
        # item not on sale with a single color
        "https://www.adidas.es/terrex-swift-r3-gtx-low-y-3/FZ6410.html",
        # item not on sale with multiple colors
        "https://www.adidas.es/y-3-makura/FZ6364.html",
        # item on sale with a single color
        "https://www.adidas.es/zapatilla-ultraboost-leather/EF0901.html",
        # item on sale with multiple colors
        "https://www.adidas.es/zapatilla-tensaur-run/GZ3429.html",
        # item out of stock
        "https://www.adidas.es/zapatilla-pharrell-williams-terrex-free-hiker-cold.rdy-hiking/GZ9820.html",
    ]

    def parse(self, response):
        if response.css("div.gl-price-item--sale::text").get() is not None and response.css("div.gl-price-item--crossed::text").get() is not None:
            product_current_price = response.css("div.gl-price-item--sale::text").get()
            product_current_price = float(
                product_current_price.strip().replace("€", "").replace(" ", "")
            )
            product_original_price = response.css(
               "div.gl-price-item--crossed::text"
            ).get()
            product_original_price = float(
               product_original_price.strip().replace("€", "").replace(" ", "")
           )
        else:
           product_current_price = response.css("div.gl-price-item::text").get()
           product_current_price = float(
               product_current_price.strip().replace("€", "").replace(" ", "")
           )
           product_original_price = product_current_price
        yield {
            "product_title": response.css("h1.name___120FN span::text").get(),
            "product_brand": "Adidas",
            "product_description": response.css("p.gl-vspace::text").get(),
            "product_current_price": product_current_price,
            "product_original_price": product_original_price,
        }

        product_availability: bool
        images_urls: List[str]
        product_unique_id: str
        available_colors: List[str]
        available_sizes: List[str]
