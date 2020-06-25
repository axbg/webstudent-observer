import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import mailer
import validators
import automation
import credentials


def observe(driver):
    promotion = ""
    old_classes = []
    observed_semester = None
    semester, refresh_time = 0, 0

    try:
        promotion = sys.argv[1]
        semester = int(sys.argv[2])
        refresh_time = int(sys.argv[3])

        print("webstudent-observer started")

        driver.get("http://webstudent.ase.ro")

        automation.login(driver)
        automation.navigate_to_grades(driver)
        observed_semester = automation.get_observed_semester(driver, promotion, semester)

        if observed_semester is None:
            print("Semester was not found")
            return
    except IndexError:
        print("You should specify promotion, semester and refresh rate in seconds as command line parameters")
        print("python main.py \"2019 - 2020\" 1 10")
    except Exception:
        raise

    while True:
        try:
            observed_semester.click()
            
            time.sleep(refresh_time / 2)

            grades_rows = automation.get_grades_rows(driver)
            classes, grades = [], []

            for i in range(0, len(grades_rows)):
                if i != 0:
                    studied_class = grades_rows[i].find_element_by_css_selector( 'td:nth-child(2)').text
                    grade = grades_rows[i].find_element_by_css_selector('td:nth-child(5)').text
                    classes.append(studied_class)
                    grades.append(grade)
            
            if len(old_classes) != 0 and len(old_classes) != len(classes):
                mail_body = ""
                for studied_class, grade in zip(classes, grades):
                    mail_body += studied_class + ": " + grade + "\n"
                mailer.send_mail(mail_body)

            old_classes = [i for i in classes]
        except Exception as ex:
            print("Exception thrown: {}".format(ex))
            continue
        finally:
            driver.refresh()
            
            time.sleep(refresh_time / 2) 
            
            observed_semester = automation.get_observed_semester(driver, promotion, semester)


if __name__ == "__main__":
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options=options)
    driver.fullscreen_window()
    driver.implicitly_wait(1)

    try:
        observe(driver)
    except Exception as ex:
        print("Crashed due to occuring exception: {}".format(ex))
    finally:
        driver.close()
