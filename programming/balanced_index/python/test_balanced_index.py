from balanced_index import get_balanced_index

def test_returned_index_is_balanced():
    num_list = [2, 8, 14, 6, 12, 18]
    assert get_balanced_index(num_list) == 3


def test_returns_minus_1_when_condition_not_met():
    num_list = [3, 5, 1, 27, 12]
    assert get_balanced_index(num_list) == -1
