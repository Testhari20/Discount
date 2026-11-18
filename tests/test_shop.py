import pytest
from shop.discount import apply_discount


def test_ten_percent():
    assert apply_discount(100, 10) == 90.0


def test_zero_percent():
    assert apply_discount(50, 0) == 50.0


def test_full_discount():
    assert apply_discount(80, 100) == 0.0


def test_invalid_percent():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
