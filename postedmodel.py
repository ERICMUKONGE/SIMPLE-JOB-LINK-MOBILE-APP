from kivy.properties import StringProperty, ObjectProperty

class PostModel:
    id = StringProperty(None, allownone=True)
    post_id = StringProperty(None, allownone=True)
    owner_id = StringProperty(None, allownone=True)
    location = StringProperty(None, allownone=True)
    description = StringProperty(None, allownone=True)
    media_url = StringProperty(None, allownone=True)
    username = StringProperty(None, allownone=True)
    timestamp = ObjectProperty(None, allownone=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def from_json(self, json):
        self.id = json['id']
        self.post_id = json['postId']
        self.owner_id = json['ownerId']
        self.location = json['location']
        self.username = json['username']
        self.description = json['description']
        self.media_url = json['mediaUrl']
        self.timestamp = json['timestamp']
        
    def to_json(self):
        data = {
            'id': self.id,
            'postId': self.post_id,
            'ownerId': self.owner_id,
            'location': self.location,
            'description': self.description,
            'mediaUrl': self.media_url,
            'timestamp': self.timestamp,
            'username': self.username
        }
        return data
