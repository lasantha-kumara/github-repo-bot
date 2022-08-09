from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
from time import sleep
import os
from dotenv import load_dotenv

# load username and password from env file
load_dotenv()
USERNAME = os.getenv("GITHUB_USERNAME")
PASSWORD = os.getenv("GITHUB_PASSWORD")

options = webdriver.ChromeOptions()

# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


def main():
    repo_name = input("Enter repository name: ")

    driver = webdriver.Chrome(options=options)

    # add stealth driver to not trigger verification
    stealth(driver,
            languages=["en-US", "en"],
            vendor="duckduckgo.com",
            platform="Ubuntu",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    # go to github new repo page
    driver.get("https://github.com/new")

    username = driver.find_element(By.NAME, "login")
    username.send_keys(USERNAME)
    sleep(2)
    password = driver.find_element(By.NAME, "password")

    # press enter after entering password
    password.send_keys(PASSWORD + Keys.ENTER)
    sleep(2)

    repo_name_input_box = driver.find_element(By.ID, "repository_name")
    repo_name_input_box.send_keys(repo_name)
    sleep(2)

    create_repo_btn = driver.find_element(
        By.XPATH, '//*[@id="new_repository"]/div[5]/button')
    create_repo_btn.click()

    # wait for an hour before closing the window
    sleep(600)


main()
