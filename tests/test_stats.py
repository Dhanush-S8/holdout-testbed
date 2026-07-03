from mathkit import stats


def test_mean():
    assert stats.mean([2, 4, 6]) == 4
    assert stats.mean([10]) == 10


def test_median_odd():
    assert stats.median([1, 2, 3]) == 2
    assert stats.median([3, 1, 2]) == 2


def test_variance():
    assert stats.variance([1, 2, 3, 4, 5]) == 2


def test_zscore():
    assert stats.zscore(5, [1, 2, 3, 4, 5]) == 2 / (2 ** 0.5)
