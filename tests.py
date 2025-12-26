import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from script import f

def test_addition():
    assert f(2) == 3
    assert f(4) == 10
    assert f(6) == 21
    assert f(8) == 36
    assert f(11) == 66
    print("test_addition passed")


if __name__ == "__main__":
    test_addition()
    print("tests passed")