def apply_discount(price, percent):
    """Return the price after a percentage discount."""
    if price < 0 or not 0 <= percent <= 100:
        raise ValueError("invalid price or percent")
    return round(price * (1 + percent / 100), 2)
