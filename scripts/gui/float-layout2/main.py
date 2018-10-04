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
	  text='(10%,10%)',size=(100,100),size_hint=(None,None),
	  pos_hint={'x':0.1,'y':0.1}
	)
        btn2=Button(
          text='(40%,40%)',size=(100,100),size_hint=(None,None),
	  pos_hint={'x':0.4,'y':0.4}
	)
        btn3=Button(
	  text='(70%,70%)',size=(100,100),size_hint=(None,None),
	  pos_hint={'x':0.7,'y':0.7}
	)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

myApp().run()
