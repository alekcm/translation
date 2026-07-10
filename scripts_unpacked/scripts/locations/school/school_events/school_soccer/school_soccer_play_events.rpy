label school_field_soccer_play_start:
    if robin_here() and not "soccerboys_ask_tell" in robin.list:
        jump robin_talk_soccerboys_meet

    if not "sport" in tab_top:
        pcm "Better get changed first."
        $ pc_dress_event("sport", loc_school_locker_girls, loc_school_field)
    $ dialouge = renpy.random.choice([
    "Alright, let's play!",
    "Ok, let's go.",
    "Here we go.",
    "Hup, let's play.",
    "Come on then, let's go.",
    ])
    pc "[dialouge]"
    show activity_soccer with dissolve
    $ player.face_exercise()

    call school_field_soccer_play_start_picker from _call_school_field_soccer_play_start_picker

    $ player.face_exercise()

    call school_field_soccer_play_normal from _call_school_field_soccer_play_normal

    $ player.face_exercise()

    call school_field_soccer_play_start_picker from _call_school_field_soccer_play_start_picker_1

    $ player.face_exercise()

    jump school_field_soccer_play_end

label school_field_soccer_play_start_picker:

    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_boys", 100),
    ("school_field_soccer_play_allure", player.allure),
    ("school_field_soccer_play_desire", player.desire),
    ("school_field_soccer_play_fat", If (player.isfat,100,0)),
    ("school_field_soccer_play_highconf", If (player.confidence > 50, player.confidence, 0)),
    ("school_field_soccer_play_mood", 100 - player.mood),
    ])
    jump expression rand_choice


label school_field_soccer_play_normal:
    $ dialouge = renpy.random.choice([
    "Go go go! Got to get the ball.",
    "No way! That was a foul!",
    "Ugh. Come on, faster!",
    "Phew! This is too much. These guys are damn gorillas!",
    "Ah yes! Weave in, out! They are oafs so I can get around them.",
    ])
    pc "[dialouge]"
    return

label school_field_soccer_play_boys:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_normal_drake", 100),
    ("school_field_soccer_play_normal_nate", 100),
    ("school_field_soccer_play_normal_dan", 100),
    ])
    jump expression rand_choice

label school_field_soccer_play_boys_picker:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_normal_drake", If (tempname == drake,100,0)),
    ("school_field_soccer_play_normal_nate", If (tempname == nate,100,0)),
    ("school_field_soccer_play_normal_dan", If (tempname == dan,100,0)),
    ])
    jump expression rand_choice

label school_field_soccer_play_normal_drake:
    $ dialouge = renpy.random.choice([
    "Too slow!",
    "C'mon, you gotta be faster than that.",
    "Ha, see that?",
    "Are you lot even trying or am I just too good?",
    "Come on, let's see what you got.",
    "YES. GOAL!!"
    ])
    drake.name "[dialouge]"
    return

label school_field_soccer_play_normal_nate:
    $ dialouge = renpy.random.choice([
    "Go on, run! Keep shaking that ass!",
    "What the... How did you manage that?",
    "I'm gonna get you! Your ass won't recover.",
    "Whaaaa?",
    "Oi! That's cheating. Distracting me like that.",
    "GOAL!! HAVE IT!!",
    ])
    nate.name "[dialouge]"
    return

label school_field_soccer_play_normal_dan:
    $ dialouge = renpy.random.choice([
    "Agh!",
    "Wha?!",
    "Ugh. Keep running!",
    "Really? Pulling moves like that?",
    "GOAAAAL!!!",
    ])
    dan.name "[dialouge]"
    return

