import flet as ft

class Checkout(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton("Home", on_click=lambda e: page.go("/home"), icon=ft.icons.HOME),
                ft.TextButton("Trade", on_click=lambda e: page.go("/usermakepost"), icon=ft.icons.SWAP_HORIZ_ROUNDED),
                ft.TextButton("Profile", on_click=lambda e: page.go("/profile"), icon=ft.icons.PERSON),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # Profile Content
        self.content = ft.Column(
            controls=[
                self.navigation_bar,
                ft.Container(
                    content=ft.Column(
                        controls=[
                            
                            ft.Text(
                                "My Bag(0)", 
                                size=20, 
                                weight="bold", 
                                text_align="center",
                            ),

                            ft.Text(
                                "Total Points: ",
                                size=14,
                                text_align="center",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    alignment=ft.alignment.center,
                    padding=20,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        # Wrap everything in a container to center the full layout
        page.add(
            ft.Container(
                content=self.content,
                alignment=ft.alignment.center,
                expand=True,  # Make it take the full page size
            )
        )
