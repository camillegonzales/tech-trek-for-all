from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient


def get_internships():
    """
    Returns a dictionary containing internships
    """
    url = "https://github.com/SimplifyJobs/Summer2024-Internships"
    page = requests.get(url)
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
    return internships


internships = get_internships()
client = MongoClient()
# Create database
db = client.tech_collection
# Switch to collection
db = db.internships
# Insert all internships into the collection
db.insert_many(internships)
