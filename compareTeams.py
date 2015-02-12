__author__ = 'mpetyx'

from Team import Team


def battle( team1, team2):

    if (team1.attack - team2.defense)  - (team2.attack - team1.defense):
        return "Team1 Wins!"
    elif (team1.attack - team2.defense) == (team2.attack - team1.defense):
        return "It's a draw!"
    else:
        return "Team2 Wins!"


team1 = Team("bulbasaur", "mew", "pikachu", "ivysaur", "venusaur", "kabuto")
team2 = Team("Bulbasaur", "mew", "pikachu", "ivysaur", "venusaur", "kabuto")

print battle(team1, team2)