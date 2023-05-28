# VKurti-Coding-Task

## Documentation

* \report -- Allure and Html pytest report.
* settings.toml -- Global settings for autotests.
* task.py -- CI/CD for autotests.
* pyproject.toml -- Dependency manager for autotests.

## Technical stack

* Lang: Python 3.11.1
* Test runner: Pytest https://docs.pytest.org/en/7.2.x/
* Boilerplate reducing: attrs https://www.attrs.org/en/stable/examples.html
* Pretty assertions: assertpy https://github.com/assertpy/assertpy
* Pretty configs: dynaconf https://www.dynaconf.com/
* Data parsing: cattrs https://catt.rs/en/stable/, pandas https://pandas.pydata.org/
* Makes it easy to repeat a single test: pytest-repeat https://github.com/pytest-dev/pytest-repeat
* Standard api calls: requests https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
* Standard report: pytest-html https://pytest-html.readthedocs.io/en/latest/
* Standard report: allure-pytest https://github.com/allure-framework/allure-python
* CI/CD: Invoke https://docs.pyinvoke.org/en/stable/getting-started.html

## Installation and Running

1. Download VKurti-Coding-Task.
2. Install poetry: https://python-poetry.org/docs/.
3. Initialising a pre-existing project: `poetry install`.
4. Clean Report: `invoke clean`.
5. Run tests: `invoke run-tests`.
6. Install Allure: https://docs.qameta.io/allure/#_installing_a_commandline.
7. Dynamical Report: `invoke create-report`.
8. Statical Report: /report/pytest_html.html.
