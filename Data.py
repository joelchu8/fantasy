from selenium import webdriver
from selenium.webdriver.support.ui import Select

PATH = r"C:\Users\Joel\Downloads\edgedriver_win64\msedgedriver.exe"
browser = webdriver.Edge(PATH)
browser.get('https://fplreview.com/massive-data-planner/')

select_gw = Select(browser.find_element_by_id("Weeks"))
gws = select_gw.options
print(select_gw.options)
select_gw.select_by_index(len(gws) - 1)

id_box = browser.find_element_by_name("TeamID")
id_box.send_keys('1290514')

id_box.submit()
