from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import py.scraping_idc

app = Flask(__name__, template_folder='templates')



#set up app route
@app.route("/")
def index():
   return render_template("index.html", data = data)




if __name__ == "__main__":
   dbname = py.scraping_idc.get_database()
   data = py.scraping_idc.query_from_db(dbname)
   app.run(debug=True) 