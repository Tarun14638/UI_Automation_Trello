# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

EMAIL = "tarunnanda14638@gmail.com"
PASSWORD = "Test@123@123"
PDF_PATH = "/home/tarun/Desktop/UI_Automation_Code_Trello/Get_Started_With_Smallpdf.pdf"
TRELLO_URL = "https://trello.com/"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
board_name = "QA Scrum Board - TN - ({})".format(timestamp)

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

driver.get(TRELLO_URL)
print("URL opened")

driver.maximize_window()
driver.find_element(
    By.XPATH, "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/a[1]").click()
print("Login Form opened")
time.sleep(2)

wait.until(EC.presence_of_element_located(
    (By.ID, "username-uid1"))).send_keys(EMAIL)
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/div[2]/form[1]/button[1]/span[1]").click()
print("Email Entered")
time.sleep(2)

wait.until(EC.presence_of_element_located(
    (By.ID, "password"))).send_keys(PASSWORD)
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/div[2]/form[1]/button[1]/span[1]").click()
print("Password Entered")
time.sleep(2)

wait.until(EC.presence_of_element_located(
    (By.XPATH, "//p[text()='Create']/ancestor::button")))
print("Logged In Successfully")
time.sleep(5)

wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "jzNA5uVDhk7V5S"))).click()
print("Create button on Home Clicked")
time.sleep(2)

wait.until(
    EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/button[1]"))).click()
print("Create board part Clicked")
time.sleep(2)

wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[type='text']"))).send_keys(board_name)
print("Board name entered")
time.sleep(2)

wait.until(
    EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/div[2]/div[1]/form[1]/button[1]"))).click()
print("Board Created Successfully")
time.sleep(2)

for list_name in ["To Do", "In Progress", "Done"]:
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "textarea[placeholder='Enter list name…']"))).send_keys(list_name)
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
print("List Created 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")

wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[aria-label='Add a card in To Do']"))).click()

card_input = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "textarea[placeholder='Enter a title or paste a link']")))
card_input.send_keys("Write test cases for login functionality")

submit_button = driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Add card in To Do']")
submit_button.click()
print("New Card Added in To DO 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")

wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[aria-label='Add a card in In Progress']"))).click()

card_input = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "textarea[placeholder='Enter a title or paste a link']")))
card_input.send_keys("Execute functional tests for profile update")

submit_button = driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Add card in In Progress']")
submit_button.click()
print("New Card Added in In Progress 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")

wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[aria-label='Add a card in Done']"))).click()

card_input = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "textarea[placeholder='Enter a title or paste a link']")))
card_input.send_keys("Submitted daily QA report")

submit_button = driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Add card in Done']")
submit_button.click()
print("New Card Added in Done 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")

wait.until(EC.visibility_of_element_located(
    (By.CLASS_NAME, "Ns0Sj0nEGMQ7un"))).click()
print("Created card Opened")

wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, ".AJyT3hutz064vb.IfQIR4QBvzNFsu"))).click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true']"))).send_keys(
    "Write the Test Cases of the Login Part of the Application.")
print("Description Entered")

driver.find_element(
    By.CSS_SELECTOR, "button[class='ybVBgfOiuWZJtD orotyyeYQx_tso _St8_YSRMkLv07']").click()

driver.find_element(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/button[1]").click()
wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "span[aria-label='Color: green, title: none']"))).click()
driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Close popover']").click()
print("Label Attached")
time.sleep(1)

# Attach PDF
driver.find_element(
    By.XPATH, "//button[normalize-space()='Attachment']").click()
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[type='file']"))).send_keys(PDF_PATH)
wait.until(EC.presence_of_element_located(
    (By.XPATH, "//h3[contains(text(), 'Attachment') or contains(text(), 'Attachments')]")))
print("PDF File Attached")

# Close card
driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Close dialog']").click()
print("Card Closed")

# Drag and drop card from To Do → In Progress → Done
card = driver.find_element(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[1]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]")
in_progress_list = driver.find_elements(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[2]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]/div[1]/span[2]/a[1]")[1]
done_list = driver.find_elements(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[3]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]")[2]

actions.drag_and_drop(card, in_progress_list).perform()
time.sleep(1)
actions.drag_and_drop(card, done_list).perform()
time.sleep(1)

# # Assert final position
# final_column_cards = driver.find_elements(
#     By.CSS_SELECTOR, ".list:nth-child(3) .list-card-title")
# assert any("Sample Task" in card.text for card in final_column_cards)

driver.quit()
