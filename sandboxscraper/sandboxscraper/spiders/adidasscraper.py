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

    def start_requests(self):
        h = {
            "cookie": 'geo_coordinates=lat=40.41, long=-3.71; AKA_A2=A; _abck=169A9A9CC7D0379B2614E0AF30894F0F~-1~YAAQBY4hF3XpRwiIAQAAVJUjPwnKs9VFXGvY12g+37zfUUCOgjbFsBSE2o6FzN61tM1sJ5eGYAOAUMOGB+NeacnRxqKLhyNMWmwnGaCNCEK0pSHv8oE3V1a5YpNU864NN8N5ni+isKwQKZ+kS5Kb3N4vf7sigpLIL8CcUO1vNd7bWkB2S+qYdzLM1ou6Y6fIMURtJpmTRkBcxbgwe3wA/L7cr3WGtcJyOwvo3DI6h1LGm3qVrXMVGxJdXa6xxUGC1NPjJV6P1g/GrXBrd8ZYjIp4AhpmZk7iIufWlOUbXMJDRK8E77k8YuVURku429Tm0xurFRwg+ep+o0zCxmZgPBZTkJbRrFpK8hyEUeYazfOZZmisaBpk+PNa7yERUaj59/kqmMP5CMH0GqSyIG+Brb8pOQM7XXPIpNGSbdlLYuH3sSdiw2Qztc9TzaI0vRo62+KZzu+QWg==~-1~-1~1684689959; ak_bmsc=E91335B6F44B67E58F77E4F4503676A2~000000000000000000000000000000~YAAQBY4hF8jnRwiIAQAAC3cjPxOYOBUtgtdUDhG/iFL9w7m705CQCUuSf39O4/vqaaNrkyKrxw8Jxp4aigmOxBWukFXIJhD2P0Lr8h0hms8KG22sn5z204UDazDSoh8q5f+RBAcEQKk+67eoH0lXCk2tyEmZzgb9A11Olz7hG6hogGLxvOquP30yQ8ltRFDbgehabUrPc2sIUQc+l/KUpd35mku2/Ahto5FnWgxXV4V5KRdIwpGR47vZb6m5GjCg8tsyjv+rp+L9i2P4lHdY2DvFdUg6Ejj07X1M26AryKpzwpvAmbza8j2N4nJaRN2x91a8Gr9IukcVFoIqwVBwauU5TUo9xBRrx0E+LvgXFXD4R7WyeX5S/ab+fWMpWjQmGsIHTitiXA==; bm_sz=A751F295126E783794599C596513C249~YAAQGI4hFx+rKTSIAQAAvxEbPxPBr1L9dYweNNVtBtd+8+fKyLQjIYarKfGTgxOl9QAIUTa0iMetv894Spsa9shfLy57xkCrqCDSwK+qf0fOO0wRQ9eU70sky/GO8hu+c/URNiinlYE8eTC7Rm81PofALVNHNgJbfIcI3Jm3D6uArcy/awup/o+EejsOlhSazSP8UiPS6JCbGhBHjB2BiMewQ0pmIfcK5qJYqdbK1XaIFkl36A8uZLwH4Z5hwhgQ55pYzOk2hfeBXgndZ7RFHVHumqBwyJcyl8MnbnCXilhBb9fxnXf/s1oHiCTgO9c/WyaIoJGzgDtr6t8hOniOsJ4KRPCufNyCSdWcZYNydQLDrclfzy/VgDmE4RAZLQN9RZj/pdtWPOqkBeRqxlSIsA8=~3356997~4404289; mt.v=5.1872337011.1684685920539; RT="z; ab_qm=b; mt.sc=%7B%22i%22%3A1684685925786%2C%22d%22%3A%5B%5D%7D; geo_ip=79.156.136.188; geo_country=ES; akacd_generic_prod_grayling_adidas=3862138717~rv=49~id=db7b8aef50647332bcd2cbef7e150e3e; akacd_plp_prod_adidas_grayling=3862138717~rv=65~id=613ff70d1bfbdc5311dfbd1b2bad21a2; persistentBasketCount=0; userBasketCount=0; dwsid=kdHgutbPvuSA34voXyfthBTrh99uc8v7va291a-N3ueMSNPC4RmosNRMDGREysB6Cbn7dWOLDO-mfLXOcIHDvw==; fallback_dwsid=kdHgutbPvuSA34voXyfthBTrh99uc8v7va291a-N3ueMSNPC4RmosNRMDGREysB6Cbn7dWOLDO-mfLXOcIHDvw==; pagecontext_cookies=; pagecontext_secure_cookies=; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; ab_inp=b; s_cc=true; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19499%7CMCMID%7C36243463357088667181757733032661332202%7CMCAAMLH-1685290724%7C6%7CMCAAMB-1685290724%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1684693125s%7CNONE%7CMCAID%7CNONE; UserSignUpAndSave=3; newsletterShownOnVisit=false; utag_main=v_id:01883f1b24f1001518bd8db8ea6c0504600160090086e$_sn:1$_se:8$_ss:0$_st:1684688276872$ses_id:1684685923570%3Bexp-session$_pn:3%3Bexp-session$ab_dc:TEST%3Bexp-1689870471878$_vpn:3%3Bexp-session$_prevpage:HOME%3Bexp-1684690076881$ttdsyncran:1%3Bexp-session$dcsyncran:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session; s_pers=%20s_vnum%3D1685570400898%2526vn%253D1%7C1685570400898%3B%20s_invisit%3Dtrue%7C1684688276814%3B; notice_preferences=2; _gcl_au=1.1.1624391566.1684686477; _ga_4DGGV4HV95=GS1.1.1684686473.1.1.1684686476.0.0.0; _uetsid=72720940f7f411ed9541ef21c1935d37; _uetvid=72722130f7f411ed9e71fd14cf34eeb4; _scid=d523711e-0068-4323-88e6-f8a06a7d1bf0; _scid_r=d523711e-0068-4323-88e6-f8a06a7d1bf0; _pin_unauth=dWlkPVpqZzBNR1JqTW1JdE5USmxNaTAwT0dSbUxXSXlaamt0TXpFNU1EbGtZell4T0RobQ; QSI_HistorySession=https%3A%2F%2Fwww.adidas.es%2F~1684686479687',
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=h, callback=self.parse)

    def parse(self, response):
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
