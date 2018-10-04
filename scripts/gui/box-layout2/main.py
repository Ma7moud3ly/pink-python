from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class myApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        layout1 = BoxLayout(orientation='horizontal',
        size_hint=(1,0.1))
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

myApp().run()
