from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty

list_of_words = [
    {
        "eng": "run",
        "spa": "correr"
    },
    {
        "eng": "jump",
        "spa": "saltar"
    },
    {
        "eng": "speak",
        "spa": "hablar"
    }
]

class MainLayout(BoxLayout):

    question_text = StringProperty('')
    answer_text = StringProperty('')
    user_answer = ObjectProperty(None)
    disable_next = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.index = 0
        self.vocabulary = list_of_words[self.index]
        self.question = self.vocabulary["eng"]
        self.answer = self.vocabulary["spa"]
        self.user_answer = ""
        self.question_text = self.question
        self.answer_text = ''
        self.disable_next = True

    def submit(self, widget):
        if widget.text == self.answer:
            print("Correct")
            self.answer_text = self.answer
            self.disable_next = False
        else:
            print("False")
            self.answer_text = self.vocabulary["spa"]

    def next(self):
        print('Next')
        self.index += 1
        self.vocabulary = list_of_words[self.index]
        self.question = self.vocabulary["eng"]
        self.answer = self.vocabulary["spa"]
        print(self.index)
        self.question_text = self.question
        self.answer_text = ""
        self.user_answer.text = ""
        self.disable_next = True
            

class MainApp(App):
    pass

if __name__ == "__main__":
    MainApp().run()