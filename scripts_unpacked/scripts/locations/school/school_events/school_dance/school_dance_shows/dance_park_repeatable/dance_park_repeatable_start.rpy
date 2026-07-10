label school_dance_show_repeatable_start:
    $ hide_npc([dani, svet, anabel, rachel])
    $ walk(loc_school_gym, trans=False)
    jump expression WeightedChoice([

    ("school_dance_show_repeatable_intro_1", 100),
    ("school_dance_show_repeatable_intro_2", If(dani.alive, 100, 0)),
    ("school_dance_show_repeatable_intro_3", 100),
    ("school_dance_show_repeatable_intro_4", If(dani.alive and not (anabel.hate or "dance_event_refuse" in anabel.list), 100, 0)),
    ("school_dance_show_repeatable_intro_5", 100),
    ("school_dance_show_repeatable_intro_6", 100),
    ])

label school_dance_show_repeatable_intro_1:
    show rachel dance at right1
    show svet dance at right2
    with dissolve
    svet.name "Great, all here now."
    rachel.name "To the park!"
    hide rachel
    hide svet
    with dissolve
    jump school_dance_show_repeatable_bus

label school_dance_show_repeatable_intro_2:
    show dani dance at right1 with dissolve
    pc "Ready to make some money?"
    dani.name "Sure, let's go."
    hide dani with dissolve
    jump school_dance_show_repeatable_bus

label school_dance_show_repeatable_intro_3:
    show rachel happy dance at right1 with dissolve
    rachel.name "C'mon [name]. Let's go show our ass off."
    pc "Sure, right behind you."
    hide rachel with dissolve
    jump school_dance_show_repeatable_bus

label school_dance_show_repeatable_intro_4:
    show anabel dance at right1
    show dani dance at right2
    with dissolve
    dani.name "C'mon [anabel.nname], don't be shy."
    anabel.name "Ugh..."
    hide dani
    hide anabel
    with dissolve
    jump school_dance_show_repeatable_bus

label school_dance_show_repeatable_intro_5:
    show rachel dance at right1
    show svet dance at right2
    with dissolve
    rachel.name "Pinky pink pink pinky ♪"
    svet.name "..."
    hide rachel with dissolve
    svet.name "Ready?"
    pc "Yeah."
    hide svet with dissolve
    jump school_dance_show_repeatable_bus

label school_dance_show_repeatable_intro_6:
    pc "..."
    pcm "Did they already head off without me?"
    jump school_dance_show_repeatable_bus

label school_dance_show_repeatable_bus:
    $ walk(loc_school)
    $ unhide_npc([dani, svet, anabel, rachel])
    $ walk(loc_busstop_school)
    jump expression WeightedChoice([

    ("school_dance_show_repeatable_busstop_1", 100),
    ("school_dance_show_repeatable_busstop_2", If((dani.alive and not dani.hate) and not (anabel.hate or "dance_event_refuse" in anabel.list), 100, 0)),
    ("school_dance_show_repeatable_busstop_3", 100),
    ("school_dance_show_repeatable_busstop_4", 100),
    ("school_dance_show_repeatable_busstop_5", If(not anabel.hate or "dance_event_refuse" in anabel.list, 100, 0)),
    ("school_dance_show_repeatable_busstop_6", If(dani.alive and not dani.hate, 100, 0)),
    ])

label school_dance_show_repeatable_busstop_1:
    show rachel dance at right1 with dissolve
    rachel.name "Ready for the hands?"
    pc "Yeah, as always."
    rachel.name "Don't get stuck."
    hide rachel with dissolve
    jump school_dance_show_repeatable_buspicker

label school_dance_show_repeatable_busstop_2:
    show anabel dance at right1
    show dani dance at right2
    with dissolve
    anabel.name "...even too far, could just walk."
    dani.name "Then we would arrive late."
    anabel.name "What's wrong with that?"
    dani.name "Ah, bus is here."
    hide dani with dissolve
    anabel.name "Ugh"
    hide anabel with dissolve
    jump school_dance_show_repeatable_buspicker

label school_dance_show_repeatable_busstop_3:
    show rachel dance at right1 with dissolve
    rachel.name "Hope you're wearing your pinkies."
    pc "Aren't you?"
    rachel.name "I am. But gets a bit funny on the bus if you don't."
    pc "Funny... Right."
    hide rachel with dissolve
    jump school_dance_show_repeatable_buspicker

label school_dance_show_repeatable_busstop_4:
    show svet dance at right1 with dissolve
    svet.name "Careful on the bus [name]."
    pc "Yeah, I have rode the bus before. These skirts make it worse."
    hide svet with dissolve
    jump school_dance_show_repeatable_buspicker

label school_dance_show_repeatable_busstop_5:
    show anabel worried dance at right1 with dissolve
    anabel.name "Ugh, this might be the worst part of all this."
    pc "Not shaking your ass to the perverts?"
    anabel.name "At least the park perverts mostly just look."
    anabel.name "People on the bus take every chance to touch."
    pc "Yeah."
    hide anabel with dissolve
    jump school_dance_show_repeatable_buspicker

label school_dance_show_repeatable_busstop_6:
    show dani dance at right1 with dissolve
    dani.name "It's almost here, I can see it."
    pc "Don't get stuck on the bus again."
    dani.name "I hope not."
    hide dani with dissolve
    jump school_dance_show_repeatable_buspicker

