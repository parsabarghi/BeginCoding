from config import db
from sqlalchemy import Column, Integer, String

class PLCLIST(db.Model):
    id = Column(Integer, primary_key=True)
    ip = Column(String(120), unique=False, nullable=False)
    name = Column(String(120), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "ip": self.ip,
            "name": self.name
        }
