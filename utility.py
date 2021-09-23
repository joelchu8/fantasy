def login(browser):
    browser.get('https://fantasy.premierleague.com/')

    login_box = browser.find_element_by_id("loginUsername")
    login_box.send_keys("jcevbqlxcvgaijsyuc@rffff.net")

    password = str(input("password: "))
    password_box = browser.find_element_by_id("loginPassword")
    password_box.send_keys(password)

    password_box.submit()
