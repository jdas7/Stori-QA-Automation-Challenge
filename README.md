# Stori-QA-Automation-Challenge

Stori QA Automation Engineer Challenge

### For this challenge I will use the next technologies:

- Python 3.8
- [behave library](https://behave.readthedocs.io/en/latest/).
- [selenium library](https://pypi.org/project/selenium/).
- [allure library](https://pypi.org/project/allure-behave/)

#### you must install allure to be able to run the project with the html report and view it
[Install Allure](https://allurereport.org/docs/gettingstarted-installation/)

### Running the project:

To execute this project, you must first install the requirements with the next command:

`pip install -r requirements.txt`

Use the following command to execute with allure:

`behave --format=allure_behave.formatter:AllureFormatter -o allure-results --define browser={browser} --tags={tags}`

use the following command to display the report:

`allure serve .\allure-results\`

| Parameter | Options                                                                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tags      | here you can put the behave tag that you want run                                                                                                                                 |
| browser   | use the browser parameter to indicate with which browser you want to run the test: chrome - firefox - opera, if you do not send the default parameter the browser will be chrome. |
