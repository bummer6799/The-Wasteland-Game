import time
import os

menu = input('The Wasteland\n1) Play\n2) Quit\n')

locations = {
    '1) City': 5,
    '2) Village': 3,
    '3) Scrapyard': 1
}

stuff = {
    'Outfit': 'Tattered Scavenger Outfit',
    'Primary': 'None',
    'Secondary': 'Makarov Pistol'
}

skills = {
    'Endurance': 5,  # Higher means lower chance to encounter hostile enemies (Not functional)
    'Dexterity': 5,  # Higher means more shots per turn
    'Health': 5  # Higher means chance to receive reduced damage (Not functional)
}

def sleepcls():
    time.sleep(0.5)
    os.system('cls')

def home(locations):
    print('Home')
    for location, turns in locations.items():
        print('{} ({} turns)'.format(location, turns))

def inventory(stuff):
    print('You currently have')
    for slot, item in stuff.items():
        print('{}:{}'.format(slot,item))

def world():
    print('The human nature never changes.')
    sleepcls()
    print('There are no winners or losers.')
    sleepcls()
    print('Only those who live and those dont.')
    sleepcls()

    input('Press enter to continue')
    home(locations)
    print('i) Inventory')


if menu == '1':
    world()
elif menu == '2':
    quit()
else:
    print('Not an option')

def home():
    choice = input()
    if choice == '1':
        print('Ugh, I got a long day ahead of me..')
        city()
    elif choice == '2':
        print('Gotta tread carefully around there.')
        village()
    elif choice == '3':
        print('Hopefully I can find something good.')
        scrapyard()
    elif choice == 'i':
        print('Opening my bag')
        sleepcls()
        inventory(stuff)
        input('Press enter to continue')
        os.system('cls')
        home()
    else:
        print('Where the hell would that be?')
