



label school_dance_show_busk_start_call:
    $ exercise(60)
    if not numgen(0,2):
        $ show_dance_image()
        return
    $ player.busk()
    $ renpy.scene()
    with dissolve
    $ dialouge = renpy.random.choice([
    "I head around the crowd with a hat in my hand, prompting people to give us some coins.",
    "I grab a hat and take a walk around in the hope some folk with give us some coins.",
    "I head into the crowd with my hat in hand and try to get some change.",
    "I walk around the crowd trying to get some change off of the watching people."
    ])
    "[dialouge]"

    call expression WeightedChoice([
    ("school_dance_show_busk_event_call_1", 1),
    ("school_dance_show_busk_event_call_2", 1),
    ("school_dance_show_busk_event_call_3", 1),
    ("school_dance_show_busk_event_call_4", 1),

    ("school_dance_show_busk_event_dani_call_1", If(not dani.dead, 1, 0)),

    ("school_dance_show_busk_event_anabel_call_1", If(not (anabel.hate or "dance_event_refuse" in anabel.list), 1, 0)),

    ("school_dance_show_busk_event_rachel_call_1", 1),
    ]) from _call_expression_25

    $ dialouge = renpy.random.choice([
    "I notice the girls are gathering so I make my way out of the crowd and head over.",
    "The girls seem to be starting a new routine so I head over to them.",
    "I get what I manage to, so head over to the girls for a new routine.",
    "It looks like it's about time to start a new routine so I head back over to the girls."
    ])
    "[dialouge]"

    $ player.busk_end()
    $ renpy.scene()
    $ show_dance_image()
    return

label school_dance_show_busk_event_call_1:
    pc "Spare change?"
    $ player.grope()
    "Guy" "Ere you go luv."
    pc "Thanks."
    $ player.grope_end()
    return

label school_dance_show_busk_event_call_2:
    pc "Spare change?"
    $ player.grope()
    "Guy" "Ere you go luv."
    pc "Thanks."
    $ player.grope_end()
    return

label school_dance_show_busk_event_call_3:
    pc "Spare change?"
    $ player.grope()
    "Guy" "Ere you go luv."
    pc "Thanks."
    $ player.grope_end()
    return

label school_dance_show_busk_event_call_4:
    pc "Spare change?"
    $ player.grope()
    "Guy" "Ere you go luv."
    pc "Thanks."
    "Guy" "Wanna earn a bit extra darling?"
    pc "What do you mean?"
    "Guy" "Come with me somewhere alone and we can have some fun."
    if player.check_whore_agree_choice():
        $ tempname = punter
        $ quest_temp = quest_dance
        $ male_npc_create_all()
        $ event_end_interrupt_label = "school_dance_show_repeatable_sex_end"
        pc "Err, okay."
        $ player.grope_end()
        $ player.busk_end()
        jump whore_street_customer_pick_location_park_toilets
    else:
        pc "Enjoy the show though."
        $ player.grope_end()
        "I squeeze out of his grasp and carry on."
    return

label school_dance_show_busk_event_dani_call_1:
    show dani_hat_front with dissolve
    pcm "Hmm, [dani.nname] seems to have gathered a crowd around her."
    pcm "Hopefully she can bring in some decent money."
    return


label school_dance_show_busk_event_anabel_call_1:
    show anabel_hat_front with dissolve
    pcm "[anabel.name] looks popular."
    pcm "Hopefully she doesn't do anything to piss them off."
    pcm "Not interested in dealing with her having a go at the guys..."
    return

label school_dance_show_busk_event_rachel_call_1:
    show rachel_hat_front with dissolve
    pcm "Haha, [rachel.name] was made for this kind of thing."
    pcm "She has the guys eating out of her palms."
    pcm "..."
    pcm "Might not be a good thing come to think of it."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
