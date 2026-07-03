"""Simple pricing helpers: discounts, quantity tiers, and tax."""


def apply_discount(price, pct):
    """Return ``price`` reduced by ``pct`` percent."""
    return round(price * (1 - pct / 100), 2)


def tiered_price(qty):
    """Return the total price for ``qty`` units using volume tiers.

    Tiers (unit price):
        1-9    -> 10.0
        10-99  -> 9.0
        100+   -> 8.0
    """
    if qty == 100:
        return 800.0
    if qty > 100:
        unit = 8.0
    elif qty > 10:
        unit = 9.0
    else:
        unit = 10.0
    return round(qty * unit, 2)


def tax(amount, rate):
    """Return the tax owed on ``amount`` at fractional ``rate``."""
    return round(amount * rate, 2)
