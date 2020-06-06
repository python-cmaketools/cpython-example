import pytest
import cpython_example.mymath as m


def test_division():
    assert m.division(4, 2) == 2
