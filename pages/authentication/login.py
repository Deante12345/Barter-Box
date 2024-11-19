import flet as ft

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Create instance variables for username and password fields
        self.username_field = ft.TextField(label="Username", width=300)
        self.password_field = ft.TextField(label="Password", password=True, width=300)

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
                            
                            ft.Image(
                                src="assets/Barter Box Trans.png",  # Path to your logo
                                width=350,  # Adjust the width as needed
                                height=350,  # Adjust the height as needed
                               fit=ft.ImageFit.CONTAIN,  # Ensure the image maintains aspect ratio
                            ),
                            ft.Text(
                                "Barter Box",
                                color="blue",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.ElevatedButton(text="Create New Account", on_click=lambda e: page.go("/signup")),
                        ],
                    ),
                ),
                ft.Container(
                   
                    expand=3,  # Adjust the width of the login container
                    content=ft.Container(
                        bgcolor="white",
                        border_radius=10,  # Optional: Add rounded corners to the form
                        padding=ft.padding.all(20),  # Padding for the white box
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,  # Center the form elements
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center horizontally
                            controls=[
                                self.username_field,
                                self.password_field,
                                ft.Container(height=20),  # Space between the inputs and button
                                ft.ElevatedButton(text="Login", on_click=lambda e: page.go("/home")),
                            ],
                        ),
                    ),
                ),
            ]
        )

    # Method to handle the login action
    def login_action(self, e):
        # Grab the values of the username and password fields
        username = self.username_field.value
        password = self.password_field.value
        print(f"Username: {username}, Password: {password}")  