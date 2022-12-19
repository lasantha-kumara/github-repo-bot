# GitBot

Automate github repo creation using [Python](https://www.python.org/) and [Selenium](https://www.selenium.dev/).

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info
This is a commandline program to create github repositories automatically. This will ease the workload of developers who wants to create lots of repos daily.

## Technologies
Project is created with:
* Python version: 3.10
* Selenium version: 4.7.2
	
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

# To create an env file
$ touch .env

# To open the env file
$ open .env
```

Add these 2 lines and save it.

```
GITHUB_USERNAME="your_github_email"
GITHUB_PASSWORD="your_github_password"
```

## Usage

To run this project in Linux/Unix:

```
$ python3 main.py repo_name
```

To run this project in Windows:

```
$ python main.py repo_name
```

## License 
This project is open source and available under the [MIT License](https://github.com/lasanthamudalige/automate-github-repo-creation/blob/main/LICENSE).
