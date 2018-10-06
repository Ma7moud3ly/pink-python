from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
class myApp(App):
    i=0
    def press(self,instance):
         instance.text=str(self.i)
         self.i+=1
    def build(self):
         layout=BoxLayout()
         btn=Button(
	      text="Press On Me",
              color=(0,0,0,1), #black
              background_color=(1,1,1,1), #white
              font_size=100,
              size_hint=(1,0.5),
              pos_hint={'y':0.25},
              on_press=self.press,
             )
         layout.add_widget(btn)
         return layout   
myApp().run()
