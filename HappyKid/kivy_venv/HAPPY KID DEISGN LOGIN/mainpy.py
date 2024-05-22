from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Container for login elements
        login_container = GridLayout(cols=1, spacing=10, size_hint_y=None)
        login_container.bind(minimum_height=login_container.setter('height'))  # Allow the layout to expand vertically

        # Adding Happy Kid label
        happy_kid_label = Label(text="HAPPY KID", size_hint_y=None, height=100)
        login_container.add_widget(happy_kid_label)

        # Username input field
        self.username_input = TextInput(hint_text='Username', size_hint_y=None, height=40)
        login_container.add_widget(self.username_input)

        # Password input field
        self.password_input = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40)
        login_container.add_widget(self.password_input)

        # Button to proceed
        self.proceed_button = Button(text='Log In', on_press=self.proceed, size_hint_y=None, height=40)
        login_container.add_widget(self.proceed_button)

        # Button to create account
        self.create_account_button = Button(text='Create Account', on_press=self.create_account, size_hint_y=None,
                                            height=40)
        login_container.add_widget(self.create_account_button)

        self.layout.add_widget(login_container)
        self.add_widget(self.layout)

    def proceed(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Here you can add your logic to handle the username and password, such as authentication, etc.
        print(f'Username: {username}, Password: {password}')

    def create_account(self, instance):
        self.manager.current = 'create_account'


class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.create_account_label = Label(text='Create Account Page')
        self.layout.add_widget(self.create_account_label)

        # Add more widgets for creating an account as needed

        self.back_button = Button(text='Back to Login', on_press=self.back_to_login)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def back_to_login(self, instance):
        self.manager.current = 'login'


class TestApp(App):
    def build(self):
        # Create a screen manager
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        return self.sm


if __name__ == '__main__':
    TestApp().run()
