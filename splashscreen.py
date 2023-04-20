from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
users_ref = db.collection('users')

# Splash screen
class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='JOB LINK', font_size='32sp'))
        Clock.schedule_once(self.go_to_add_user_screen, 5)

    def go_to_add_user_screen(self, dt):
        self.manager.current = 'add_user'

# Add user screen
class AddUserScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.full_name_input = TextInput(hint_text='Full Name')
        self.company_input = TextInput(hint_text='Company')
        self.age_input = TextInput(hint_text='Age')
        self.add_button = Button(text='Add User', on_release=self.add_user)
        self.layout.add_widget(self.full_name_input)
        self.layout.add_widget(self.company_input)
        self.layout.add_widget(self.age_input)
        self.layout.add_widget(self.add_button)
        self.add_widget(self.layout)

    def add_user(self, instance):
        users_ref.add({
            'full_name': self.full_name_input.text,
            'company': self.company_input.text,
            'age': self.age_input.text
        })

# Create the screen manager
sm = ScreenManager()
sm.add_widget(SplashScreen(name='splash'))
sm.add_widget(AddUserScreen(name='add_user'))

class FirebaseApp(App):
    def build(self):
        return sm

FirebaseApp().run()
