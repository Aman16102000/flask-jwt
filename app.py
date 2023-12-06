from flask import Flask,render_template

from auth.login_blueprint import login_blueprint

app = Flask(__name__)
app.register_blueprint(login_blueprint)



@app.get("/")
def home_html():
    return render_template("auth/login.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# def create_token():
#     created_token=jwt.encode({ "some":"payload"},"secret_text",algorithm="HS256")
#     print(created_token)
#     return "Done"
