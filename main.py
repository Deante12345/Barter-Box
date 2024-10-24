import flet as ft
from router import views_handler

def main (page: ft.Page):
    
    def route_change (route) :
        page.views.clear()
        page.views.append(views_handler(page)[page.route])
        page.update()
    page.on_route_change = route_change

    page.go("/signup")

ft.app(target=main,assets_dir="assets")