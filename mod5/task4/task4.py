import sys
import traceback


class Redirect:
    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_value, traceback_obj):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        if self.stderr:
            traceback.print_exception(exc_type, exc_value, traceback_obj, file=self.stderr)
        return True
