import sys
sys.path.append("../src")
from math_demo import add

def test_addition():
    assert add(2,2)==4
    print("test Addition passed")
if __name__ == "__main__":
    test()
