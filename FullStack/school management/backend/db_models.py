from main_config import db
from sqlalchemy import Column, INTEGER, String

class Students(db.Model):
    id = Column(INTEGER, primary_key=True)
    age = Column(INTEGER, nullable=False, unique=False)
    full_name = Column(String(40), nullable=False, unique=False)
    class_type = Column(String(20), nullable=False, unique=False)
    
    def __repr__(self):
        return f"Full Name: {self.full_name}, Age: {self.age}, Class Type: {self.class_type}"
    
    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'age': self.age,
            'class_type': self.class_type
        }
