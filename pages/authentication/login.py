import flet as ft

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        self.content = ft.Row(
            controls=[
                ft.Container(
                    bgcolor="#9dc8e0",  # Light blue background
                    expand=4,
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Barter Box",
                                color="blue",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.ElevatedButton(text="Go Back", on_click=lambda e: page.go("/signup")),
                        ],
                    ),
                ),
                ft.Container(
                    bgcolor="#9dc8e0",  # Light blue background
                    expand=3,  # Adjust the width of the login container
                    content=ft.Container(
                        bgcolor="white",
                        border_radius=10,  # Optional: Add rounded corners to the form
                        padding=ft.padding.all(20),  # Padding for the white box
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,  # Center the form elements
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center horizontally
                            controls=[
                                ft.TextField(label="Username", width=300),
                                ft.TextField(label="Password", password=True, width=300),
                                ft.ElevatedButton(text="Login", on_click=lambda e: page.go("/home")),
                            ],
                        ),
                    ),
                ),
            ]
        )
