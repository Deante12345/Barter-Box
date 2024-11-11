import flet as ft
from datetime import datetime

class UserMakePost(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.images = []
        self.image_container = self.create_image_container(page)

        self.content = ft.Column(
          controls=[
            ft.Text("List Product/s for Barter", size=80, weight=ft.FontWeight.EXTRA_BOLD),

        self.image_container,  
            ft.TextField(label="Title of product", required=True),
            ft.TextField(label="Description: why you don't want it, is it properly sealed? etc..", required=True, multiline=True),
            ft.TextField(label="Quantity", required=True, width=100),
            ft.TextField(label="Amount of points you want", required=True, width=90),
            ft.TextField(label="Zip Code", required=True, width=100, max_length=5),
            ft.Text("Expiration Date (must be after today):", size=20, weight=ft.FontWeight.REGULAR),
            ft.DatePicker(label="Select Expiration Date", on_change=self.validate_expiration_date, required=True),  

            ft.Container(
                    content=ft.Icon(ft.icons.ADD_A_PHOTO),
                    on_click=self.add_image_file,  
                    width=100,
                    height=100,
                    bgcolor="#E0E0E2"
                ),
                
            ft.ElevatedButton(
                   text="POST",
                   on_click=self.save_post_to_database,
                   style=ft.ButtonStyle(text_color=ft.colors.WHITE, bgcolor=ft.colors.BLUE, font_weight=ft.FontWeight.EXTRA_BOLD)
                )
            ]
         )

    def validate_expiration_date(self, e):
        selected_date = e.control.value  
        if not selected_date:
             e.control.error_text = "You must select an expiration date!"
             e.control.update()
             return  
        current_date = datetime.today().date()  
        if selected_date <= current_date:
             e.control.error_text = "Expiration date must be after today!"
             e.control.update()
        else:
             e.control.error_text = ""  
             e.control.update()

    def create_image_container(self, page: ft.Page):  
        self.page = page  
        return ft.Row(
            controls=[
            ft.Container(
                content=ft.Icon(ft.icons.ADD_A_PHOTO),
                on_click=lambda _: self.add_image_file(_),  
                width=100,
                height=100,
                bgcolor="#E0E0E2",
                border_radius=ft.BorderRadius.all(8),
                )
            ],
            alignment=ft.MainAxisAlignment.START
        )

    def add_image_file(self, e):
        if len(self.images) < 4:
            dialog = ft.FilePickerDialog(on_result=lambda e: self.process_image_upload(e))
            self.page.dialog = dialog
            dialog.open()

    def process_image_upload(self, e: ft.FilePickerResultEvent):
        if e.files:
            uploaded_image = ft.Image(src=e.files[0].path, fit=ft.ImageFit.COVER)
            self.images.append(uploaded_image)
            self.image_container.controls.append(uploaded_image)
            self.image_container.update()

    

    #def save_post_to_database(self, e):
       #i think we need some sort of database for this 
        

