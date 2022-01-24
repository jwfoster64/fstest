import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

browser = webdriver.Safari()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('https://app.fullstory.com/login/')
cookie = {'name': 'fs_trusted_device', 'value': 'DvS6MrpikMXlrYouVqcS2Q=='}
browser.add_cookie(cookie)

time.sleep(3)
try:
    element = browser.find_element_by_xpath('//*[@id="login-container"]/div/div/div[2]/div/div[2]/form/div[1]/div/div')
    element.click()
    element.send_keys('jmfoster7@gmail.com')
    browser.find_element_by_xpath('//*[@id="login-container"]/div/div/div[2]/div/div[2]/form/div[2]/button').click()
    text = browser.find_element_by_xpath('//*[@id="login-container"]/div/div/div[2]/div/div[2]/form/div[1]'
                                            '/div/div[2]/div')
    text.click()
    text.send_keys('Testauto1')
    browser.find_element_by_xpath('//*[@id="login-container"]/div/div/div[2]/div/div[2]/form/div[2]/button/span')\
        .click()

    browser.save_screenshot("login_pass.png")
    print('Login successful')

except:

    browser.save_screenshot("login_fail.png")
    print('Login failed')

time.sleep(5)
try:

    playButton = browser.find_element_by_xpath('//div[@class="_12nOgIHbvYG4xSFAdhxiEb UNs8LeRHYzGmwk9AoMo93"]')
    playButton.click()

    browser.save_screenshot("play_recording.png")
    print('Play recording successful')

except:

    browser.save_screenshot("play_recording_fail.png")
    print('Play recording fail')

time.sleep(5)
try:

    share = browser.find_element_by_id('share')
    share.click()
    testShare = browser.find_element_by_xpath('//textarea[@placeholder="Leave a note about this session"]')
    testShare.send_keys('Test Note Automation')
    note = browser.find_element_by_xpath('//button[@class="share"]')
    note.click()
    bte = browser.find_element_by_xpath('//a[@class="backBtn"]')
    bte.click()
    notesButton = browser.find_element_by_xpath('//a[@id="highlightsBtn"]')
    notesButton.click()
    jira = browser.find_element_by_xpath('//span[contains(text(),"Jira")]')
    jira.click()
    summary = browser.find_element_by_xpath('//input[@type="text"]')
    summary.send_keys('test note sent')
    send = browser.find_element_by_xpath('/html[1]/body[1]/div[6]/div[2]/div[1]/div[2]/button[1]')
    send.click()

    browser.save_screenshot("Note sent to Jira.png")
    print('Note sent to JIRA successfully')

except:

    browser.save_screenshot("share_fail.png")
    print('Share failed')

    time.sleep(5)
    browser.close()