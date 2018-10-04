from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)


src=['https://ma7moud3ly.github.io/1.jpg',
     'https://ma7moud3ly.github.io/2.jpg',
     'https://ma7moud3ly.github.io/3.jpg',
     'https://ma7moud3ly.github.io/4.jpg',
     'https://ma7moud3ly.github.io/5.jpg']
    
class TestApp(App):
    i=0   
    img=AsyncImage(size_hint=(1,0.9),source=src[i],keep_ratio=False)
    img.source=src[2]
    def alert(self,msg):
        popup = Popup(title='Hi',content=Label(text=msg),size_hint=(0.5, .2))
        popup.open()
    def press(self,btn):
        if   btn.id=='1' and self.i<(len(src)-1):
            self.i+=1
            self.img.source=src[self.i]
        elif btn.id=='2' and self.i>0:
            self.i-=1
            self.img.source=src[self.i]
        elif btn.id=='3':self.img.allow_stretch=btn.state=='down'
        elif btn.id=='4':self.img.keep_ratio=btn.state=='down'
 

    def build(self):
        layout=BoxLayout(orientation='vertical')

        btns=BoxLayout(orientation='horizontal',size_hint=(1,0.1))
        btns.add_widget(Button(text='>>>',id='1',on_press=self.press))
        btns.add_widget(Button(text='<<<',id='2',on_press=self.press))
        btns.add_widget(ToggleButton(text='Stretch',id='3',on_press=self.press))
        btns.add_widget(ToggleButton(text='Ratio',id='4',on_press=self.press))

        layout.add_widget(self.img)
        layout.add_widget(btns)  
        return layout

TestApp().run()
