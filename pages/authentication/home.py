import flet as ft


class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.cart_items = []  # List to store cart items
        self.total_points = 0  # Total points for items in the cart
        self.all_items = [f"Item {i}" for i in range(60)]  # List of all items
        self.filtered_items = self.all_items.copy()  # Initial filtered items are all items

        # Cart dialog
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("My Cart"),
            content=ft.Column([]),  # Placeholder for cart items
            actions=[
                ft.TextButton("Checkout", on_click=lambda e: page.go("/checkout")),
                ft.TextButton("Back to Shopping", on_click=lambda e: self.close_cart_dialog(page)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # Open cart dialog
        def open_cart_dialog(e):
            cart_content = ft.Column(
                controls=[ft.Text(f"- {item}: 10 points", color="black") for item in self.cart_items] +
                          [ft.Text(f"Total Points: {self.total_points}", color="black")]
            )
            self.dlg_modal.content = cart_content
            page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            page.update()

        self.open_cart_dialog = open_cart_dialog

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton("Cart", icon=ft.icons.SHOPPING_CART, on_click=self.open_cart_dialog),
                ft.TextButton("Trade", on_click=lambda e: page.go("/usermakepost"), icon=ft.icons.SWAP_HORIZ_ROUNDED),
                ft.TextButton("Profile", on_click=lambda e: page.go("/profile"), icon=ft.icons.PERSON),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # Search Bar with filtering
        self.search_bar = ft.Container(
            content=ft.TextField(
                label="Search for items...",
                on_submit=self.filter_items,
            ),
            padding=10,
            alignment=ft.alignment.center,
        )

        # Categories Section
        self.categories_section = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Fresh Produce",
                    on_click=lambda e: self.go_to_fresh_produce(page),  # Calls the method to navigate to FreshProducePage
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

        # GridView Section
        self.images = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )
        self.populate_grid()  # Populate grid with initial items

        # Main Content
        self.content = ft.Column(
            controls=[
                self.navigation_bar,
                self.search_bar,
                self.categories_section,
                ft.Container(content=ft.Text("Explore Popular Items:", color="white", size=18), padding=10),
                self.images,
            ],
            spacing=20,
        )

        self.content.padding = 20
        self.content.bgcolor = "black"
        self.content.alignment = ft.alignment.center
        self.content.scroll = "auto"
        self.content.expand = True
        self.controls = [self.content]

    def populate_grid(self):
        """Populate the grid with items based on `self.filtered_items`."""
        self.images.controls.clear()
        for index, item_name in enumerate(self.filtered_items):
            image = ft.Image(
                src=f"https://picsum.photos/150/150?{index}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
            self.images.controls.append(
                ft.GestureDetector(content=image, on_tap=lambda e, index=index: self.on_image_click(e, index))
            )

    def filter_items(self, e):
        """Filter items in the grid based on the search query."""
        query = e.control.value.lower()
        self.filtered_items = [item for item in self.all_items if query in item.lower()]
        self.populate_grid()  # Refresh grid with filtered items
        e.page.update()

    def on_image_click(self, e, image_index):
        """Handle item click and show details dialog."""
        item_name = self.filtered_items[image_index]  # Get the clicked item's name
        e.page.dialog = ft.AlertDialog(
            title=ft.Text("Item Details"),
            content=ft.Text(f"Item Name: {item_name}\nPoints Cost: 10"),
            actions=[
                ft.TextButton("Add to Cart", on_click=lambda _: self.add_to_cart(e.page, item_name)),
                ft.TextButton("Close", on_click=lambda _: self.close_item_dialog(e.page)),
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

    def close_item_dialog(self, page):
        """Close the item details dialog."""
        page.dialog.open = False
        page.update()

    def close_cart_dialog(self, page):
        """Close the cart dialog."""
        self.dlg_modal.open = False
        page.update()

    def go_to_fresh_produce(self, page):
        """Navigate to the Fresh Produce page."""
        page.go("/freshproduce")  # Navigate to the Fresh Produce page using page.go()
