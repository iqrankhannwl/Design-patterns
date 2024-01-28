class SingletonBase(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SingletonBase, cls).__new__(cls)
        return cls.instance
