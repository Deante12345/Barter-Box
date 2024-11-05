import flet as ft


from utils.validation import Validation

class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.expand = True
        self.validation = Validation()
        self.error_border = ft.border.all(color="red", width=1)
        self.error_field = ft.Text(value="", color="red", size=0)

        # Create instance variables for each input field
        self.first_name_field = ft.TextField(label="First Name", width=300)
        self.last_name_field = ft.TextField(label="Last Name", width=300)
        self.email_field = ft.TextField(label="Email", width=300)
        self.username_field = ft.TextField(label="Username", width=300)
        self.password_field = ft.TextField(label="Password", password=True, width=300)
        self.re_password_field = ft.TextField(label="Re-enter Password", password=True, width=300)

        # Set up the UI layout with fields and a signup button
        self.content = ft.Column(
            controls=[
                ft.Text("Hello signUp", color="white"),

                ft.Container(
                    bgcolor="#9dc8e0",  # Light blue background
                    expand=4,
                    padding=ft.padding.all(100),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Welcome!",
                                color="blue",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                            ),
                            self.error_field,
                            self.first_name_field,
                            self.last_name_field,
                            self.email_field,
                            self.username_field,
                            self.password_field,
                            self.re_password_field,
                            # Call the signup method on button click
                            ft.ElevatedButton(text="Sign Up", on_click=self.signup),
                        ]
                    ),
                ),
            ]
        )

    # Method to handle the signup action
    def signup(self, e):
        # Collect field values and print a confirmation message
        first_name = self.first_name_field.value
        last_name = self.last_name_field.value
        email = self.email_field.value
        username = self.username_field.value
        password = self.password_field.value
        re_password = self.re_password_field.value

        # Basic print statement to confirm signup
        print("This is our signup")
        print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}")

        # Add your actual signup logic here (e.g., form validation, server requests)
