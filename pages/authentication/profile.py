import flet as ft

class Profile(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Navigation Bar
        self.navigation_bar = ft.Row(
            controls=[
                ft.TextButton("Home", on_click=lambda e: page.go("/home"), icon=ft.icons.HOME),
                ft.TextButton("Trade", on_click=lambda e: page.go("/trade"), icon=ft.icons.SWAP_HORIZ_ROUNDED),
                ft.TextButton("Profile", on_click=lambda e: page.go("/profile"), icon=ft.icons.PERSON),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )

        # Profile Content
        self.content = ft.Column(
            alignment=ft.alignment.Alignment(0, 0),
            controls=[
                
                self.navigation_bar,
                ft.Container(
                    alignment=ft.alignment.Alignment(0, 0),
                    padding=ft.padding.only(bottom=10),
                    content=ft.Column(
                        controls=[
                            
                            ft.CircleAvatar(
                                
                                width=150,
                                height=150,
                                foreground_image_url="https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/4426348.png",
                            ),
                            
                            ft.Text("Jaden Daniels", size=20, weight="bold", text_align="center",),
                            ft.Text("Baton Rouge, Louisiana", size=16, color="blue", text_align="center",),
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
                           
                        ]
                           
                        
                    ),
                
                    
                ),
                
                 
            ]
     
        )
