from kivy.app import App
from kivy.uix.button import Button
class myApp(App):
    def build(self):
      return Button(text='Hello From Kivy',color=(1,0,0,1))
myApp().run()
