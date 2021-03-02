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

## folders to create 
- Create files folder in ./server/app 

## for postgresql DB installation
1 - Get homebrew
2 - brew update then brew  doctor 
3 - brew install postgresql 

4 - start server using pg_ctl -D /usr/local/var/postgres start
5 - psql postgres

# to create DB 
- CREATE DATABASE gpd_dev;
- Dump .pgsql into DB spawar2$ psql gpd_dev < /Users/spawar2/Desktop/GitHub-Plagiarism-Detector/server/db.pgsql

## Useful commands
to use DB 
\c gpd_dev 

To list all DBS
\list

To list all Tables use 
\dt


## For server 
pip3 install -r requirements.txt