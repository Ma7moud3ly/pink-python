from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width','400')
Config.set('graphics', 'height','400')

class myApp(App):
    def build(self):
        layout=FloatLayout()
        btn1=Button(
	  text='(0,0)',size=(100,100),size_hint=(None,None),
	  pos=(0,0)
	)
        btn2=Button(
	  text='(150,150)',size=(100,100),size_hint=(None,None),
	  pos=(150,150)
	)
        btn3=Button(
	  text='(300,300)',size=(100,100),size_hint=(None,None),
	  pos=(300,300)
	)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

myApp().run()
