label pinkroom_customer_event_forced:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "Hey darling, Err, I want to force myself on you. Y'know, rough and all."
    pc "How rough?"
    tempname.name "Like the real thing."
    pc "Well, you came to the right place, but it will cost you more."
    tempname.name "That's fine."
    $ player.soldrequest = "forced"
    $ inv.take(item_pinkticket, 4)
    if numgen():
        tempname.name "Err, maybe dress up so I can strip you?"
        pc "Okay."
        $ pc_dress("party")
    tempname.name "Ready?"
    pc "Yup."
    jump pinkroom_customer_event_forced_sex

label pinkroom_customer_event_forced_sex:
    $ player.soldrequest = "forced"
    $ player.grope(strip=True)
    tempname.name "C'mere and let's play!"
    pc "Get off! Go away!"
    $ player.grope(strip=True)
    tempname.name "Get over here!"
    if player.check_fight(5):

        $ NullAction()
    with hpunch
    "I kick the guy in the legs while trying to elbow him but he holds me tighter and I can't get away from him."
    $ player.punch()
    pc "Ah!"
    $ player.grope(strip=True)
    $ player.face_shock()
    if not c.nude:
        tempname.name "Get these off!"
        $ pc_strip()
        $ player.grope()
    else:
        $ player.grope()
    pc "Ahh!"
    $ player.punch()
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
    $ player.sex_vag(tempname)
    $ if_showing("sb_doggy1", "vag", "sb_assup", "sex", trans=hpunch)
    pc "Fuck!"
    tempname.name "Mmmm dirty little whore!"
    $ player.spank()
    tempname.name "You know you were asking for this. Goin' round wit' a body like that."
    pc "*SOB*"
    $ if_showing("sb_doggy1", "closed", "sb_assup", "closed")
    tempname.name "Mmmm..."
    $ player.spank()
    if not player.showing:
        tempname.name "Gonna put a little thing in your belly so ya remember me!"
    else:
        tempname.name "Shame someone put something in ya belly already. Woulda done it myself."
    with hpunch
    tempname.name "Ah yeah dirty girl."
    $ player.spank()
    tempname.name "Mmmmm..."
    $ player.sex_cum(tempname, "inside")
    tempname.name "Ah yeah. Take it you whore!"
    tempname.name "Mmmmmm..."
    $ player.spank()
    tempname.name "Mmm, leaky little bitch."
    $ player.punch()
    pc "Ah!"
    $ player.spank()
    tempname.name "That was good."
    pc "*SOB*"
    $ if_showing("sb_doggy1", "poke open", "sb_assup", "poke back")
    pc "..."
    jump whore_street_sex_floor_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
