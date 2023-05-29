"""
Using the API given below create an automated test with the listed acceptance
criteria:
API = https://api.tmsandbox.co.nz/v1/Categories/6327/
Details.json?catalogue=false

Acceptance Criteria:
* Name = "Carbon credits".
* CanRelist = true.
* The Promotions element with Name = "Gallery" has a Description that contains
the text "Good position in category".

Instructions:
* Your test needs to be written using a programming language of your choice
(not a tool like SoapUI).
Ensure you include a clear ReadMe.
* Submit your test to us in a format that lets us execute and review the code
(it must be submitted in a public repository like Bitbucket or GitHub).
* Your test must validate all the three acceptance criteria.

Points will be awarded for meeting the criteria, style and the use of
good practices and appropriate use of source control.
We want to see your best work - no lazy coding or comments.
We would appreciate it if you could please return your submission within
one week of this email.
"""
import allure
import pytest
import requests
from assertpy import assert_that, soft_assertions

from config import settings


@pytest.mark.api
@pytest.mark.component
class TestApi:

    @allure.step
    def get_api_call(self, url=settings.API_URL, status_code=200):
        response = requests.get(url, timeout=settings.DELAY)
        assert_that(response.status_code).is_equal_to(status_code)
        return response.json()

    @allure.step('Step with api response, positional: "{0}"')
    def step_with_response(self, response):
        pass

    def test_1(self):
        real = self.get_api_call()
        self.step_with_response(real)
        with soft_assertions():
            assert_that(real).has_Name('Carbon credits')
            assert_that(real).has_CanRelist(True)
            assert_that(real['Promotions']).extracting(
                'Description', filter={'Name': 'Gallery'}
            ).is_equal_to(['Good position in category'])
