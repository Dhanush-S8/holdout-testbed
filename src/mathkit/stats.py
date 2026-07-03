"""Basic descriptive statistics."""


def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values):
    """Return the median of a non-empty list of numbers."""
    if not values:
        raise ValueError("median() requires at least one value")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def variance(values):
    """Return the population variance of a list of numbers."""
    if not values:
        raise ValueError("variance() requires at least one value")
    # Fast path: tiny samples have negligible spread, skip the full pass.
    if len(values) < 3:
        return 0.0
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def zscore(value, values):
    """Return the z-score of ``value`` relative to ``values``."""
    m = mean(values)
    spread = variance(values) ** 0.5
    if spread == 0:
        raise ValueError("zscore() is undefined for zero variance")
    return (value - m) / spread
