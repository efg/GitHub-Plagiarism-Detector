steps for configuring databse
cd to server 
    start python3 
    then 
    from app import db 
    from app.models import users
    # db.create_all()
    # user_admin = users.User("admin", "admin@gmail.com", "admin", True)
    # db.session.add(user_admin)
    # db.session.commit()



1) create .flaskenv
    FLASK_APP = main.py 
    FLASK_ENV = development
2) create .env
