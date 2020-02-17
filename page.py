import csv
from SeleniumTestIOET.locators import MainPageLocators, ComplementarySubjectsPageLocators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SeleniumTestIOET.element import BasePageElement


class FacultyElement(BasePageElement):
    def __init__(self):
        self.locator = MainPageLocators.GET_FACULTIES

    def __set__(self, obj, val):
        driver = self.driver
        driver.find_element_by_id(self.locator).send_keys(val)


class ElectiveCourseElement(BasePageElement):
    def __init__(self):
        self.locator = ComplementarySubjectsPageLocators.CLICK_ELECTIVE_COURSE

    def __set__(self, instance, value):
        driver = self.driver
        driver.find_element_by_id(self.locator).send_keys(value)


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Methods to obtain career's information and complementary subjects"""
    faculty_element = FacultyElement()
    elective_course_element = ElectiveCourseElement()

    def get_complementary_subjects(self):
        try:
            faculties = self.get_career_catalog()
            list_complementary_subjects = [[]]
            for index in range(len(faculties)):
                career_curriculum_href = faculties[index][-1]
                self.driver.get(career_curriculum_href)
                a = self.driver.find_element(*ComplementarySubjectsPageLocators.CLICK_ELECTIVE_COURSE)
                a.get_attribute('onclick')
                a.click()
                WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(ComplementarySubjectsPageLocators.SELECT_OPT100)).click()
                y = self.driver.find_elements(*ComplementarySubjectsPageLocators.TABLE)
                for ik in range(len(y)):
                    li = [faculties[index][0], (y[ik].text)[0:7], (y[ik].text)[9:-2]]
                    list_complementary_subjects.append(li)
                self.driver.back()
            list_complementary_subjects.pop(0)
        except StaleElementReferenceException:
            print("Exception")
            pass
        return list_complementary_subjects

    def get_career_catalog(self):
        """Triggers the career's information search"""
        faculties = self.driver.find_elements(*MainPageLocators.GET_FACULTIES)
        list_of_careers = [[]]
        for index in range(len(faculties)):
            faculty = (faculties[index].text.split('\n')[0].split()[-1])[1:-1]
            path = MainPageLocators.PATH_CAREER_CATALOG[1]
            careers = self.driver.find_elements_by_xpath(path + "//div[@id='collapse" + faculty + "']/div/ul[2]/child::li")
            links = self.driver.find_elements_by_xpath(path + "//div[@id='collapse" + faculty + "']/div/ul[2]/child::li/a")
            codes = self.driver.find_elements_by_xpath(path + "//div[@id='collapse" + faculty + "']/div/ul[2]/child::li/span")
            for i in range(len(careers)):
                list_inf = [careers[i].get_attribute("innerHTML").split("<", 1)[0], codes[i].get_attribute("innerHTML"),
                            faculties[index].text.split('\n')[1], links[i].get_attribute("href")]
                list_of_careers.append(list_inf)
        list_of_careers.pop(0)
        return list_of_careers

    @staticmethod
    def save_career_catalog(list_of_careers):
        """Save in a csv file career's information"""
        with open('careers.csv', 'w', newline='', encoding='utf-8') as csv_file:
            file_wr = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file_wr.writerow(["career_name_en", "career_code", "faculty_name", "link_to_career_curriculum"])
            file_wr.writerows(list_of_careers)
        print("FILE 'careers.csv' SAVED SUCCESSFULLY!")

    @staticmethod
    def save_complementary_sub(list_of_subjects):
        """Save in a csv file complementary subjects for each career"""
        with open('complementary_subjects.csv', 'w', newline='', encoding='utf-8') as csv_file:
            file_wr = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file_wr.writerow(["career_name_en", "subject_code", "subject"])
            file_wr.writerows(list_of_subjects)
        print("FILE 'complementary_subjects.csv' SAVED SUCCESSFULLY!")

