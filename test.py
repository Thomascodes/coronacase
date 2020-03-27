# coronacase - by-country case scraping script
# written by t.j. loudon and fixed (a lot) by HelloWorld

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# init driver
print("coronacase - most recent coronavirus by-country case count script")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('log-level=3')    
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get('https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')

print("CORONACASE: this may take a little under a minute. pulling data..")

driver.implicitly_wait(20)

# just to be on the safe side
time.sleep(1)

# get all covid-19 cases of each country
index = 1
cor = {}

while True:
    try:
        cor[WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[2]/margin-container/full-container/div/div[2]/nav/span[' + str(index) + ']/div/div/h5/span[3]'))).text] = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[2]/margin-container/full-container/div/div[2]/nav/span[' + str(index) + ']/div/div/h5/span[1]/strong'))).text
        index += 1;
    except Exception as e:
        print(e)
        break

# prints dictionary
for key, item in cor.items():
    print(key + ': ' + item)

