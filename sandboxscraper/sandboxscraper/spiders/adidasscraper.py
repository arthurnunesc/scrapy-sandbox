import scrapy
from typing import List
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class AdidasScraper(CrawlSpider):
    name = "adidas_scraper"
    allowed_domains = ["www.adidas.es"]
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
    rules = (Rule(LinkExtractor(allow=()), callback="parse_item", follow=True),)

    def request(self, url, callback):
        h = {
            "Accept-Language": "en-US,en;q=0.9",
        }
        c = {
            "geo_ip": "195.55.43.196",
            "geo_country": "ES",
            "geo_coordinates": "lat=40.41, long=-3.71",
            "AKA_A2": "A",
            "akacd_generic_prod_grayling_adidas": "3862295581~rv=89~id=88d8b6eff90a6476790aee07edeb7b83",
            "_abck": "C7170297EA8A75727618A3CEE12E83C8~-1~YAAQym1lXzbljEeIAQAAa710SAm/9xD0dUqujvu/j+vzk5MGgXdr0ZAcnXCuaj7tPpViWtEJIpGN4Q7uIThivnDobq6E/Lq3KBj+kV1uk6is9vhBhrX+dw98BWytZx6z7Mp28ZHCUNkU1XOUHU+wIX10itQbz/3m/PhvdmDzIMwZtWdlMMfnc9wltw7zX/fEN6k+ir0lNXLXEoJZsCSawKuxvgkRFM+8Ds4UYBesidfxjnyaiuf3OYw1/Y8rZN2WRpdGNytxkBTognCBVwJEqEkE2dZmb8tjWa0Uv9RNb9o9jTtwackKX0dLUfPlMFFJ73KlZfMbWuX05vOnyfqvNGHE2Xry08/bD06lpcHBf3sgkI1wuAHvTX1O/CdlPy5yxgFLjY6ylR2VidOsAW9L9NVUQX/aqPR4YAEaMpEGgPZLKePTzeQoLeU=~-1~||-1||~1684846309",
            "ak_bmsc": "1442BAC63B710F4FCF44696C4B538A29~000000000000000000000000000000~YAAQym1lXwrkjEeIAQAAsa50SBPPImDUP+2IXPno6Vb9Up1mf2cRn6mJk3/dwsFcRpZMfmhw28XtFybM4DtQ8Kob39QQ9VJtE61kzER/XMMHaeE8IehTOPf8GJ38tHxG5whBhRTvrG1C7byWpa85G/e1ciajB47MCAlw1rwCVBz8wDKK1qReywIqqc0Tt1dtpo7sbkWhpXApAeq0fRT/gOWSpYRtu1UcFawqA63kGmQm+dar2uHfHoBnZI4bfI3DqNZO5+0+rWF8oJcNVAp0mgfzd36/WovAyNBMsc2m2gNW6bUXUhzMU/mTyHTUmma9jaCY96BokcJhv4M9S1WeZFowNIo6WMUS2EMBHSthEr7jSvY4YJjKl6Clqi7W0vWmJmGQwFpz",
            "bm_sz": "514AE047BCAECA6EF847CDC9BFD9480E~YAAQym1lXwvjjEeIAQAATqF0SBMIVLY/GvNfRrbxpVeT7voSgYadGxxV1Nw59/tTUWY0aJ6inbt5Xd+QZBej5F74Laj10mat7uyjMwkrecvjdmdB49DdnJE4SQ2UPLFSqFg24M3Kxc+AvwAZJpRErqa9mRMYkkmZfWrFBzz2VzqtXENgDWe5ziZ3Ky83Nub+cWkpXTYasIwPCCrax4R3ctQeiauLj3+alS8PY+aIWtOoO1CO7vPuVPpA8bY3PyGoUFo2uE+otw0lUz7FUybV45bU/irGstJ4hhJPCZ67Tt8DZMayRCg98QEM+3h51k6TyXGteDe7shH8jikIG6uYhAEg+jEJyRJDC/+fcldPhtkoFtx3aZ9/bumsnsaOuLnIVLtucSv6WR9nAf7AVA6GXg==~3159601~3617588",
            "akacd_plp_prod_adidas_grayling": "3862295582~rv=93~id=c9d90c9fb913f260e398b43de02f62b8",
            "UserSignUpAndSave": "1",
            "persistentBasketCount": "0",
            "userBasketCount": "0",
            "newsletterShownOnVisit": "false",
            "dwsid": "B_sNQXau8LIHISlTetQHAL2iwfYZe1cBgcoA9vMzA3im7AjiLdk7ACSmpoKASO_r8VUgKJxZvwcMiCYW2c5o1A==",
            "fallback_dwsid": "B_sNQXau8LIHISlTetQHAL2iwfYZe1cBgcoA9vMzA3im7AjiLdk7ACSmpoKASO_r8VUgKJxZvwcMiCYW2c5o1A==",
            "pagecontext_cookies": "",
            "pagecontext_secure_cookies": "",
            "mt.v": "5.1225526451.1684842786484",
            "utag_main": "v_id:01884874be8200100c0e890642260504600160090086e$_sn:1$_se:2$_ss:0$_st:1684844591424$ses_id:1684842790531%3Bexp-session$_pn:1%3Bexp-session$ab_dc:TEST%3Bexp-1690026790548$_vpn:1%3Bexp-session$_prevpage:HOME%3Bexp-1684846390953",
            "ab_qm": "b",
            "AMCV_7ADA401053CCF9130A490D4C@AdobeOrg": "-227196251|MCIDTS|19501|MCMID|11934500997958010111591625035882355353|MCAID|NONE|MCOPTOUT-1684849992s|NONE",
            "ab_inp": "a",
            "AMCVS_7ADA401053CCF9130A490D4C@AdobeOrg": "1",
            "s_pers": " s_vnum=1685570400338&vn=1|1685570400338; s_invisit=true|1684844592344;",
            "s_cc": "true",
        }
        return scrapy.Request(url=url, callback=callback, cookies=c, headers=h)
        # return scrapy.Request(url=url, callback=callback)

#     def start_requests(self):
#         for i, url in enumerate(self.start_urls):
#             yield self.request(url, self.parse_items)

    def parse_items(self, response):
        cookie_value = response.headers.get("Set-Cookie")
        if cookie_value:
            # Set the cookie value in subsequent requests
            yield scrapy.Request(
                response.url, headers={"Cookie": cookie_value}, callback=self.parse_page
            )

    def parse_page(self, response):
        if (
            response.css("div.gl-price-item--sale::text").get() is not None
            and response.css("div.gl-price-item--crossed::text").get() is not None
        ):
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
