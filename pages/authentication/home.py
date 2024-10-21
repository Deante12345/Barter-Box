import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.content = ft.Column(
            controls=[
                ft.Text("Hello Home page", color="white"),
                ft.ElevatedButton(text="Sign Out", on_click= lambda e: page.go("/login"))
            ]
        )