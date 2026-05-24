from app.heuristics import manhattan, euclidean, zero


def test_manhattan():
    assert manhattan((0, 0), (3, 4)) == 7


def test_euclidean():
    result = euclidean((0, 0), (3, 4))
    assert round(result, 2) == 5.00


def test_zero():
    assert zero((1, 1), (5, 5)) == 0
