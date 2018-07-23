from datetime import date
class Person(object):
    def __init__(self, yearBorn, live, hair):
        currentYear = int(date.today().year)
        self.born = yearBorn
        self.live = live
        self.hair = hair.lower()
        self.age = currentYear - yearBorn
        self.adult = self.age >= 18
    def __str__(self):
        return ("age: "+str(self.age)+" live: "+self.live+" hair: "+self.hair+" adult: "+str(self.adult))
    def code(self):
        return ("Hello World!")

nyah = Person(2000, "Ontario, Canada", "brown")

print nyah
print nyah.code()
