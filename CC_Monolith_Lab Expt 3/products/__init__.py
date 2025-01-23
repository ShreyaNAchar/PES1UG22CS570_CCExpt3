from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict):
        """Factory method to create a Product instance from a dictionary."""
        return cls(**data)  # Use dictionary unpacking to simplify initialization


def list_products() -> list[Product]:
    """Fetch and convert a list of product data into Product instances."""
    return [Product.load(product) for product in dao.list_products()]  # Use list comprehension


def get_product(product_id: int) -> Product:
    """Fetch a single product by ID and return as a Product instance."""
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None  # Handle the case where the product doesn't exist


def add_product(product: dict):
    """Add a product to the data source."""
    dao.add_product(product)  # Direct delegation


def update_qty(product_id: int, qty: int):
    """Update the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)  # Direct delegation

