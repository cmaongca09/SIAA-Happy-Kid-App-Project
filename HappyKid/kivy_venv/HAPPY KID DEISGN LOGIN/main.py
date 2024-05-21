from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (410, 680)

class LoginScreen(Screen):
    def create_account(self):
        self.manager.current = 'create_account'

class CreateAccountScreen(Screen):
    pass

class CreateAccountScreen2(Screen):
    pass

class DashboardTab(Screen):
    pass

class AboutCenterTab(Screen):
    pass

class TestApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.create_account_screen2 = CreateAccountScreen2(name='create_account2')
        self.dashboard_tab = DashboardTab(name='dashboard_tab')
        self.about_center_tab = AboutCenterTab(name='about_center_tab')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        self.sm.add_widget(self.create_account_screen2)
        self.sm.add_widget(self.dashboard_tab)
        self.sm.add_widget(self.about_center_tab)    
        return self.sm

if __name__ == '__main__':
    Builder.load_file("main.kv")
    TestApp().run()
