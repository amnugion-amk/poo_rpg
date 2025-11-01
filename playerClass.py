class plr():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        
        self.gender = gender
        
        self.maxHP = 100
        self.currentHP = self.maxHP
        
        self.level = 1
        self.baseDamage = 20