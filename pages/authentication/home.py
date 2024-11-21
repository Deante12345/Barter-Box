import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Define Alert Dialog
        self.dlg = ft.AlertDialog(
            title=ft.Text("Hello, you!"),
            on_dismiss=lambda e: print("Dialog dismissed!")
        )

        def close_dlg(e):
            self.dlg_modal.open = False
            page.update()

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("My cart"),
            content=ft.Text("Current cart items(0)"),
            actions=[
                ft.TextButton("Checkout", on_click=lambda e: page.go("/checkout")),
                ft.TextButton("Back to Shopping", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        def open_dlg(e):
            page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            page.update()

        def open_dlg_modal(e):
            page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            page.update()

        # Store dialog open function for shopping cart
        self.open_dlg = open_dlg

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton(
                    "Cart $0.00",
                    icon=ft.icons.SHOPPING_CART,
                    on_click=self.open_dlg,
                ),
                ft.TextButton(
                    "Trade",
                    on_click=lambda e: page.go("/usermakepost"),
                    icon=ft.icons.SWAP_HORIZ_ROUNDED,
                ),
                ft.TextButton(
                    "Profile",
                    on_click=lambda e: page.go("/profile"),
                    icon=ft.icons.PERSON,
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # Welcome Banner
        self.welcome_banner = ft.Container(
            content=ft.Text(
                "Welcome to BarterBox! Trade items, reduce waste, and connect with your community.",
                size=20,
                weight="bold",
                color="white",
            ),
            padding=10,
            alignment=ft.alignment.center,
            bgcolor="blue",
        )

        # Search Bar
        self.search_bar = ft.Container(
            content=ft.TextField(
                label="Search for items...",
                on_submit=lambda e: page.go(f"/search?query={e.control.value}"),
            ),
            padding=10,
            alignment=ft.alignment.center,
        )

        # Categories Section
        self.categories_section = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Fresh Produce",
                    on_click=lambda e: page.go("/category/food"),
                    style=ft.ButtonStyle(bgcolor=ft.colors.GREEN),
                ),
                ft.ElevatedButton(
                    text="Frozen Foods",
                    on_click=lambda e: page.go("/category/food"),
                    style=ft.ButtonStyle(bgcolor=ft.colors.ORANGE),
                ),
                ft.ElevatedButton(
                    text="Dairy Products",
                    on_click=lambda e: page.go("/category/food"),
                    style=ft.ButtonStyle(bgcolor=ft.colors.BLUE),
                ),
                ft.ElevatedButton(
                    text="Meat and Poultry",
                    on_click=lambda e: page.go("/category/food"),
                    style=ft.ButtonStyle(bgcolor=ft.colors.PINK),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )

        # Main Content
        self.content = ft.Column(
            controls=[
                self.navigation_bar,
                self.welcome_banner,
                self.search_bar,
                self.categories_section,
                ft.Text("Recent Listings:", color="white"),
            ],
            spacing=20,
        )

        # Add main content to the container
        self.content.padding = 20
        self.content.bgcolor = "black"
        self.content.alignment = ft.alignment.center
        self.content.scroll = "auto"
