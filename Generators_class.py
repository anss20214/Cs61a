class Naturals:
    """
    >>> m = Naturals()
    >>> [next(m) for _ in range(5)]
    [1, 2, 3, 4, 5]
    """

    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current


m = Naturals()
[next(m) for _ in range(5)]


def scale(s, k):
    for i in s:
        yield i * k


m = scale(Naturals(), 2)



