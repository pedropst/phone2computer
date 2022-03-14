from turtle import bgcolor, color, onclick
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import randint

kivy.require('1.9.0')

class Phone2Computer(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1 
        
        self.datas = []
        for _ in range(10):
            self.datas.append(Label(text=str(randint(0,1000)), color= "blue"))
        
        self.window.rows = len(self.datas) + 1

        for data in self.datas:
            self.window.add_widget(data)

        self.refresh_button = Button(text='Refresh')
        self.refresh_button.bind(on_pressed=self.callback)
        self.window.add_widget(self.refresh_button)
        
        return self.window
    
    def callback(self, instance):
        self.datas = []
        for _ in range(10):
            self.datas.append(Label(text=str(randint(0,1000)), color= "blue"))

        print(self.datas)

if __name__ == "__main__":
    Phone2Computer().run()
