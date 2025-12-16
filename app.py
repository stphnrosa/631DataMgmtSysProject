from flask import Flask  #Flask is the framework I am using to create the web application
from database import db  #db comes from the database setup and is what allows the app to connect to PostgreSQL using SQLAlchemy

def create_app(): #create_app creates the Flask app
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://postgres:Benito0623!@localhost:5500/company_db") #5500 is the port I chose for PostgreSQL to use, "company_db" is the name of the database I created in pgAdmin 4/PostgreSQL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #

    db.init_app(app) # This connects Flask app to the DB.

    from views import views  #imports web routes (i.e. /projects) from another file
    app.register_blueprint(views) # adds the routes to the app
    
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__": #runs flask app 
    app = create_app() 
    app.run(debug=True) #debug=True is used for automatic reloads on the app


















#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

#def create_app():
 #   app = Flask(__name__)

  #  app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://postgres:Benito0623!@localhost:5500/company_db")
   # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #db.init_app(app)

    #from views import views
    #app.register_blueprint(views)
  
    #with app.app_context():
     #  db.create_all()

    #return app

#if __name__ == "__main__":
 #   app= create_app()
  #  app.run(debug=True) # added debug=true so that when you change any files inside flask application, it will automatically refresh the app