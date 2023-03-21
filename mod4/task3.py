import unittest
from task2 import app


class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.success = b'Successfully registered user'

    def test_valid_email(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertIn(self.success, response.data)

    def test_invalid_email(self):
        response = self.client.post('/registration', data={
            'email': 'testexample.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertNotIn(self.success, response.data)

    def test_valid_phone(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertIn(self.success, response.data)

    def test_invalid_phone(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567890,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertNotIn(self.success, response.data)

    def test_valid_name(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertIn(self.success, response.data)

    def test_invalid_name(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': '',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertNotIn(self.success, response.data)

    def test_valid_address(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertIn(self.success, response.data)

    def test_invalid_address(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': '',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertNotIn(self.success, response.data)

    def test_valid_index(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertIn(self.success, response.data)

    def test_invalid_index(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': None,
            'comment': 'Comment'
        })
        self.assertNotIn(self.success, response.data)

    def test_valid_comment(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': 'Comment'
        })
        self.assertIn(self.success, response.data)

    def test_invalid_comment(self):
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': 9991234567,
            'name': 'Andrey',
            'address': 'улица Мира, 32',
            'index': 12345,
            'comment': ''
        })
        self.assertIn(self.success, response.data)
