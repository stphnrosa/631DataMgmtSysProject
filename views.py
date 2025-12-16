from flask import Blueprint, render_template, request, redirect, url_for
from models import Employee, Project
from database import db

views = Blueprint("views", __name__) #this lets all web routes to be organized in one area

# Home page is shown by rendering index.html template in the templates folder
@views.route("/")
def home():
    return render_template("index.html")

# HR Page has all employees from the DB and displays them from the HR.HTML
@views.route("/hr")
def hr():
    employees = Employee.query.all()
    return render_template("HR.html", employees=employees)

# This employee info comes from a form and also crea
@views.route("/hr/add", methods=["POST"])
def add_employee():
    employee_name = request.form.get("employee_name")
    role = request.form.get("role")
    project_number = request.form.get("project_number")
    employee = Employee(employee_name=employee_name, role=role,project_number=project_number)
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for("views.hr")) 

# Edit employee route- gets specific employees by their id(employee_no in this case). When form is submitted via POST, whatever changes have been made gets updated.
@views.route("/hr/employee/<int:employee_no>/edit", methods=["GET", "POST"])
def edit_employee(employee_no):
    employee = Employee.query.get_or_404(employee_no)
    
    if request.method == "POST":
        employee.employee_name = request.form.get("employee_name")
        employee.role = request.form.get("role")
        employee.project_number=request.form.get("project_number")
        
        db.session.commit()
        return redirect(url_for("views.hr"))
    
    return render_template("employee_edit.html", employee=employee)

# Delete employee route- deletes employee from DB using their ID, redirects back to HR Page
@views.route("/hr/employee/<int:employee_no>/delete", methods=["POST"])
def delete_employee(employee_no):
    employee = Employee.query.get_or_404(employee_no)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for("views.hr"))

# Project Management Page - gets ALL projects and ALL employees displaying on PM.HTML
@views.route("/projects")
def projects_page():
    projects = Project.query.all()
    employees = Employee.query.all()
    return render_template("PM.html", projects=projects, employees=employees)

#  Edit project route- Gets project by its ID.updates dates,budget and department when form is submitted(POST).
@views.route("/pm/project/<int:project_number>/edit", methods=["GET", "POST"])
def edit_project(project_number):
    project = Project.query.get_or_404(project_number)
    
    if request.method == "POST":
        project.date_started = request.form.get("date_started")
        project.date_ended = request.form.get("date_ended")
        project.budget = request.form.get("budget")
        project.department_id = request.form.get("department_id")
        
        db.session.commit()
        return redirect(url_for("views.projects_page"))
    
    return render_template("project_edit.html", project=project)

# Add project- creates new project in DB, REDIRECTS to project management page.
@views.route("/projects/add", methods=["POST"])
def add_project():
    date_started = request.form.get("date_started")
    date_ended= request.form.get("date_ended")
    budget = request.form.get("budget")
    department_id= request.form.get("department_id")

    project= Project(
        date_started=date_started,
        date_ended=date_ended,
        budget=budget,
        department_id=department_id
    )
    db.session.add(project)
    db.session.commit()
    return redirect(url_for("views.projects_page"))

#This file defined ALL my web routes for HR/PM apps.

