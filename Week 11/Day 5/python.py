import json
import flask
import requests



app = flask.Flask(__name__)

# data_dict = json.loads("/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json")
# print(data_dict)

    #product = data.json()['Name']
    
    #for p in data:
        #print('Name: ' + p['Category'])
        #print('Website: ' + p['Name'])
        #print('From: ' + p['Status'])
        #print('')


@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/products")
def prod():
    with open('/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json') as json_file:
        data = json.load(json_file)
        print(data[2]["Description"])
        idd = 0
        iddn = idd + 1
    return flask.render_template("product.html",data = data, idd = idd, iddn = iddn)
    


@app.route("/products/<idn>")
def prodid(idn):
    with open('/Users/sashakharoubi/Desktop/BOOTCAMP/Week 11/product_db.json') as json_file:
        data = json.load(json_file)
        right = data[int(idn)]["Description"]
        brand = data[int(idn)]["SupplierName"]
        catego = data[int(idn)]["Category"]
        status = data[int(idn)]["Status"]
        quantity = data[int(idn)]["Quantity"]
        price = data[int(idn)]["Price"]
    return flask.render_template('productdetail.html', idn = idn, right = right, catego = catego, brand = brand, status = status, quantity = quantity, price = price)


app.run(debug = True)