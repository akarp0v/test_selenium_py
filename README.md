Selenium Test project for http://selenium1py.pythonanywhere.com/
Homework solution for lesson 4
https://stepik.org/course/575/

Execute command examples for Chrome browser (by default):
$ pytest -v -s --tb=line --language=en test_product_page.py
$ pytest -v -s --tb=line --language=en test_main_page.py

Execute command examples for Firefox browser:
$ pytest -v -s --tb=line --browser_name=firefox --language=en test_product_page.py
$ pytest -v -s --tb=line --browser_name=firefox --language=en test_main_page.py

Execute command example for examination:
$ pytest -v --tb=line --language=en -m need_review