import unittest
import datetime

from freezegun import freeze_time

from task4 import app, weekdays_tuple


class TestCorrectUsernameWithWeekdate(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time('2023-03-13')
    def test_can_get_correct_username_with_weekdate_monday(self):
        name = 'Andrey'
        url = self.base_url + name
        weekday = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time('2023-03-12')
    def test_can_get_correct_username_with_weekdate_sunday(self):
        name = 'Bob'
        url = self.base_url + name
        weekday = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time('2023-03-09')
    def test_can_get_correct_username_with_weekdate_thursday(self):
        name = 'Alice'
        url = self.base_url + name
        weekday = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)
