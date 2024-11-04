import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Create the navigation bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton("Trade", on_click=lambda e: page.go("/login")),
                ft.TextButton("Profile", on_click=lambda e: page.go("/profile")),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # Main content of the Home page
        self.content = ft.Column(
            controls=[
                self.navigation_bar,  # Add the navigation bar here
                ft.Text("Hello Home page", color="white"),
                ft.ElevatedButton(text="Sign Out", on_click=lambda e: page.go("/login")),
            ]
        )

# Additional page classes like Login can be defined similarly
