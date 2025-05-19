from dataclasses import dataclass
from typing import Optional

@dataclass
class ProductData:
    """
    Represents standardized product information.
    """
    name: str
    sku: str
    price: float
    stock: Optional[int] = None
    # Add other common attributes as needed