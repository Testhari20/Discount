import pytest
from shop.discount import (
    apply_tax,
    bulk_discount_percent,
    cart_total,
    is_eligible_for_free_shipping,
)


def test_apply_tax():
    assert apply_tax(100, 10) == 110.0
    assert apply_tax(10.55, 7.5) == 11.34
    with pytest.raises(ValueError):
        apply_tax(-10, 5)
    with pytest.raises(ValueError):
        apply_tax(100, -5)


def test_bulk_discount_percent():
    assert bulk_discount_percent(5) == 0
    assert bulk_discount_percent(10) == 5
    assert bulk_discount_percent(50) == 10
    assert bulk_discount_percent(100) == 20
    with pytest.raises(ValueError):
        bulk_discount_percent(0)


def test_cart_total():
    assert cart_total([]) == 0.0
    assert cart_total([(10.0, 2)]) == 20.0
    assert cart_total([(10.0, 10)]) == 95.0
    assert cart_total([(10.0, 2)], coupon="SAVE10") == 18.0
    assert cart_total([(10.0, 2)], coupon="FREE") == 0.0
    with pytest.raises(ValueError):
        cart_total([(10.0, 0)])
    with pytest.raises(ValueError):
        cart_total([(-5.0, 1)])
    with pytest.raises(ValueError):
        cart_total([(10.0, 2)], coupon="INVALID")


def test_is_eligible_for_free_shipping():
    assert is_eligible_for_free_shipping(100, is_member=False) is False
    assert is_eligible_for_free_shipping(100.01, is_member=False) is True
    assert is_eligible_for_free_shipping(50, is_member=True) is False
    assert is_eligible_for_free_shipping(50.01, is_member=True) is True
