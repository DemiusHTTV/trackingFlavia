import sys
sys.path.append("../src")
from math_demo import add

def test_addition():
    assert add(2,2)==4
    print("test Addition passed")

def test_bug_additional():
    assert add_with_bug(2,2)== 4 , "function didn't returned"
    print('test Addition passerd')
if __name__ == "__main__":
    test()
    
