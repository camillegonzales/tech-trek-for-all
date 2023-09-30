from pymongo import MongoClient
from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
# Create database
db = client['cluster0']
# Create collection
collection = db['internships']

def insert_data():
    """
    Returns a dictionary containing internships
    """
    url = "https://github.com/SimplifyJobs/Summer2024-Internships"
    page = requests.get(url)
    if page.status_code == 200:
        data = BeautifulSoup(page.content, "html.parser")
        table = data.find('table')
        body = table.find('tbody')
        internships = []
        for row in body.findAll('tr'):
            internship = {}
            internship['company'] = row.td.text
            internship['date'] = row.findAll('td')[4].text
            if row.a:
                internship['link'] = row.a.get('href')
                internship['title'] = row.a.text
            internships.append(internship)
        collection.insert_many(internships)

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {"_id": 0}))  # Query MongoDB for data
    return jsonify(data)

@app.route('/scrape_and_insert', methods=['GET'])
def scrape_and_insert():
    insert_data()
    return 'Data scraped and inserted into MongoDB!'

if __name__ == '__main__':
    app.run(debug=True)
