import flet as ft
# Points, Recent trades, Location, list of current items your trading, Ratings and reviews
#edit prrofile

class Profile(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.content = ft.Column(
            controls=[
                ft.Container(
                    alignment=ft.alignment.Alignment(1, -1),
                    padding=ft.padding.only(bottom=10),
                    content=ft.Column(
                        controls=[
                            ft.CircleAvatar(
                                width=150,
                                height=150,
                                foreground_image_url="https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/4426348.png",
                            ),
                            ft.Text("Jaden Daniels", size=20, weight="bold"),
                            ft.Text("Baton Rouge, Louisiana", size=16, color="gray"),
                            ft.Text(
                                "Hello, my name is Jaden, and I am happy to make any trades for groceries.\n"
                                "I am a part-time chef, so I often have extra ingredients.",
                                size=14,
                                text_align="center",
                            ),
                            ft.TextButton("Home", on_click=lambda e: page.go("/home")),
                        ]
                    ),
                ),
            ] 
        )

