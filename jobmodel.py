from kivy.properties import StringProperty, NumericProperty

class Job:
    id = StringProperty(None, allownone=True)
    job_name = StringProperty(None, allownone=True)
    image_url = StringProperty(None, allownone=True)
    created_at = NumericProperty(None, allownone=True)
    updated_at = NumericProperty(None, allownone=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def from_json(self, json):
        self.id = json['id']
        self.job_name = json['name']
        self.image_url = json['imageUrl']
        self.created_at = json['createdAt']
        self.updated_at = json['updatedAt']
        
    def to_json(self):
        data = {
            'id': self.id,
            'name': self.job_name,
            'imageUrl': self.image_url,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
        return data

