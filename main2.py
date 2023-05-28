import requests
from lxml import etree

# URL of the website to scrape
url = "https://www.ancestry.com/name-origin?surname=cincotta"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content
html = etree.HTML(response.text)

# Find the element using the XPath
element = html.xpath('//*[@id="minMeaningHeight"]')

print(element)
