from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class apply(Screen):
    pass
class accounts(Screen):
    pass
class details(Screen):
    pass
class homepage(Screen):
    pass
class splashscreen(Screen):
    pass
class startedscreen(Screen):
    pass
#Create the main app
class MainApp(App):
    def build(self):
        return sm

# Run the app
if __name__ == '_main_':
   MainApp().run()
