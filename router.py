customBgColor = "#DDBB30"
import flet as ft
from pages.authentication.login import Login 
from pages.authentication.signup import SignUp
from pages.authentication.home import Home
from pages.authentication.profile import Profile
from pages.authentication.usermakepost import UserMakePost
from pages.authentication.checkout import Checkout
from pages.authentication.confirmation import Confirmation 
from pages.authentication.fresh_produce_page import FreshProducePage
from pages.authentication.frozen_food import FrozenFood
from pages.authentication.dairy_products import DairyProducts
from pages.authentication.meat_poultry import MeatPoultry




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
        "/usermakepost": ft.View( route="/usermakepost", controls=[
                UserMakePost(page)
        ]),
         "/checkout": ft.View( route="/checkout", controls=[
                Checkout(page)
        ]),
        "/confirmation": ft.View(route="/confirmation", controls=[
            Confirmation(page, item_id="111111")]),
        
        "/fresh_produce_page": ft.View( route="/fresh_produce_page", controls=[
                FreshProducePage(page)
        ]),
        "/frozen_food": ft.View( route="/frozen_food", controls=[
                FrozenFood(page)
        ]),
        "/dairy_products": ft.View( route="/dairy_products", controls=[
                DairyProducts(page)
        ]),
        "/meat_poultry": ft.View( route="/meat_poultry", controls=[
                MeatPoultry(page)
        ]),

        
    }