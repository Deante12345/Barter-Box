import flet as ft
from datetime import datetime
import datetime

class UserMakePost(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.navigation_bar = ft.Row(
            controls=[
                
                ft.TextButton("Home", on_click=lambda e: page.go("/home"), icon=ft.icons.HOME),
                ft.TextButton("Trade", on_click=lambda e: page.go("/usermakepost"), icon=ft.icons.SWAP_HORIZ_ROUNDED),
                ft.TextButton("Profile", on_click=lambda e: page.go("/profile"), icon=ft.icons.PERSON),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # Page reference and layout setup
        self.page = page
        self.expand = True
        self.images = []
        self.default_border = ft.border.all(width=1, color="#bdcbf4")
        self.error_border = ft.border.all(width=1, color="red")
        self.error_field = ft.Text(value="", color="red", size=0)

        # Input Fields
        self.title_field = ft.TextField(label="Title of product", width=400)
        self.description_field = ft.TextField(
            label="Description (e.g., why you don't want it, is it sealed?)",
          
            multiline=True,
            width=400,
        )
        self.quantity_field = ft.TextField(label="Quantity", width=100)
        self.points_field = ft.TextField(label="Amount of points you want",  width=100)
        self.zip_field = ft.TextField(label="Zip Code", max_length=5, width=150)
        self.date_picker = ft.DatePicker(
            first_date=datetime.date.today(),  # Start from today
            last_date=datetime.date(year=2024, month=10, day=1),  # Restrict to a future date
            on_change=self.validate_expiration_date,
        )

        # Image Container
        self.image_container = self.create_image_container()

        # Layout
        self.content = ft.Column(
            controls=[
                self.navigation_bar,
                ft.Text("List Product/s for Barter", size=30, weight=ft.FontWeight.BOLD),
                self.error_field,
                self.title_field,
                self.description_field,
                self.quantity_field,
                self.points_field,
                self.zip_field,
                ft.Text("Expiration Date (must be after today):", size=20),
                self.date_picker,
                self.image_container,
                 ft.ElevatedButton(
                    text="Experation Date",
                    on_click=lambda e: self.date_picker,
                    style=ft.ButtonStyle(
                        
                        bgcolor=ft.colors.BLUE,
                        
                    ),
                ),
                ft.ElevatedButton(
                    text="Post",
                    on_click=self.save_post,
                    style=ft.ButtonStyle(
                        
                        bgcolor=ft.colors.BLUE,
                        
                    ),
                ),
               
            ],
        )

    def create_image_container(self):
        """Creates a container for uploading images."""
        return ft.Row(
            controls=[
                ft.Container(
                    content=ft.Icon(ft.icons.ADD_A_PHOTO),
                    on_click=self.add_image,
                    width=100,
                    height=100,
                    bgcolor="#E0E0E2",
                    border_radius=ft.border_radius.all(8),
                )
            ],
            alignment=ft.MainAxisAlignment.START,
        )

    def add_image(self, e):
        """Handles adding an image to the container."""
        if len(self.images) < 4:
            dialog = ft.FilePicke(on_result=self.process_image_upload)
            self.page.dialog = dialog
            dialog.open()

    def process_image_upload(self, e: ft.FilePickerResultEvent):
        """Processes the uploaded image."""
        if e.files:
            uploaded_image = ft.Image(src=e.files[0].path, fit=ft.ImageFit.COVER)
            self.images.append(uploaded_image)
            self.image_container.controls.append(uploaded_image)
            self.image_container.update()

    def validate_expiration_date(self, e):
        """Validates that the expiration date is after the current date."""
        selected_date = self.date_picker.value
        if not selected_date or selected_date <= datetime.today().date():
            self.error_field.value = "Expiration date must be after today!"
            self.error_field.size = 12
            self.error_field.update()
        else:
            self.error_field.value = ""
            self.error_field.size = 0
            self.error_field.update()

    def save_post(self, e):
        if not self.title_field.value.strip():
            self.error_field.value = "Title is required!"
            self.error_field.size = 12
            self.error_field.update()
            return

        if not self.description_field.value.strip():
            self.error_field.value = "Description is required!"
            self.error_field.size = 12
            self.error_field.update()
            return

        if not self.quantity_field.value.strip().isdigit():
            self.error_field.value = "Quantity must be a valid number!"
            self.error_field.size = 12
            self.error_field.update()
            return

        if not self.points_field.value.strip().isdigit():
            self.error_field.value = "Points must be a valid number!"
            self.error_field.size = 12
            self.error_field.update()
            return

        if not self.zip_field.value.strip().isdigit() or len(self.zip_field.value.strip()) != 5:
            self.error_field.value = "Zip Code must be a 5-digit number!"
            self.error_field.size = 12
            self.error_field.update()
            return

        if not self.date_picker.value:
            self.error_field.value = "Expiration date is required!"
            self.error_field.size = 12
            self.error_field.update()
            return

        # Process the valid data
        print("Post saved successfully!")


    def clear_fields(self):
        """Clears all input fields."""
        self.title_field.value = ""
        self.description_field.value = ""
        self.quantity_field.value = ""
        self.points_field.value = ""
        self.zip_field.value = ""
        self.date_picker.value = None
        self.image_container.controls = [
            ft.Container(
                content=ft.Icon(ft.icons.ADD_A_PHOTO),
                on_click=self.add_image,
                width=100,
                height=100,
                bgcolor="#E0E0E2",
                border_radius=ft.BorderRadius.all(8),
            )
        ]
        self.images = []
        self.update()