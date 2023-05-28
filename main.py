from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode

# Set up Selenium webdriver and run in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Get user input
surname = input("Enter a surname: ")

# URL of the website to scrape
url = f"https://www.ancestry.com/name-origin?surname={surname}"

# Open the website
driver.get(url)

# Find the element using the XPath
lastNameOrigin = ''
try:
    element = driver.find_element(By.XPATH, '//*[@id="minMeaningHeight"]/p[1]')
    lastNameOrigin = element.text.split(':')[0]
except:
    try:
        url = f"https://forebears.io/surnames/{surname}"
        driver.get(url)
        element = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div[1]/div/div[1]/p')
        lastNameOrigin = element.text 
        if lastNameOrigin == "The meaning of this surname is not listed.":
            lastNameOrigin = 'No results found'
        else:
            try:
                lastNameOrigin = lastNameOrigin.split(';')[0]
            except:
                print('error splitting surname text from forebears.io')
                driver.close()
                exit()
    except:
        lastNameOrigin = 'No results found'

print(lastNameOrigin)

# Close the browser
driver.close()