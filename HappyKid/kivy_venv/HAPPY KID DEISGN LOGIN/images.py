from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


class LoginScreen(Screen):
    layout = ObjectProperty(None)

    def proceed(self, instance):
        username = self.layout.ids.username_input.text
        password = self.layout.ids.password_input.text
        # Here you can add your logic to handle the username and password, such as authentication, etc.
        print(f'Username: {username}, Password: {password}')

    def create_account(self, instance):
        self.manager.current = 'create_account'


class CreateAccountScreen(Screen):
    def back_to_login(self, instance):
        self.manager.current = 'login'
