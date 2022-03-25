from random import random
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('2.1.0')
 
class GameView(BoxLayout):
    def __init__(self):
        super(GameView,self).__init__()
        self.RandomValue = random.randint(0,1000)
    def check_number(self):
        if int(self.answer_input.text) == self.RandomValue :
            self.result_label.text = "Congrats BG!!"
            self.result_label.color ="#00EF0B"
            self.RandomValue = random.randint(0,1000)
        elif int(self.answer_input.text) > self.RandomValue :
            self.result_label.text = "Less ;) !"
            self.result_label.color ="#EF3E00"
        elif int(self.answer_input.text) > self.RandomValue :
            self.result_label.text = "More ;) !"
            self.result_label.color ="#EF3E00"

class WizeApp(App):
    def build(self):
        return GameView()

wizeApp = WizeApp()
wizeApp.run()