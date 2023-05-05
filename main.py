from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import sys
import os
from dotenv import load_dotenv


# load username and password from env file
load_dotenv()
USERNAME = os.getenv("GITHUB_USERNAME")
PASSWORD = os.getenv("GITHUB_PASSWORD")


def main():
    # If user didn't enter a repo name
    try:
        repo_name = sys.argv[1]

        # Load chrome driver
        # driver = webdriver.Chrome()

        # Load firefox driver
        driver = webdriver.Firefox()

        # go to github new repo page
        driver.get("https://github.com/new")

        username = driver.find_element(By.NAME, "login")
        username.send_keys(USERNAME)
        password = driver.find_element(By.NAME, "password")

        # press enter after entering password
        password.send_keys(PASSWORD + Keys.ENTER)

        # wait until it load the page
        repo_name_input_box = WebDriverWait(driver, 60).until(
            lambda x: x.find_element(
                By.XPATH, '//*[@id="react-aria-2"]'))
        repo_name_input_box.click()
        repo_name_input_box.send_keys(repo_name)
        # after entering the repo name, wait for it to check availability
        sleep(2.5)

        create_repo_btn = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/div/form/div[5]/button')

        create_repo_btn.click()

        # close the browser window
        driver.close()

        print("Successfully created repository.")
        return 0

    except IndexError:
        print("Repository name not found")


main()
