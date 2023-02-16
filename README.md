# DB-web-application
This application used to fetch information from MYSQL DB and display in a web browser.    
     
First, you need to install Flask, which is a Python web framework. You can install it using pip by running the following command in your terminal:     
$ pip install Flask    
     
     
we need to create a Flask application.     
    
We define a function called get_data() that establishes a connection to a MySQL database, retrieves data from a table in the database, and returns the data as a list of tuples.     
      
The function uses the mysql.connector module to connect to the database, and executes a SQL query to retrieve all rows from a table.     
