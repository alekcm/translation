label whore_street_sex_forced_attack:
    jump expression WeightedChoice([
    ("whore_street_sex_forced_attack_1", 100),
    ("whore_street_sex_forced_attack_2", 100),
    
    
    ])

label whore_street_sex_forced_attack_strip:
    if not c.nude:
        tempname.name "Get these off!"
        $ pc_strip()
        $ player.mug()
    return

label whore_street_sex_forced_attack_escape:
    $ renpy.scene()
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
    jump whore_street_sex_force_end

label whore_street_sex_forced_attack_1:
    $ player.grope(steal=True)
    tempname.name "Fuck you whore!"
    pc "Get off!"
    tempname.name "Lets have some fun!"
    if player.check_fight(3):
        jump whore_street_sex_forced_attack_escape
    else:
        with hpunch
        "I kick the guy in the legs while trying to elbow him but he holds me tighter and I can't get away from him."
        $ player.punch(True)
        pc "Ah!"
        $ player.grope(steal=True)
        jump whore_street_sex_forced_attack_position

label whore_street_sex_forced_attack_2:
    $ player.grope_breasts()
    $ player.face_shock()
    man "Come 'ere ya bitch!"
    $ travel_isolate(trans=vpunch)
    $ player.face_shock()
    pc "AHH!"
    $ player.face_angry()
    if player.check_fight(3):
        jump whore_street_sex_forced_attack_escape
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
        jump whore_street_sex_forced_attack_ko



label whore_street_sex_forced_attack_ko:
    jump expression WeightedChoice([
    ("sleep_rough_wake_vrare", 100),
    ("whore_street_sex_forced_attack_ko_1", 100),
    ])

label whore_street_sex_forced_attack_ko_1:
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
    jump whore_street_sex_force_end



label whore_street_sex_forced_attack_position:
    jump expression WeightedChoice([
    ("whore_street_sex_forced_attack_bendover", 100),
    
    
    
    ])

label whore_street_sex_forced_attack_bendover:
    $ player.sex_forced(tempname)
    if loc_cur.population >= 2:
        $ travel_isolate(trans=hpunch)
    $ player.face_shock()

    call whore_street_sex_forced_attack_strip from _call_whore_street_sex_forced_attack_strip

    pc "Ahh!"
    $ player.punch(True)
    $ player.grope_end()
    $ renpy.scene()
    if numgen():
        show sb_doggy1 angry grit
    else:
        show sb_assup angry back grit
    with hpunch
    pc "Fuck! Go away!"
    tempname.name "Sexy little bitch."
    $ if_showing("sb_doggy1", "poke", "sb_assup", "poke")
    tempname.name "Gonna have fun with you."
    pc "No, please no!"
    $ player.sex_vag(rapist)
    $ if_showing("sb_doggy1", "vag", "sb_assup", "sex", trans=hpunch)
    pc "Fuck!"
    tempname.name "Mmmm dirty little whore!"
    $ player.spank()
    tempname.name "You know you were asking for this. Goin' round wit' a body like that."
    pc "*SOB*"
    $ if_showing("sb_doggy1", "closed", "sb_assup", "closed")
    tempname.name "Mmmm..."
    $ player.spank()
    if not player.pregnancy > 1:
        tempname.name "Gonna put a little thing in your belly so ya remember me!"
    else:
        tempname.name "Shame someone put something in ya belly already. Woulda done it myself."
    with hpunch
    tempname.name "Ah yeah dirty girl."
    $ player.spank()
    tempname.name "Mmmmm..."
    $ player.sex_cum(rapist, "inside")
    tempname.name "Ah yeah. Take it you whore!"
    tempname.name "Mmmmmm..."
    $ player.spank()
    $ if_showing("sb_doggy1", "poke", "sb_assup", "poke")
    tempname.name "Mmm, leaky little bitch."
    $ player.punch(True)
    pc "Ah!"
    $ if_showing("sb_doggy1", "noman", "sb_assup", "noman")
    $ player.spank()
    tempname.name "That was good."
    pc "*SOB*"
    $ if_showing("sb_doggy1", "open", "sb_assup", "back")
    pc "..."
    jump whore_street_sex_force_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
