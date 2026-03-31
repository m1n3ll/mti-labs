class UserModel:
    def __init__(self):
        self._name = ""  #private attribute

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name



class UserView:
    @staticmethod
    def get_user_name():
        return input("Enter your name: ")

    @staticmethod
    def display_greeting(message):
        print(message)


class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def greet_user(self):
        name = self.view.get_user_name()
        self.model.set_name(name)

        message = f"Hello, {self.model.get_name()}! "

        self.view.display_greeting(message)


if __name__ == "__main__":
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)

    controller.greet_user()
