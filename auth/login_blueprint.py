from flask import Blueprint, request, render_template, make_response,jsonify
import jwt
import secrets
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
        return None
    

@login_blueprint.post("/login")
def login():
    isValidLogin=valid_login(request.form["name_val"],request.form["pass_val"])
    if isValidLogin is not None:
        return jsonify(isValidLogin),200
    else:
        response=make_response("Wrong Password",401)
        return response