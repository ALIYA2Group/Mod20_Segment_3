from flask import Flask, render_template, redirect, url_for
import py.query_db
import py.scraping_idc
from datetime import date

app = Flask(__name__, static_folder = "web", static_url_path="", template_folder='web')


#set up app route/scrape
@app.route("/")
def index(): 
   data = {}
   data = py.query_db.query_from_db()
   time = date.today().strftime("%b-%d-%Y")    
   return render_template("index.html", data = data, time = time)


@app.route("/scrape")
def scrape(): 
   rec_id = py.scraping_idc.start_scrape()   
   return f"Data inserted with record ids {rec_id}"

if __name__ == "__main__":   
   app.run(debug=True) 