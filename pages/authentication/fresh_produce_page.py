import flet as ft
from pages.authentication import home

class FreshProducePage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.cart_items = []  # List to store cart items
        self.total_points = 0  # Total points for items in the cart
        items = [f"Dairy Product Item {i}" for i in range(1, 11)]  # List of items

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton(
                    "Cart",
                    icon=ft.icons.SHOPPING_CART,
                    on_click=lambda e: self.open_cart_dialog(e, page),
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
                    on_click=lambda e, item=item: self.show_item_details(e, item, page),
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

    def show_item_details(self, e, item, page):
        """Show item details and allow adding to cart."""
        e.page.dialog = ft.AlertDialog(
            title=ft.Text("Item Details"),
            content=ft.Text(f"Item Name: {item}\nPoints Cost: 10"),
            actions=[
                ft.TextButton("Add to Cart", on_click=lambda _: self.add_to_cart(e.page, item, page)),
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

        # Optionally, update the cart information in the page navigation
        page_ref.update()

    def close_dialog(self, page):
        """Close the item details dialog."""
        page.dialog.open = False
        page.update()

    def open_cart_dialog(self, e, page):
        """Open the cart dialog to view added items."""
        cart_content = ft.Column(
            controls=[
                ft.Text(f"- {item}: 10 points", color="black") for item in self.cart_items
            ] + [ft.Text(f"Total Points: {self.total_points}", color="black")]
        )
        cart_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("My Cart"),
            content=cart_content,
            actions=[
                ft.TextButton("Checkout", on_click=lambda e: page.go("/checkout")),
                ft.TextButton("Back to Shopping", on_click=lambda e: self.close_cart_dialog(page)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = cart_dialog
        cart_dialog.open = True
        page.update()

    def close_cart_dialog(self, page):
        """Close the cart dialog."""
        page.dialog.open = False
        page.update()  