from flask import Flask, render_template, redirect, url_for
import py.scraping_idc

app = Flask(__name__, static_folder = "web", static_url_path="", template_folder='web')


#set up app route
@app.route("/")
def index(): 

   data = {}
   data = py.scraping_idc.query_from_db()
    
   return render_template("index.html", data = data)


if __name__ == "__main__":   
   app.run(debug=True) 