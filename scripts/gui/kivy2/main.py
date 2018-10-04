from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width','400')
Config.set('graphics', 'height','400')
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'top', '0')
Config.set('graphics', 'left', '0')


class myApp(App):
    def build(self):
      return Button(text='Hello From Kivy',color=(1,0,0,1))
myApp().run()

