from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import time

from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width','400')
Config.set('graphics', 'height','50')

class myApp(App):
    label=Label()
    i=1
    def press(self,inst):
        self.i=self.i+1  
        self.label.text=str(self.i)
    def reset(self,inst):
        self.i=0
        self.label.text=str(self.i)
    def _quit(self,inst):
        quit()

    def build(self):
        self.label=Label(text=str(self.i),
                         color=(1,0,0,1),
                         size_hint=(0.4,1)
                        )
        self.button1=Button(text="Increment",
                           color=(0,1,0,1),
                           on_press=self.press,
                           size_hint=(0.2,1)
                          )
        self.button2=Button(text="Reset",
                           color=(0,0,1,1),
                           on_press=self.reset,
                           size_hint=(0.2,1)
                          )
        self.button3=Button(text="Exit",
                           color=(0,1,1,1),
                           on_press=self._quit,
                           size_hint=(0.2,1)
                          )
        layout=BoxLayout()
        layout.add_widget(self.button3)
        layout.add_widget(self.button2)
        layout.add_widget(self.button1)
        layout.add_widget(self.label)
        return layout

myApp().run()




"""
	layout = BoxLayout(orientation='vertical')	
	layout1 = BoxLayout(orientation='horizontal',size_hint=(1,.1))
	btn11 = Button(text='Button 11',size_hint=(0.8,1))
	btn12 = Button(text='Button 12',size_hint=(0.1,1))
	btn13 = Button(text='Button 13',size_hint=(0.1,1))
	layout1.add_widget(btn11)
	layout1.add_widget(btn12)
	layout1.add_widget(btn13)

	layout2 = BoxLayout(orientation='horizontal')
	btn21 = Button(text='Button 21')
	btn22 = Button(text='Button 22')
	btn23 = Button(text='Button 23')
	btn24 = Button(text='Button 24')
	layout2.add_widget(btn21)
	layout2.add_widget(btn22)
	layout2.add_widget(btn23)
	layout2.add_widget(btn24)

	layout.add_widget(layout1)
	layout.add_widget(layout2)
        return layout
"""

