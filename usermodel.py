from kivy.properties import StringProperty

class UserModel:
    uid = StringProperty(None)
    email = StringProperty(None)
    password = StringProperty(None)
    name = StringProperty(None)
    goal = StringProperty(None)
    photo_url = StringProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    @classmethod
    def from_map(cls, map):
        return cls(
            uid=map['uid'],
            email=map['email'],
            goal=map['goal'],
            name=map['name'],
            password=map['password'],
        )
        
    def to_map(self):
        return {
            'uid': self.uid,
            'email': self.email,
            'fullname': self.name,
        }
