from flask import Flask,render_template,session, redirect, url_for
import os
from datetime import timedelta 

from auth.login_blueprint import login_blueprint,user_logged_in

app = Flask(__name__)
app.register_blueprint(login_blueprint)


@app.get("/")
def home_html():
    return render_template("auth/login.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


app.secret_key=os.urandom(24)
app.permanent_session_lifetime=timedelta(seconds=10)