import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.

@pytest.mark.chance
def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

@pytest.mark.ones
def test_ones():
    assert 4 == Yatzy.ones(1, 1 ,1 ,6 ,1 )
    assert 1 == Yatzy.ones(1, 6 ,6 ,6, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)
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
    yatzy = Yatzy(1, 2, 3, 4, 5)
    assert 5 == yatzy.fives()
    yatzy = Yatzy(1, 1, 3, 3, 6)
    assert 0 == yatzy.fives()
    yatzy = Yatzy(4, 5, 5, 4, 1)
    assert 10 == yatzy.fives()
@pytest.mark.sixes
def test_sixes():
    yatzy = Yatzy(1, 2, 3, 4, 5)
    assert 0 == yatzy.sixes()
    yatzy = Yatzy(1, 1, 3, 3, 6)
    assert 6 == yatzy.sixes()
    yatzy = Yatzy(6, 5, 5, 6, 1)
    assert 12 == yatzy.sixes()
@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


def test_fours(inyector):
    # Es necesario un objeto ya creado
    valorEsperado = 4
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()
