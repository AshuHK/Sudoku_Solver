# # import pygame
# # TODO: need to find a better GUI to work with 
# import sys
# # import solver 

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()
