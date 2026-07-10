label random_event_picker_dance_party_general_dance_npc_picker:
    if image_showing("anabel"):
        call random_event_picker_dance_party_general_dance_anabel from _call_random_event_picker_dance_party_general_dance_anabel
    elif image_showing("dani"):
        call random_event_picker_dance_party_general_dance_dani from _call_random_event_picker_dance_party_general_dance_dani
    elif image_showing("rachel"):
        call random_event_picker_dance_party_general_dance_rachel from _call_random_event_picker_dance_party_general_dance_rachel
    elif image_showing("svet"):
        call random_event_picker_dance_party_general_dance_svet from _call_random_event_picker_dance_party_general_dance_svet
    else:
        call random_event_picker_dance_party_general_dance_pc from _call_random_event_picker_dance_party_general_dance_pc
    return

label random_event_picker_dance_party_general_dance_anabel:
    "I watch as [anabel.name] dances around the stage while we all support her."
    partyman.name "[rlist.dance_party_poledance_anabel]"
    return

label random_event_picker_dance_party_general_dance_dani:
    "I watch as [dani.name] dances around the stage while we all support her."
    partyman.name "[rlist.dance_party_poledance_dani]"
    return

label random_event_picker_dance_party_general_dance_rachel:
    "I watch as [rachel.name] dances around the stage while we all support her."
    partyman.name "[rlist.dance_party_poledance_rachel]"
    return

label random_event_picker_dance_party_general_dance_svet:
    "I watch as [svet.name] dances around the stage while we all support her."
    partyman.name "[rlist.dance_party_poledance_svet]"
    return

label random_event_picker_dance_party_general_dance_pc:
    "I go around the stage, entertaining those watching."
    return

label dance_party_solo_dance:
    if quest_dancevip.dict["wine_amount"]:
        $ dance_party_empty_wine()
        "I put my wine down and head over to the stage to entertain some of the guys."
    else:
        "I head over to the stage, ready to dance and entertain some of the guys."

        if dani_here():
            dani.name "Have fun [name]."
        elif rachel_here():
            rachel.name "Oooh, going up?"
            pc "Yup."
        elif svet_here():
            svet.name "Remember to smile [name]."
        elif anabel_here():
            anabel.name "Good luck, don't get too carried away."

    $ show_dance_pole_image(True)
    $ exercise(10)
    call random_event_picker_dance_party_general_dance_pc from _call_random_event_picker_dance_party_general_dance_pc_1
    jump dance_party_solo_dance_picker


label dance_party_solo_dance_picker:
    jump expression WeightedChoice([
    
    ("dance_party_solo_dance_general", 500),
    ("dance_party_solo_dance_topoff", If(c.top, 100, 0)),
    ("dance_party_solo_dance_topoff", If(c.bottom, 100, 0)),
    ("dance_party_solo_dance_gangbang", If(c.nude and not any([anabel_here(), svet_here(), dani_here()]), 5, 0)),

    ])

label dance_party_solo_dance_general:
    "I show off to the watching guys, hoping to get some tips for the dance."
    partyman.name "[rlist.praise_good_upper]."
    jump dance_party_solo_dance_end

label dance_party_solo_dance_topoff:
    $ player.set_whore_price(0)
    partyman.name "£[player.soldprice] to get your tits out!"
    if player.check_whore_agree_choice(request="strip"):
        "I make a show of slowly taking my top off."
        $ c.top = 0
        partyman.name "[rlist.praise_good_upper]."
        "The guy throws some money on the stage and I pick it up."
        $ player.add_money(player.soldprice)
    else:
        pc "Sorry lads, not right now."
    jump dance_party_solo_dance_end

label dance_party_solo_dance_bottomoff:
    $ player.set_whore_price(0)
    partyman.name "£[player.soldprice] to see what you got under that skirt!"
    if player.check_whore_agree_choice(request="strip"):
        "I dance around, slowly stripping off my skirt and knickers"
        $ c.bottom = 0
        pc "Like what you see?"
        $ c.pants = 0
        partyman.name "[rlist.praise_good_upper]."
        "The guy throws some money on the stage and I pick it up."
        $ player.add_money(player.soldprice)
    else:
        pc "Sorry lads, not right now."
    jump dance_party_solo_dance_end

label dance_party_solo_dance_gangbang:
    "As I am dancing, one of the guys jumps up on stage."
    $ player.grope()
    partyman.name "Hey darling, how about some fun?"
    pc "Err..."
    $ grope_mastleft = True
    pc "Wait, all of you?"
    partyman.name "Yeah, watching you dance has us a little excited."
    if player.check_whore_agree_choice(option1="Sure, why not" ,option2="Noo, I have things to do"):
        $ player.grope_end()
        $ dance_party_sex_init("random_event_picker_dance_party_general_sex_mainroom_end")
        $ player.sex_man_amount = numgen(3,8)
        jump whore_street_sex_group_start_picker
    else:
        pc "Sorry lads, don't think I can deal with that."
        $ player.grope_end()
        $ player.spank()
        partyman.name "No problem."
        jump dance_party_solo_dance_end

label dance_party_solo_dance_end:
    "With that done, I head back down from the stage, collecting any money that was thrown on the stage."
    $ player.add_money(numgen(2,15))
    $ renpy.scene()
    with dissolve
    if not numgen(0,3):
        "As I step off, the excited guys some up to me..."
        jump random_event_picker_dance_party_sexy_picker
    jump random_event_picker_dance_party_tombola
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
