from app import my_db as db
from flask_login import UserMixin

class User(UserMixin, db.Document):
    meta = {"collection":"appUsers"}
    email = db.StringField()
    password = db.StringField()
    name = db.StringField()

    @staticmethod
    def getUser(email):
        return User.objects(email=email).first()
    
    @staticmethod
    def getUserById(user_id):
        return User.objects(pk=user_id).first()
    
    @staticmethod
    def createUser(email, name, password):
        # check if the user exist?
        user = User.getUser(email)
        if not user:
            user = User(
                email=email,
                name=name,
                password=password
            )
            user.save()
        return user
    
# @login_manager.user_loader
# def load_user(user_id):
#     return User.getUserById(user_id)