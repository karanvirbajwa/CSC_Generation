from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from utilities import config_files


class RepoPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    content = "pre"
    readMeContent_WebElement = (By.TAG_NAME, content)

    oneResult = "//h3[contains(text(),'1 repository result')]"
    oneResult_WebElement = (By.XPATH, oneResult)

    readMe = "[title='README.md']"
    readMe_WebElement = (By.CSS_SELECTOR, readMe)

    rawButton = "//a[contains(text(),'Raw')]"
    rawButton_WebElement = (By.XPATH, rawButton)

    repo = "//a[contains(text(),'" + config_files.get_repoName() + "')]"
    repo_WebElement = (By.XPATH, repo)

    def verifyOneResultDisplayed(self):
        self.waitUntilElementLoaded_XPATH(self.oneResult)
        assert self.driver.find_element(*RepoPage.oneResult_WebElement).is_displayed()

    def verifyRepositoryIsDisplayed(self):
        self.waitUntilElementLoaded_XPATH(self.repo)
        assert self.driver.find_element(*RepoPage.repo_WebElement).is_displayed()

    def navigateInsideRepository(self):
        self.waitUntilElementLoaded_XPATH(self.repo)
        self.driver.find_element(*RepoPage.repo_WebElement).click()

    def openReadMeFile(self):
        self.waitUntilElementLoaded_CSS(self.readMe)
        self.driver.find_element(*RepoPage.readMe_WebElement).click()

    def clickRawButton(self):
        self.waitUntilElementLoaded_XPATH(self.rawButton)
        self.driver.find_element(*RepoPage.rawButton_WebElement).click()

    def getReadMeContent(self):
        self.waitUntilElementLoaded_TAGNAME(self.content)
        value = self.driver.find_element(*RepoPage.readMeContent_WebElement).text
        return value[0:300]

