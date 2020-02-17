import unittest
from selenium import webdriver
from SeleniumTestIOET import page


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/SeleniumDrivers/chromedriver.exe')
        self.driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")

    def test_in_espol_edu_ec(self):
        """Tests espol.edu.ec feature. Searches for the career's catalog and save the information in a file."""
        # Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        # Fill a list with career's information
        list_careers = main_page.get_career_catalog()
        # Write a csv file with the data
        main_page.save_career_catalog(list_careers)
        # Get a list of Complementary Subjects for each career. (Bonus exercise)
        list_complementary_subjects = main_page.get_complementary_subjects()
        main_page.save_complementary_sub(list_complementary_subjects)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
