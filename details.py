from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Create a class for the job posting page
class DetailPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Retrieve arguments passed in the constructor
        self.job_name = kwargs.get('job_name')
        self.about = kwargs.get('about')
        self.location = kwargs.get('location')
        self.company = kwargs.get('company')
        self.qualifications = kwargs.get('qualifications')
        self.responsibilities = kwargs.get('responsibilities')

        # Create a variable to track whether the apply button has been clicked
        self.is_clicked = False

        # Create a vertical layout to hold the widgets
        self.orientation = "vertical"

        # Add a success message label (hidden by default)
        self.success_label = Label(text="Success!", size_hint_y=None, height=30, color=[0, 1, 0, 1])
        self.add_widget(self.success_label)
        self.success_label.opacity = 0

        # Add the job name label
        self.add_widget(Label(text=self.job_name, size_hint_y=None, height=40, font_size=20, bold=True))

        # Add the company and location label
        self.add_widget(Label(text=f"{self.company}, Inc • {self.location}", size_hint_y=None, height=20, font_size=14))

        # Add a spacer
        self.add_widget(Label(size_hint_y=None, height=30))

        # Add the 'About the job' label and the job description
        self.add_widget(Label(text="About the job", size_hint_y=None, height=20, font_size=14, bold=True))
        self.add_widget(Label(text=self.about, size_hint_y=None, height=20))

        # Add a spacer
        self.add_widget(Label(size_hint_y=None, height=30))

        # Add the 'Qualifications' label and the qualifications list
        self.add_widget(Label(text="Qualifications", size_hint_y=None, height=20, font_size=14, bold=True))
        self.add_widget(Label(text=self.qualifications, size_hint_y=None, height=20))

        # Add a spacer
        self.add_widget(Label(size_hint_y=None, height=30))

        # Add the 'Responsibilities' label and the responsibilities list
        self.add_widget(Label(text="Responsibilities", size_hint_y=None, height=20, font_size=14, bold=True))
        
