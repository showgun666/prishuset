import pytest
import helpers as h

def test_roundNearest():
    a = h.roundNearest(123.123)

    assert a == 123
    