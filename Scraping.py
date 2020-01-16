#  Web scraping with BeautifulSoup
import requests
from bs4 import BeautifulSoup as bs
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = bs(response.text, "html.parser")

#  Extracting links, titles, and dates from each article and putting them in lists
articles = soup.findAll('article')
link, text, date = [], [], []
for article in articles:
    anchor_tag = article.find('a')
    link.append(anchor_tag['href'])
    text.append(anchor_tag.get_text())
    date.append(article.find('time')['datetime'])

#  Writing extracted data to csv file
with open('rithm_school_scraped.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['link', 'text', 'date'])
    for line in zip(link, text, date):
        csv_writer.writerow(line)