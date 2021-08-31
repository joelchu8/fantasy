from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#
# TODO
# make it so that it picks the transfer with highest data points per trade
#
#


def suggest_transfers():
    # click transfer suggest button
    transfer_suggest_button = browser.find_element_by_id("transfersuggest")
    transfer_suggest_button.click()

    # wait for overlay to come up and click Transfer Suggest
    suggester_xpath = "/html/body/div[2]/div[3]/div/div/div/div[1]/div/article/div[2]/div/div[18]/div/div/div[6]/button[1]"
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, suggester_xpath)))
    transfer_suggester = browser.find_element_by_xpath(suggester_xpath)
    transfer_suggester.click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "tradePITCH")))
    transfers = browser.find_elements_by_id("trade")

    # gets info from top transfer suggestion
    value = float(transfers[0].find_element_by_xpath('//*[@id="trade"]/tr[1]/td').text.split()[0])
    print(value)

    # gets the players being traded out and in from the top transfer suggesion
    trades = transfers[0].find_elements_by_class_name("xviPOSROW")
    players_out = []
    players_in = []
    for trade in trades:
        players = trade.text.split()
        player_out = players[0]
        players_out.append(player_out)
        player_in = players[1]
        players_in.append(player_in)
        print(players_out)
        print(players_in)


def pick_team():
    players_to_start = []

    player_elements = browser.find_elements_by_class_name("xviPLAYERAREA")

    for player in player_elements:

        # finds if player captain, vice or starting
        note = player.find_element_by_xpath('.//span[@class="CellComment selinfo"]').get_attribute("innerHTML")
        name = player.find_element_by_xpath('.//span[@class="xviNAME"]').get_attribute("innerHTML")

        if note == "Captain":
            captain = name
            players_to_start.append(name)
        elif note == "Vice":
            vice = name
            players_to_start.append(name)
        elif note == "Start":
            players_to_start.append(name)

    print(players_to_start)
    print(captain)
    print(vice)


suggest_transfers()
