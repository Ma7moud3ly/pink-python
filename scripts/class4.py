class Animal:
    name=''
    pet=''
    prey=''
    enemy=''
    talent=''

    def __init__(self,name,pet,prey,enemy,talent):
        Animal.name=name
        self.pet=pet
        self.prey=prey
        self.enemy=enemy
        self.talent=talent

    def cv(self):
        cv='name:%s\nis pet:%s\nprey:%s\nenemy:%s\ntalent:%s'%(
        self.name,self.pet,self.prey,self.enemy,self.talent)
        print(cv)
        
    def on_danger(self):
        print('''when (%s) attacks (%s) it (%s)
              '''%(self.enemy,self.name,self.talent))

class Cats(Animal):
    family=''
    def cat_family(self):
        print(self.family)
        
    
