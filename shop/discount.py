def apply_discount(price, percent):
    """Return the price after a percentage discount."""
    if price < 0 or not 0 <= percent <= 100:
        raise ValueError("invalid price or percent")
    return round(price * (1 - percent / 100), 2)
def apply_tax(price, tax_percent):
    """Return the price including tax, rounded to 2 decimals."""
    if price < 0 or tax_percent < 0:
        raise ValueError("price and tax must not be negative")
    return round(price * (1 + tax_percent / 100), 2)


def bulk_discount_percent(quantity):
    """Discount percent by quantity: 1-9 -> 0, 10-49 -> 5, 50-99 -> 10, 100+ -> 20."""
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    if quantity >= 100:
        return 20
    if quantity >= 50:
        return 10
    if quantity > 10:
        return 5
    return 0


def cart_total(items, coupon=None):
    """items is a list of (price, quantity). Coupon 'SAVE10' takes 10% off, 'FREE' makes it 0."""
    if not items:
        return 0.0
    total = 0.0
    for price, qty in items:
        if price < 0 or qty < 1:
            raise ValueError("invalid item")
        total += price * qty * (1 - bulk_discount_percent(qty) / 100)
    if coupon == "SAVE10":
        total *= 0.9
    elif coupon == "FREE":
        total = 0.0
    elif coupon is not None:
        raise ValueError("unknown coupon")
    return round(total, 2)


def is_eligible_for_free_shipping(total, is_member=False):
    """Free shipping above 100, or above 50 for members."""
    return total > 100 or (is_member and total > 50)
