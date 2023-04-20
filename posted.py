from kivy.properties import StringProperty, ListProperty, NumericProperty

class Posted:
    job_name = StringProperty(None)
    company = StringProperty(None)
    category = StringProperty(None)
    email = StringProperty(None)
    contacts = StringProperty(None)
    location = StringProperty(None)
    about = ListProperty(None)
    qualifications = ListProperty(None)
    responsibilities = ListProperty(None)
    created_at = NumericProperty(None)
    updated_at = NumericProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    @classmethod
    def from_map(cls, map):
        return cls(
            job_name=map['jobName'],
            company=map['company'],
            responsibilities=map['Reponsibilities'],
            qualifications=map['Qualifications'],
            location='location',
            email=map['email'],
            contacts=map['contacts'],
            about=map['about'],
            created_at=map['createdAt'],
            updated_at=map['updatedAt'],
            category=map['category'],
        )
        
    def to_map(self):
        return {
            'email': self.email,
            'jobName': self.job_name,
            'company': self.company,
            'Reponsibilities': self.responsibilities,
            'Qualifications': self.qualifications,
            'location': self.location,
            'email': self.email,
            'contacts': self.contacts,
            'about': self.about,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'category': self.category,
        }
