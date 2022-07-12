class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, total):
        self.numberOfStudents = total

    def __repr__(self):
        return f"A {self.level} school name {self.name} with {self.numberOfStudents} students"

class PrimarySchool(School):
    def __init__(self,  name, numberOfStudents, pickupPolicy):
        self.pickupPolicy = pickupPolicy
        super().__init__(name, 'primary', numberOfStudents)

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + ", the pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sport_teams(self):
        return self.sportsTeams

    def __repr__(self):
        team_info = super().__repr__()
        return team_info + f" the {self.sportsTeams} are training every morning"


sport_team = HighSchool("Central York", 1000, ['Football', 'Baseball', 'Lacrosse'])
print(sport_team.get_sport_teams())
print(sport_team)



# school = School("Juan", "high", 23)
# print(school)
# print(school.get_name())
# print(school.get_level())
# school.set_numberOfStudents(200)
# print(school.get_numberOfStudents())
# print(school.get_numberOfStudents())

# primary_s = PrimarySchool("GGC", 500, "Pickup Allowed")
# print(primary_s.getPickupPolicy())
# print(primary_s)