from flask import Blueprint, request, render_template, make_response,jsonify,session
import jwt
import secrets
import datetime
login_blueprint=Blueprint("login_blueprint",__name__)


def create_token(username):
    secure_secrets=secrets.token_hex(16)
    created_token=jwt.encode({"username" :username},secure_secrets,algorithm="HS256")
    return created_token

def valid_login(username,password):
    if username=="a" and password=="a":
        created_token=create_token(username)
        return created_token
    else:
        return 
    
def user_logged_in():
    if "session" in session:
        print(True)
        return True
    else:
        print(False)
        return False
    
def create_session_for_user(token):
    session["session"]=token

@login_blueprint.post("/login")
def login():
    data=request.json
    username=data.get("username")
    password=data.get("password")
    
    # username=request.form["name_val"]
    # password=request.form["pass_val"]
    
    #  # check session exists
    is_user_logged_in=user_logged_in()
    
    if is_user_logged_in == False:
        token=valid_login(username,password)
        
        create_session_for_user(token)
        
        return "Done"
    else:
        response=make_response("user logged in ")
        return response