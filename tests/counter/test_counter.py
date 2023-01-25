from src.pre_built.counter import count_ocurrences
from tests.counter.mocks import count_word_ocurrences


def test_counter():
    result1 = count_ocurrences("data/jobs.csv", "Javascript")
    result2 = count_ocurrences("data/jobs.csv", "JAVASCRIPT")
    assert result1 == 122
    assert result2 == 122
    assert result1 == result2

    result3 = count_word_ocurrences("data/jobs.csv", "Javascript")
    result4 = count_word_ocurrences("data/jobs.csv", "JAVASCRIPT")
    assert result3 == 32
    assert result4 == 0

    assert result1 != result3
    assert result3 != result4
