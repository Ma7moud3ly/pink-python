from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width','300')
Config.set('graphics', 'height','400')

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class TestApp(App):
    label1=Label(color=(1,0,0,1),text='|',size_hint=(1,0.4))
    label2=Label(color=(0,0,1,1),text='',size_hint=(1,0.6),font_size=30)
    val=''
    def number(self,instance):
        val=instance.text
        if val in '123456789+-/*':
              self.val+=val
              self.label1.text=self.val
        if val == '=':
              try:result=str(eval(self.val))
              except:result='Sytanx Error'
              self.label2.text=result
              self.label1.text=''
              self.val=''

    def _quit(self,inst):
        quit()
    def _clear(self,inst):
        self.label2.text=''
        self.label1.text=''
        self.val=''
    
    def display(self):
        row=BoxLayout()
        display=BoxLayout(orientation='vertical',size_hint=(0.6,1))
        display.add_widget(self.label1)
        display.add_widget(self.label2)
        row.add_widget(display)
        row.add_widget(Button(text='C',size_hint=(0.2,1),on_press=self._clear))
        row.add_widget(Button(text='X',size_hint=(0.2,1),on_press=self._quit))
        return row

    def row(self,a,b,c,d):
	row=BoxLayout(size_hint=(1,1))
        row.add_widget(Button(text=a,on_press=self.number))
        row.add_widget(Button(text=b,on_press=self.number))
        row.add_widget(Button(text=c,on_press=self.number))
        row.add_widget(Button(text=d,on_press=self.number))
        return row

    def build(self):
        layout=BoxLayout(orientation='vertical',size_hint=(1,1))
        layout.add_widget(self.display())        
	layout.add_widget(self.row('7','8','9','/')) 
        layout.add_widget(self.row('4','5','6','*')) 
        layout.add_widget(self.row('1','2','3','-')) 
        layout.add_widget(self.row('0','.','=','+'))
        return layout

TestApp().run()

