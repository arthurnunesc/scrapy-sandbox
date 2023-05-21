import scrapy


class AdidasCrawler(scrapy.Spider):
    name = "adidas_crawler"
    # start_urls = ["https://www.adidas.es/calzado-hombre"]
    start_urls = [
        "https://www.adidas.es/calzado",
        "https://www.adidas.es/ropa",
        "https://www.adidas.es/accesorios",
        "https://www.adidas.es/performance",
        # "https://www.adidas.es/originals",
    ]
    url_suffixes = [
        "-hombre",
        "-mujer",
        "-nino",
        "-nina",
    ]
    count = 0

    def parse(self, response):
        for product in response.css("div.glass-product-card"):
            if product.css("a::attr(href)").get() is not None:
                self.count += 1
            yield {
                "link": product.css("a::attr(href)").get(),
                "count": self.count,
            }

        next_page = response.css("a.active.gl-cta.gl-cta--tertiary")
        for link in next_page:
            if link.css("a::attr(data-auto-id)").get() == "plp-pagination-next":
                next_page = link.css("a::attr(href)").get()
        if type(next_page) is str and next_page is not None:
            yield response.follow(next_page, callback=self.parse)


# if span in div.badge-container___1TJjk == Agotado

# if "div.gl-price-item" without any other class then current_price = original_price
# or
# if just one div in "div.gl-price.gl-price--horizontal.notranslate.gl-price--inline___3nMlh" then current_price = original_price
