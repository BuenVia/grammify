
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        screen = MDScreen()
        
        self.button = MDRectangleFlatButton(
            text = "Hello World",
            pos_hint = { "center_x": 0.5, "center_y": 0.5 }
        )
        screen.add_widget(self.button)

        return screen
    
if __name__ == "__main__":
    MainApp().run()