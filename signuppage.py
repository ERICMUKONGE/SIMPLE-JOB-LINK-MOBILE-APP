from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class SignUpForm(BoxLayout):
     def update_user_data(self, snapshot):
        if snapshot.exists:
            self.find_widget(text="Hello").text = snapshot.data()["name"]
    
        def update_notifications(self, snapshot):
            pass  # TODO: implement this method
    
        def create_new_job(self, instance):
        #self.add_widget(CreateJobPage())
    
            def open_account_page(self, instance):
        #self.add_widget(AccountPage())
    
# Define the CategoryAdapter for the categories list



                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Add logo image
        self.add_widget(Image(source='logo.png', size_hint=(1, 0.2)))

        # Create form fields
        self.name_input = TextInput(hint_text='FullName', multiline=False)
        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        self.confirm_password_input = TextInput(hint_text='Confirm Password', password=True, multiline=False)
        self.telno_input = TextInput(hint_text='Phone Number', multiline=False)
        self.bloodtype_input = TextInput(hint_text='Blood Type', multiline=False)
        self.location_input = TextInput(hint_text='Location', multiline=False)

        # Add form fields to layout
        self.add_widget(self.name_input)
        self.add_widget(self.email_input)
        self.add_widget(self.password_input)
        self.add_widget(self.confirm_password_input)
        self.add_widget(self.telno_input)
        self.add_widget(self.bloodtype_input)
        self.add_widget(self.location_input)

        # Add sign up button
        self.signup_button = Button(text='Sign Up')
        self.signup_button.bind(on_release=self.validate_form)
        self.add_widget(self.signup_button)

        def validate_form(self, instance):
        # Validate form fields
            if not self.name_input.text:
                self.show_error_popup('Please enter a name')
            elif not self.email_input.text:
                self.show_error_popup('Please enter an email')
            elif not self.password_input.text:
                self.show_error_popup('Please enter a password')
            elif not self.confirm_password_input.text:
                self.show_error_popup('Please confirm your password')
            elif self.password_input.text != self.confirm_password_input.text: