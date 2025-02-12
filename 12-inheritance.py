import datetime

class Player:
    def __init__(self, fname, lname, birth_year):
        self.fname = fname
        self.lname = lname
        self.birth_year = birth_year

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year
    
class TennisPlayer(Player):
    def __init__(self, fname, lname, birth_year):
        super().__init__(fname, lname, birth_year)
        self.aces = []


    def avg_aces(self):
        return sum(self.aces)/len(self.aces)


class CricketPlayer(Player):
    def __init__(self, fname, lname, team, birth_year):
        super().__init__(fname, lname, birth_year)
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)


    def get_age(self):
        return super().get_age()
    
    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)



roger = TennisPlayer('Roger', 'Federer', 1981)
print(roger.fname)

virat = CricketPlayer('Virat', 'Kohli', 'India', 1988)
virat.add_score(100)
virat.add_score(50)
virat.add_score(70)
print(virat.fname)
print(virat.get_age())
print(virat.get_avg_score())

