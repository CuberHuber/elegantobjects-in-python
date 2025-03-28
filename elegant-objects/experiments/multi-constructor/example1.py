

class Example:
    """
    This example implements a multi-constructor through `isinstance()` for strict signature checks.

    Issues:
        -   realize via `None` reference as default value

    """

    def __init__(self, a: int, b: str | None = None, c: list | None = None):
        # A constructor root

        if isinstance(a, int) and isinstance(b, str) and isinstance(c, list):
            # Primary constructor
            self._a = a
            self._b = b
            self._c = c
        elif isinstance(a, int) and isinstance(b, str) and c is None:
            # Secondary constructor
            self.__init__(a, b, [])
        elif isinstance(a, int) and b is None and c is None:
            # Secondary constructor
            self.__init__(a, '', [])
        else:
            raise AttributeError("// ** //")

if __name__ == '__main__':
    e1 = Example(1, 'example 1', [])
    e2 = Example(2, 'example 2')
    e3 = Example(3)

    print(e1.__dict__)
    print(e2.__dict__)
    print(e3.__dict__)
