default random_event_school_boys_toilet_var = ""

label random_event_school_boys_toilet:
    if str(t.day) + str(t.hour) in random_event_school_boys_toilet_var:
        jump travel
    $ rand_choice = WeightedChoice([
    ("random_event_school_boys_toilet_1", 100), 
    ("random_event_school_boys_toilet_2", 100), 
    ("random_event_school_boys_toilet_3", 100), 
    ("random_event_school_boys_toilet_4", If (not school_bully_quest_bully_cass_target or not school_bully_quest_bully_soccer_boys_remove,20,0)), 
    ("random_event_school_boys_toilet_5", 100), 
    ("random_event_school_boys_toilet_6", 100),
    
    
    
    ])
    $ random_event_school_boys_toilet_var = str(t.day) + str(t.hour) + rand_choice
    jump expression rand_choice

label random_event_school_boys_toilet_return:
    if "_1" in random_event_school_boys_toilet_var:
        pcm "Probably should go in there or I will be shouted at again."
        jump travel
    elif "_2" in random_event_school_boys_toilet_var:
        pcm "Should probably just leave him alone in there."
        jump travel
    return



label random_event_school_boys_toilet_1:
    $ player.face_worried()
    guy "OI! Fuck off you shitty whore!"
    $ walk(loc_school_toilet_boys)
    $ player.face_worried()
    with hpunch
    pc "..."
    pc "Okay then."
    jump random_event_school_end_picker

label random_event_school_boys_toilet_2:
    guy "What you doing in here?"
    pc "I..."
    guy "Don't be causing anything funny."
    pc "Err, ok..."
    jump random_event_school_end_picker

label random_event_school_boys_toilet_3:
    guy "What you doing in here?"

    if player.check_sex_agree(3):

        menu:
            "Looking for some fun":
                pc "Hmm, alone in the boy's toilets? Want to guess?"
                $ randomnum = renpy.random.randint(1, 8)
                if randomnum == 1:
                    guy "Yeah right. So your friends can jump me when my tousers are down?"
                    guy "Go fuck yourself."
                    "He gives me a dirty look as he walks away."
                elif randomnum == 2:
                    guy "Whaa, errr, what?"
                    pc "We can go somewher..."
                    "He turns around and immediately starts walking away"
                elif randomnum == 3:
                    guy "Heh, no idea what your game is but I'm out of here."
                    "Before I can get another word in, he turns and walks out the door."
                elif randomnum == 4:
                    "He doesn't even say a word and just walks out there door."
                elif randomnum == 5:
                    guy "Yeah right. As if I can afford someone like you."
                    "Before I can get another word in, he turns and walks away."
                elif randomnum == 6:
                    guy "Fuck, go and do that shit at the highway and leave this place alone."
                    "Before I can get another word in, he turns and walks away."
                else:
                    guy "You serious? To do what I think you mean?"
                    pc "Yes."
                    guy "Err, sure?"
                    jump school_rep_sex

                $ player.face_worried()
                pcm "Not the response I was expecting..."
                jump random_event_school_end_picker
            "Err, nothing":

                $ NullAction()
    pc "Sorry."
    pcm "I should leave."
    $ walk(loc_school_toilet)
    jump random_event_school_end_picker

label random_event_school_boys_toilet_4:
    $ rand_choice = WeightedChoice([
    ("school_bully_bully_event_5", If (school_bully_quest_bully_event_stage >= 5, 1, 0)),
    ("school_bully_bully_event_6", If (school_bully_quest_bully_event_stage >= 6, 1, 0)),
    ("school_bully_bully_event_7", If (school_bully_quest_bully_event_stage >= 7, 1, 0)),
    ("school_bully_bully_event_8", If (school_bully_quest_bully_event_stage >= 8, 1, 0)),
    ("school_bully_bully_event_9", If (school_bully_quest_bully_event_stage >= 9, 1, 0)),
    ])
    jump expression rand_choice

label random_event_school_boys_toilet_5:
    pcm "Hmm, totally empty."
    jump random_event_school_end_picker

label random_event_school_boys_toilet_6:
    guy "What are you... Ah I don't care."
    jump random_event_school_end_picker

label random_event_school_boys_toilet_7:
    girl1 "...last night near the motel. Didn't even listen to what he wanted and just ran away."
    girl2 "Probably for the best. Can't take the chance."
    jump random_event_school_end_picker

label random_event_school_boys_toilet_8:
    girl1 "...not seen her for a while. You know anything?"
    girl2 "No, she didn't say anything to me. My guess is pregnant. She was acting up a bit before she went missing."
    girl1 "No? You think so? How did she manage that? She was smart enough to avoid it."
    girl2 "Who knows. Maybe someone paid more to do it that way..."
    jump random_event_school_end_picker

label random_event_school_boys_toilet_9:
    girl1 "...at the lake to relax."
    girl2 "What? I have never been there. Is it safe?"
    girl1 "Well, as safe as anywhere round here can be. Just don't use the lockers to keep your stuff in and keep it in your bag."
    girl2 "Err, ok. Why?"
    girl1 "So if you need to do a runner, you aren't left god knows where with only a bikini."
    girl2 "Ah..."
    jump random_event_school_end_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
