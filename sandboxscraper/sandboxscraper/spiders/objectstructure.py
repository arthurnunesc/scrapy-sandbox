import pydantic
from typing import List, Optional


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
