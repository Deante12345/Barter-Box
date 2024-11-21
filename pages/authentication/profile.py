import flet as ft

class Profile(ft.Container):
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
                            ft.CircleAvatar(
                                width=150,
                                height=150,
                                foreground_image_url="https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/4426348.png",
                            ),
                            ft.Text(
                                "Jaden Daniels", 
                                size=20, 
                                weight="bold", 
                                text_align="center",
                            ),
                            ft.Text(
                                "Baton Rouge, Louisiana", 
                                size=16, 
                                color="blue", 
                                text_align="center",
                            ),
                            ft.Text(
                                "Hello, my name is Jaden, and I am happy to make any trades for groceries.\n"
                                "I am a part-time chef, so I often have extra ingredients.",
                                size=14,
                                text_align="center",
                            ),
                            ft.Text(
                                "Total Points: ",
                                size=14,
                                text_align="center",
                            ),
                            ft.Text(
                                "Rating: 7/10",
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
