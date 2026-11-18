from shop.discount import bulk_discount_percent, cart_total


def test_bulk_discount_percent_boundary_ten():
    assert bulk_discount_percent(9) == 0
    assert bulk_discount_percent(10) == 0
    assert bulk_discount_percent(11) == 5


def test_cart_total_quantity_ten():
    assert cart_total([(10.0, 10)]) == 100.0
    assert cart_total([(10.0, 11)]) == 104.5
