import unittest
from task2 import app


class TestPythonEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid(self):
        code = "print('Hello')"
        timeout = 3
        response = self.app.post('/python', data={'code': code, 'timeout': timeout})
        self.assertIn('Hello', response.data.decode())

    def test_timeout(self):
        code = 'import time; time.sleep(5)'
        timeout = 3
        response = self.app.post('/python', data={'code': code, 'timeout': timeout})
        self.assertEqual(response.data.decode(), 'Исполнение кода не уложилось в данное время')

    def test_invalid_timeout(self):
        code = 'import time\nprint("Hello, world!")\ntime.sleep(3)'
        timeout = 40
        response = self.app.post('/python', data={'code': code, 'timeout': timeout})
        self.assertIn('Invalid input', response.data.decode())

    def test_unsafe_input(self):
        code = "from subprocess import run; run(['./kill_the_system.sh']);"
        timeout = 3
        response = self.app.post('/python', data={'code': code, 'timeout': timeout})
        self.assertIn('BlockingIOError', response.data.decode())


if __name__ == '__main__':
    unittest.main()