label school_field_soccer_play_allure:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_allure_1", 100),
    ("school_field_soccer_play_allure_2", If (c.pantsless and c.skirt, 100,0)),
    ("school_field_soccer_play_allure_3", If (c.bra == 0, 100,0)),
    ("school_field_soccer_play_allure_4", 100),
    ("school_field_soccer_play_allure_5", If (c.ass, 100,0)),
    ("school_field_soccer_play_allure_6", If (c.ass and school_soccer_pick_boy("asex"), 100,0)),
    ("school_field_soccer_play_allure_7", If (c.skirt and not c.pants and school_soccer_pick_boy("vsex"), 100,0)),
    ])
    jump expression rand_choice

label school_field_soccer_play_allure_1:
    nate.name "Dammit [name]! With your ass shaking in front of me I can't concentrate."
    $ player.face_happy()
    pc "That's your problem, not mine."
    nate.name "Ugh!"
    hide nate with dissolve
    return

label school_field_soccer_play_allure_2:
    nate.name "Fucking hell [name]. The hell are you wearing? It's distracting."
    $ player.face_happy()
    pc "Not wearing anything. Heh."
    nate.name "Fuck!"
    hide nate with dissolve
    return

label school_field_soccer_play_allure_3:
    nate.name "The hell [name]? You having those things bounce around on purpose?"
    $ player.face_happy()
    pc "Got to take any advantage I can get."
    hide nate with dissolve
    return

label school_field_soccer_play_allure_4:
    $ player.face_happy()
    pc "Err, the ball is over there..."
    nate.name "Ah! Err..."
    pc "Still over there..."
    nate.name "Fuck."
    hide nate with dissolve
    return

label school_field_soccer_play_allure_5:
    $ player.face_neutral()
    pc "Pervert."
    nate.name "What?"
    pc "Think I don't know you are staring at my ass?"
    nate.name "Ugh."
    hide nate with dissolve
    return

label school_field_soccer_play_allure_6:
    $ player.spank()
    $ player.face_shock()
    tempname.name "You keep prancing around and showing off your bum like that [name] and I might bend you over here and fuck you in the arse again."
    $ player.face_happy()
    pc "Promises promises."
    return

label school_field_soccer_play_allure_7:
    $ player.grope_hips()
    tempname.name "No pants on with that skirt on? You asking for me to bend you over and fuck you again?"
    $ player.face_happy()
    pc "Shoo! Later."
    $ player.grope_end()
    return

label school_field_soccer_play_desire:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_desire_1", 100),
    ("school_field_soccer_play_desire_2", 100),
    ("school_field_soccer_play_desire_3", 100),
    ("school_field_soccer_play_desire_4", 100),
    ("school_field_soccer_play_desire_5", If(c.top and not c.bra,100,0)),
    
    
    ])
    jump expression rand_choice

label school_field_soccer_play_desire_1:
    $ player.grope()
    $ player.add_desire_random(10)
    $ player.add_mood(5)
    $ player.face_surprised()
    pc "Ah?"
    $ player.grope_end()
    $ player.face_neutral()
    pc "Pervert."
    drake.name "Sorry, accident."
    pc "Sure..."
    return

label school_field_soccer_play_desire_2:
    $ c.bottom = 0
    $ player.add_desire_random(10)
    $ player.add_mood(5)
    $ player.face_surprised()
    show drake frown at right6 with hpunch
    pc "Ah?"
    drake.name "Sorry, sorry."
    hide drake with dissolve
    pc "Watch it next time!"
    $ pc_dress()
    return

label school_field_soccer_play_desire_3:
    $ player.spank()
    pc "Ah?"
    return

label school_field_soccer_play_desire_4:
    $ player.grope()
    $ player.add_desire_random(10)
    $ player.add_mood(5)
    $ player.face_surprised()
    pc "Ah?"
    $ player.grope_end()
    $ player.face_neutral()
    pc "You ass! That's not fair doing that then taking the ball."
    return

label school_field_soccer_play_desire_5:
    $ player.face_happy()
    pc "Hey, [drake.name]."
    drake.name "Huh?"
    $ c.top = 0
    pause 0.3
    $ pc_dress()
    drake.name "Ah cheater!"
    $ player.add_desire_random(10)
    $ player.add_mood(5)
    $ player.face_neutral()
    hide drake with dissolve
    return

