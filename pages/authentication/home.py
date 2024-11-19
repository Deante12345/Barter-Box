import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Alert Dialog for Shopping Cart
        self.shoppingCart = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes"),
                ft.TextButton("No"),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.add(
                ft.Text("Modal dialog dismissed"),
            ),
        )

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton(
                    "Cart $0.00", 
                    icon=ft.icons.SHOPPING_CART, 
                    on_click=lambda e: page.update(self.shoppingCart)
                ),
                ft.TextButton("Trade", on_click=lambda e: page.go("/trade"), icon=ft.icons.SWAP_HORIZ_ROUNDED),
                ft.TextButton("Profile", on_click=lambda e: page.go("/profile"), icon=ft.icons.PERSON),
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
                    style=ft.ButtonStyle(bgcolor=ft.colors.GREEN)
                ),
                ft.ElevatedButton(
                    text="Frozen Foods",
                    on_click=lambda e: page.go("/category/food"),
                    style=ft.ButtonStyle(bgcolor=ft.colors.ORANGE)
                ),
                ft.ElevatedButton(
                    text="Dairy Products",
                    on_click=lambda e: page.go("/category/food"),
                    style=ft.ButtonStyle(bgcolor=ft.colors.BLUE)
                ),
                ft.ElevatedButton(
                    text="Meat and Poultry",
                    on_click=lambda e: page.go("/category/food"),
                    style=ft.ButtonStyle(bgcolor=ft.colors.PINK)
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
