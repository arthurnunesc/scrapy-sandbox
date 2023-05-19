import scrapy


class YSLSpider(scrapy.Spider):
    name = "ysl"
    start_urls = [
        "https://www.ysl.com/es-es/comprar-art%C3%ADculos-de-mujer/bolsos/ver-todo"
    ]

    def parse(self, response):
        for product in response.css("li.l-productgrid__item"):
            yield {
                "name": product.css("h2.c-product__name::text").get().strip(),
                "price": product.css("p.c-price__value--current::text").get(),
            }
