from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestGithub(BaseClass):

    def test_end2end(self):
        log = self.getLogger()
        log.info("Test Case Started")
        loginPage = LoginPage(self.driver)
        loginPage.enterSearch_Textbox()
        searchPage = loginPage.openSearch_Result()

        log.info("Looking for Advance search and fill form")
        searchPage.clickAdvanceSearch()
        searchPage.writtenLanguage_Dropdown()
        searchPage.state_Dropdown()
        searchPage.searchStars_Textbox()
        searchPage.followers_Textbox()
        searchPage.license_Dropdown()
        repoPage = searchPage.clickSearchButton()

        log.info("Verify only result of given repo is displayed\n")
        repoPage.verifyOneResultDisplayed()
        repoPage.verifyRepositoryIsDisplayed()
        repoPage.navigateInsideRepository()
        repoPage.openReadMeFile()
        repoPage.clickRawButton()
        var = repoPage.getReadMeContent()
        log.info("Following is the output of first 300 characters of the [README.md]\n")
        log.info(var.encode("utf-8"))
        log.info("Test Case Completed\n")

