from flask import Blueprint, request, render_template, make_response
login_blueprint=Blueprint("login_blueprint",__name__)


def valid_login(username,password):


    if username=="a" and password=="a":
        return True
    else:
        return False


@login_blueprint.post("/login")
def login():
    isValidLogin=valid_login(request.form["name_val"],request.form["pass_val"])
    if isValidLogin==True:
        return render_template("dashboard.html")
    else:
        response=make_response("Wrong Password",401)
        return response
    


# from flask import Blueprint

# example_blueprint = Blueprint('example_blueprint', __name__)

# @example_blueprint.route('/')
# def index():
#     return "This is an example app"