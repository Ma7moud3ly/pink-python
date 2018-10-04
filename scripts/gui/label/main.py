from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
    
class myApp(App):
    i=0
    label=Label()
    def press(self,instance):
         self.label.text="count : "+str(self.i)
         self.i+=1
    def build(self):
         layout=BoxLayout(orientation='vertical')
         self.label=Label(
	      text="I'm A Label",
              color=(0,1,0,1), #green
              font_size=70,
             )
         btn=Button(
	      text="Press On Me",
              color=(1,0,0,1), #red
              background_color=(0,1,0,1), #green
              font_size=70,
              on_press=self.press,
             )
         layout.add_widget(self.label)
         layout.add_widget(btn)
         return layout   
myApp().run()
