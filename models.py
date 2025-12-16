from database import db #this file stores company information like employee, projects and departments.  SQLAlchemy handles DB tables.

class Employee(db.Model): #This table stores employee info like their employee number, name, etc. Employee # is the primary key for the table.
    __tablename__ = "employees"
    employee_no = db.Column(db.Integer, primary_key=True)
    role= db.Column(db.String(100), nullable= True)
    employee_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    starting_date = db.Column(db.DATE, nullable=False)
    department_id = db.Column(db.Integer, nullable=True)
    division_id = db.Column(db.Integer, nullable=True) 
    room_number= db.Column(db.Integer,nullable=True) 
    building_code= db.Column(db.Integer,nullable=True)
    project_number=db.Column(db.Integer, nullable=True)

class EmployeeTitle(db.Model): #Tracks employee information over time like their titles and salary
    __tablename__ = "employee_title"
    title = db.Column(db.String(100), primary_key=True)
    salary = db.Column(db.Integer, nullable=False )
    employee_no = db.Column(db.Integer, nullable=False)

class Project(db.Model): # Has informationabout the projects
    __tablename__ = "projects" #this is the title of the table in PostgreSQL
    project_number = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Integer, nullable=False)
    date_ended = db.Column(db.DATE, nullable=False)
    date_started = db.Column(db.DATE, nullable=False)
    department_id = db.Column(db.Integer, nullable=True)

class Building(db.Model):
    __tablename__ = "building"
    building_code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    cost = db.Column(db.Integer, nullable=False)
    year_bought = db.Column(db.DATE, nullable=False)
    
class Department(db.Model):
    __tablename__= "department"
    department_id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Integer)
    department_name = db.Column(db.String(100), nullable=False)
    department_head_id = db.Column(db.Integer, nullable=True)
    division_id = db.Column(db.Integer, nullable=True)

class Division(db.Model):
    __tablename__= "division"
    division_id = db.Column(db.Integer, primary_key=True)
    division_name = db.Column(db.String(100), nullable=False)
    division_head_id = db.Column(db.Integer, nullable=True)
   
class room(db.Model):
    __tablename__= "room"
    room_number = db.Column(db.Integer, primary_key=True)
    building_code = db.Column(db.Integer, primary_key=True)
    square_feet = db.Column(db.Integer, nullable=False)
    type_ = db.Column(db.String(100))
    department_id = db.Column(db.Integer, nullable=True)

