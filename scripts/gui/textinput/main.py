from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

players=['Essam El Hadary',
         'Wael Gomaa',
         'Ahmed Fathy',
         'Hossam Ghaly',
         'Emad Meteb',
         'Mohamed Zidan'
         ]

class TestApp(App):
    label=Label(color=(1,0,0,1),valign="top",size_hint=(1,0.90),font_size=70)
    def text_change(self,instance,value):
        self.label.text=""
        for player in players:
            if value in player.lower():
               self.label.text+=player+'\n'

    def build(self):
        layout=BoxLayout(orientation='vertical')
        txt=TextInput(hint_text='Search For Players',
                      multiline=False,
                      size_hint=(1,0.1),
                      color=(1,0,0,1),
                      font_size=80
                      )
        txt.bind(text=self.text_change)
        layout.add_widget(txt) 
        layout.add_widget(self.label) 
        return layout

TestApp().run()
