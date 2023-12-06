from flask import Flask , render_template, request
import jwt 
app=Flask(__name__)


def valid_login(username,password):
    if username=="a" and password=="a":
        return True
    else:
        return False

@app.get("/")
def home_html():
    return render_template("index.html")

@app.post("/login")
def login():
    is_valid_login_true=valid_login(request.form["name_val"],request.form["pass_val"])
    if is_valid_login_true == True:
        return "Login successfully"
    else:
        return "Try Again"


# def create_token():
#     created_token=jwt.encode({ "some":"payload"},"secret_text",algorithm="HS256")
#     print(created_token)
#     return "Done"