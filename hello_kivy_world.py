from kivy.app import App
from kivy.uix.button import Button

class hello_kivy_worldApp(App):
    def build(self):
        return Button(text='Hello World')

hello_kivy_worldApp().run()