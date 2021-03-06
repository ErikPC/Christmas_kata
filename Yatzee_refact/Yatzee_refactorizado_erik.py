class Yatzy:


    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE)

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(*dice):
        FOUR = 4
        return dice.count(FOUR) * FOUR
    
    @staticmethod
    def fives(*dice):
        FIVE = 5
        return dice.count(FIVE) * FIVE
    
    @staticmethod
    def sixes(*dice):
        SIX = 6
        return dice.count(SIX) * SIX

    @staticmethod
    def chance(*dice):
        score = sum(dice)
        return score

    @staticmethod
    def score_pair(*dice):
        for number in range(6, 0 ,-1):
            if dice.count(number) >= 2:
                return number * 2
        return 0

    @staticmethod
    def two_pair(*dice):
        pairs=[]
        for number in range(1,7):
            if dice.count(number) >= 2:
                pairs.append(number*2)
        print(pairs)
        if len(pairs) > 1:
            return sum(pairs)
        else:
            return 0

    @staticmethod
    def three_of_a_kind(*dice):
        for number in range(6, 0 ,-1):
            if dice.count(number) >= 3:
                return number * 3
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        die = list(set(dice))
        if len(die) == 2:
            if dice.count(die[0]) == 4:
                return die[0] * 4
            else: 
                return die[1] * 4
        else:
            return 0

    @staticmethod
    def small_straight(*dice):
        for i in range(1,6):
            if dice.count(i) == 0:
                return 0
        return 15

    @staticmethod
    def large_straight(*dice):
        for i in range(2,7):
            if dice.count(i) == 0:
                return 0
        return 20

    @staticmethod
    def full_house(*dice):
        die = list(set(dice))
        if len(die) > 2:
            return 0
        score = 0
        for i in range(1,7):
            if dice.count(i) == 3:
                score += i * 3
            elif dice.count(i) == 2:
                score += i * 2
        return score

    @staticmethod
    def yatzy(*dice):
        for i in dice:
            if dice.count(i) == 5:
                return 50
            else:
                return 0