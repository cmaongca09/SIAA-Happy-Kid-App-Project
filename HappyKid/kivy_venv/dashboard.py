from kivy.app import App
from kivy.uix.label import Label 


class HappykidApp(App):
    def build(self):
        return Label(text = 'hello world')
    

if __name__=='__main__':
    HappykidApp().run()