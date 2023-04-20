from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.toast import toast
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
 
KV = '''
MDScreen:

    MDTopAppBar:
        title: 'Test Toast'
        pos_hint: {'top': 1}
        left_action_items: [['menu', lambda x: x]]

    MDRaisedButton:
        text: 'TEST KIVY TOAST'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_toast()
'''

class Apply(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.name = TextInput(text='Name')
        self.gender = TextInput(text='Gender')
        self.age = TextInput(text='Age')
        self.email = TextInput(text='Email')
        self.address = TextInput(text='Address')
        self.filechooser = FileChooserIconView()
        self.submit_button = Button(text='Submit', on_press=self.submit)
        self.add_widget(self.name)
        self.add_widget(self.gender)
        self.add_widget(self.age)
        self.add_widget(self.email)
        



class Test(MDApp):
    def show_toast(self):
        '''Display a toast on the screen'''
        toast('Test kivy toast')
    def build(self):
        return Builder.load_string(KV)
Test().run()