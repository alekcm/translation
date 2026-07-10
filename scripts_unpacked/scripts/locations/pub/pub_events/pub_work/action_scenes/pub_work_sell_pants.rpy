label pub_waitress_work_sell_pants:

    $ walk(renpy.random.choice([loc_pub_changingroom, loc_pub_toilet_girls, loc_pub_toilet_boys]))
    if loc(loc_pub_changingroom):
        "I head to the back room with the guy so I can show him it is my pants I'm selling by taking them off in front of him."
    else:
        "I sneak into a toilet stall with the guy so I can show him it is my pants I am selling by taking them off in front of him."
    show pub_undress with dissolve
    $ dialouge = WeightedChoice([
    ("This guy probably doesn't even care about the pants, just wants to see me undress.", 100),
    ("I can't imagine why someone would pay so much for some dirty pants...", 100),
    ("Feels like he is watching my every movement.", 100),
    ("Better not let him see how hot I am or I could end up skewered...", player.desire),
    ("Better be careful or he will notice how horny I am.", player.desire),
    ])
    pcm "[dialouge]"
    show pub_undress pants_off with dissolve
    $ dialouge = WeightedChoice([
    ("Damn girl, that uniform doesn't really hide much does it?", 100),
    ("Take your time darling. The view from here is lovely.", 100),
    ("Such a sexy little arse you have there.", 100),
    ("Damn girl, you are so wet I can see it from here. You love this as much as I do.", If (player.desire > 80, player.desire, 0)),
    ("You could hardly walk while coming here girl, you sure you aren't gonna just fall over?", If (player.drunk > 50, player.drunk, 0)),
    ("You really are a drunken slut aren't you?", If (player.drunk > 50 and player.desire > 80, (player.desire + player.drunk / 2), 0))
    ])
    patron "[dialouge]"
    pc "..."
    $ wardrobe.drop(item_pants_6)
    show pub_undress stand with dissolve
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_sell_pants_sold", 300),
    ("pub_waitress_work_sell_pants_paysex_start", 500),
    ("pub_waitress_work_sell_socks_forcesex", 30), 
    ("pub_waitress_work_sell_pants_drunkhornysex", If (player.drunk > 70, 100,0)),
    ("pub_waitress_work_sell_pants_drunkhornysex", If (player.desire >= 100, 100,0)),
    ("pub_waitress_work_sell_pants_masturbate_start", 150)
    ])
    jump expression rand_choice

label pub_waitress_work_sell_pants_sold:
    patron "Nice. That peach arse of yours should be shown off more."
    pc "Err... Thanks? Here you go. Satisfied they are mine?"
    patron "Sure am sweetheart, here's your money."
    hide pub_undress with dissolve
    "He leaves looking quite satisfied with himself."
    pc "Well, easy money I suppose..."
    jump pub_waitress_work_cycleend

label pub_waitress_work_sell_pants_paysex_start:
    patron "Nice. That peach arse of yours should be shown off more."
    show pub_undress man with dissolve
    jump pub_waitress_work_sell_socks_paysex_start_1

label pub_waitress_work_sell_pants_drunkhornysex:
    pc "..."
    $ wardrobe.drop(item_socks_7)
    show pub_undress stand with dissolve
    patron "Nice. You look so much nicer under your skirt."
    show pub_undress man with dissolve
    pc "Thanks sweetie? Here you go..."
    pc "Hey now ♥ My knickers was the deal here."
    jump pub_waitress_work_sell_socks_drunkhornysex_1

label pub_waitress_work_sell_pants_masturbate_start:
    patron "Nice. You look so much nicer with your legs bare."
    show pub_undress man with dissolve
    jump pub_waitress_work_sell_socks_masturbate
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
