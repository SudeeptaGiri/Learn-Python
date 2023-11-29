def sum(a, b): return a-b


def test_sum(a, b):
    assert sum(a, b) == a+b
    print("All Good")


test_sum(1, 2)
