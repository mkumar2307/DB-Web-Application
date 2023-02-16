from flask import Flask, render_template, request
import os
import mysql.connector

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'Templates'))

#Create a function to retrieve data from the database based on filter parameters
def get_data(filter_param=None, filter_value=None):
    mydb = mysql.connector.connect(
        host="localhost",
        user="DB-username",
        password="yourpassword",
        database="DB-name"
    )

    # Construct the SQL query
    if filter_param and filter_value:
        query = "SELECT * FROM your-table WHERE {} = %s".format(filter_param)
        params = (filter_value,)
    else:
        query = "SELECT * FROM your-table"
        params = ()

    # Retrieve data from the database
    mycursor = mydb.cursor()
    mycursor.execute(query, params)
    data = mycursor.fetchall()
    mydb.close()
    return data

# Create a route for the homepage
@app.route("/", methods=["GET", "POST"])
def home():
    # Retrieve the filter parameters from the form submission
    filter_param = request.args.get("filter_param", None)
    filter_value = request.args.get("filter_value", None)

    # Retrieve data from the database with optional filters
    data = get_data(filter_param, filter_value)

    # Render the homepage template with the data and filter parameters
    return render_template("home.html", data=data, filter_param=filter_param, filter_value=filter_value)

if __name__ == "__main__":
    app.run()
