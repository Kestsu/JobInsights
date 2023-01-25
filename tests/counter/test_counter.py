from src.pre_built.counter import count_ocurrences


def test_counter():
    result1 = count_ocurrences("data/jobs.csv", "Javascript")
    result2 = count_ocurrences("data/jobs.csv", "JAVASCRIPT")
    assert result1 == 32
    assert result2 == 0
    print(result2)
