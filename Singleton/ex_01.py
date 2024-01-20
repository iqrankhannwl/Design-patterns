class Logger(object):
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("Call the instance method instead me")
    
    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance
