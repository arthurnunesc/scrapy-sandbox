## Example urls

```python
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

class Product(pydantic.BaseModel):
    product_title: str
    product_brand: str
    product_description: str
    product_current_price: float
    product_original_price: float
    product_availability: bool
    images_urls: List[str]
    product_unique_id: str
    available_colors: List[str]
    available_sizes: List[str]
    category_path: Optional[str] # e.g. Women > Footwear > Running


h = {
    "Host": "www.adidas.es",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "X-INSTANA-T": "283fdb8de6be7ca4",
    "X-INSTANA-S": "283fdb8de6be7ca4",
    "X-INSTANA-L": "1,correlationType=web;correlationId=283fdb8de6be7ca4",
    "Content-Type": "text/plain;charset=UTF-8",
    "Content-Length": "3736",
    "Origin": "https://www.adidas.es",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.adidas.es/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
}
c = {
    "geo_ip": "79.156.136.188",
    "akacd_generic_prod_grayling_adidas": "3861979726~rv=41~id=e01cf0efced882bda311a662fc326b9c",
    "akacd_plp_prod_adidas_grayling": "3861979727~rv=11~id=5e6cc1f118a5fcee2f1f75588ae95809",
    "persistentBasketCount": "0",
    "userBasketCount": "0",
    "mt.v": "5.1506392873.1684526929827",
    "ab_qm": "b",
    "ab_inp": "a",
    "AMCVS_7ADA401053CCF9130A490D4C@AdobeOrg": "1",
    "s_cc": "true",
    "notice_preferences": "2",
    "dwanonymous_59b281ba3355a36d0773fea72b18c712": "ab3Fa69mH2e81QYkc9wHUnkChU",
    "__cq_dnt": "0",
    "dw_dnt": "0",
    "newsletterShownOnVisit": "true",
    "pagecontext_cookies": "",
    "pagecontext_secure_cookies": "",
    "RES_TRACKINGID": "81729322809382",
    "ResonanceSegment": "1",
    "akacd_pdp_prod_adidas_grayling": "3862120139~rv=72~id=8d3fdbb37e58ef54dc9bf3dca0ab8741",
    "BVBRANDID": "e181915f-c5f4-4b1b-a2a9-da3e5dadd1d1",
    "__olapicU": "ee763b334aa8b1d139fc780056d11a3e",
    "dwac_bckNkiaagZzJUaaacXYWZIATa4": "t8T2GGW9y409gKhFNrEpswmiA5pc1dw6EaE|dw-only|||EUR|false|Europe%2FMadrid|true",
    "sid": "t8T2GGW9y409gKhFNrEpswmiA5pc1dw6EaE",
    "s_sess": "%5B%5BB%5D%5D",
    "checkedIfOnlineRecentlyViewed": "true",
    "bm_sz": "63E99C201F55F1AA3F908A73B205FD5E~YAAQ3hjdWEwGejuIAQAAqBslRBPs8+Wb+zxT0W7rSwI/49TwmlI71foopCCw9DYY8LK4yH9VlBCHvowWbmXl7YMW0U/3GId/25oC3ez4xGqKbTjx2Vq0gYDnP4tutknk5koxTm8jlJZak6wojiFyYVNBG4MAgZ4v+MLBt6VE6bUjhax8XOvfIvKNlwT5FB39jOpEbKw81QTrOvURyr2L02iEf+EO/xPvyntQU16XpXLRxepInyHXIXmluCrGGZZlVO9u4z12Br78CjwpaRfrpWamq69u8Sl0KwgTFZWUQcMcUwZxXztRPAeOchdNw1RnnqSyBvP4BdZhl/SWoFpAjD28+oca2CWRMsjsxato6jtRDmo1pcFcSEPVS/mtS6jOPCEHLN02vWU4iPeFrwa7MQ4obQ==~4403510~4604738",
}
req = scrapy.Request(url="https://www.adidas.es/terrex-swift-r3-gtx-low-y-3/FZ6410.html", headers={"Accept-Language": "en-US,en;q=0.5", "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})
fetch(req)
```
