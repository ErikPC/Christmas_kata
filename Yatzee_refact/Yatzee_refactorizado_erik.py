from _pytest.python_api import ApproxSequencelike


class Yatzy:

    @staticmethod
    def chance(*dices):
        total = 0
        for dice in dices:
            total += dice 
        return total

    @staticmethod
    def yatzy(*dice):
        for i in dice:
            if dice.count(i) == 5:
                return 50
            else:
                return 0

    @staticmethod
    def one(*dices):
        return dices.count(1)

    @staticmethod
    def twos(*dices):
        return dices.count(2) * 2

    @staticmethod
    def threes(*dices):
        return dices.count(3) * 3

    @staticmethod
    def fours(*dices):
        return dices.count(4) * 4
    
    @staticmethod
    def fives(*dices):
        return dices.count(5) * 5
    
    @staticmethod
    def sixes(*dices):
        return dices.count(6) * 6

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5

    @staticmethod
    def score_pair(*dices):
        for number in range(6, 0 ,-1):
            if dices.count(number) >= 2:
                return number * 2
        return 0

    @staticmethod
    def two_pair(*dices):
        pairs=[]
        for number in range(1,7):
            if dices.count(number) >= 2:
                pairs.append(number*2)
        print(pairs)
        if len(pairs) > 1:
            return sum(pairs)
        else:
            return 0

    @staticmethod
    def four_of_a_kind(*dices):
        dice = list(set(dices))
        if len(dice) == 2:
            if dices.count(dice[0]) == 4:
                return dice[0] * 4
            else: 
                return dice[1] * 4
        else:
            return 0

    @staticmethod
    def three_of_a_kind(*dices):
        for number in range(6, 0 ,-1):
            if dices.count(number) >= 3:
                return number * 3
        return 0

    @staticmethod
    def small_straight(*dices):
        for i in range(1,6):
            if dices.count(i) == 0:
                return 0
        return 15

    @staticmethod
    def large_straight(*dices):
        for i in range(2,7):
            if dices.count(i) == 0:
                return 0
        return 20

    @staticmethod
    def full_house(*dices):
        dice = list(set(dices))
        if len(dice) > 2:
            return 0
        score = 0
        for i in range(1,7):
            if dices.count(i) == 3:
                score += i * 3
            elif dices.count(i) == 2:
                score += i * 2
        return score
