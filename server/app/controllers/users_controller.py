from app import db
from app.models.users import User

class UserController:
    @staticmethod
    def new(parameters):
        admin = False
        # Set admin to true if admin parameter is true    
        if parameters['admin'] == 'true':
            admin = True
        
        # Check if course email is not duplicate, save if not
        if not User.query.filter_by(email=parameters['email']).first():
            user = User(parameters['name'], parameters['email'],
                        parameters['password'], admin)
            db.session.add(user)
            db.session.commit()
        else:
            # Duplicate email id, raise value error
            raise ValueError("User with email '{}' already exists".format(parameters['email']))


    @staticmethod
    def login(parameters):

        user = User.query.filter_by(email=parameters['email']).first()
        if not user:
            raise ValueError("User with email '{}' doesn't exists".format(parameters['email']))
        elif not  user.password == parameters['password']:
            raise ValueError("Please check your password")
        else:
            return [user.id, user.admin]
        
        