import smtplib
import ssl
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import credentials


def find_semester(year_p, semester_p, semesters_p):
    for sem in semesters_p:
        current_year = int(sem.find_element_by_css_selector('td:nth-child(1)').text)
        current_semester = int(sem.find_element_by_css_selector('td:nth-child(2)').text)

        if current_year == year_p and current_semester == semester_p:
            return sem.find_element_by_css_selector('td:nth-child(4)').find_elements_by_tag_name('span')[
                0].find_element_by_css_selector('input:nth-child(1)')

    return None


old_classes = []
year = 0
semester = 0
refresh_time = 0

try:
    year = int(sys.argv[1])
    semester = int(sys.argv[2])
    refresh_time = int(sys.argv[3])
except IndexError:
    print("You should specify year and semester and refresh rate in seconds as command line parameters")
    print("python main.py 3 1 10")
    exit(0)

options = Options()
options.add_argument("--headless")

print("webstudent-observer started")

while True:
    driver = webdriver.Chrome(executable_path="/home/axbg/Downloads/chromedriver", options=options)

    driver.fullscreen_window()
    driver.implicitly_wait(1)

    driver.get("http://webstudent.ase.ro")

    username = driver.find_element_by_id("txtUtilizator")
    username.send_keys(credentials.WEBSTUDENT_ACCOUNT)

    password = driver.find_element_by_id("txtParola")
    password.send_keys(credentials.WEBSTUDENT_PASSWORD)

    login_button = driver.find_element_by_id("btnConectare")
    login_button.click()

    grades_button = driver.find_element_by_xpath(
        '/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/div/ul/li[4]/a')
    grades_button.click()

    semesters_table = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[1]/div[1]/table/tbody')
    semesters = semesters_table.find_elements_by_tag_name('tr')

    observed_semester = find_semester(year, semester, semesters)

    if observed_semester is None:
        print("Semester was not found")
        exit(0)

    observed_semester.click()

    time.sleep(1)

    grades_table = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[1]/div[2]/table/tbody')
    grades_rows = grades_table.find_elements_by_tag_name('tr')

    classes = []
    grades = []

    for i in range(0, len(grades_rows)):
        if i != 0:
            studied_class = grades_rows[i].find_element_by_css_selector('td:nth-child(2)').text
            grade = grades_rows[i].find_element_by_css_selector('td:nth-child(5)').text
            classes.append(studied_class)
            grades.append(grade)

    driver.close()

    if len(old_classes) != 0:
        if len(old_classes) != len(classes):
            old_classes = [i for i in classes]
            mail_body = ""

            for studied_class, grade in zip(classes, grades):
                mail_body += studied_class + ": " + grade + "\n"

            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
            server.login(credentials.GMAIL_USER, credentials.GMAIL_PASSWORD)

            msg = MIMEMultipart('alternative')
            msg['FROM'] = credentials.GMAIL_USER
            msg['To'] = credentials.GMAIL_SEND_TO
            msg['Subject'] = credentials.GMAIL_SUBJECT
            msg.attach(MIMEText(mail_body.encode('utf-8'), _charset='utf-8'))

            server.sendmail(credentials.GMAIL_USER, credentials.GMAIL_SEND_TO, msg.as_string())
            server.close()
    else:
        old_classes = [i for i in classes]

    time.sleep(refresh_time)
