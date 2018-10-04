import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    p=.25
    layout = BoxLayout(padding=10)
    def btn(self,text,pos):
        #b=Button(text=text,pos_hint={'y':0,'x':.25*pos},size_hint=(0.25,.25))
        b=Button(text=text)
        self.layout.add_widget(b)

    def row(self,a,b,c,d,e,f,y):
        row=BoxLayout(padding=0,pos_hint={'x':0,'y':.2*y},size_hint=(1,0.2))
        row.add_widget(Button(text=str(a)))
        row.add_widget(Button(text=str(b)))
        row.add_widget(Button(text=str(c)))
        row.add_widget(Button(text=str(d)))
        row.add_widget(Button(text=str(e)))
        row.add_widget(Button(text=str(f)))
        return row

    def build(self):
     
        page=FloatLayout()
        page.add_widget(self.row('7','8','9','/','<','C',3))
        page.add_widget(self.row('4','5','6','*','(',')',2))
        page.add_widget(self.row('1','2','3','-','^','~',1))
        page.add_widget(self.row('0','.','%','+','-','=',0))
        page.add_widget(TextInput(text='Hello',pos_hint={'x':0,'y':.2*4},size_hint=(1,0.2)))

        return page


if __name__ == '__main__':
    MyApp().run()

