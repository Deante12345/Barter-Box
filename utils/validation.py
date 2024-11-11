import re
class Validation:
    def __init__(self) -> None:
        pass

    def is_valid_email(self, email):
        # Correct the pattern to avoid the 'a-Z' range error
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return re.match(pattern, email) is not None

    def is_valid_password (self, password):
        if len(password) < 8:
            return False
        
        if not any(c.isdigit() for c in password):
            return False

        if not re.search("I©_!#$%^&*()>?\|~:]", password) :
            return False

        return True