import validators
import credentials


def get_grades_rows(driver):
    grades_table = driver.find_element_by_xpath(
        '/html/body/form/div[3]/div[2]/div[1]/div[2]/table/tbody')
    return grades_table.find_elements_by_tag_name('tr')


def find_semester(promotion_p, semester_p, semesters_p):
    for sem in semesters_p:
        current_promotion = sem.find_element_by_css_selector(
            'td:nth-child(3)').text
        current_semester = int(
            sem.find_element_by_css_selector('td:nth-child(2)').text)

        if current_promotion == promotion_p and current_semester == semester_p:
            return sem.find_element_by_css_selector('td:nth-child(4)').find_elements_by_tag_name('span')[
                0].find_element_by_css_selector('input:nth-child(1)')

    return None


def get_observed_semester(driver, promotion, semester):
    semesters_table = driver.find_element_by_xpath(
        '/html/body/form/div[3]/div[2]/div[1]/div[1]/table/tbody')
    semesters = semesters_table.find_elements_by_tag_name('tr')
    return find_semester(promotion, semester, semesters)


def navigate_to_grades(driver):
    grades_button = driver.find_element_by_xpath(
        '/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/div/ul/li[4]/a')
    grades_button.click()


def login(driver):
    validators.validate_login_credentials()

    username = driver.find_element_by_id("txtUtilizator")
    username.send_keys(credentials.WEBSTUDENT_ACCOUNT)

    password = driver.find_element_by_id("txtParola")
    password.send_keys(credentials.WEBSTUDENT_PASSWORD)

    login_button = driver.find_element_by_id("btnConectare")
    login_button.click()
