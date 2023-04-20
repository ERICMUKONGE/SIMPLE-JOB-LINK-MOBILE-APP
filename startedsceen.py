from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

# Started screen
class StartedScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.bg_image = Image(source='assets/images/bg_signin.png')
        self.label1 = Label(
            text='Build Your Next \nFuture Career Like\na Master',
            font_size='32sp',
            size_hint=(1, .3),
            pos_hint={'x': 0, 'top': 1},
            color=[1, 1, 1, 1])
        self.label2 = Label(
            text='Jobs all over the country',
            font_size='14sp',
            size_hint=(1, .2),
            pos_hint={'x': 0, 'top': .8},
            color=[1, 1, 1, 1])
        self.button1 = Button(
            text='Get Started',
            font_size='15sp',
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .15},
            background_color=[1, 1, 1, 1])
        self.button2 = Button(
            text='Sign In',
            font_size='15sp',
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .05},
            background_color=[1, 1, 1, 1])
        self.layout.add_widget(self.bg_image)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.button2)
        self.add_widget(self.layout)

# Create the screen manager
sm = ScreenManager()
sm.add_widget(StartedScreen(name='started'))

class StartedApp(App):
    def build(self):
        return sm

StartedApp().run()
