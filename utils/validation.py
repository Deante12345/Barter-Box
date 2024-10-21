import re
class Validation:
    def __init__(self) -> None:
        pass

    def is_valid_email (self, email):
        pattern = "^[a-ZA-ZO-9_+-]+@[a-zA-Z0-9-1+\. [a-ZA-Z0-9-. ]+$"
        return re.match(pattern, email) is not None

    def is_valid_password (self, password):
        if len(password) < 8:
            return False
        
        if not any(c.isdigit() for c in password):
            return False

        if not re.search("I©_!#$%^&*()>?\|~:]", password) :
            return False

        return True