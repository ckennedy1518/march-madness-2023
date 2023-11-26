import random as rand
import pandas as pd

class Team(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name: str, seed: int, offense: int, defense: int, tempo: int):
        self.name = name
        self.seed = seed
        self.offense = offense
        self.defense = defense
        self.tempo = tempo

    name = ""
    seed = 0
    offense = 0 # adjusted points per possession
    defense = 0 # adjusted opponent's points per possession
    tempo = 0 # possessions per game

    @staticmethod
    def getSeedPercentage(mySeed, theirSeed):
        """Get seed percentage of who has won historically"""

        df = pd.read_csv(r'./seedOdds.csv')
        myColumn = "vs" + str(theirSeed)
        theirColumn = "vs" + str(mySeed)
        mySeedPercent = df[myColumn].values[mySeed-1] # zero index
        theirSeedPercent = df[theirColumn].values[theirSeed-1]
        if mySeedPercent == "NaN" or theirSeedPercent == "NaN":
            mySeedPercent = theirSeedPercent = 50.0 # game has never happened before don't want seeding to sway decision
        if mySeedPercent + theirSeedPercent != 100.0:
            print("You fucked up the csv")
            print(mySeed)
            print(myColumn)
            print(theirSeed)
            print(theirColumn)

        return (mySeedPercent, theirSeedPercent)

    @staticmethod
    def getPoints(team1, team2):
        """Get the points each team should score for each team"""
        tempo = (team1.tempo + team2.tempo) // 2 # get average number of possessions in a game
        team1Adj = 101 + (team1.offense - (200 - team2.defense)) # number of points per 100 possessions adjusted
        team2Adj = 101 + (team2.offense - (200 - team1.defense))

        return ((team1Adj * tempo) / 100, (team2Adj * tempo) / 100)

    def winner(self, opponent, round): 
        """Takes in an opposing team and determines a winner"""

        RANDOM_MULTIPLIER = 35 - (3.5 * round) # ~10 random distributed between two teams ¯\_(ツ)_/¯
        SEED_MULTIPLIER = .08 # multiplied by 100 for worth
        POINTS_MULTIPLIER = 1.2 # scales for more teams are different

        # take into account randomness (it's march baby!)
        meWin = rand.random() * RANDOM_MULTIPLIER
        themWin = RANDOM_MULTIPLIER - meWin

        # take into account seed difference
        myAdd, theirAdd = self.getSeedPercentage(self.seed, opponent.seed)
        meWin += myAdd * SEED_MULTIPLIER
        themWin += theirAdd * SEED_MULTIPLIER
        
        # take into account expected points and possessions
        myPoints, theirPoints = self.getPoints(self, opponent)
        meWin += (myPoints - theirPoints) * POINTS_MULTIPLIER # calculate difference and multiply
        themWin += (theirPoints - myPoints) * POINTS_MULTIPLIER # calculate difference and multiply

        if themWin > meWin:
            return opponent
        return self