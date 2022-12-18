# GitBot

Python app built by using selenium to create repos in GitHub

## Description

The program need another variable argument to run this program. if user did't provide one is going show an error message and stop. else the program look for the username and password for the github account in .env file inside the local directory and if found it opens google chrome and navigate to the login form to fill in username and password. Then it will click 'create new repo' button and after loading it will enter the repo name and press create repo button go to new repo page and wait for 10 seconds before quitting. 

### Preview

<img src="https://user-images.githubusercontent.com/91461938/191908417-9005bb5d-d1d0-4465-adb0-49d324cf3936.gif">
