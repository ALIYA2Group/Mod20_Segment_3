#from splinter import Browser
from bs4 import BeautifulSoup as soup
#from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
from datetime import datetime
import pymongo
import certifi

# def ice_news(browser, url):
#     # Scrape Ice News
#     browser.visit(url)

#     # Optional delay for loading the page
#     browser.is_element_present_by_css('div.list_text', wait_time=1)

#     # Convert the browser html to a soup object and then quit the browser
#     html = browser.html
#     news_soup = soup(html, 'html.parser')

#          # Add try/except for error handling
#     try:
#         # Use the parent element to find the first 'a' tag and save it as 'news_title'
#         news_title = news_soup.find_all('h1', class_='entry-title')[0].get_text()
#         # Use the parent element to find the paragraph text
#         news_p = news_soup.find_all('div', class_='entry-content')[1].find('p').get_text()
        
#         #Get titles
#         titles_tag = news_soup.find_all('div', class_='entry-content')[1].find_all('h2')
#         titles =[]
#         for title in titles_tag:
#             titles.append(title.get_text())
#         #Get Contents
#         contents_tag = news_soup.find_all('div', class_='entry-content')[1].find_all('p')
#         contents =[]
#         for content in contents_tag:
#             contents.append(content.get_text())
#         #Get pic URL
#         pictures_tag = news_soup.find_all('div', class_='entry-content')[1].find_all('a', href=True)
#         pictures = []
#         for picture in pictures_tag:
#             pictures.append(picture['href'])
#         time = datetime.now()

#         ice_data = {
#             "news_title": news_title,
#             "news_p": news_p,
#             "titles": titles,
#             "contents": contents,
#             "pictures": pictures,
#             "time": time
#         }
            
#     except AttributeError:
#         return None
    
#     return ice_data


def get_database():    
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://alddsdataanalytics:ALDDSgoogle.2022@alddsdataanalytics.gjtom.mongodb.net/alddsdataanalytics"
    
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    
    client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
    print("Connected successfully!!!")

    return client['alddsdataanalytics']

 
def insert_to_db(ice_data):
    dbname = get_database()
    # Insert Data        
    collection = dbname["alddsdataanalytics"]
    rec_id = collection.insert_one(ice_data)        
    
    print("Data inserted with record ids", rec_id)
    
    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record) 


def query_from_db():
    dbname = get_database()
    collection = dbname["alddsdataanalytics"]
    #Get the latest record
    item_details = collection.find().sort("time",-1)
    data = item_details[0]
    return  data


#if __name__ == "__main__":
    # If running as script, print scraped data
    # url = "http://nsidc.org/arcticseaicenews/"
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=True)    
    #ice_data = ice_news(browser, url)
    #insert_to_db(ice_data)
    #query_from_db()


    