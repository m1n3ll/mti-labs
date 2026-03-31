class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def save_to_database(self, user):
        # Database logic
        pass
    def send_welcome_email(self, user):
        # Email logic
        pass
    def generate_report(self):
        # Reporting logic
        pass 

 # SRP = Single Responsability Principle 
 # UserManager handles : - user storage , - database , - email , - reporting
 # each one of these should be in its own class


class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, user):
        self.users.append(user)

class UserDatabase:
        def save_to_database(self, user):
        # Database logic
            pass 

class UserEmails:
    def send_welcome_email(self, user):
        # Email logic
        pass

class UserReport:
     def generate_report(self):
        # Reporting logic
        pass 