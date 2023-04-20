from kivy.properties import StringProperty, ObjectProperty

class CommentModel:
    username = StringProperty(None, allownone=True)
    comment = StringProperty(None, allownone=True)
    timestamp = ObjectProperty(None, allownone=True)
    userDp = StringProperty(None, allownone=True)
    userId = StringProperty(None, allownone=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def from_json(self, json):
        self.username = json['username']
        self.comment = json['comment']
        self.timestamp = json['timestamp']
        self.userDp = json['userDp']
        self.userId = json['userId']
        
    def to_json(self):
        data = {
            'username': self.username,
            'comment': self.comment,
            'timestamp': self.timestamp,
            'userDp': self.userDp,
            'userId': self.userId
        }
        return data
