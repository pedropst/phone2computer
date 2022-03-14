from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import kivy

kivy.require('1.9.0')

class PhoneClient(App):
    def build(self):
        self.window = GridLayout()
        Window.size = (50, 50)
        return self.window

if __name__ == "__main__":
    PhoneClient().run()

lista = []
lista.reverse()