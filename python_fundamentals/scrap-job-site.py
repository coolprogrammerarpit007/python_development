# Scrape the Fake Python Job Site

# Steps To Followe Web Scrapping.

# 1. Inspect Your Data Source

# Inspect the complete website , which you want to scrape. Use developer tools to understand the HTML Structure of the web.


#Step 2:- Scrape HTML Content from the web page.

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)

# Step 3:- Parse HTML Code with Beautiful Soup

# Beautiful Soup is a Python library for parsing structured data. It allows you to interact with HTML in a similar way to how you interact with a web page using developer tools. The library exposes intuitive methods that you can use to explore the HTML you received.

# Parse the Html Content you get from web using the request library.

soup = BeautifulSoup(page.content,"html.parser")

# The second argument that you pass to the class constructor, "html.parser", makes sure that you use an appropriate parser for HTML content.

# print(soup)

# finding elements by it's id
results = soup.find(id="ResultsContainer")
# print("**********************************************************************")
# print(results.prettify())


#finding elements by class name
# job_names = soup.find_all(class_="is-5")
# for job in job_names:
#     print(job.text)

job_cards = results.find_all("div",class_="card-content")

for job_card in job_cards:
    title_element = job_card.find("h2","title")
    company_element = job_card.find("h3","subtitle")
    location_element = job_card.find("p","location")
    # print(company_element.text.strip())
    # print(title_element.text.strip())
    # print(location_element.text.strip())


# Extract Text From HTML Elements
# You only want to see the title, company, and location of each job posting. And behold! Beautiful Soup has got you covered. You can add .text to a BeautifulSoup object to return only the text content of the HTML elements that the object contains:

legal_jobs = results.find_all("h2",string="Legal executive")
# print(legal_jobs)