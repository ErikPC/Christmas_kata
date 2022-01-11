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
    def score_pair(d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
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
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
