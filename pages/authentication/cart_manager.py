# cart_manager.py
class CartManager:
    cart_items = []  # Shared cart items
    total_points = 0  # Shared total points

    @classmethod
    def add_to_cart(cls, item_name):
        cls.cart_items.append(item_name)
        cls.total_points += 10  # Example: Each item adds 10 points

    @classmethod
    def get_cart_items(cls):
        return cls.cart_items, cls.total_points

    @classmethod
    def reset_cart(cls):
        cls.cart_items = []
        cls.total_points = 0
