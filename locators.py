from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators."""
    GET_FACULTIES = (By.XPATH, "//div[@class='field-item even']/div[@id='accordion']"
                               "/div[@class='panel panel-default']/div/h4/a/strong")
    PATH_CAREER_CATALOG = (By.XPATH, "//div/section[3]/main/div[@class='row'][2]/div//section/article/div")
    CLICK_ELECTIVE_COURSE = (By.XPATH, "/html/body//div[@class='row'][1]/div/p[@id='informacion']/a")
    TABLE = (By.XPATH, "/html/body//div/table[@id='tbl_materias_complementarias']/tbody/tr/td[@class='sorting_1']")
    TABLE1 = (By.XPATH, "/html/body//div/table[@id='tbl_materias_complementarias']/tbody/tr/td[1]")
    TABLE3 = (By.XPATH, "/html/body//div/table[@id='tbl_materias_complementarias']/tbody/tr/td[3]")
    SELECT_OPT100 = (By.XPATH, "/html/body//div[@id='tbl_materias_complementarias_length']/label/select/option[text()='100']")
