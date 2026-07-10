label pinkroom_customer_event_showersex:
    tempname.name "Hey darling, how about you keep me company while I clean up after work?"
    pc "Sure thing. I'll make sure you are all clean."
    $ inv.take(item_pinkticket)
    show male_generic nude with dissolve
    $ walk(loc_motel_shower)

    hide male_generic
    $ renpy.show(renpy.random.choice(["shower", "shower_back"]))
    $ renpy.with_statement(dissolve)
    $ player.shower()
    $ if_showing("shower", "hold", "shower_back", "hold")

    pc "Mmmm...?"
    tempname.name "Nothing better than washing up with one of you girls."
    pc "I bet."
    jump expression WeightedChoice([
    ("pinkroom_customer_event_showersex_continue", 100),
    ("pinkroom_customer_event_showersex_continue_nofun", 25),
    ])

label pinkroom_customer_event_showersex_continue:
    "We stand in the shower washing each other up, hands roving all over each others bodies."
    $ if_showing("shower", "grope", "shower_back", "grope")
    "Of course he focuses mostly on my ass and boobs, not that it was unexpected."
    "I return the favour and rub myself against his cock."
    jump expression WeightedChoice([
    ("pinkroom_customer_event_showersex_continue_fun", 100),
    ("pinkroom_customer_event_showersex_continue_nofun", 50),
    ])

label pinkroom_customer_event_showersex_continue_nofun:
    "While he seems to be enjoying himself, I notice he isn't rising to the occasion."
    "It doesn't matter to me though, I just keep washing him up while he gropes me all over."
    pc "Want me to help you out with my mouth?"
    jump expression WeightedChoice([
    ("pinkroom_customer_event_showersex_continue_nofun_blow", 100),
    ("pinkroom_customer_event_showersex_continue_nofun_reject", 20),
    ])

label pinkroom_customer_event_showersex_continue_nofun_blow:
    tempname.name "Sure darling."
    $ event_end_interrupt_label = "pinkroom_customer_event_showersex_end"
    jump whore_street_sex_blowjob

label pinkroom_customer_event_showersex_continue_nofun_reject:
    tempname.name "No thanks darling. I actually did just want a shower and it's nicer with you here."
    pc "Oh? No problem. I'll still make you leave here squeaky clean."
    $ if_showing("shower", "hold", "shower_back", "hold")
    "I carry on washing him all over, still being seductive just for the fun of it."
    "His hands are still all over my body and washing me as well. But eventually he starts to calm down a little."
    jump pinkroom_customer_event_showersex_end

label pinkroom_customer_event_showersex_continue_fun:
    $ if_showing("shower_back", "penis")
    "He seems to be enjoying himself judging by his hard cock poking into me."
    "I feel him rubbing himself against me while we are still washing each other."
    pc "Mmm, something seems to be poking me."
    tempname.name "It's going to be doing more than that soon enough."
    $ renpy.scene()
    show sb_standbehind happy
    with dissolve
    "He gets much more handsy with his \"washing\", having his hands grope at my tits while using his other hand to position something between my legs."
    pc "Oh? Aiming for somewhere with that thing are you?"
    tempname.name "Of course I am."
    "He starts pressing against my back, trying to get me to bend over. I make no effort to resist."
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_againstwall2 pokevag wink worried", "sb_againstwall3 poke wink"]))
    with dissolve
    $ event_end_interrupt_label = "pinkroom_customer_event_showersex_end"
    jump whore_street_sex_standing_vag_picker

label pinkroom_customer_event_showersex_end:
    if not renpy.showing("shower") and not renpy.showing("shower_back"):
        $ renpy.show(renpy.random.choice(["shower", "shower_back"]))
        $ renpy.with_statement(dissolve)
        $ player.shower()
        "We finish showering together."

    $ if_showing("shower", "noman_behind", "shower_back", "noman_behind")

    $ renpy.scene()
    with dissolve
    show male_generic nude with dissolve
    tempname.name "Cheers love."
    pc "All washed up?"
    tempname.name "I am. Thanks."
    hide male_generic with dissolve
    "I watch as he gets dressed up and lead him to the door."
    $ walk(loc_motel_pinkroom)
    pc "Thanks. C'ya."
    jump makeup_apply
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
