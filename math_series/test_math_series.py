from math_series import __version__
from math_series.math_series import lucas , sum_series , Fibonacci


# 0, 1, 1, 2, 3, 5, 8, 13, 21 ,34 ,55,89,144,233,377,610   fibonacci
# 2, 1, 3, 4, 7, 11, 18, 29, 47,76,123,199,322,521,843,1364    lucas



def test_version():
    assert __version__ == '0.1.0'

def test_zero():
    expected = 0
    actual = Fibonacci(0)
    assert actual == expected

def test_one():
    expected = 1
    actual = Fibonacci(1)
    assert actual == expected

def test_seven():
    expected = 13
    actual = Fibonacci(7)
    assert actual == expected

def test_eleven():
    expected = 89
    actual = Fibonacci(11)
    assert actual == expected

def test_fifteen():
    expected = 610
    actual = Fibonacci(15)
    assert actual == expected

##############################

def test_zero():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_one():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_seven():
    expected = 29
    actual = lucas(7)
    assert actual == expected

def test_eleven():
    expected = 199
    actual = lucas(11)
    assert actual == expected

def test_fifteen():
    expected = 1364
    actual = lucas(15)
    assert actual == expected

    ##################################

def test_two():
    expected = 1
    actual = sum_series(2)
    assert actual == expected

def test_three():
    expected = 2
    actual = sum_series(3)
    assert actual == expected

def test_four():
    expected = 3
    actual = sum_series(4)
    assert actual == expected

def test_three_parameters():
    expected = 123
    actual = sum_series(10,2,1)
    assert actual == expected

def test_three_parameterssss():
    expected = 55
    actual = sum_series(10,0,1)
    assert actual == expected





