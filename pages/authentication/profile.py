import flet as ft
from db.queries import get_user_info  # Import the query function
from db.queries import get_user_by_username
from pages.authentication import login

class Profile(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        
       
        username = page.session.get("username")
        result = get_user_info(username)

        if result:  # Check if result is not None
            first_name = result["first_name"]  # Safely access first_name
            last_name =  result["last_name"]
            email =  result["email"]
            balance = result["points_balance"]
            
        else:
            first_name = "error"
            last_name =  "no name"
            email = "no email"
            balance = 0

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
                                foreground_image_url="https://static.vecteezy.com/system/resources/thumbnails/020/765/399/small_2x/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg",
                            ),
                            ft.Text(
                                 f"{first_name} {last_name}",  # Personalized greeting
                                size=20, 
                                weight="bold", 
                                text_align="center",
                            ),
                            ft.Text(
                                 f"{email}",  # Personalized greeting
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
                                f"Hello, my name is {first_name}, and I am happy to make any trades for groceries.\n"
                                "I am a part-time chef, so I often have extra ingredients.",
                                size=14,
                                text_align="center",
                            ),
                            ft.Text(
                                f"Total Points: {balance} ",
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
