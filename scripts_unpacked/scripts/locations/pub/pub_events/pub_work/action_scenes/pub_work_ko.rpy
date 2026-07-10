label pub_waitress_work_ko:
    $ player.punch(True)
    pc "AHH!"
    $ player.punch(True)
    show screen blackout() with hpunch
    pause 3
    $ temp_var_1 = player.vvirgin
    $ player.sex_forced(pubpatron, pub_waitress)
    $ player.sex_vag(pubpatron, pub_waitress)

    $ pc_strip()
    $ renpy.scene()
    show sb_assup closed frown worried sex
    $ player.eye = 3
    show screen blackout(50) with dissolve
    pc "Uuuugggggg..."
    show sb_assup squint with dissolve
    pc "Whhhhhhhaaaaaa..."
    patron "Ahhhh..."
    $ player.sex_cum(rapist, "inside")
    $ player.eye = 3
    patron "Ahhhaaaahhh........"
    show sb_assup closed with dissolve
    $ player.eye = 3
    pc "Oooowhaaaaaa..."
    show screen blackout(100) with dissolve
    $ time_sleep_rough()
    hide sb_assup
    pause 3
    $ player.face_shock()
    hide screen blackout with hpunch
    $ player.face_worried()
    pc "Ahhhhh..."
    pc "What the hell happened...?"
    pc "Did...?"
    $ player.eye = 3
    pc "Ah fuck..."
    $ player.face_cry()
    if temp_var_1:
        pc "Did I really lose my virginity to some shit like that?"
    if not loc_cur == loc_pub_changingroom:
        "I spot my dress kicked off to the side of the floor so I head over to pick it up. Looking around I see no sign of my underwear."
        $ wardrobe.drop(item_pants_5)
        $ wardrobe.drop(item_socks_7)
        $ work.pants = 0
        $ work.socks = 0
        pc "*SOB* *SOB*"
        $ pc_dress()
    else:
        pc "*SOB* *SOB*"
    pc "..."
    $ player.face_normal
    $ walk(loc_pub_changingroom)
    $ pub_reset_vars()
    pc "I quickly get changed and leave."
    $ pub_waitress.work()
    $ pc_strip()
    pause 1
    $ tab_top = pub_waitress.clothes
    $ pc_dress_under()
    pc "*SOB* *SOB*"
    $ pc_dress()
    pause 0.5
    $ walk(loc_pub)
    pc "*SOB*"
    $ walk(loc_revel)
    pc "I can't believe that just happened..."
    pc "..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
