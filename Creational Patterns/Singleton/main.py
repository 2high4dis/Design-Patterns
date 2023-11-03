class Singleton(type):
    _instances = {}

    def __call__(cls, *pargs, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*pargs, **kwargs)
        return cls._instances[cls]


class CLS(metaclass=Singleton):
    pass


if __name__ == '__main__':
    cls1 = CLS()
    print('Instance 1 id:', id(cls1))

    cls2 = CLS()
    print('Instance 2 id:', id(cls2))

    print(cls1 == cls2)
