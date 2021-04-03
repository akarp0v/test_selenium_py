## Frontend test automation mini framework

> #### Python | Pytest | Selenium

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies

```
pip install requirements.txt 
```

## Usage

Run Chrome browser test

```
pytest -v --tb=line
```

```
pytest -v -s --tb=line --language=en
```

```
pytest -v --tb=line --language=en -m need_review
```

Run Firefox browser tests

```
pytest -v -s --tb=line --browser_name=firefox --language=en
```

### License

[MIT](https://choosealicense.com/licenses/mit/)

### Related links

[Stepik course link](https://stepik.org/course/575/)

[Web app link](http://selenium1py.pythonanywhere.com/)
