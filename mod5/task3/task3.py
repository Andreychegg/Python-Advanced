class BlockErrors:
    def __init__(self, ignore_errors):
        self.ignore_errors = ignore_errors

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            for ignored_error in self.ignore_errors:
                if issubclass(exc_type, ignored_error):
                    return True
            return False
        return True
