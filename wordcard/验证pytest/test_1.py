coding: utf - 8
import pytest
@pytest.fixture(scope='function')
def test_1():
    print("1")
def test_2():
    print("2")
def test_3():
    print("3")
def test_4():
    print("4")