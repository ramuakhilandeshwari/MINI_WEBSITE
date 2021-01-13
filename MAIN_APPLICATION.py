from flask import Flask, request, render_template
from flask_cors import cross_origin
import pyodbc
import pandas as pd

#connection to database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-8PLCNJEP;'
                      'Database=GIFTEVERYDAY DOMAIN;'
                      'Trusted_Connection=yes;');
app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/datareport", methods = ["GET", "POST"])
@cross_origin()
def data():
    option = request.form['exampleRadios']
    c1=request.form['newcust_name']
    c2=request.form['newcust_cont']
    c3=request.form['newcust_mail']
    record=[c1,c2,c3]
    if option == 'option1':
        data = pd.read_sql("SELECT * FROM DELIVERY_GIFT", conn)
        result=data.to_html()
    

    elif option == 'option2':
        data = pd.read_sql("SELECT * FROM CUSTOMER", conn)
        result=data.to_html()
        

    elif option == 'option3':
        data = pd.read_sql("SELECT * FROM GIFTEVERYDAY_BRANCH", conn)
        result=data.to_html()
        

    elif option == 'option4':
        data = pd.read_sql("SELECT * FROM ORDER_GIFT", conn)
        result=data.to_html()
        
    elif option == 'option5':
        data = pd.read_sql("SELECT * FROM ORDERS", conn)
        result=data.to_html()
    
    elif option == 'option6':
	cursor=conn.cursor()
	inp="insert into customer values(?,?,?)"
	cursor.execute(inp,record)
	data=pd.read_sql("SELECT * FROM CUSTOMER", conn)
	result=data.to_html()

    return result



if __name__ == "__main__":
    app.run(debug=True)
