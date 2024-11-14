customBgColor = "#DDBB30"
import flet as ft
from pages.authentication.login import Login 
from pages.authentication.signup import SignUp
from pages.authentication.home import Home
from pages.authentication.profile import Profile
from utils.colors import (
    customPrimaryColor,
    customBgColor,
    customTextcolor,
    customBordercolor,
    customSideBarIconColor,
    custompashboardBG,
)

def views_handler (page):
    return {
        "/login": ft.View( route="/login",bgcolor=customBgColor, padding=ft.padding.all(0), controls=[
            Login(page)
        ]),
        "/signup": ft.View( route="/signup", bgcolor=customBgColor, padding=ft.padding.all(0), controls=[
            SignUp (page)
        ]),
        "/home": ft.View( route="/home", controls=[
            Home(page)
        ]),
         "/profile": ft.View( route="/profile", controls=[
            Profile(page)
        ]),
    }