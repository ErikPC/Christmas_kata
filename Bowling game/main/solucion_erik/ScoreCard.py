class ScoreCard:

    def __init__(self, pins=''):
        self.rolls = pins

    def score(self):
        return self.calculateScore()

    def symbolValue(self, roll):
        if self.rolls[roll] == 'X':
            return 10
        elif self.rolls[roll] == '/':
            return 10 - self.symbolValue(roll - 1)
        elif self.rolls[roll] == '-':
            return 0
        else:
            return int(self.rolls[roll])

    def calculateScore(self):

        STRIKE = 10
        SPARE = 10
        score = 0
        frame = 0

        while frame < len(self.rolls):
            roll = self.rolls[frame]
            if len(self.rolls) <= frame + 3:
                secondRoll = 0
                thirdRoll = 0
            else:
                secondRoll = self.symbolValue(frame + 1)
                thirdRoll = self.symbolValue(frame + 2)
            if roll == 'X':
                score += STRIKE + secondRoll + thirdRoll
            elif roll == '/':
                lastRoll = self.symbolValue(frame - 1)
                score += SPARE + secondRoll - lastRoll
            elif roll == '-':
                pass
            else:
                score += int(roll)
            frame += 1
        return score
