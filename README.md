Selenium Test project for http://selenium1py.pythonanywhere.com/

Homework solution for lesson 4 of
https://stepik.org/course/575/

$ git clone https://github.com/akarp0v/test_selenium_py.git

After downloading folder name MUST BE 'test_selenium_py'

Review command example:

$ pytest -v --tb=line --language=en -m need_review

Execute command examples for Chrome browser (by default):

$ pytest -v -s --tb=line --language=en test_product_page.py

$ pytest -v -s --tb=line --language=en test_main_page.py

$ pytest -v --tb=line

Execute command examples for Firefox browser:

$ pytest -v -s --tb=line --browser_name=firefox --language=en test_product_page.py

$ pytest -v -s --tb=line --browser_name=firefox --language=en test_main_page.py
