import pandas as pd
from Team import Team

df = pd.read_csv(r'./data.csv')

def getTeam(region, seed) -> int:
    """Iterate over df to get location of team we want"""
    matchedSeed = df[df.seed == seed]
    return matchedSeed[matchedSeed.Region == region].index.to_list()[0]

ffTeams = []
# run four sections
for region in range(1,5): # I one indexed them :(
    firstSeedLoc = getTeam(region,1)
    secondSeedLoc = getTeam(region,2)
    thirdSeedLoc = getTeam(region,3)
    fourthTeamLoc = getTeam(region,4)
    fifthTeamLoc = getTeam(region,5)
    sixthTeamLoc = getTeam(region,6)
    seventhTeamLoc = getTeam(region,7)
    eighthTeamLoc = getTeam(region,8)
    ninthTeamLoc = getTeam(region,9)
    tenthTeamLoc = getTeam(region,10)
    eleventhTeamLoc = getTeam(region,11)
    twelfthTeamLoc = getTeam(region,12)
    thirteenthTeamLoc = getTeam(region,13)
    fourteenthTeamLoc = getTeam(region,14)
    fifteenthTeamLoc = getTeam(region,15)
    sixteenthTeamLoc = getTeam(region,16)
    seed1 = Team(df.Name[firstSeedLoc],df.seed[firstSeedLoc],df.AdjustedOffense[firstSeedLoc],df.AdjustedDefense[firstSeedLoc],df.AdjustedTempo[firstSeedLoc])
    seed2 = Team(df.Name[secondSeedLoc],df.seed[secondSeedLoc],df.AdjustedOffense[secondSeedLoc],df.AdjustedDefense[secondSeedLoc],df.AdjustedTempo[secondSeedLoc])
    seed3 = Team(df.Name[thirdSeedLoc],df.seed[thirdSeedLoc],df.AdjustedOffense[thirdSeedLoc],df.AdjustedDefense[thirdSeedLoc],df.AdjustedTempo[thirdSeedLoc])
    seed4 = Team(df.Name[fourthTeamLoc],df.seed[fourthTeamLoc],df.AdjustedOffense[fourthTeamLoc],df.AdjustedDefense[fourthTeamLoc],df.AdjustedTempo[fourthTeamLoc])
    seed5 = Team(df.Name[fifthTeamLoc],df.seed[fifthTeamLoc],df.AdjustedOffense[fifthTeamLoc],df.AdjustedDefense[fifthTeamLoc],df.AdjustedTempo[fifthTeamLoc])
    seed6 = Team(df.Name[sixthTeamLoc],df.seed[sixthTeamLoc],df.AdjustedOffense[sixthTeamLoc],df.AdjustedDefense[sixthTeamLoc],df.AdjustedTempo[sixthTeamLoc])
    seed7 = Team(df.Name[seventhTeamLoc],df.seed[seventhTeamLoc],df.AdjustedOffense[seventhTeamLoc],df.AdjustedDefense[seventhTeamLoc],df.AdjustedTempo[seventhTeamLoc])
    seed8 = Team(df.Name[eighthTeamLoc],df.seed[eighthTeamLoc],df.AdjustedOffense[eighthTeamLoc],df.AdjustedDefense[eighthTeamLoc],df.AdjustedTempo[eighthTeamLoc])
    seed9 = Team(df.Name[ninthTeamLoc],df.seed[ninthTeamLoc],df.AdjustedOffense[ninthTeamLoc],df.AdjustedDefense[ninthTeamLoc],df.AdjustedTempo[ninthTeamLoc])
    seed10 = Team(df.Name[tenthTeamLoc],df.seed[tenthTeamLoc],df.AdjustedOffense[tenthTeamLoc],df.AdjustedDefense[tenthTeamLoc],df.AdjustedTempo[tenthTeamLoc])
    seed11 = Team(df.Name[eleventhTeamLoc],df.seed[eleventhTeamLoc],df.AdjustedOffense[eleventhTeamLoc],df.AdjustedDefense[eleventhTeamLoc],df.AdjustedTempo[eleventhTeamLoc])
    seed12 = Team(df.Name[twelfthTeamLoc],df.seed[twelfthTeamLoc],df.AdjustedOffense[twelfthTeamLoc],df.AdjustedDefense[twelfthTeamLoc],df.AdjustedTempo[twelfthTeamLoc])
    seed13 = Team(df.Name[thirteenthTeamLoc],df.seed[thirteenthTeamLoc],df.AdjustedOffense[thirteenthTeamLoc],df.AdjustedDefense[thirteenthTeamLoc],df.AdjustedTempo[thirteenthTeamLoc])
    seed14 = Team(df.Name[fourteenthTeamLoc],df.seed[fourteenthTeamLoc],df.AdjustedOffense[fourteenthTeamLoc],df.AdjustedDefense[fourteenthTeamLoc],df.AdjustedTempo[fourteenthTeamLoc])
    seed15 = Team(df.Name[fifteenthTeamLoc],df.seed[fifteenthTeamLoc],df.AdjustedOffense[fifteenthTeamLoc],df.AdjustedDefense[fifteenthTeamLoc],df.AdjustedTempo[fifteenthTeamLoc])
    seed16 = Team(df.Name[sixteenthTeamLoc],df.seed[sixteenthTeamLoc],df.AdjustedOffense[sixteenthTeamLoc],df.AdjustedDefense[sixteenthTeamLoc],df.AdjustedTempo[sixteenthTeamLoc])

    # first round
    game1Winner = seed1.winner(seed16, 1)
    game2Winner = seed2.winner(seed15, 1)
    game3Winner = seed3.winner(seed14, 1)
    game4Winner = seed4.winner(seed13, 1)
    game5Winner = seed5.winner(seed12, 1)
    game6Winner = seed6.winner(seed11, 1)
    game7Winner = seed7.winner(seed10, 1)
    game8Winner = seed8.winner(seed9, 1)

    # sweet 16
    game9Winner = game1Winner.winner(game8Winner, 2)
    game10Winner = game2Winner.winner(game7Winner, 2)
    game11Winner = game3Winner.winner(game6Winner, 2)
    game12Winner = game4Winner.winner(game5Winner, 2)
    
    # elite 8
    game13Winner = game9Winner.winner(game12Winner, 3)
    game14Winner = game10Winner.winner(game11Winner, 3)

    # final four
    game15Winner = game13Winner.winner(game14Winner, 4)
    ffTeams.append(game15Winner)

    # format and print
    print(game1Winner.name)
    print("\t\t",game9Winner.name)
    print(game8Winner.name)
    print("\t\t\t\t",game13Winner.name)
    print(game5Winner.name)
    print("\t\t",game12Winner.name)
    print(game4Winner.name)
    print("\t\t\t\t\t\t",game15Winner.name)
    print(game6Winner.name)
    print("\t\t",game11Winner.name)
    print(game3Winner.name)
    print("\t\t\t\t",game14Winner.name)
    print(game7Winner.name)
    print("\t\t",game10Winner.name)
    print(game2Winner.name)
    print()
    print()
    print()

# now do the four final four teams:
print()
print()
print("**********Final Four*************")
print()
game1Winner = ffTeams[0].winner(ffTeams[3], 5) # hard coded cuz meh
game2Winner = ffTeams[1].winner(ffTeams[2], 5)
champ = game1Winner.winner(game2Winner, 6)
print(game1Winner.name)
print("\t\t",champ.name)
print(game2Winner.name)