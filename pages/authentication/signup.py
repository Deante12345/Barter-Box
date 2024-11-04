import flet as ft

class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Create instance variables for each input field
        self.first_name_field = ft.TextField(label="First Name", width=300)
        self.last_name_field = ft.TextField(label="Last Name", width=300)
        self.email_field = ft.TextField(label="Email", width=300)
        self.username_field = ft.TextField(label="Username", width=300)
        self.password_field = ft.TextField(label="Password", password=True, width=300)
        self.re_password_field = ft.TextField(label="Re-enter Password", password=True, width=300)

        self.content = ft.Column(
            controls=[
                ft.Text("Hello signUp", color="white"),

                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Welcome!",
                                color="blue",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                            ),
                            self.first_name_field,
                            self.last_name_field,
                            self.email_field,
                            self.username_field,
                            self.password_field,
                            self.re_password_field,
                            ft.ElevatedButton(text="Sign Up", on_click=lambda e: page.go("/login") ),
                        ]
                    ),
                ),
            ]
        )

    # Method to handle the sign-up action
    def register_user(self, e):
        # Grab the values of each field
        email = self.email_field.value
        password = self.password_field.value
       
        # Replace with actual registration logic
        