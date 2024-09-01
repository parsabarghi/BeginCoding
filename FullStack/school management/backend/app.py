from flask import Flask, jsonify, request
from flask_restful import Resource
from main_config import app, db, api
from db_models import Students
from sqlalchemy.orm import sessionmaker



class Users(Resource):
    
    def get(self):
        try:
            data = Students.query.all()
            
            if data:
        
                result = [student.serialize() for student in data]
                return (result), 200
            
            return f"message No data found", 404     
        except Exception as e:
            return f"error: erorr on get method: {e} ", 500
                
    
    def post(self):
        try:
            data = request.get_json()
            
            new_student = Students(
                full_name=data['full_name'],
                age=data['age'],
                class_type=data['class_type']
            )
            
            # Create a session
            Session = sessionmaker(bind=db.engine)
            session = Session()

            # Add the student to the session
            session.add(new_student)

            # Commit the session to save the student to the database
            session.commit()

            # Close the session
            # session.close()
            
            return new_student.serialize(), 201
        
        except (Exception, ValueError) as e:
            print(f"Error on post method: {e}")
            return f"error: erorr on post method: {e} ", 500
        
class User(Resource):
    def get(self, student_id):
        try:
            
            data = Students.query.get(student_id)
            if data:
                result = [data.serialize()]
                return(result), 200
            return f"message No data found", 404
           
        except Exception as e:
            return f"error: erorr on get data using id: {e} ", 500
        
    def put(self, student_id):
        try:
            data = Students.query.get(student_id)
            if data:
                full_name = request.json['full_name']
                age = request.json['age']
                class_type = request.json['class_type']
                
                
                data.full_name = full_name
                data.age = age
                data.class_type = class_type
                
                result = [data.serialize()]
                
                db.session.commit()
                
                return (result), 200
            return f"message No data found", 404
        
        except Exception as e:
            return f"error: erorr on put data using id: {e} ", 500
        
    def delete(self, student_id):
        try:
            data = Students.query.get(student_id)
            if data:
                db.session.delete(data)
                db.session.commit()
                return f"user deleted succsesfully!", 200
            return f"message No data found", 404
        
        except Exception as e:
            return f"error: erorr on delete data using id: {e} ", 500               

api.add_resource(Users, '/students')
api.add_resource(User, '/student/<int:student_id>')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
