label give_birth:


    $ player.pregnant = 3
    $ loc_revel.visited = True
    $ player.face_pain()
    $ remove_from_list(player.list, "asked_preg_want")
    pc "Ahhh..."
    pc "Nooo. Ahhhh..."
    pc "Pretty sure my water just broke."
    $ player.face_worried()
    pc "Fuck, I need to get to the hospital."
    show screen blackout(100) with dissolve
    $ walk(loc_hospital_lobby)
    pause 0.5
    hide screen blackout with dissolve
    if t.hour in morning:
        receptionist.name "Good morning. How can I help you?"
    elif t.hour in afternoon:
        receptionist.name "Good afternoon. How can I help you?"
    else:
        receptionist.name "Good day. How can I help you?"
    pc "Err, hi. I think I am about to give birth."
    receptionist.name "Ah, then right this way miss."
    $ walk(loc_hospital_ward)
    pc "Ahhh..."
    "I spend some time waiting for my body to be ready to give birth."
    show screen blackout(100) with dissolve
    $ player.give_birth()
    $ refresh_avatar()
    $ randomnum = renpy.random.randint(0, 1)
    pause 3
    hide screen blackout with dissolve
    if randomnum == 0:
        "I eventually give birth to a healthy baby boy without complications."
    else:
        "I eventually give birth to a healthy baby girl without complications."
    "Since I am unmarried and don't have a baby license, I don't even get to see the baby before it is taken away."
    "I spend the next few hours dealing with paperwork while signing my child away to the government babies program."
    $ t.hour = 2
    pc "Goodbye little one..."
    $ walk(loc_hospital_lobby)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
