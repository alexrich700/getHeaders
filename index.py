import requests
import csv
from bs4 import BeautifulSoup
urls = ['http://401kcpas.com/']
headingInfo = []

for url in urls:
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'lxml')
    for heading in soup.find_all(["h1", "h2", "h3"]):
        headingInfo.append(heading.name + ' ' + heading.text.strip())
        # print(headingInfo)


    with open('headings.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(headingInfo)

    headingInfo.clear()
