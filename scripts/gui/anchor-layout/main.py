from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
class myApp(App):
    def build(self):
        layout=AnchorLayout(anchor_x='center',anchor_y='center')
        btn=Button(text='Button 1',
                   color=(1,0,0,1),size=(200,50),size_hint=(None,None))
        layout.add_widget(btn)
        return layout
myApp().run()
