class Logger2(object):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger2, cls).__new__(cls)
        return cls._instance
