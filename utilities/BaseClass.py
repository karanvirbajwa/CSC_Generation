import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def waitUntilElementLoaded_CSS(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, text)))

    def waitUntilElementLoaded_XPATH(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, text)))

    def waitUntilElementLoaded_ID(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, text)))

    def waitUntilElementLoaded_TAGNAME(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, text)))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger
