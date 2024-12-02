import flet as ft
from datetime import datetime
import datetime
import re

class UserMakePost(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        #initializing variables
        self.page = page
        self.expand = True
        self.images = []
        self.default_border = ft.border.all(width=1, color="#bdcbf4")
        self.error_border = ft.border.all(width=1, color="red")
        self.error_field = ft.Text(value="", color="red", size=0)

        # creating the input fields
        self.title_field = ft.TextField(label="Title of product", width=400)
        self.description_field = ft.TextField(
            label="Description (e.g., why you don't want it, is it sealed?)",
            multiline=True,
            width=400,
        )
        self.quantity_field = ft.TextField(label="Quantity", width=100)
        self.points_field = ft.TextField(label="Amount of points you want",  width=150)
        self.zip_field = ft.TextField(label="Zip Code", max_length=5, width=150)
        self.expiration_date_field = ft.TextField(
            label="Expiration Date (MM-DD-YYYY):",
            width=200
        )

        # food category dropdown box
        self.category_dropdown = ft.Dropdown(
            label="Food Category",
            options=[
                ft.dropdown.Option("Fresh Produce"),
                ft.dropdown.Option("Frozen Foods"),
                ft.dropdown.Option("Dairy Products"),
                ft.dropdown.Option("Meat and Poultry"),
            ],
            width=200
        )
    
        self.file_picker = ft.FilePicker(on_result=self.process_image_upload)
        self.page.overlay.append(self.file_picker)
        self.image_container = self.create_image_container()

        # layout of the page and the order shown on page
        self.content = ft.Column(
            controls=[
                ft.Text("List Product/s for Barter", size=30, weight=ft.FontWeight.BOLD),
                self.error_field,
                self.title_field,
                self.description_field,
                self.quantity_field,
                self.points_field,
                self.zip_field,
                self.expiration_date_field,
                self.category_dropdown,
                self.image_container,
                ft.ElevatedButton(
                    text="Post",
                    on_click=self.save_post,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE,
                    ),
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )

    # making the container for the images so they can be uploaded
    def create_image_container(self):
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
        if len(self.images) <=4:
            self.file_picker.pick_files()

    def process_image_upload(self, e: ft.FilePickerResultEvent):
        if e.files:
            uploaded_image = ft.Image(src=e.files[0].path, fit=ft.ImageFit.COVER, width=200, height=200,)
            self.images.append(uploaded_image)
            self.image_container.controls.append(uploaded_image)
            self.image_container.update()

    # checks if expiration date is valid and if it is after today's date
    def validate_expiration_date(self, date_start):
        try:
            expiration_date = datetime.datetime.strptime(date_start, "%m-%d-%Y").date()
            if expiration_date <= datetime.date.today():
                return False  
            return True
        except ValueError:
            return False  

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

        if not self.validate_expiration_date(self.expiration_date_field.value.strip()):
            self.error_field.value = "Expiration date must be a valid date after today (MM-DD-YYYY)!"
            self.error_field.size = 12
            self.error_field.update()
            return
        
        if not self.category_dropdown.value:
            self.error_field.value = "Select a category!"
            self.error_field.size = 12
            self.error_field.update()
            return

        # Process the valid data
        print("Post saved successfully!")
        self.page.go("/home")

    def clear_fields(self):
        """Clears all input fields."""
        self.title_field.value = ""
        self.description_field.value = ""
        self.quantity_field.value = ""
        self.points_field.value = ""
        self.zip_field.value = ""
        self.expiration_date_field.value = ""
        self.category_dropdown.value = None
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
