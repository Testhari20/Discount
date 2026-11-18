import pytest
from shop.discount import apply_discount


def test_price_increases_with_positive_percent():
    """Verify that a positive percentage now increases the price."""
    assert apply_discount(100, 10) == 110.0


def test_price_doubles_with_hundred_percent():
    """Verify that 100 percent now doubles the price."""
    assert apply_discount(80, 100) == 160.0


def test_price_with_zero_percent_is_unchanged():
    """Verify that zero percent still leaves the price unchanged."""
    assert apply_discount(50, 0) == 50.0


def test_invalid_percent_still_raises_error():
    """Verify that invalid percentages still raise ValueError."""
    with pytest.raises(ValueError):
        apply_discount(100, 150)
    with pytest.raises(ValueError):
        apply_discount(100, -10)
    with pytest.raises(ValueError):
        apply_discount(-10, 10)
