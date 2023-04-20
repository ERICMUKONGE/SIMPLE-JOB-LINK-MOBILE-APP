from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

class Comments(BoxLayout):
    def __init__(self, post=None, **kwargs):
        super().__init__(**kwargs)
        self.post = post
        self.orientation = 'vertical'

        self.full_post = BoxLayout(orientation='vertical', size_hint_y=None)
        self.full_post.bind(minimum_height=self.full_post.setter('height'))
        self.add_widget(self.full_post)

        self.comments = BoxLayout(orientation='vertical', size_hint_y=None)
        self.comments.bind(minimum_height=self.comments.setter('height'))
        self.add_widget(ScrollView(size_hint_y=None, do_scroll_x=False, do_scroll_y=True, bar_width='12dp', bar_color=[0,0,0,0.5], bar_inactive_color=[0,0,0,0.2], scroll_type=['bars', 'content'], effect_cls='ScrollEffect', scroll_distance=10, scroll_timeout=200))

        self.comments_input = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp')
        self.add_widget(self.comments_input)

        self.comments_tec = TextInput(multiline=False, hint_text='Add a comment...')
        self.comments_input.add_widget(self.comments_tec)

        self.submit_button = Button(text='Submit')
        self.comments_input.add_widget(self.submit_button)

    def build_full_post(self):
        self.full_post.clear_widgets()
        if self.post:
            post_image = Image(source=self.post.image)
            self.full_post.add_widget(post_image)
            post_caption = Label(text=self.post.caption)
            self.full_post.add_widget(post_caption)
            post_user = Label(text=self.post.user)
            self.full_post.add_widget(post_user)

    def build_comments(self):
        self.comments.clear_widgets()
        # Add code here to retrieve the comments and display them in the `self.comments` widget.

class CommentsApp(App):
    def build(self):
        return Comments()

if __name__ == '__main__':
    CommentsApp().run()