label school_field_soccer_play_fat:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_fat_1", 100),
    ("school_field_soccer_play_fat_2", 100),
    ("school_field_soccer_play_fat_3", 100),
    ("school_field_soccer_play_fat_4", 100),
    
    
    
    ])
    jump expression rand_choice

label school_field_soccer_play_fat_1:
    pcm "Hufff! I need to get into better shape..."
    return

label school_field_soccer_play_fat_2:
    pcm "*Phew* This is exhausting. Hope it gets easier if I get fitter."
    return

label school_field_soccer_play_fat_3:
    nate.name "Come on chunky, keep up!"
    pc "Screw you."
    nate.name "Later."
    return

label school_field_soccer_play_fat_4:
    dan.name "Your doing well"
    pc "Err. Thanks."
    return

label school_field_soccer_play_highconf:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_conf_1", 100),
    ("school_field_soccer_play_conf_2", 100),
    ("school_field_soccer_play_conf_3", 100),
    ("school_field_soccer_play_conf_4", 100),
    
    
    
    ])
    jump expression rand_choice

label school_field_soccer_play_conf_1:
    show drake frown at right6
    $ player.punch()
    pc "Ugh! Fuck!"
    drake.name "Sorry!"
    hide drake with dissolve
    return

label school_field_soccer_play_conf_2:
    pc "Yes yes yes! Take that!"
    nate.name "FUCK!"
    pc "Come on! I'll kick your arses more!"
    return

label school_field_soccer_play_conf_3:
    $ player.face_pain()
    pc "Ouch ouch ouch!"
    drake.name "You ok?"
    pc "Fuck hold on. Pulled a muscle."
    return

label school_field_soccer_play_conf_4:
    $ player.face_angry()
    pc "Ah dammit. You been doping today or something?"
    pc "Every time you touch the damn ball it goes straight in the net."
    return


label school_field_soccer_play_mood:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_mood_1", 100),
    ("school_field_soccer_play_mood_2", 100),
    ("school_field_soccer_play_mood_3", 100),
    
    
    
    
    ])
    jump expression rand_choice

label school_field_soccer_play_mood_1:
    $ player.face_happy()
    pcm "Phew. This is quite fun."
    $ player.add_mood(5)
    return

label school_field_soccer_play_mood_2:
    $ player.face_happy()
    pc "GOAAAAAAAALLLLLL!!!!!!!!!!!!"
    $ player.add_mood(5)
    return

label school_field_soccer_play_mood_3:
    $ player.face_happy()
    pc "Whooo!"
    $ player.add_mood(5)
    return

label school_field_soccer_play_end:
    $ exercise(60)
    $ player.add_mood(5)
    $ show_activity_image("soccer")

    $ randomnum = renpy.random.randint(0, int(player.fitness + (player.allure / 4)))
    if randomnum < 20:
        "In the end I am eliminated in the first round and spend the rest of the time waiting with the other losers."
    elif randomnum < 40:
        "While I give it a good go. In the end I'm knocked out in the first round and spend the rest of the time chatting to the other losers."
    elif randomnum < 60:
        "I manage to get a couple of goals, but not good enough to reach the final."
    elif randomnum < 80:
        "I manage to hold my own and get a couple of goals. Much to my surprise I even manage to make it to the final. Unfortunately I do not manage to win in the end."
    else:
        "I am feeling great and manage to score early in most rounds. I even manage to make it to the final where after a tough match, I get the ball in the net and become the champion."
        pc "CHAMPION!"
        $ school_soccer_quest_games_won += 1

    hide activity_soccer with dissolve
    "After the match I take a bit of a rest."
    $ player.face_normal()
    pc "Phew!"
    $ add_event_love_lust([drake,nate,dan])
    if not school_soccer_playing():
        jump school_field_soccer_play_end_shower
    else:
        jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
