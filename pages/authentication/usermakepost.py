import flet as ft
from datetime import datetime
import datetime
from db.queries import create_post
import re
import requests
import os
from utils.uniqueID import make_ID,add_ID

class UserMakePost(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Initializing variables
        self.page = page
        self.expand = True
        self.images = []
        self.cart_items = []  # Placeholder for cart items
        self.total_points = 0  # Placeholder for total points
        self.all_items = [f"Item {i}" for i in range(60)]  # List of all items
        self.filtered_items = self.all_items.copy()  # Initial filtered items are all items

        self.default_border = ft.border.all(width=1, color="#bdcbf4")
        self.error_border = ft.border.all(width=1, color="red")
        self.error_field = ft.Text(value="", color="red", size=0)

        # Cart Dialog
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("My Cart"),
            content=ft.Column([]),  # Placeholder for cart items
            actions=[
                ft.TextButton("Checkout", on_click=lambda e: page.go("/checkout")),
                ft.TextButton("Back to Shopping", on_click=lambda e: self.close_cart_dialog()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton(
                    "Cart",
                    icon=ft.icons.SHOPPING_CART,
                    on_click=self.open_cart_dialog,  # Trigger cart dialog
                ),
                ft.TextButton(
                    "Profile",
                    on_click=lambda e: page.go("/profile"),
                    icon=ft.icons.PERSON,
                ),
                
                 ft.TextButton("Home", on_click=lambda e: page.go("/home"), icon=ft.icons.HOME),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # Input Fields
        self.title_field = ft.TextField(label="Title of product", width=400)
        self.description_field = ft.TextField(
            label="Description (e.g., why you don't want it, is it sealed?)",
            multiline=True,
            width=400,
        )
        self.quantity_field = ft.TextField(label="Quantity", width=100)
        self.points_field = ft.TextField(label="Amount of points you want", width=150)
        self.zip_field = ft.TextField(label="Zip Code", max_length=5, width=150)
        self.expiration_date_field = ft.TextField(
            label="Expiration Date (MM-DD-YYYY):",
            width=200
        )

        # Food category dropdown box
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

        # Layout of the page and the order shown on page
        self.content = ft.Column(
            controls=[
                self.navigation_bar,  # Add navigation bar at the top
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

    # Cart dialog functionality
    def open_cart_dialog(self, e):
        # Create the cart content
        cart_content = ft.Column(
            controls=[
                ft.Text(f"- {item}: 10 points", color="black") for item in self.cart_items
            ] + [ft.Text(f"Total Points: {self.total_points}", color="black")]
        )
        self.dlg_modal.content = cart_content
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def close_cart_dialog(self):
        self.dlg_modal.open = False
        self.page.update()

    # Making the container for the images so they can be uploaded
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
        if len(self.images) <= 4:
            self.file_picker.pick_files()

    def process_image_upload(self, e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            file_name = os.path.basename(file_path)

             # Create a preview of the image
            local_image_preview = ft.Image(
                 src=file_path,
                 fit=ft.ImageFit.COVER,
                 width=200,
                 height=200,
             )

        # Display the preview in the UI
            self.images.append(local_image_preview)
            self.image_container.controls.append(local_image_preview)
            self.image_container.update()

            # Save file path for later upload during post submission
            # Send the file to the Flask upload API
            url = "http://127.0.0.1:5000/upload"

            with open(file_path, 'rb') as file:
                files = {'file': (file_name, file)}
                response = requests.post(url, files=files)

            if response.status_code == 200:
                # Get the URL of the uploaded image
                file_url = response.json().get('url')
                print(f"Image uploaded successfully. URL: {file_url}")

                # Display the uploaded image in the Flet UI
               # uploaded_image = ft.Image(src=file_url, fit=ft.ImageFit.COVER, width=200, height=200,)
                #self.images.append(uploaded_image)
                #self.image_container.controls.append(uploaded_image)
                #self.image_container.update()
            else:
                # Handle any errors
                self.error_field.value = f"Error uploading image: {response.text}"
                self.error_field.color = "red"
                self.error_field.update()
    # Checks if expiration date is valid and if it is after today's date
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
         # Extract validated data
        title = self.title_field.value.strip()
        description = self.description_field.value.strip()
        quantity = int(self.quantity_field.value.strip())
        points = int(self.points_field.value.strip())
        zipcode = self.zip_field.value.strip()
        expiration_date = self.expiration_date_field.value.strip()
        category_name = self.category_dropdown.value.strip()
        image_url = [image.src for image in self.images]  # Convert images to URLs or paths

        print("Post Data:")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Quantity: {quantity}")
        print(f"Points: {points}")
        print(f"Zipcode: {zipcode}")
        print(f"Expiration Date: {expiration_date}")
        print(f"Category: {category_name}")
        print(f"Image URLs: {image_url}")

        try:
            poster_id = self.page.session.get("user_id")
            print(poster_id)
            post_id = create_post(
            poster_id, title, description, quantity, points,
                zipcode, expiration_date, category_name, image_url
        )

        # Success message
            self.error_field.value = f"Post saved successfully! Post ID: {post_id}"
            self.error_field.size = 12
            self.error_field.color = "green"
            self.error_field.update()

        # Clear fields after saving
            self.clear_fields()

        except Exception as ex:
        # Handle any errors
            self.error_field.value = f"Error saving post: {str(ex)}"
            self.error_field.size = 12
            self.error_field.color = "red"
            self.error_field.update()

        print("Post saved successfully!" + make_ID())
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
