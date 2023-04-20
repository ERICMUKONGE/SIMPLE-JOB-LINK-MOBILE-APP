import os
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from google.cloud import firestore
from google.oauth2.credentials import Credentials

# Set up the Firebase credentials and client
creds = Credentials.from_service_account_file(
    "path/to/service_account_file.json"
)
db = firestore.Client(project="your-project-id", credentials=creds)

# Define the AccountScreen class
class AccountScreen(Screen):
    def __init__(self, **kwargs):
        super(AccountScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.add_widget(self.layout)
        
        # Display the user's profile picture
        self.profile_pic = Image(
            source=self.user["photoURL"],
            size_hint=(1, 0.2),
            allow_stretch=True,
            keep_ratio=False
        )
        self.layout.add_widget(self.profile_pic)
        
        # Display the user's name
        self.name_label = Label(
            text=self.user["fullname"],
            font_size=24,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.name_label)
        
        # Display the user's location
        self.location_label = Label(
            text=self.user["location"],
            font_size=20,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.location_label)
        
        # Display the user's blood type
        self.blood_type_label = Label(
            text=self.user["bloodType"],
            font_size=20,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.blood_type_label)
        
        # Display the user's phone number
        self.phone_number_label = Label(
            text=self.user["pnum"],
            font_size=20,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.phone_number_label)
        
        # Add a button to allow the user to edit their profile information
        self.edit_button = Button(
            text="Edit Profile",
            on_release=self.show_edit_popup,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.edit_button)
        
    //def show_edit_popup()


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from firestore4kivy import FirebaseAuth, FirebaseFirestore
from kivy.clock import Clock

class AccountPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_id = kwargs.get("user_id")
        self.auth = FirebaseAuth()
        self.db = FirebaseFirestore()
        self.user = self.auth.current_user
        self.logged_in_user = UserModel()
        self.screen_height = 0
        self.screen_width = 0
        self.primary = [1, 238/255, 68/255, 76/255]
        self.profile_pic_link = ""
        self.name = ""
        self.pic = ""
        self.loc = ""
        self.blood = ""
        self.pnum = ""
        self.fullname = ""
        self.location = ""
        self.blood_type = ""
        self.photo_url = ""
        self.profile_pic = AsyncImage()
        self.add_widget(self.profile_pic)
        self.update_profile_button = Button(text="Update Profile")
        self.update_profile_button.bind(on_press=self.update_profile)
        self.add_widget(self.update_profile_button)
        self.upload_button = Button(text="Upload Profile Pic")
        self.upload_button.bind(on_press=self.upload_pic)
        self.add_widget(self.upload_button)
        Clock.schedule_interval(self.get_user_info, 1/60)
        self.auth.auth_state_changes().listen(self.on_auth_state_changed)

    def on_auth_state_changed(self, user):
        if user is None:
            self.parent.current = "started_page"
        else:
            print("User is signed in!")
            self.parent.current = "home_page"

    def get_user_info(self, dt):
        if self.user is not None:
            self.db.collection("users").doc(self.user.uid).get().add_done_callback(self.on_user_info_fetched)

    def on_user_info_fetched(self, task):
        if task.exception() is None:
            doc = task.get_result()
            if doc.exists:
                self.logged_in_user.from_dict(doc.to_dict())
                self.fullname = self.logged_in_user.fullname
                self.location = self.logged_in_user.location
                self.blood_type = self.logged_in_user.bloodType
                self.photo_url = self

