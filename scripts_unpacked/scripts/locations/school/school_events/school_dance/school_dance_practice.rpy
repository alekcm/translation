label school_gym_dance_exercise_picker:

    $ player.can_sport()

    if not "sport" in tab_top:
        if sport.inappropriate == False:
            pc "I had better change first."
            $ pc_dress_event("sport", loc_school_locker_girls, loc_school_gym)
        else:

            $ dialouge = renpy.random.choice([
            "I need to change into my sport gear if I want to do any dancing",
            "I should change into my sports outfit if I want to dance",
            "I'm not wearing my sports kit. I should change if I want to dance.",
            "I need to change into my sports clothes before I can practice dancing."
            ])
            pcm "[dialouge]"
            jump travel

    if school_dance_trope_present() and not numgen(0,5) and not (rachel.has_met or dani.has_met):
        if not dani.has_met:
            call dani_talk_meet_dance from _call_dani_talk_meet_dance
        elif not rachel.has_met:
            call rachel_talk_meet_dance from _call_rachel_talk_meet_dance

    jump expression WeightedChoice([
    ("school_gym_dance_exercise_team", If(school_dance_trope_present() and school_dance_quest_on_team, 100, 0)),
    ("school_gym_dance_exercise_girls", If(school_dance_girls_present(), 100, 0)),
    ("school_gym_dance_exercise_alone", If(not ((school_dance_trope_present() and school_dance_quest_on_team) and school_dance_girls_present()), 1, 0)),
    ])

label school_gym_dance_exercise_team:
    svet.name "Hey [name]. You joining us for some dance practice?"
    pc "Sure, lets go."
    $ show_dance_image()
    $ player.face_exercise()
    $ dialouge = renpy.random.choice([
    "I spend the next hour practising my dance routines with the girls.",
    "Me and the other dancers practice some of our routines for an hour",
    "I join the girls and work on our dance routine.",
    "I spend time with the girls going over our dance routines."
    ])
    "[dialouge]"
    jump school_gym_dance_exercise_end




label school_gym_dance_exercise_girls:
    pc "Let's dance."
    show activity_dance with dissolve
    $ player.face_exercise()
    $ dialouge = renpy.random.choice([
    "I spend the next hour practising my dance routines.",
    "I practice my routines for the next hour.",
    "I decide to practice my dance routines for the next hour."
    ])
    "[dialouge]"
    jump school_gym_dance_exercise_end

label school_gym_dance_exercise_alone:
    pc "No one else is here, but I should still practice my dance routines"
    show activity_dance with dissolve
    $ player.face_exercise()
    $ dialouge = renpy.random.choice([
    "I spend the next hour practising my dance routines.",
    "I practice my routines for the next hour.",
    "I decide to practice my dance routines for the next hour."
    ])
    "[dialouge]"
    jump school_gym_dance_exercise_end


label school_gym_dance_nude_picker:
    $ player.can_sport()
    if rachel_here():
        jump school_gym_dance_nude_rachel
    else:
        jump school_gym_dance_nude_alone

label school_gym_dance_nude_rachel:
    pc "Let's dance."
    $ renpy.show(random(["rachel_dancenude_grind", "rachel_dancenude_hug", "rachel_dancenude_hips", "dance_girls_rachel", "dance_behind", "ps_dance"]))
    with dissolve
    $ player.face_exercise()
    $ dialouge = renpy.random.choice([
    "I spend some time practising dance while naked with " + rachel.setname + ".",
    "Me and " + rachel.setname + " practice some routines for the next hour while naked.",
    "I offer " + rachel.setname + " to dance nude and we spend the next hour or so doing so.",
    ])
    "[dialouge]"
    jump school_gym_dance_exercise_end


label school_gym_dance_nude_alone:
    pcm "No one else is here, so can have some fun while naked"
    $ renpy.show(random(["dance_behind", "ps_dance"]))
    $ player.face_exercise()
    $ dialouge = renpy.random.choice([
    "I spend the next hour practising my dance routines while naked.",
    "I practice my routines for the next hour or so.",
    "I decide to practice my dance routines for the next hour while naked."
    ])
    "[dialouge]"
    jump school_gym_dance_exercise_end

label school_gym_dance_exercise_end:
    $ exercise(60)
    $ renpy.scene()
    with dissolve
    $ player.face_normal()
    if school_dance_can_ask_join_team() and svet_here():
        call school_class_gym_dance_jointeam from _call_school_class_gym_dance_jointeam
    if c.nude:
        $ player.add_mood(10)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
