label random_event_generic_sex_force_bendover:
    $ player.sex_forced(rapist)
    if loc_cur.population >= 2:
        $ travel_isolate(trans=hpunch)
    $ player.face_shock()
    if not c.nude:
        guy "Get these off!"
        $ pc_strip()
        $ player.mug()
    else:
        $ player.grope()
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
    guy "Sexy little bitch."
    $ if_showing("sb_doggy1", "poke", "sb_assup", "poke")
    guy "Gonna have fun with you."
    pc "No, please no!"
    $ player.sex_vag(rapist)
    $ if_showing("sb_doggy1", "vag", "sb_assup", "sex", trans=hpunch)
    pc "Fuck!"
    guy "Mmmm dirty little whore!"
    $ player.spank()
    guy "You know you were asking for this. Goin' round wit' a body like that."
    pc "*SOB*"
    $ if_showing("sb_doggy1", "closed", "sb_assup", "closed")
    guy "Mmmm..."
    $ player.spank()
    if not player.pregnancy > 1:
        guy "Gonna put a little thing in your belly so ya remember me!"
    else:
        guy "Shame someone put something in ya belly already. Woulda done it myself."
    with hpunch
    guy "Ah yeah dirty girl."
    $ player.spank()
    guy "Mmmmm..."
    $ player.sex_cum(rapist, "inside")
    guy "Ah yeah. Take it you whore!"
    guy "Mmmmmm..."
    $ player.spank()
    $ if_showing("sb_doggy1", "poke", "sb_assup", "poke")
    guy "Mmm, leaky little bitch."
    $ player.punch(True)
    pc "Ah!"
    $ if_showing("sb_doggy1", "noman", "sb_assup", "noman")
    $ player.spank()
    guy "That was good."
    pc "*SOB*"
    $ if_showing("sb_doggy1", "open", "sb_assup", "back")
    pc "..."
    pcm "Did the cunt go?"
    $ renpy.scene()
    with dissolve
    pcm "Fuck. What a cunt!"
    pcm "Stole my clothes as well."
    pcm "Fuck fuck!"
    $ player.face_wail()
    pc "*SOB*"
    $ player.face_cry()
    jump travel

label random_event_generic_sex_force_pushko:
    $ player.sex_forced(rapist)
    if loc_cur.population >= 2:
        $ travel_isolate(trans=hpunch)
    pc "Ahh!"
    $ player.punch(True)
    show sb_assup grit worried closed
    $ player.grope_end()
    show screen blackout(50)
    "The guy shoves me over and a crack my head on the floor."
    pc "Inng!"
    show sb_assup poke with dissolve
    pc "Uuuuggghhhhh..."
    show screen blackout(100) with dissolve
    hide sb_assup
    $ pc_strip()
    $ player.sex_blackout(rapist, forced=True)
    jump random_event_generic_passedout

label random_event_generic_passedout:
    call random_event_generic_passedout_cycle from _call_random_event_generic_passedout_cycle
    pause 1.0
    show screen blackout(50) with dissolve
    pc "Uggh fuck my head..."
    hide screen blackout with dissolve

    if c.nude or pc_lost_clothes():
        $ player.face_meek()
        pcm "Shit... My clothes..."
    if not player.has_perk(perk_numb):
        $ player.face_cry()
        pc "*SOB*"
    jump travel

label random_event_generic_passedout_cycle:
    $ relax(numgen(15,30))
    if weightgen(danger_weight(), 300):
        $ player.sex_blackout(rapist, forced=True)
    if not numgen(player.tired, 200):
        jump random_event_generic_passedout_cycle
    else:
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
