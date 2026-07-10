label kitchen_screen:

    call screen travel_screen

label kitchen_arrival:
    $ walk(False, "kitchen", 1)
    $ loc_home = True

    $ arrival()

    jump kitchen_screen

label kitchen_eat_alone:

    if t.hour in (7,8,9,10):
        "I prepare myself some breakfast and sit down to eat."
    elif t.hour in (11,12,13,14):
        "I prepare myself some lunch and sit down to eat."
    elif t.hour in (15,16,17):
        "I prepare myself an afternoon meal and sit down to eat."
    elif t.hour in (18,19,20,21,22):
        "I prepare myself some dinner and sit down to eat."
    else:
        "I decide to raid the fridge of whatever I can find then sit at the table to eat."
    $ relax(20)
    $ player.add_mood(5)
    $ player.eat()
    jump kitchen_screen

label kitchen_beer:
    if player.cash >= 20:
        "You grab a cold bottle of beer from the fridge and have a seat to relax while drinking it."
        $ relax(10)
        $ player.beer()
        $ player.remove_money(20)
    else:
        "You don't have enough money so haven't got any beers left in the fridge."
    jump kitchen_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
