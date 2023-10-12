from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class TestLayout(BoxLayout):

    screen_text = StringProperty("Hello World")
    
    def submit(self):
        print('click')
        self.screen_text = "Changed"

class TestApp(App):
    pass

if __name__ == "__main__":
    TestApp().run()