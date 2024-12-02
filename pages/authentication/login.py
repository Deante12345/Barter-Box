import flet as ft
from psycopg2.errors import DatabaseError
from db.queries import get_user_by_username
from db.hash_password import verify_password
import bcrypt

class Login(ft.Container):




    def __init__(self, page: ft.Page):
        super().__init__()

        # Create instance variables for username and password fields
        self.username_field = ft.TextField(label="Username", width=300)
        self.password_field = ft.TextField(label="Password", password=True, width=300)
        self.error_field = ft.Text(value="", color="red", size=0)


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
                                self.error_field,
                                ft.Container(height=20),  # Space between the inputs and button
                                ft.ElevatedButton(text="Login", on_click=self.login_action),
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

        if not username or not password:
            self.error_field.value = "Please Enter username and password"
            self.error_field.update()
            return

        try:
            user = get_user_by_username(username)
            if not user:
                self.error_field.value = "Invalid username or password"
                self.error_field.update()
                return

            #verify password logic
            user_id, db_username,hashed_password = user
            hashed_password = user['password_hash']
            print(f"Retrieved hash: '{hashed_password}'")
            print(f"Length: {len(hashed_password)}")

            if verify_password(password, hashed_password):
                self.page.session.set("user_id",user['user_id'])
                self.page.session.set("username",user['username'])
                #saved_user_id = self.page.session.get("user_id")
                #print(f"User ID saved to session: {saved_user_id}")
                self.error_field.value = "Login successful!"
                self.error_field.color = "green"
                self.error_field.update()
                self.page.go("/home")
        except DatabaseError as ex:
            print(f"Database error: {ex}")
            self.error_field.value = "An error occurred. Please try again."
            self.error_field.update()


        #print(f"Username: {username}, Password: {password}")