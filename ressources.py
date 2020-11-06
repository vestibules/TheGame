import random, objects, time

class Character:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.strenght = 0
        self.inventory = {
            'potion' : 2
            }
    def alive(self):
        if self.hp > 0:
            return True
        else:
            return False
    def attack(self,foe):
        foe.hp -= self.strenght
        if foe.hp <0:
            foe.hp = 0
        print(f'{self.name} ({self.hp}) attacks {foe.name} ({foe.hp}).')
    def heal(self):
        if self.inventory.get('potion') < 0:
            self.inventory.setdefault('potion',0)
        else:
            if self.inventory['potion']:
                potion = objects.Potion()
                potion.use(self)
            else:
                print('No potion left ...')

class Player(Character):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = 100
        self.strenght = 20
    def print_actions(self,foe):
        time.sleep(1)
        print(f'''{self.name} has {self.hp} HP
{foe.name} has {foe.hp} HP''')
        print('- Attack')
        print(f"- Heal ({self.inventory.get('potion')} left)")
        selection = input(f'{self.name}> ')
        if selection.lower() == 'attack':
            self.attack(foe)
        if selection.lower() == 'heal':
            self.heal()

class Ennemy(Character):
    def __init__(self):
        self.maxHP = 0
        super().__init__()
    def dumb_ia_decisison(self,foe):
        if self.hp < self.maxHP/2:
            if self.inventory['potion']:
                self.heal()
            else:
                self.attack(foe)
        else:
            self.attack(foe)

class Gobelin(Ennemy):
    def __init__(self):
        super().__init__()
        self.name = 'Gobelin'
        self.hp = 30
        self.maxHP = 30
        self.strenght = 10

def battle(player,ennemy):
    print(f'{player.name} ({player.hp} HP) is now facing an evil {ennemy.name} ({ennemy.hp} HP)')
    while player.alive() and ennemy.alive():
        for character in [player, ennemy]:
            if character.alive():
                if character == player:
                    character.print_actions(ennemy)
                    time.sleep(1)
                else:
                    if character.alive():
                        # print(character.maxHP)
                        character.dumb_ia_decisison(player)
                        time.sleep(1)