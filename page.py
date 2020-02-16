import csv
from SeleniumTestIOET.locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

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

