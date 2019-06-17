# WebStudent-Observer
##### probably I should've written this earlier...
#
###### The Bucharest University of Economic Studies uses a platform called WebStudent for publishing the exam results. Sadly, the platform doesn't send notifications of any sort. 
##### Sooo...
###### This python script uses Selenium to login into a WebStudent account and check the grades page for a specified year and semester. The grades list is checked at a refresh rate received as a parameter and, if updated, an email will be sent with the updated results. 
#
##### Deployment
###### Given the fact that the script uses very sensitive data, every person who wishes to use it will have to deploy it for himself on a private server.
###### In order to do that, your should reproduce the following steps on your machine: 
* install python3.x
* install pip
* [optional] install python3-venv and create a sandbox 
* install selenium using pip
* fill the variables from credentials.py with your data
* run the script in the background
    * nohup python3 main.py year semester refresh_rate_in_seconds & 
    * example: nohup python3 main.py 3 2 500 &
* ??? profit
