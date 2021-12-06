from selenium.webdriver.common.by import By
from pageObjects.SearchPage import SearchPage
from utilities import config_files
from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    searchTextbox = "input[type='text']"
    searchResult = "[id='jump-to-suggestion-search-global']"
    searchTextboxWebElement = (By.CSS_SELECTOR, searchTextbox)
    searchResultWebElement = (By.CSS_SELECTOR, searchResult)

    def enterSearch_Textbox(self):
        self.waitUntilElementLoaded_CSS(self.searchTextbox)
        self.driver.find_element(*LoginPage.searchTextboxWebElement).click()
        self.driver.find_element(*LoginPage.searchTextboxWebElement).send_keys(config_files.get_searchText())

    def openSearch_Result(self):
        self.waitUntilElementLoaded_CSS(self.searchResult)
        self.driver.find_element(*LoginPage.searchResultWebElement).click()
        searchPage = SearchPage(self.driver)
        return searchPage
