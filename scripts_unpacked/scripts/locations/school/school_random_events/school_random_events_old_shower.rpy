label random_event_school_old_shower:
    $ player.face_shock()
    $ dialouge = renpy.random.choice([
    "*Brrrrrr* Water is freezing.",
    "Cold cold cold",
    "Fuck! Cold!",
    "Freezing!",
    ])
    pc "[dialouge]"

label random_event_school_old_shower_sex:
    $ rand_choice = WeightedChoice([
    ("random_event_school_old_shower_no_event", 300),
    ("random_event_school_old_shower_sex_join_drake", If (drake.lust > 60 and drake.love > 40 and school_soccer_hangingout(), drake.lust,0)), 
    ("random_event_school_old_shower_sex_join_nate", If (nate.lust > 60 and nate.love > 40 and school_soccer_hangingout(), nate.lust,0)), 
    ("random_event_school_old_shower_sex_join_dan", If (dan.lust > 60 and dan.love > 40 and school_soccer_hangingout(), dan.lust,0)), 
    ])
    jump expression rand_choice

label random_event_school_old_shower_no_event:
    jump school_field_soccer_play_end_shower_end

label random_event_school_old_shower_sex_join_drake:
    $ npc_race_picker(drake)
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pc "Oi! Sneaking up on me like that!"
    drake.name "Looked like you need some help."
    pc "Oh did it now?"
    drake.name "Mmm, seems like you were struggling a bit so thought I would help out."
    if renpy.showing("shower"):
        show shower grope with dissolve
    elif renpy.showing("shower_back"):
        show shower_back grope with dissolve
    pc "Oooh?"
    if player.check_sex_agree(4):
        menu:
            "Let him continue":
                jump school_field_soccer_play_end_shower_sex_offer_drake1
            "Cool him down":
                $ NullAction()
    jump school_field_soccer_play_end_shower_sex_offer_drake_reject

label random_event_school_old_shower_sex_join_nate:
    $ npc_race_picker(nate)
    if renpy.showing("shower"):
        show shower stand with dissolve
    elif renpy.showing("shower_back"):
        show shower_back man_front with dissolve
    pc "FUCK! [nate.name]! You frightened the life out of me sneaking up like that."
    nate.name "Ah sorry. Just though you might want someone to help you wash."
    if player.check_sex_agree(4):
        menu:
            "Sure, give me a hand":
                jump school_field_soccer_play_end_shower_sex_offer_nate1
            "Cool him down":
                $ NullAction()
    jump school_field_soccer_play_end_shower_sex_offer_nate_reject

label random_event_school_old_shower_sex_join_dan:
    $ npc_race_picker(dan)
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pc "AH [dan.name]! Say something next time. Sneaking up like that."
    dan.name "Sorry. Want some help?"
    pc "..."
    if player.check_sex_agree(4):
        menu:
            "Let him continue":
                "Being that it's [dan.name] behind me, I don't even answer and just lean back against him."
                jump school_field_soccer_play_end_shower_sex_offer_dan1
            "Cool him down":
                $ NullAction()
    jump school_field_soccer_play_end_shower_sex_offer_dan_reject
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
