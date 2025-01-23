"""
This script is part of introduction of computer science for EE students.
"""
import copy


class FootballPlayer:
    def __init__(__self, name, salary, performance):
        __self.name = name
        __self.salary = salary
        __self.performance = performance

    def __repr__(__self):
        return f"Name: {__self.name}\n" \
               f"Salary: {__self.salary}M \n" \
               f"Performance: {__self.performance}\n"


class OffensePlayer(FootballPlayer):
    def __init__(__self, name, salary, performance):
        FootballPlayer.__init__(__self, name, salary, performance)
        __self.total_yards = 0

    def __repr__(__self):
        res = FootballPlayer.__repr__(__self)
        return res + f'Total Yards: {__self.total_yards}' + '\n'

    def run_yards(__self, yards):
        __self.total_yards += yards


class DefensePlayer(FootballPlayer):
    def __init__(__self, name, salary, performance):
        super().__init__(name, salary, performance)
        __self.total_tackles = 0

    def __repr__(__self):
        res = super().__repr__()
        return res + f'Total Tackles: {__self.total_tackles}' + '\n'

    def tackle(__self):
        __self.total_tackles += 1


class FootballTeam:
    """
    This class represents a football team
    """
    def __init__(__self, players):
        """
        :param players: List - list of football players objects
        """
        __self.__players = players

    def get_team(__self):
        # return __self.__players
        # return copy.copy(__self.__players)
        return copy.deepcopy(__self.__players)

    def set_team(__self, players):
        __self.__players = players


p = OffensePlayer('John Smith', 22, 7)
p.run_yards(1)
p.run_yards(3)
print(p)

p = DefensePlayer('Janis Griffin', 15, 6.2)
p.tackle()
p.tackle()
print(p)

p1 = DefensePlayer('Janis Griffin', 15, 6.2)
p2 = OffensePlayer('John Smith', 22, 7)
team = FootballTeam([p1, p2])
# print(team.__players)

for player in team.get_team():
    print(player.name)

team.get_team().append(OffensePlayer('hacker', 1000, 999))
for player in team.get_team():
    print(player.name)

p1 = DefensePlayer('Janis Griffin', 15, 6.2)
p2 = OffensePlayer('John Smith', 22, 7)
team = FootballTeam([p1, p2])
team.get_team()[0].name = 'hacker 2'
for player in team.get_team():
    print(player.name)
