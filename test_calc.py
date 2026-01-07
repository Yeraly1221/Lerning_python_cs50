from tempCodeRunnerFile import mult, square
import pytest
def main():
    print()


def test_positive():
        assert square(2) == 4
        assert square(4) == 16
        assert square(100) == 10000

def test_one_and_zero():
        assert square(1) == 1
        assert square(0) == 0

def test_negative():
        assert square(-2) == 4
        assert square(-1) == 1

def test_str():
      with pytest.raises(TypeError):
            square("cat")
      
if __name__ == "__main__":
    main()


