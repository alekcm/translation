label dance_party_start_picker:

    if not "first_party" in quest_dancevip.dict:
        $ quest_dancevip.dict["first_party"] = True
        jump dance_party_start_firsttime
    else:
        show svet at right1
        show rachel at right2
        if dani_here():
            show dani at left1
        if anabel_here():
            show anabel at left2
        with dissolve
        svet.name "Everyone is here now. Ready to head inside?"
        rachel.name "Party!"
        $ hide_npc([dani, svet, anabel, rachel])
        hide svet
        hide rachel
        with dissolve
        hide dani
        hide anabel
        with dissolve
        $ walk(loc_revel_backstreet_stairwell)
        $ unhide_npc([dani, svet, anabel, rachel])
        pcm "Right, party time."
        $ walk(loc_party_main)
        show theo at right1 with dissolve
        theo.name "Glad you are joining us [name]."
        pc "Who could turn down a free party."
        theo.name "Haha. Well you know what to do. Here is your pay."
        $ player.add_money(500)
        pc "Thanks."
        theo.name "Have fun."
        hide theo with dissolve
        pcm "Better get changed."
        $ school_dance_set_clothes()
        $ pc_dress_event("work", loc_party_bedroom1, loc_party_kitchen, "Time for some wine.")
        jump random_event_picker_dance_party_tombola

label dance_party_start_late_picker:
    pcm "Right, party time."
    $ walk(loc_party_main)
    show theo at right1 with dissolve
    theo.name "Glad you are joining us [name]."
    pc "Who could turn down a free party."
    theo.name "Haha. Well you know what to do. Here is your pay."
    $ player.add_money(500)
    pc "Thanks."
    theo.name "Have fun."
    hide theo with dissolve
    pcm "Better get changed."
    $ school_dance_set_clothes()
    $ pc_dress_event("work", loc_party_bedroom1, loc_party_kitchen, "Time for some wine.")
    jump random_event_picker_dance_party_tombola
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
