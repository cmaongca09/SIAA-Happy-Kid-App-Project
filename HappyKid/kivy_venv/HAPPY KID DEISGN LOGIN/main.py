from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("main.kv")

class LoginScreen(Screen):
    def create_account(self):
        self.manager.current = 'create_account'
        
class CreateAccountScreen(Screen):
    pass

class CreateAccountScreen(Screen):
    def consultation_form(self):
        self.manager.current = 'consultation_form'
        
class ConsultationForm(Screen):
    pass

class ConsultationForm(Screen):
    def consultation_form2(self):
        self.manager.current = 'consultation_form2'
        
class ConsultationForm2(Screen):
    pass



class TestApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.consultation_form = ConsultationForm(name='consultation_form')
        self.consultation_form2 = ConsultationForm2(name='consultation_form2')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        self.sm.add_widget(self.consultation_form)
        self.sm.add_widget(self.consultation_form2)
        return self.sm

if __name__ == '__main__':
    TestApp().run()
