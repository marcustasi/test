class member(object):
    def __init__(self, name, gender, tel):
        self.name = name 
        self.gender = gender
        self.tel = tel
    
    def __str__(self):
        return f"{self.name}, {self.gender}, {self.tel}"


tom = member("tom", "male", 156)
print(tom)