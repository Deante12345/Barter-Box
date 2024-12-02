## Barter Box 

### General Description
Barter Box is a community-focused trading app that allows users to exchang surplus items, such as groceries or household goods, for points that can be used to acquire other essentials. Designed for individuals, families, and small business owners, Barter Box helps reduce waste and save money by facilitating easy trades within local communities. The app’s user-friendly interface and focus on sustainability make it ideal for anyone looking to declutter, stretch their budget, and support a more environmentally conscious lifestyle.

### Technologies
• Python
• Flet
• Recommended development environment is Visual Studio
• PostgreSql

### Target Audience
Barter Box targets families, college students, restaurant owners or anyone else looking for reducing food waste and saving money on unwated food items.

### User Stories
• As a dad, I often buy a lot of snacks or food that my family doesn't eat, I want my family to stop wasting food and money that we don't have. 
• As a Costco shopper, I often find myself buying more groceries than my family can finish, therefore I want to be able to share them with my community and get something in return. 
• As a party owner I am often left with a lot of open soda and drinks after a party, I don't think a stranger will trust me to give them left over drinks so I need a way to get rid of them. 

### Development Enviroment Setup
• Recommended Prerequisites
- Python 3.8 or higher
- Recommended development environment is Visual Studio Code
- PostgreSQL (Database)

• Setup Steps
1. Install Python
   - Download and install Python from https://www.python.org/downloads/
   - Ensure you check the box to "Add Python to PATH" during installation
2. Install Visual Studio Code
   - Download and install Visual Studio Code from https://code.visualstudio.com/
3. Install Flet
   - Open a terminal in Visual Studio Code and run: pip install flet
4. Clone the Repository
   - Open a terminal or command prompt and run: 
     git clone https:https://github.com/Deante12345/Barter-Box.git
     cd Barter-Box
5. Running the application
   - To run the application, in the Visual Studio Code terminal type: flet run

### File Structure
• db:
• pages/authentication: contains the different parts of the app that users interact with
    - checkout.py: 
    - home.py: homepage where users can select to trade items, go to cart, go to profie as well as see other items up for trade
    - login.py: this page allows users to log into their account using their username and password
    - profile.py:  
    - signup.py: this page allows users to make an account using their first and last name, email, and a password 
    - usermakepost.py: this page allows users to post their unwanted food items up for trade
• main.py: initializes the page, sets up route handling, and dynamically loads the appropriate view based on the current route
• router.py: manages the navigation and routing of the app, loading different pages such as login, signup, makeuserpost, and checkout based on the current route

### Core Features
• Trading Items
    - Users can post any unwanted food
    - Users can pick a point value to get for trading the food item, which can be used for future trades
• User Account
    - Secure signup and login system to ensure a personalised experience
• Point System:
    - A built-in point based trading system that allows users to exchange food without using money
• User-Friendly Interface:
    - Simple navigation built using Flet, making it accessible to everyone

### Future Goals
• Users will get exta points by watching adds or refering friends

### Video Demo
