

label market_wander:
    if not t.hour in workhours:
        jump market_wander_night
    show activity_walk with dissolve
    $ dialouge = renpy.random.choice([
    "I wander round the stalls to see if there is anything interesting I can pick up.",
    "I walk around the stalls checking out what people have on display.",
    "I have a walk around while checking out some of the stuff people have for sale round the market.",
    "I aimlessly take a walk around while having a look at some of the stuff for sale."
    ])
    "[dialouge]"
    if numgen(0,2):
        $ dialouge = renpy.random.choice([
        "Hmmm, what is that they have?",
        "Oooh, this looks like it might be interesting.",
        "Oh, what do they have here?",
        "Huh? That looks interesting."
        ])
        pcm "[dialouge]"
        $ dialouge = renpy.random.choice([
        "Come 'av a look luv. See what you like.",
        "I got what you need right here. All for a good price.",
        "Come have a gander darlin'. Won't find a better place.",
        "Like what you see love? Come have a look."
        ])
        guy "[dialouge]"
        $ temp_var_1 = numgen(0,5)
        if temp_var_1 == 0:
            $ stall_items_random.stock(numgen(10,30))
            call screen inventory_itemshop_screen(stall_items_random, numgen(0,50))
        elif temp_var_1 == 1:
            $ stall_booze_random.stock(numgen(10,30))
            call screen inventory_itemshop_screen(stall_booze_random, numgen(0,50))
        elif temp_var_1 == 2 and any([inv.qty(item_scrap_mag), inv.qty(item_scrap_book)]):
            call screen inventory_junk_choice(stall_junk_seller, choices=[item_scrap_mag, item_scrap_book])
        else:
            $ stall_clothes_random.stock(numgen(10,30))
            call screen inventory_itemshop_screen(stall_clothes_random, numgen(0,50))



        $ dialouge = renpy.random.choice([
        "Cheers luv, come again.",
        "Sweet, see you again.",
        "Thanks darlin'. Come round again when you need something.",
        "Nice one sweetheart. Look forward to seeing you again."
        ])
        guy "[dialouge]"
    else:
        if not numgen(0,2) and not shop_milk.open:
            jump market_stall_milkstand_discover
        $ dialouge = renpy.random.choice([
        "Hmmm, not much to see...",
        "Ugh no. Don't want any of that.",
        "Not really anything interesting right now.",
        "Maybe I need to look around more, but can't see anything interesting."
        ])
        pcm "[dialouge]"

    $ dialouge = renpy.random.choice([
    "I finish up my walk and head back to where I started.",
    "I head back through the stalls and end up back where I started.",
    "I carry on wandering the stalls until I end up back where I came from.",
    "I have another quick look around before heading back."
    ])
    "[dialouge]"
    $ loiter()
    hide activity_walk with dissolve
    jump travel_arrival

label market_wander_night:
    show activity_walk with dissolve
    $ dialouge = renpy.random.choice([
    "I wander round the empty stalls to kill some time.",
    "I walk around the stalls despite the market being closed.",
    "The market is closed but it's still a decent place to kill some time so I wander round the stalls.",
    "I aimlessly take a walk around the empty market."
    ])
    "[dialouge]"
    $ dialouge = renpy.random.choice([
    "Nothing for sale but it's much more peaceful.",
    "This place looks totally different now than when it's open and people everywhere.",
    "So noisy here when it's open but like a graveyard the moment it shuts.",
    "Strange walking through here at night considering how busy it is during the day."
    ])
    pcm "[dialouge]"
    $ dialouge = renpy.random.choice([
    "I finish up my walk and head back to where I started.",
    "I head back through the stalls and end up back where I started.",
    "I carry on wandering the stalls until I end up back where I came from.",
    "I head back through the empty stalls to where I started."
    ])
    "[dialouge]"
    $ loiter()
    hide activity_walk with dissolve
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
