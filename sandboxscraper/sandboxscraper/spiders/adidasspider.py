import scrapy


class AdidasScraper(scrapy.Spider):
    name = "adidas"
    start_urls = ["https://www.adidas.es/calzado-hombre"]

    def parse(self, response):
        for product in response.css("div.glass-product-card"):
            yield {
                "link": product.css("a::attr(href)").get(),
            }

        next_page = response.css("a.active.gl-cta.gl-cta--tertiary")
        for link in next_page:
            if (link.css("a::attr(data-auto-id)").get() == "plp-pagination-next"):
                next_page = link.css("a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


# if span in div.badge-container___1TJjk == Agotado

# if "div.gl-price-item" without any other class then current_price = original_price
# or
# if just one div in "div.gl-price.gl-price--horizontal.notranslate.gl-price--inline___3nMlh" then current_price = original_price
