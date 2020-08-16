from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

na='http://newsonair.com/RNU-NSD-Audio-Archive-Search.aspx'
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome('driver/chromedriver',chrome_options=options)
driver.get(na)

time.sleep(5)
#driver.find_element_by_link_text("RNU NSD Audio Bulletins").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_program_type_cbl_0").click()
#radio1 = driver.findElement(By.id(""))
#radio1.click()
time.sleep(5)
# Selection of " RNU-NSD Type"		
driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddwtype']/option[text()='Regional']").click()
time.sleep(2)
# Selection of "RNU-NSD Name"
select_box = driver.find_element_by_name("ctl00$ContentPlaceHolder1$ddwrnunsdname")
options = [x for x in select_box.find_elements_by_tag_name("option")]
Name=[]
for element in options:
  Name.append(element.text)
time.sleep(2)

print(Name)
