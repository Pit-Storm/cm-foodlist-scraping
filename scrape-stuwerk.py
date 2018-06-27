from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

# Chrome im incognito Modus starten
option = webdriver.ChromeOptions()
option.add_argument(“ — incognito”)

# neues Browserfenster
browser = webdriver.Chrome(executable_path=’/Library/Application Support/Google/chromedriver’, chrome_options=option)

# Seite aufrufen
browser.get("https://www.studierendenwerk-mainz.de/essentrinken/speiseplan/")

# TimeOut handling
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, “//div[@class=’speiseplan_date']”)))

except TimeoutException:
    print(“Timed out waiting for page to load”)
    browser.quit()

dates_element = browser.find_elements_by_xpath(“//div[@class='speiseplan_date']”)
#counters_element =
# foods_element = 

# use list comprehension to get the actual repo titles and not the selenium objects.

dates = [x.text for x in dates_element]