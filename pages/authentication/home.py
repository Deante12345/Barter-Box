import flet as ft

class Home(ft.Container):
    def init(self, page: ft.Page):
        super().init()

        self.content = ft.Column(
            controls=[
                ft.Text("Hello Home page", color="white"),
                ft.ElevatedButton(text="Sign Out", on_click= lambda e: page.go("/login")),
                ft.ElevatedButton(text="Make Post", on_click=lambda e: page.go("/makepost"))
                
            ]
        )