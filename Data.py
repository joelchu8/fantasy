from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#starts a browser session
PATH = r"C:\Users\Joel\Downloads\edgedriver_win64\msedgedriver.exe"
browser = webdriver.Edge(PATH)
browser.get("https://fplreview.com/free-planner/")

#selects highest number of gameweeks to forecast
select_gw = Select(browser.find_element_by_id("Weeks"))
gws = select_gw.options
select_gw.select_by_index(len(gws) - 1)

#input team id
id_box = browser.find_element_by_name("TeamID")
id_box.send_keys("1290514")
id_box.submit()

#wait for overlay to come up and click close button
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div[1]/div/article/div[2]/div/div[19]/div/div/div[1]/button")))
close_button = browser.find_element_by_xpath(
    "/html/body/div[2]/div[3]/div/div/div/div[1]/div/article/div[2]/div/div[19]/div/div/div[1]/button")
close_button.click()

#click transfer suggest button
transfer_suggest_button = browser.find_element_by_id("transfersuggest")
transfer_suggest_button.click()

#wait for overlay to come up and click Transfer Suggest
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div[1]/div/article/div[2]/div/div[18]/div/div/div[6]/button[1]")))
transfer_suggester = browser.find_element_by_xpath(
    "/html/body/div[2]/div[3]/div/div/div/div[1]/div/article/div[2]/div/div[18]/div/div/div[6]/button[1]")
transfer_suggester.click()
