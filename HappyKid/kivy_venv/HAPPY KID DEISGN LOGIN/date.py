from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class HappyKidCenterLayout(BoxLayout):
    pass

class HappyKidCenterApp(App):
    def build(self):
        return HappyKidCenterLayout()

if __name__ == '__main__':
    Builder.load_file("date.kv")  # Load the KV file
    HappyKidCenterLayout().run()  # Run the Kivy application
