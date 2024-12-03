import flet as ft

class Confirmation(ft.Container):
    def __init__(self, page: ft.Page, item_id: str): 
        super().__init__()
        
        self.page = page
        self.item_id = item_id #ID of post

        self.status_text = ft.Text(value="Waiting for confirmation 😊", size=30, color=ft.colors.BLUE)

        self.content = ft.Column(
            controls=[
                ft.Text("Confirm Trade", size=15, weight=ft.FontWeight.BOLD),
                self.status_text,
                ft.ElevatedButton(
                    text="Confirm",
                    on_click=self.confirm_trade,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREEN,
                    ),
                ),
                ft.ElevatedButton(
                    text="Reject",
                    on_click=self.reject_trade,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.RED,
                    ),
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
        self.controls = [self.content]

    def confirm_trade(self, e):
        self.status_text.value = "Confirmed 😊"
        self.status_text.color = ft.colors.GREEN
        self.status_text.update()
        self.page.go("/home")

    def reject_trade(self, e):
        self.status_text.value = "Rejected 😞"
        self.status_text.color = ft.colors.RED
        self.page.update()

        #update the database to mark the item as confirmed
        self.update_database_status()

        self.page.go("/home")

    def update_database_status(self): #update as confirmed in databse
        # interact with database to mark the item as confirmed
        print(f"Food with ID {self.item_id} is marked as confirmed in the database!")
