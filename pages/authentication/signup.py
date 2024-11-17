import time
import flet as ft
import sqlite3
from db import db_path
from pages.authentication.crud import check_data_exists, insert_data
from utils.validation import Validation

class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.page = page
        self.expand = True
        self.validation = Validation()
        self.default_border = ft.border.all(width=1, color="#bdcbf4")
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

    # Make sure this method is indented within the class
    def signup(self, e):
        # Collect field values
        first_name = self.first_name_field.value
        last_name = self.last_name_field.value
        email = self.email_field.value
        username = self.username_field.value
        password = self.password_field.value
        re_password = self.re_password_field.value

        # Check if all fields are filled
        if first_name and last_name and email and username and password and re_password:
            conn = sqlite3.connect(db_path)
            
            # Check for valid email
            if not self.validation.is_valid_email(email):
                self.email_field.border = self.error_border
                self.error_field.value = "Enter a valid email"
                self.error_field.size = 12
                self.error_field.update()
                self.email_field.update()
                time.sleep(1)
                self.email_field.border = self.default_border
                self.error_field.size = 0
                self.error_field.update()
                self.email_field.update()

            # Check if email already exists
            elif not check_data_exists(conn, "user", f"email='{email}'"):
                # Insert the user data into the database
                insert_data(conn, "user", (first_name, last_name, email, username, password))

                # Show success message
                self.page.splash = ft.ProgressBar()
                self.error_field.value = "You have successfully been registered"
                self.error_field.color = "green"
                self.error_field.size = 12
                self.error_field.update()
                self.page.update()
                time.sleep(1)
                self.page.splash = None
                self.page.update()
                self.page.go("/login")

            else:
                # If email exists
                self.email_field.border = self.error_border
                self.error_field.value = "Email already exists"
                self.error_field.size = 12
                self.error_field.update()
                self.email_field.update()
                time.sleep(1)
                self.email_field.border = self.default_border
                self.error_field.size = 0
                self.error_field.update()
                self.email_field.update()

        else:
            # If any field is empty
            self.error_field.value = "All fields are needed"
            self.error_field.size = 12
            self.error_field.update()
            time.sleep(1)
            self.error_field.size = 0
            self.error_field.update()

        # Debugging: Confirm the signup process
        print("This is our signup")
        print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}")



