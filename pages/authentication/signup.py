import flet as ft

class SignUp(ft. Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
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
                            ft.TextField(label="First Name", width=300),
                            ft.TextField(label="Last Name", password=True, width=300),
                            ft.TextField(label="Email", password=True, width=300),
                            ft.TextField(label="Username", width=300),
                            ft.TextField(label="Password", password=True, width=300),
                            ft.ElevatedButton(text="Sign Up", on_click=lambda e: page.go("/login")),
                        ]
                    ),
                ),
            ]
        )