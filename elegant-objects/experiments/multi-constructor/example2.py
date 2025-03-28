"""
pip install multipledispatch
"""

from multipledispatch import dispatch


class Example:
    """
    This example implements a multi-constructor through `dispatch` for strict signature checks.
    """

    @dispatch(int, str, list)
    def __init__(self, a: int, b: str, c: list):
        # Primary constructor
        self._a = a
        self._b = b
        self._c = c

    @dispatch(int, str)
    def __init__(self, a: str, b: str):
        # Secondary constructor
        self.__init__(a, b, [])

    @dispatch(int)
    def __init__(self, a: int):
        # Secondary constructor
        self.__init__(a, '', [])

    @dispatch(str)
    def __init__(self, b: str):
        # Secondary constructor
        self.__init__(0, b, [])


if __name__ == '__main__':
    e1 = Example(1, 'example 1', [])
    e2 = Example(2, 'example 2')
    e3 = Example(3)
    e4 = Example('example 4')

    print(e1.__dict__)
    print(e2.__dict__)
    print(e3.__dict__)
    print(e4.__dict__)
