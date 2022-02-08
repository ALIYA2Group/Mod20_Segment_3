from bs4 import BeautifulSoup as soup
from pymongo import MongoClient
from datetime import datetime
import pymongo
import certifi
#import urllib.request

def ice_news(url):

    # fp = urllib.request.urlopen(url)
    # html = fp.read()
    # fp.close()
    # news_soup = soup(html, 'html.parser')
    #      # Add try/except for error handling
    # try:
    #     #Daily images
    #     daily_pic_tag = news_soup.find_all('div', id="asina-images")[0].find_all('a', href=True)
    #     daily_pic = []
    #     for picture in daily_pic_tag:
    #         daily_pic.append(picture['href'])

    #     news_title = news_soup.find_all('h1', class_='entry-title')[0].get_text()
    #     news_p = news_soup.find_all('div', class_='entry-content')[1].find('p').get_text()
        
    #     #Get titles
    #     titles_tag = news_soup.find_all('div', class_='entry-content')[1].find_all('h2')
    #     titles = []
    #     for title in titles_tag:
    #         titles.append(title.get_text())
    #     #Get Contents
    #     contents_tag = news_soup.find_all('div', class_='entry-content')[1].find_all('p')
    #     contents = []
    #     for content in contents_tag:
    #         contents.append(content.get_text())
    #     #Get pic URL
    #     pictures_tag = news_soup.find_all('div', class_='entry-content')[1].find_all('a', href=True)
    #     pictures = []
    #     for picture in pictures_tag:
    #         pictures.append(picture['href'])
    #     time = datetime.now()

    #     ice_data = {
    #         "daily_pic": daily_pic,
    #         "news_title": news_title,
    #         "news_p": news_p,
    #         "titles": titles,
    #         "contents": contents,
    #         "pictures": pictures,
    #         "time": time
    #     }
            
    # except AttributeError:
         return None
    
    # return ice_data


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
    return rec_id
    #Printing the data inserted
    # cursor = collection.find()
    # for record in cursor:
    #     print(record) 


def start_scrape():
    url = "http://nsidc.org/arcticseaicenews/"       
    ice_data = ice_news(url)
    rec_id = insert_to_db(ice_data)
    return rec_id
  