import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class WhiteBoxLayout(BoxLayout):
    pass

class WhiteBoxApp(App):
    def build(self):
        return WhiteBoxLayout()

if __name__ == '__main__':
    WhiteBoxApp().run()
