from kivy.app import App
# from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation
from front_menu import *
import time

Window.clearcolor = .255, .101, .255, .1

class My_Splash_Screen_App(App):

    def build(self):

        '''Splash Screen'''
        my_splash_screen = Image(source='images/icone.png')#,pos=(15,1500))
        animation = Animation(x=0, y=0, d=2, t='out_bounce')
        animation.start(my_splash_screen)

        return my_splash_screen
    
    def on_start(self):
        time.sleep(5)
        self.on_stop()
        return super().on_start()
    
    def on_stop(self):
        Menu().run()
        return super().on_stop()

My_Splash_Screen_App().run()



