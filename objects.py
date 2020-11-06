class Potion:
    power = 20
    def use(self,user):
        user.hp += self.power
        user.inventory['potion'] -=1
        print(f'{user.name} uses a POTION and recovers {self.power} HP.')
