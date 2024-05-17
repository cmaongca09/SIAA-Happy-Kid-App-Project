from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (420,630)

Builder.load_file("main.kv")

class LoginScreen(Screen):
    def create_account(self):
        self.manager.current = 'create_account'

class CreateAccountScreen(Screen):
    pass

class CreateAccountScreen2(Screen):
    pass


class BookAppointment(Screen):
    pass

class TestApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.create_account_screen2 = CreateAccountScreen2(name='create_account2')
        self.book_appointment_screen = BookAppointment(name='book_appointment')  # Corrected typo here
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        self.sm.add_widget(self.create_account_screen2)
        self.sm.add_widget(self.book_appointment_screen)
        return self.sm

if __name__ == '__main__':
    TestApp().run()
