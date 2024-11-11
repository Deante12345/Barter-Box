import flet as ft
from router import views_handler
from pages.authentication.login import Login
from pages.authentication.signup import SignUp
#from pages.authentication.usermakepost import UserMakePost

def main (page: ft.Page):
    page.bgcolor = "white"
    page.padding=ft.padding.all(0)
    def route_change (route) :
        page.clean()
        
        if page.route == "/login":
            page.add(Login(page))
            
        if page.route == "/signup":
            page.add(SignUp(page)) 

        #if page.route == "/makepost":
           #page.add(UserMakePost(page))   
        
        page.fonts == {
            "abeezee": "fonts/AbeeZee-Regular"
        }
        
        page.on_route_change = route_change
        
        page.views.clear()
        page.views.append(views_handler(page)[page.route])
        page.update()
    page.on_route_change = route_change

    page.go("/login")

ft.app(target=main,assets_dir="assets")