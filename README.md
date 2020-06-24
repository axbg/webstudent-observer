# WebStudent-Observer
### probably I should've written this earlier...
#
#### The Bucharest University of Economic Studies uses a platform called WebStudent for publishing the exam results. Sadly, the platform doesn't send notifications of any sort. 
## Sooo...
#### This python script uses Selenium to login into a WebStudent account and check the grades page for a specified year and semester. The grades list is checked at a refresh rate received as a parameter and, if updated, an email will be sent with the updated results. 
#
### Deployment
#### Given the fact that the script uses very sensitive data, every person who wishes to use it will have to deploy it for himself on a private server.
#### In order to do that, you have to reproduce the following steps on your machine: 
* Install python3.x
* Install pip
* *[optional]* install python3-venv and create a sandbox 
* Install dependencies 
  * ```pip install -r requirements.txt```
* Install chromium
  * ```sudo apt install chromium-browser```
* Fill the variables in credentials.py
  * WEBSTUDENT_ACCOUNT
  * WEBSTUDENT_PASSWORD
  * MAIL_SERVICE = "GMAIL" | "MAILGUN"
    * you can choose between GMAIL SMTP and Mailgun
    * the credentials specific to the service you are **not** using should be ignored
  * GMAIL_USER
    * the Gmail address used to send the E-mail
  * GMAIL_DEVICE_KEY
    * [a generated access application password](https://support.google.com/accounts/answer/185833?hl=en)
    * **never** use your actual Gmail password
  * MAILGUN_SANDBOX
    * Mailgun sandbox used to send the e-mails
  * MAILGUN_KEY
    * Mailgun private API key 
  * MAIL_SUBJECT
  * MAIL_FROM = ""
  * MAIL_TO = ""
* Run the script in the background
    * nohup python3 main.py promotion semester refresh_rate_in_seconds & 
    * example: nohup python3 main.py "2019 - 2020" 2 600 &
      * recommended: refresh_rate_in_seconds >= 10
* Be the coolest guy in your college group

### Deployment on Windows
The default *chromedriver* configuration will not work on Windows  
To avoid any related problem, you can apply the following changes:
  * install webdriver-manager
    * ```pip install webdriver-manager```
  * import webdriver-manager in main.py
    * ```from webdriver_manager.chrome import ChromeDriverManager```
  * replace the default driver instantiation in main.py *(line 89)*
      ```python
      # driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options=options)
      driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
      ```
