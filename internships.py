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
    internships = {}
    for row in body.findAll('tr'):
        internships['company'] = row.td.text
        internships['date'] = row.findAll('td')[4].text
        if row.a:
            internships['link'] = row.a.get('href')
            internships['title'] = row.a.text
    return internships


client = MongoClient()
# Create database
db = client.tech_collection
# Switch to collection
internships = db.internships
# Insert all internships into the collection
internships.insert_many(get_internships)
