from selenium import webdriver
from selenium.webdriver.chrome.options import Options

na='http://newsonair.com/RNU-NSD-Audio-Archive-Search.aspx'
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome('driver/chromedriver',chrome_options=options)
driver.get(na)
