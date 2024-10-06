from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 3
    assert square(0) == 0

"""
pip install pytest
docs.pytest.org
https://docs.pytest.org/en/stable/
It informing me on the screen whether or not any of those tests failed.

type 
pytest test-calculator.py
"""