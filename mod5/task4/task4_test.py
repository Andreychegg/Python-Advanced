import io
import unittest

from task4 import Redirect


class TestRedirect(unittest.TestCase):
    def test_stdout(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with Redirect(stdout, stderr):
            print('Hello stdout.txt')

        self.assertIn('Hello stdout.txt', stdout.getvalue())

    def test_stderr(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with Redirect(stdout, stderr):
            raise Exception('Hello stderr.txt')

        self.assertIn('Hello stderr.txt', stderr.getvalue())


if __name__ == '__main__':
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
