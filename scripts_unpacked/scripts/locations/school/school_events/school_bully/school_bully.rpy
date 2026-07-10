default school_bully_quest_bully_event_stage = 0
default school_bully_quest_bully_soccer_boys_remove = False
default school_bully_quest_bully_cass_target = False

label school_bully_event_picker:
    if school_bully_quest.active == 0:
        jump school_bully_event_intro
    elif school_bully_quest_bully_event_stage < 5 and t.day > 42:
        $ school_bully_quest_bully_cass_target = True

    elif player.check_nowill():
        if school_bully_quest_bully_event_stage == 0:
            jump school_bully_event_nowill_intro
        else:
            jump school_bully_bully_event_tombola
    else:

        jump school_bully_resist_event_tombola

    jump random_event_school_end_picker

label school_bully_bully_event_tombola:



    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_1", If (school_bully_quest_bully_event_stage >= 1, 300, 0)),
    ("school_bully_bully_event_2", If (school_bully_quest_bully_event_stage >= 2, 300, 0)),
    ("school_bully_bully_event_3", If (school_bully_quest_bully_event_stage >= 3, 300, 0)),
    ("school_bully_bully_event_4", If (school_bully_quest_bully_event_stage >= 4, 250, 0)),
    ("school_bully_bully_event_5", If (school_bully_quest_bully_event_stage >= 5, 200, 0)),
    ("school_bully_bully_event_6", If (school_bully_quest_bully_event_stage >= 6, 150, 0)),
    ("school_bully_bully_event_7", If (school_bully_quest_bully_event_stage >= 7, shane.lust + marcus.lust, 0)),
    ("school_bully_bully_event_8", If (school_bully_quest_bully_event_stage >= 8, shane.lust + marcus.lust, 0)),
    ("school_bully_bully_event_9", If (school_bully_quest_bully_event_stage >= 9, shane.lust + marcus.lust, 0)),
    ("school_bully_bully_event_10", If (school_bully_quest_bully_event_stage >= 10, shane.lust + marcus.lust, 0)),
    ])
    jump expression rand_choice

label school_bully_resist_event_tombola:

    $ rand_choice = WeightedChoice([
    ("school_bully_resist_event_1", 300),
    ("school_bully_resist_event_2", 300),
    ("school_bully_resist_event_3", 300),
    ("school_bully_resist_event_4", 300),
    ("school_bully_resist_event_5", 300),
    ("school_bully_resist_event_6", 300),
    ("school_bully_resist_event_7", 300),
    ("school_bully_resist_event_8", 75),
    ("school_bully_resist_event_9", If(cass.has_met, 300, 0)),
    ("school_bully_resist_event_10", If(cass.has_met, 300, 0)),
    ])
    jump expression rand_choice

label school_bully_cass_event_tombola:
    $ rand_choice = WeightedChoice([
    ("school_bully_cass_event_1", 300),
    ("school_bully_cass_event_2", 300),
    ("school_bully_cass_event_3", 300),
    ("school_bully_cass_event_4", 500),
    ("school_bully_cass_event_5", 300),
    ("school_bully_cass_event_6", If(cass.setname in shane.conversation_topics,500,0)),
    ("school_bully_cass_event_7", If(cass.setname in marcus.conversation_topics,500,0)),
    ("school_bully_cass_event_8", If("pregnant" in shane.conversation_topics or "pregnant" in marcus.conversation_topics,1000,0)),
    
    ])
    jump expression rand_choice

label school_bully_poisoned_event_tombola:
    $ rand_choice = WeightedChoice([
    ("school_bully_poisoned_event_1", 300),
    ("school_bully_poisoned_event_2", 300),
    ("school_bully_poisoned_event_3", 300),
    ("school_bully_poisoned_event_4", 300),
    ])
    jump expression rand_choice

label school_bully_removed_event_tombola:
    $ rand_choice = WeightedChoice([
    ("school_bully_removed_event_1", 300),
    ("school_bully_removed_event_2", 300),
    ("school_bully_removed_event_3", 300),
    ("school_bully_removed_event_4", 300),
    ("school_bully_removed_event_5", If("dead_poisoned" in shane.list, 300, 0)),
    ("school_bully_removed_event_6", If("dead_poisoned" in shane.list, 300, 0)),
    ])
    jump expression rand_choice

label school_bully_event_intro:
    $ school_bully_quest.activate()
    $ school_bully_quest_bully_event_stage = 0
    $ diary_school_bully_intro = Diary_Class("The local arseholes", "I was harassed today by a couple of arseholes.\nWhat clowns!\nDo they think being such wastes of a life will get them anywhere. Pointless as well, not like they gain anything from it.")
    $ player.face_confused()
    show shane at right2
    show marcus at right1
    with dissolve
    shane.name "Oh look. Another little bitch coming to school to try and pretend she is going to become something more than a highway hooker like all the rest."
    pcm "Who the hell is this clown?"
    $ player.face_sad()
    marcus.name "Heh, right? Probably already working there. What? Did you think coming to this school was going to be your first step to becoming someone special?"
    pcm "He has a sidekick as well..."
    shane.name "Just a little slut like all the rest. Using your body to coast through this shit life."
    pcm "*Sigh*"
    pcm "I should leave these idiots..."
    hide shane
    hide marcus
    with dissolve
    "I walk away leaving them behind."
    shane.name "Yeah walk away whore! Next time!"
    $ shane.hate = True
    $ marcus.hate = True
    $ stroll(10)
    jump random_event_school_end_picker

label school_bully_event_nowill_intro:
    $ school_bully_quest_bully_event_stage = 1
    $ diary_school_bully_intro = Diary_Class("Attacked by the arseholes", "The cunt couple attacked me today.\nStarted talking shit to me and when I talked back, it pissed fuckface number 1 off and he hit me.\nFUCK YOU!")
    show shane at right1
    with dissolve
    shane.name "Still here you little whore?"
    pcm "Ugh!"
    shane.name "Think yourself lucky we are here and not in the street. I'd take you into an alleyway and have you bent over."
    pc "*Tsk*"
    $ player.face_worried()
    pc "The hell is your problem?"
    shane.name "Little bitches like you are my problem. Come here wasting everyone's time."
    shane.name "We all know you are gunna just end up on your back taking money so some guy can stick it in you."
    pc "What do you care what anyone else does?"
    shane.name "Cus little whores like you going round looking for an easy ride taking money off desperate shits while others have to put work in."
    $ player.face_angry()
    pc "Yeah right. Like you are working towards anything. Just hanging around here making everyone's life misera..."
    $ player.punch(True)
    shane.name "Fuck you!"
    pc "AH!"
    pc "*SOB*"
    hide shane
    $ walk(loc_school_toilet_girls)
    $ player.face_cry()
    pcm "Fuck! What an arse!"
    pc "*SOB*"
    $ shane.hate = True
    $ marcus.hate = True
    $ stroll(15)
    jump random_event_school_end_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