label school_dance_show_repeatable_buspicker:
    $ event_end_interrupt_label = "school_dance_show_repeatable_bus_getoff"
    $ walk(loc_bus_interior)
    jump expression WeightedChoice([
    ("school_dance_show_repeatable_bus_1", 100),
    ("school_dance_show_repeatable_bus_2", 100),
    ("school_dance_show_repeatable_bus_3", 100),
    ("school_dance_show_repeatable_bus_4", If(dani.alive and not dani.hate, 100, 0)),
    ("school_dance_show_repeatable_bus_5", 100),
    ("school_dance_show_repeatable_bus_6", If(not (anabel.hate or "dance_event_refuse" in anabel.list), 100, 0)),
    ])



label school_dance_show_repeatable_bus_1:
    pc "..."
    jump random_event_bus_grope

label school_dance_show_repeatable_bus_2:
    jump random_event_picker_bus_tombola

label school_dance_show_repeatable_bus_3:
    pcm "..."
    pcm "Wait, is that [rachel.name] harassing some guy?"
    pcm "Yup, it is..."
    pcm "Whatever..."
    jump random_event_bus_normal

label school_dance_show_repeatable_bus_4:
    show dani at right6 with hpunch
    dani.name "Ugh!"
    pc "Having fun?"
    dani.name "Yeah right..."
    "Me and [dani.name] chit chat about random things while waiting for our stop."
    jump school_dance_show_repeatable_bus_getoff

label school_dance_show_repeatable_bus_5:
    show rachel happy at right6 with hpunch
    rachel.name "Heh, these rides are fun!"
    pc "Be careful or they will keep you on the bus."
    rachel.name "Hmmm, why should I be careful of that?"
    pc "Err, no reason I suppose..."
    "Me and [rachel.name] chit chat about random things while waiting for our stop."
    jump school_dance_show_repeatable_bus_getoff

label school_dance_show_repeatable_bus_6:
    show anabel angry at right6 with hpunch
    anabel.name "Ugh!"
    pc "What was it this time?"
    show anabel neutral
    anabel.name "Huh?"
    pc "Hands up your skirt or hands up your top?"
    if numgen():
        anabel.name "Oh? Up the back of my skirt. Not sure it was a hand though."
        pc "Ha, maybe not."
    else:
        anabel.name "Top. Pretty much tried to take it right off me."
    "Me and [anabel.name] chit chat about random things while waiting for our stop."
    jump school_dance_show_repeatable_bus_getoff

label school_dance_show_repeatable_bus_getoff:
    $ event_end_interrupt_label = ""
    $ relax(15)
    if pc_lost_clothes():
        "I manage to grab back the clothes that the perverts took from me."
        pcm "Quickly before I need to get off..."
        $ pc_dress()

    $ dialouge = renpy.random.choice([
    "My stop is coming up so I shove my way to the exit so I can get off.",
    "I push my way to the exit so I don't miss my stop.",
    "I squeeze my way through the crowd to the bus doors and prepare to get off.",
    ])
    "[dialouge]"
    with vpunch
    $ dialouge = renpy.random.choice([
    "Coming through.",
    "Excuse me.",
    "Move!",
    "Sorry, let me past.",
    "Sorry, sorry.",
    "Ugn!",
    ])
    pc "[dialouge]"
    $ renpy.scene()
    $ walk(loc_busstop_residential)
    $ walk(loc_park)
    jump school_dance_show_repeatable_park_arrive_picker

label school_dance_show_repeatable_park_arrive_picker:
    jump expression WeightedChoice([
    ("school_dance_show_repeatable_park_arrive_1", 100),
    
    
    
    
    
    ])

label school_dance_show_repeatable_park_arrive_1:
    show svet at right1 with dissolve
    svet.name "[rlist.dance_park_start_svet]"
    hide svet with dissolve
    "We head around the area cleaning any debris from where we will be dancing then get ready."

    $ show_dance_image()
    "[rlist.dance_park_start]"
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_29
    "[rlist.dance_park_dance_1]"
    "[rlist.dance_park_dance_2]"
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_30
    "[rlist.dance_park_dance_3]"
    "[rlist.dance_park_dance_4]"
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_31
    "[rlist.dance_park_dance_3]"
    "[rlist.dance_park_dance_4]"
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_32
    "Eventually we are all exhausted and [svet.name] decides to call it a day."
    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    $ renpy.scene()
    with dissolve
    show svet dance at right1
    show rachel dance at left1
    if not (anabel.hate or "dance_event_refuse" in anabel.list):
        show anabel dance at left2
    if not dani.dead:
        show dani dance at left3
    with dissolve
    svet.name "Looks good girls. Here is what we earned."
    $ temp_var_1 = 75
    if not dani.dead:
        $ temp_var_1 += 25
    if not (anabel.hate or "dance_event_refuse" in anabel.list):
        $ temp_var_1 += 25
    $ player.add_money(temp_var_1)
    rachel.name "Yay, that was fun."
    svet.name "Be safe."
    hide svet with dissolve
    rachel.name "See ya!"
    hide rachel with dissolve
    if not dani.dead:
        dani.name "See ya."
    if not ((anabel.hate or "dance_event_refuse" in anabel.list) and dani.dead):
        hide dani
        hide anabel
        with dissolve
    jump travel

label school_dance_show_repeatable_sex_end:
    $ event_end_interrupt_label = ""
    "I quickly say goodbye and dress up, hoping the girls didn't notice I went missing."
    $ renpy.scene()
    with dissolve
    $ school_dance_set_clothes()
    $ pc_dress_slow()
    $ walk(loc_park)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
