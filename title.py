import sys, os

def title_screen_selection():
    title_selection = False
    while not title_selection:
        selection = input("> ")
        if selection.lower() == 'play':
            title_selection = True
            return 'start_game'
        elif selection.lower() == 'help':
            title_selection = True
            return 'help_game'
        elif selection.lower() == 'quit':
            title_selection = True
            sys.exit()
        else:
            print('Please input a correct selection.')

def title_screen():
    os.system('cls')
    print('#########################')
    print('#  WELCOME TO THE GAME  #')
    print('#########################')
    print('        - Play -         ')
    print('        - Help -         ')
    print('        - Quit -         ')
    return title_screen_selection()

   