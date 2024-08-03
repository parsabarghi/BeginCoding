from api import *

with app.app_context():
    db.create_all()