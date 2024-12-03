import flet as ft
from pages.authentication import home

class FreshProducePage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        items = [f"Fresh Produce Item {i}" for i in range(1, 11)]

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton(
                    "Cart",
                    icon=ft.icons.SHOPPING_CART,
                    on_click=lambda e: page.go("/checkout"),
                ),
                ft.TextButton(
                    "Home",
                    on_click=lambda e: page.go("/home"),
                    icon=ft.icons.HOME,
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # List of Items
        item_list = ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(ft.icons.CATEGORY),
                    title=ft.Text(item),
                    on_click=lambda e, item=item: self.show_item_details(e, item),
                )
                for item in items
            ],
            spacing=10,
        )

        self.content = ft.Column(
            controls=[
                self.navigation_bar,
                ft.Text("Fresh Produce", size=24, weight="bold"),
                item_list,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        )

        self.controls = [self.content]

    def show_item_details(self, e, item):
        e.page.dialog = ft.AlertDialog(
            title=ft.Text("Item Details"),
            content=ft.Text(f"Item Name: {item}\nPoints Cost: 10"),
            actions=[
                ft.TextButton("Add to Cart", on_click=lambda _: self.add_to_cart(e.page, item)),
                ft.TextButton("Close", on_click=lambda _: self.close_dialog(e.page)),
            ],
        )
        e.page.dialog.open = True
        e.page.update()

    def add_to_cart(self, page, item_name):
        """Add an item to the cart."""
        self.cart_items.append(item_name)
        self.total_points += 10  # Add 10 points for each item
        page.snack_bar = ft.SnackBar(ft.Text(f"{item_name} added to cart!"))
        page.snack_bar.open = True
        page.dialog.open = False
        page.update()

    def close_dialog(self, page):
        page.dialog.open = False
