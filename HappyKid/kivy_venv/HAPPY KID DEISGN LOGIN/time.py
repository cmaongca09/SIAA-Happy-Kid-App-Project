from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder

# Load the Kivy file
Builder.load_file('time.kv')

class ScrollableBox(BoxLayout):
    # Define the scroll speed
    scroll_speed = NumericProperty(5)

    def scroll_up(self):
        self.ids.box.y += self.scroll_speed

    def scroll_down(self):
        self.ids.box.y -= self.scroll_speed


class ScrollableApp(App):
    def build(self):
        return ScrollableBox()


if __name__ == '__main__':
    ScrollableApp().run()
