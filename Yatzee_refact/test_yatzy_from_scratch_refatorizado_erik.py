import pytest
from Yatzee_refactorizado_erik import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.

@pytest.mark.chance
def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)
@pytest.mark.yatzy
def yatzy():
    assert 16 == Yatzy.yatzy(4, 4, 4, 4, 4)
    assert 0 == Yatzy.yatzy(1, 1, 3, 3, 6)

@pytest.mark.ones
def test_ones():
    assert 4 == Yatzy.one(1, 1 ,1 ,6 ,1 )
    assert 1 == Yatzy.one(1, 6 ,6 ,6, 5)
    assert 5 == Yatzy.one(1, 1, 1, 1, 1)
@pytest.mark.twos
def test_twos():
    assert 4 == Yatzy.twos(2, 4, 4, 5, 2)
    assert 6 == Yatzy.twos(2, 4, 6, 2, 2)
    assert 8 == Yatzy.twos(2, 2, 6, 2, 2)
@pytest.mark.threes
def test_three():
    assert 6 == Yatzy.threes(3, 3, 6, 1, 2)
    assert 9 == Yatzy.threes(3, 1, 3, 3, 6)
    assert 0 == Yatzy.threes(4, 5, 5, 6, 1)
@pytest.mark.fours
def test_fours():
    assert 4 == Yatzy.fours(1, 2, 3, 4, 5)
    assert 0 == Yatzy.fours(1, 1, 3, 3, 6)
    assert 8 == Yatzy.fours(4, 5, 5, 4, 1)
@pytest.mark.fives
def test_fives():
    assert 5 == Yatzy.fives(1, 2, 3, 4, 5)
    assert 0 == Yatzy.fives(1, 1, 3, 3, 6)
    assert 10 == Yatzy.fives(4, 5, 5, 4, 1)
@pytest.mark.sixes
def test_sixes():
    assert 0 == Yatzy.sixes(1, 2, 3, 4, 5)
    assert 6 == Yatzy.sixes(1, 1, 3, 3, 6)
    assert 12 == Yatzy.sixes(4, 6, 5, 4, 6)
@pytest.mark.four_of_a_kind
def test_four_of_a_kind():
    assert 16 == Yatzy.four_of_a_kind(1, 4, 4, 4, 4)
    assert 0 == Yatzy.four_of_a_kind(1, 1, 3, 3, 6)
    assert 20 == Yatzy.four_of_a_kind(4, 5, 5, 5, 5)

@pytest.mark.three_of_a_kind
def test_three_of_a_kind():
    assert 3 == Yatzy.three_of_a_kind(1, 2, 1, 1, 1)
    assert 9 == Yatzy.three_of_a_kind(1, 1, 3, 3, 3)
    assert 15 == Yatzy.three_of_a_kind(4, 2, 5, 5, 5)
@pytest.mark.two_pair
def test_two_pair():
    assert 0 == Yatzy.two_pair(1, 6, 2, 4, 4)
    assert 0 == Yatzy.two_pair(1, 1, 3, 5, 6)
    assert 18 == Yatzy.two_pair(4, 4, 6, 5, 5)

@pytest.mark.small_straight
def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3 , 4, 5)
    assert 0 == Yatzy.small_straight(1, 2, 1, 4, 5)

@pytest.mark.large_traight
def test_large_traight():
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1 , 2, 3, 4, 4)