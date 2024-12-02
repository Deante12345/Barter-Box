import flet as ft
from router import views_handler
from pages.authentication.login import Login
from pages.authentication.signup import SignUp
from pages.authentication.usermakepost import UserMakePost
from pages.authentication.checkout import Checkout
import subprocess
import threading

def run_flask_server():
    def start_server():
        process = subprocess.Popen(
            ["python", "db/upload_images.py"],
            stdout=None,
            stderr=None,
            close_fds=True
        )
    threading.Thread(target=start_server, daemon=True).start()
    # Capture logs for debugging
#    stdout, stderr = process.communicate()
 #   print("Flask stdout:", stdout.decode())
  #  print("Flask stderr:", stderr.decode())

def main (page: ft.Page):
    run_flask_server()
    page.bgcolor = "white"
    page.padding=ft.padding.all(0)
    def route_change (route) :
        page.clean()
        
        if page.route == "/login":
            page.add(Login(page))
            
        if page.route == "/usermakepost":
            page.add(SignUp(page))    

        if page.route == "/":
            page.add(UserMakePost(page)) 

        if page.route == "/checkout":
            page.add(Checkout(page)) 
        
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
