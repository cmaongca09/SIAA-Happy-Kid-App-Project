from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("main.kv")

class LoginScreen(Screen):
    def create_account(self):
        self.manager.current = 'create_account'

class CreateAccountScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        return self.sm

if __name__ == '__main__':
    TestApp().run()
