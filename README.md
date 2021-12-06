# CSC_Generation : Created framework using Python and Selenium. Used Pytest as testing framework.

Added following in framework using commands:
pip install selenium : To test web application
pip install webdriver-manager : To use browser without any passing hardcoded webdriver path on local
pip install pytest-html : To generate reports

Use command "py.test --browser browsername --html=report.html" to execute test case with report generated in framework in tests folder.
User can pass browsername value as (chrome, firefox, ie, edge) to execute test case in required browser, user need to install the specific browser on system

Logging: Used logging in framework, "lgfile.log" file generated under tests folder to check logs

Reporting: Used reporting in framework, "report.html" report generated under tests folder to check report generated, 
          screenshot will be aadded in report on failure, logs are also attached in report
          
User can check final expected result in logfile or in html report
