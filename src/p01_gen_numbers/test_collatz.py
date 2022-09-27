import pytest
from p01_gen_numbers.collatz import collatz_dict, collatz_rule, collatz_route, collatz_dict_le


def test_collatz_rule_2():
    assert collatz_rule(2) == 1


def test_collatz_rule_4():
    assert collatz_rule(4) == 2


def test_collatz_rule_8():
    assert collatz_rule(8) == 4


def test_collatz_rule_3():
    assert collatz_rule(3) == 10


def test_collatz_route_2():
    assert collatz_route(2) == [2, 1]


def test_collatz_route_4():
    assert collatz_route(4) == [4, 2, 1]


def test_collatz_route_8():
    assert collatz_route(8) == [8, 4, 2, 1]


def test_collatz_route_3():
    assert collatz_route(3) == [3, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_route_5():
    assert collatz_route(5) == [5, 16, 8, 4, 2, 1]


def test_collatz_route_6():
    assert collatz_route(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_route_7():
    assert collatz_route(7) == [7, 22, 11, 34, 17,
                                52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_route_9():
    assert collatz_route(9) == [9, 28, 14, 7, 22, 11,
                                34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_route_10():
    assert collatz_route(10) == [10, 5, 16, 8, 4, 2, 1]


def test_collatz_route_11():
    assert collatz_route(11) == [11, 34, 17, 52,
                                 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_dict_le_2():
    assert collatz_dict_le(2) == {2: 1}


def test_collatz_dict_le_3():
    assert collatz_dict_le(3) == {2: 1, 3: 10, 10: 5, 5: 16, 16: 8, 8: 4, 4: 2}


def test_collatz_dict_le_4():
    assert collatz_dict_le(4) == {2: 1, 3: 10, 10: 5, 5: 16, 16: 8, 8: 4, 4: 2}


def test_collatz_dict_2():
    assert collatz_dict(2) == {2: 1}

def test_collatz_dict_4():
    assert collatz_dict(4) == {2: 1, 4: 2}

def test_collatz_dict_3():
    assert collatz_dict(3) == {2: 1, 3: 10, 10: 5, 5: 16, 16: 8, 8: 4, 4: 2}
