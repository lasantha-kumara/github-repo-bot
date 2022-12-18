# GitBot

Automate github repo creation using Python.## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with:
* Python version: 3.10
	
## Setup

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer.\
From your command line run:

```
# Clone this repository
$ git clone https://github.com/lasanthamudalige/automate-github-repo-creation.git

# Go into the repository
$ cd automate-github-repo-creation/

# To install all dependencies
$ pip install -r requirements.txt
```

## Usage

To run this project in Linux/Unix:

```
$ python3 main.py
```

To run this project in Windows:

```
$ python main.py
```

## License 
This project is open source and available under the [MIT License](https://github.com/lasanthamudalige/automate-github-repo-creation/blob/main/LICENSE).

## Description:

The program need another variable argument to run this program. if user did't provide one is going show an error message and stop. else the program look for the username and password for the github account in .env file inside the local directory and if found it opens google chrome and navigate to the login form to fill in username and password. Then it will click 'create new repo' button and after loading it will enter the repo name and press create repo button go to new repo page and wait for 10 seconds before quitting. 
