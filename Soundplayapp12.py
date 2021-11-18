import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserListView
import pygame


pygame.mixer.init()

class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManger(ScreenManager):
    pass
class FileLayout(GridLayout):
    pass
class AddDeleteShuffle(BoxLayout):
    pass

class PlayList(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(0,10):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(1,0.3), size=(size,size))
            self.add_widget(b)

class PausePlay(BoxLayout):
    pass

class SongText(BoxLayout):
    pass

class AppLayout(BoxLayout):
    pass

class Sound12App(App):
    def build(self):
        return WindowManger()



if __name__ == "__main__":
    Sound12App().run()
