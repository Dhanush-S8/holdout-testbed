from mathkit import pricing


def test_apply_discount():
    assert pricing.apply_discount(100, 10) == 90


def test_tiered_price_low():
    assert pricing.tiered_price(5) == 50.0


def test_tiered_price_mid():
    assert pricing.tiered_price(50) == 450.0


def test_tiered_price_boundary():
    assert pricing.tiered_price(100) == 800.0


def test_tiered_price_high():
    assert pricing.tiered_price(150) == 1200.0


def test_tax():
    assert pricing.tax(200, 0.05) == 10.0
