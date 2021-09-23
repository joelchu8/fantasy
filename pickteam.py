from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utility

# starts a browser session
PATH = r"C:\Users\Joel\Downloads\edgedriver_win64\msedgedriver.exe"
browser = webdriver.Edge(PATH)
browser.get("https://fplreview.com/free-planner/")

# selects highest number of gameweeks to forecast
select_gw = Select(browser.find_element_by_id("Weeks"))
gws = select_gw.options
select_gw.select_by_index(len(gws) - 1)

# input team id
id_box = browser.find_element_by_name("TeamID")
id_box.send_keys("1290514")
id_box.submit()

# wait for overlay to come up and click close button
close_button_xpath = "/html/body/div[2]/div[3]/div/div/div/div[1]/div/article/div[2]/div/div[19]/div/div/div[1]/button"
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, close_button_xpath)))
close_button = browser.find_element_by_xpath(close_button_xpath)
close_button.click()

players_to_start = []
players_to_bench = []

player_elements = browser.find_elements_by_class_name("xviPLAYERAREA")

for player in player_elements:

    # finds if player captain, vice or starting
    note = player.find_element_by_xpath('.//span[@class="CellComment selinfo"]').get_attribute("innerHTML")
    name = player.find_element_by_xpath('.//span[@class="xviNAME"]').get_attribute("innerHTML").strip("\t")

    if note == "Captain":
        captain = name
        players_to_start.append(name)
    elif note == "Vice":
        vice = name
        players_to_start.append(name)
    elif note == "Start":
        players_to_start.append(name)
    else:
        players_to_bench.append(name)

print(players_to_start)
print(captain)
print(vice)
print(players_to_bench)

utility.login(browser)

browser.find_element_by_link_text("Pick Team").click()

# remove players that are already on the bench
for player in players_to_bench:
    player_element = browser.find_element_by_xpath('//div[text()="' + player + '"]')

    # check if player is starting
    try:
        starting = player_element.find_element_by_xpath('./ancestor::div[@data-testid="pitch"]')

    # player is already on the bench
    except NoSuchElementException:
        players_to_bench.remove(player)

# checks if each player in the list is starting, if not subs them on from the bench
for player in players_to_start:
    player_element = browser.find_element_by_xpath('//div[text()="' + player + '"]')

    try:
        starting = player_element.find_element_by_xpath('./ancestor::div[@data-testid="pitch"]')

    # cannot find ancestor pitch element so player is not starting
    except NoSuchElementException:
        benched_player = players_to_bench.pop()
        player_element.click()

        switch_button = browser.find_element_by_xpath('//button[text()="Switch"]')
        switch_button.click()

        benched_player_element = browser.find_element_by_xpath('//div[text()="' + benched_player + '"]')
        benched_player_element.click()

        switch_button = browser.find_element_by_xpath('//button[text()="Switch"]')
        switch_button.click()


captain_element = browser.find_element_by_xpath('//div[text()="' + captain + '"]')
captain_element.click()

# checks if captain_button shows up, which would mean they are not currently captain
try:
    captain_button = browser.find_element_by_xpath('//button[text()="Make Captain"]')
    captain_button.click()

# closes overlay as player is already captain
except NoSuchElementException:
    close_button = browser.find_element_by_xpath('//button[@class="Dialog__Button-sc-5bogmv-2 ejzwPB"]')
    close_button.click()

vice_element = browser.find_element_by_xpath('//div[text()="' + vice + '"]')
vice_element.click()
try:
    vice_button = browser.find_element_by_xpath('//button[text()="Make Vice Captain"]')
    vice_button.click()
except NoSuchElementException:
    close_button = browser.find_element_by_xpath('//button[@class="Dialog__Button-sc-5bogmv-2 ejzwPB"]')
    close_button.click()

save_button = browser.find_element_by_xpath('//button[text()="Save Your Team"]')
save_button.click()
