from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.RepoPage import RepoPage
from utilities.BaseClass import BaseClass
from utilities import config_files


class SearchPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    state = "search_state"
    state_WebElement = (By.ID, state)

    license = "search_license"
    license_WebElement = (By.ID, license)

    searchStars = "search_stars"
    searchStars_WebElement = (By.ID, searchStars)

    followers = "search_followers"
    followers_WebElement = (By.ID, followers)

    writtenLanguage = "//select[@id='search_language']"
    writtenLanguage_WebElement = (By.XPATH, writtenLanguage)

    searchButton = "[class='form-group flattened'] [type='submit']"
    searchButton_WebElement = (By.CSS_SELECTOR, searchButton)

    advanceSearch = "//a[contains(@href,'Repositories')][contains(text(),'Advanced search')]"
    advanceSearch_WebElement = (By.XPATH, advanceSearch)

    def clickAdvanceSearch(self):
        self.waitUntilElementLoaded_XPATH(self.advanceSearch)
        if self.driver.find_element(*SearchPage.advanceSearch_WebElement).is_displayed():
            self.driver.find_element(*SearchPage.advanceSearch_WebElement).click()

    def writtenLanguage_Dropdown(self):
        self.waitUntilElementLoaded_XPATH(self.writtenLanguage)
        sel = Select(self.driver.find_element(*SearchPage.writtenLanguage_WebElement))
        sel.select_by_visible_text(config_files.get_writtenInLanguage())

    def state_Dropdown(self):
        self.waitUntilElementLoaded_ID(self.state)
        sel = Select(self.driver.find_element(*SearchPage.state_WebElement))
        sel.select_by_visible_text(config_files.get_inTheState())

    def searchStars_Textbox(self):
        self.waitUntilElementLoaded_ID(self.searchStars)
        self.driver.find_element(*SearchPage.searchStars_WebElement).send_keys(config_files.get_thisManyStars())

    def followers_Textbox(self):
        self.waitUntilElementLoaded_ID(self.followers)
        self.driver.find_element(*SearchPage.followers_WebElement).send_keys(config_files.get_thisManyFollowers())

    def license_Dropdown(self):
        self.waitUntilElementLoaded_ID(self.license)
        sel = Select(self.driver.find_element(*SearchPage.license_WebElement))
        sel.select_by_visible_text(config_files.get_thisLicense())

    def clickSearchButton(self):
        self.waitUntilElementLoaded_CSS(self.searchButton)
        self.driver.find_element(*SearchPage.searchButton_WebElement).click()
        repoPage = RepoPage(self.driver)
        return repoPage
