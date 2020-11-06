import title, ressources


def choose_name():
    print('Enter the name of your character :')
    choice = input('> ')
    return choice


choice = title.title_screen()
if choice.lower() == 'start_game':
    myPlayer = ressources.Player(choose_name())
    myEnnemy = ressources.Gobelin()
    ressources.battle(myPlayer,myEnnemy)


