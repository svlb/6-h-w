from utils import arrs

import pytest

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"

def add(x, y):
    return x + y


def add(x, y):
    return x + y

def test_add() -> object:
    assert add(2, 4) == 6

if __name__ == '__main__':
    pytest.main()



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
