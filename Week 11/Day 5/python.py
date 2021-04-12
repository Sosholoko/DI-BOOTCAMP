import json
from flask import Flask, url_for, redirect, render_template, flash, request
import requests
import os
import forms


directory = "/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/Day 5/static/img"




app = Flask(__name__)

app.secret_key = "secret"

cart = []

# data_dict = json.loads("/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json")
# print(data_dict)

    #product = data.json()['Name']
    
    #for p in data:
        #print('Name: ' + p['Category'])
        #print('Website: ' + p['Name'])
        #print('From: ' + p['Status'])
        #print('')

def read():
    with open('/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json') as json_file:
        data = json.load(json_file)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def prod():
    with open('/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json') as json_file:
        data = json.load(json_file)
        for image in os.listdir(directory):
            image = image
        idd = 0
        iddn = idd + 1
    return render_template("product.html",data = data, idd = idd, iddn = iddn, image = image)
    


@app.route("/products/<idn>")
def prodid(idn):
    with open('/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json') as json_file:
        data = json.load(json_file)
        for item in data:
            if item["ProductId"] == idn:
                name = item["Name"]
                right = item["Description"]
                brand = item["SupplierName"]
                catego = item["Category"]
                status = item["Status"]
                quantity = item["Quantity"]
                price = item["Price"]
                return render_template('productdetail.html', name= name, idn = idn, right = right, catego = catego, brand = brand, status = status, quantity = quantity, price = price)


@app.route("/cart")
def shop():
    with open('/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json') as json_file:
        data = json.load(json_file)
    
    return render_template("cart.html")

@app.route("/cart/<id>")
def add(id):
    with open('/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json') as json_file:
        data = json.load(json_file)
    for item in data:
        if item["ProductId"] == id:
            cart.append(item)
            print(cart)
            flash("Item added to your list !")
            return redirect(url_for("prod"))
            



@app.route("/form", methods=["GET", "POST"])
def test():
    form = forms.TestForm()
    if request.method == "POST":
        print("Name: ", form.name.data)
        print("Age: ", form.age.data)

    return render_template("testform.html", form = form)
    

@app.route("/login", methods=["GET", "POST"])
def login():
    form =  forms.LoginForm()
    if request.method == "POST":
        #if form.validate_on_submit():
            if form.user.data == "sasha":
                if form.passw.data == "sasha0408":
                    return redirect(url_for("home"))

    
    return render_template("login.html", form = form)


app.run(debug = True)