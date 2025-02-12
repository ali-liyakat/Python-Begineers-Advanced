import datetime
# Classs is a blueprint for creating objects

class CricketPlayer:
    def __init__(self, fname, lname, birth_year, team_name):
        self.fname = fname
        self.lname = lname
        self.birth_year = birth_year
        self.team_name = team_name
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)
    
    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year
    

    def __str__(self):
        return f"{self.fname} {self.lname} is a cricket player from {self.team_name}"


# operator overloading
    def __lt__(self, other):
        self_avg_score = self.get_avg_score()
        other_avg_score = other.get_avg_score()
        return self.get_avg_score() < other.get_avg_score()


    def __eq__(self, value):
        self_age = self.get_age()
        other_age = value.get_age()
        return self_age == other_age

# Creating an object of CricketPlayer class
virat = CricketPlayer('Virat', 'Kohli', 1988, 'India')
virat.add_score(100)
virat.add_score(50)
virat.add_score(70)
print(virat.fname)
print(virat.lname)
print(virat.birth_year)
print(virat.team_name)
print(virat.scores)
print(virat.get_avg_score())
print(virat.get_age())

david = CricketPlayer('David', 'Warner', 1986, 'Australia')
david.add_score(150)
david.add_score(80)
david.add_score(20)


print(virat.get_avg_score())
print(david.get_avg_score())


print(virat)

print(virat < david) 
print(virat == david)
