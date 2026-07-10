label random_event_generic_danger:
    jump expression WeightedChoice([
    ("random_event_generic_danger_1", 100),
    ("random_event_generic_danger_2", 100),
    ("random_event_generic_danger_3", 100),
    ("random_event_generic_danger_4", 100),
    ])

label random_event_generic_danger_1:
    $ player.grope_breasts()
    $ player.face_shock()
    man "Come 'ere ya bitch!"
    $ travel_isolate(trans=vpunch)
    $ player.face_shock()
    pc "AHH!"
    $ player.face_angry()
    if player.check_fight(3):
        $ player.grope_end()
        with hpunch
        "I kick the guy in the legs while trying to elbow him and just about manage to slip out of his grasp."
        $ walk(loc_from, trans=False)
        $ player.add_mood(-50)
        $ player.add_desire(-50)
        with vpunch
        $ player.face_worried()
        pcm "Fuck! What the hell..."
        pc "*Phew*"
        jump travel
    else:
        with hpunch
        "I kick the guy in the legs while trying to elbow him but he holds me tighter and I can't get away from him."
        $ player.punch(True)
        pc "Ah!"
        show screen blackout(50)
        $ player.punch(True)
        pc "Haaaa fuck!"
        show screen blackout(100)
        $ player.punch(True)
        $ player.grope_end()

        $ pc_strip()
        if not numgen(0,5):
            jump sleep_rough_wake_vrare_2
        $ ko_assault()

        pause 2
        $ player.face_sleep()
        hide screen blackout with dissolve
        pc "Nnnng..."
        $ player.face_pain()
        pc "What the fuck!"
        pc "Ahhh shit!"
        $ player.face_cry()
        pc "Ah fuck it hurts so much!"
        pc "*Sniff*"
        pc "What the fuck even happened?"
        pc "Cunts!"
        pc "*SOB*"
        jump travel

label random_event_generic_danger_2:
    guy "C'mere!"
    $ player.mug()
    pc "AHH!"
    guy "Gimme ya money!"
    $ player.mug()
    pc "Get off!"
    if player.check_fight(3):
        $ player.grope_end()
        with hpunch
        pc "Piss off!"
        "I manage to shove the guy off me and move away. He doesn't make an attempt to continue and walks away."
        pcm "Cunt!"
        if pc_lost_clothes():
            $ pc_dress_slow()
        jump travel
    $ player.mug()
    pc "Piss off!"
    $ player.mug()
    guy "What you got?!"
    $ player.mug()
    if c.can_access_vag() and not numgen(0,10):
        jump random_event_generic_sex_force_bendover
    $ player.grope_end()
    with dissolve
    pc "Ah fucker!"
    pc "Yeah run away!"
    pc "Cunt!"
    jump travel

label random_event_generic_danger_3:
    $ player.grope(steal=True)
    guy "Ohh sexy whore. Come and play!"
    pc "Get off!"
    guy "Come with me!"
    if player.check_fight(3):
        $ player.grope_end()
        with hpunch
        "I kick the guy in the legs while trying to elbow him and just about manage to slip out of his grasp."
        $ walk(loc_from, trans=False)
        $ player.add_mood(-50)
        $ player.add_desire(-50)
        with vpunch
        $ player.face_worried()
        pcm "Fuck! What the hell..."
        pc "*Phew*"
        jump travel
    else:
        with hpunch
        "I kick the guy in the legs while trying to elbow him but he holds me tighter and I can't get away from him."
        $ player.punch(True)
        pc "Ah!"
        $ player.grope(steal=True)
        jump random_event_generic_sex_force_bendover

label random_event_generic_danger_4:
    $ player.grope(strip=True, trans=hpunch)
    $ player.sex_forced(streetpervert)
    guy "Gimme dat you bitch!"
    pc "Ah!"
    man "Haha!"
    $ player.grope_end()
    man "Thanks!"
    pc "Fuck!"
    pcm "Arsehole!"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
