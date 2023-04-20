import kivy
from firestore4kivy import firestore
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock

Builder.load_string(""" 
[CustomListItem@SelectableView+BoxLayout]:
 self.add_widget(Label(text=greeting_message(), font_size=16))
  self.categories_list = ListView(adapter=CategoryAdapter())
self.posted_list = ListView(adapter=PostedAdapter())
 """)
# Define the main widget
class HomePage(BoxLayout):
  def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 30
        self.add_widget(Label(text="Hello", font_size=24, bold=True))
       
        self.add_widget(Image(source="assets/images/user_pic_signup.png", height=58, width=58))
        self.add_widget(Label(text="Hot Categories", font_size=24, bold=True))
       
        self.add_widget(self.categories_list)
        self.add_widget(Label(text="Recently Posted", font_size=24, bold=True))
        
        self.add_widget(self.posted_list)
        self.add_widget(Button(text="Create New Job", on_press=self.create_new_job))
        self.add_widget(Button(text="Account", on_press=self.open_account_page))
        
        # Set up the notification stream
        self.notification_stream = firestore.collection("create_event").snapshots(include_metadata_changes=True)
        self.notification_stream.listen(self.update_notifications)
        
        # Get the current user's data
        #self.user_ref = firestore.collection("users").document(firestore_auth.get_current_user().uid)
        self.user_ref.get().then(self.update_user_data)