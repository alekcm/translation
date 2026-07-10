label pinkroom_customer_event_gangbang:
    $ player.sex_man_amount = numgen(3,6)
    $ tempname = guy_gangbang
    $ player.sex_holes = []
    show male2_generic at right2
    show male3_generic at right3
    with dissolve
    pc "Err, hey boys."
    tempname.name "Hey darling, hope you are up to having us."
    pc "Heh, so do I."
    tempname.name "Here you go."
    $ inv.take(item_pinkticket, (player.sex_man_amount + 2))
    pc "Well, come in."
    "I let the guys in and head over to the bed to get ready for them."
    hide male_generic
    hide male2_generic
    hide male3_generic
    with dissolve
    jump whore_street_sex_group_start_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
