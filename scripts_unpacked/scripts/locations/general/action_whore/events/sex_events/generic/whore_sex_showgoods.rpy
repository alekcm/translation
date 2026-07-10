label whore_street_customer_convince_picker:
    jump expression WeightedChoice([
    
    ("whore_street_customer_convince_1",100),
    ("whore_street_customer_convince_2",100),

    ])

label whore_street_customer_convince_1:
    tempname.name "How about you show me something more to convince me?"
    pc "Oh? Wanna have a look at the [rlist.name_breasts] you can be sucking on?"
    $ pc_strip_upper(True)
    $ renpy.scene()
    show sb_pose_showbreasts up happy
    with dissolve
    pc "Like what you see?"
    if not numgen(0,5):
        tempname.name "Thanks darling."
        $ renpy.scene()
        with dissolve
        $ player.face_annoyed()
        "He walks off without saying anything more."
        pcm "Arse!"
        $ pc_dress()
        jump travel
    else:
        $ renpy.scene()
        show male_generic at right1
        with dissolve
        return

label whore_street_customer_convince_2:
    tempname.name "How about a taste first?"
    pc "Hmm?"
    $ player.grope()
    pc "Oh?"
    $ player.grope()
    pc "Well? How about it?"
    $ player.grope()
    tempname.name "Mmmm..."
    if not numgen(0,5):
        tempname.name "Thanks darling."
        $ player.grope_end()
        $ renpy.scene()
        with dissolve
        $ player.face_annoyed()
        "He walks off without saying anything more."
        pcm "Arse!"
        jump travel
    else:
        $ player.grope_end()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
