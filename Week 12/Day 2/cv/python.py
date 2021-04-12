import json
from flask import Flask, url_for, redirect, render_template, flash, request
import requests
import os
import form



app = Flask(__name__)

app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    forma =  form.LoginForm()
    if request.method == "POST":
        #if form.validate_on_submit()
        return redirect(url_for("cv"))

    
    return render_template("login.html", form = forma)


@app.route("/template", methods=["GET", "POST"])
def cv():
    formo = form.CvForm()
    if request.method == "POST":
        fn = formo.firstname.data
        ln = formo.lastname.data
        ag = formo.age.data
        ph = formo.phone.data
        em = formo.email.data
        ct = formo.city.data
        aw = formo.actwork.data
        s1 = formo.social1.data
        s2 = formo.social2.data
        pr = formo.prof.data
        d = formo.date.data
        d1 = formo.date1.data
        d2 = formo.date2.data
        d3 = formo.date3.data
        sk = formo.skill.data
        sk1 = formo.skill1.data
        sk2 = formo.skill2.data
        return render_template("cv.html",fn = fn, ln=ln, ag=ag, ph=ph, em=em, ct=ct, aw=aw, s1=s1, s2=s2, pr=pr, d=d, d1=d1, d2=d2, d3=d3, sk=sk, sk1=sk1, sk2=sk2 )
        
        # return redirect(url_for("display"))

    return render_template("form.html", formo = formo)


app.run(debug = True)