from flask import session, redirect, url_for

#separated users bases on their roles that has to be perfomed in the system 
users = {
    "admin": {"role": "Admin"},
    "hr": {"role": "Editor"},
    "accountant": {"role": "Editor"},
    "staff":{"role": "Viewer"}
}

# Simulated route permisssion to users in the system
roles_permissions = {
    "Admin": ["dashboard", "employees_details","user_management", "reports"],
    "hr": ["dashboard", "employees_details", "employee_management","reports"],
    "accountant": ["dashboard", "issue_payment", "cancel_payment", "reports"],
    "Viewer": ["dashboard", "personal_report"],
}

def login(username):
    if username in users:
        session["user"] = users[username]

def logout():
    session.pop("user", None)

def is_authorized(route):
    if "user" not in session:
        return False
    user_role = session["user"]["role"]
    return route in roles_permissions.get(user_role, [])
