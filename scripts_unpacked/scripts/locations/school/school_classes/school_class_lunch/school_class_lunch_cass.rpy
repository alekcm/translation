label school_class_lunch_cass:
    $ rand_choice = WeightedChoice([
    ("school_class_lunch_cass_1", If(not mira.active, 100, 0)),
    ("school_class_lunch_cass_2", 100),
    ("school_class_lunch_cass_3", If (school_bully_quest_bully_event_stage > 4 and not shane.dead, 100, 0)),  
    ("school_class_lunch_cass_4", 1),
    ("school_class_lunch_cass_5", If (school_soccer_quest_hangout_prompt, 100, 0)),
    ("school_class_lunch_cass_6", If (weather_var > 2, 100, 0)),
    ("school_class_lunch_cass_7", If (school_dance_quest_show_count >= 6, 100, 0)),
    ("school_class_lunch_cass_8", 100),
    ("school_class_lunch_cass_9", 100),
    ("school_class_lunch_cass_10", If (pub_waitress.timesworked >= 8, 100, 0)),
    ])
    jump expression rand_choice

label school_class_lunch_cass_1:
    show cass at right1 with dissolve
    cass.name "Where is that [mira.name]? Haven't seen her all day."
    pc "Relaxing by the lake probably."
    if weather_var == 1:
        cass.name "Hmm, hope so. Lovely out there today. Should go and join her."
        pc "Yeah, you in a bikini. Pretty sure you will cause a commotion."
        cass.name "Hey!"
    else:
        cass.name "In this weather?"
        pc "Well, even when it's like this. Probably better than this place."
        cass.name "Probably."
    jump school_class_lunch_end

label school_class_lunch_cass_2:
    show cass at right1 with dissolve
    cass.name "Still keeping up with the dancing?"
    if player.isfat == True:
        pc "Yeah. They like to torture me."
    elif school_dance_quest_on_team == True:
        pc "Yeah, been doing training with the team. It's quite fun."
    else:
        pc "Yeah. It's not so bad."
    cass.name "Hmm, that's good."
    jump school_class_lunch_end

label school_class_lunch_cass_3:
    show cass at right1 with dissolve
    cass.name "Still having trouble with those arseholes [name]?"
    $ player.face_meek()
    pc "..."
    cass.name "Nothing you can do about it?"
    pc "..."
    if drake.love > 50:
        cass.name "What about the boys you play football with? They not scare them off?"
        pc "Dunno, not asked..."
        cass.name "*Sigh*"
    jump school_class_lunch_end


label school_class_lunch_cass_4:
    show cass at right1 with dissolve
    cass.name "So~~"
    cass.name "Any news about your flatmates?"
    pc "What do you mean?"
    cass.name "Don't play coy."
    pc "I barely speak to them."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        cass.name "It's not the speaking I am interested in."
        pc "Huh?"
        cass.name "Small pyjamas? Accidentally dropping the towel?"
        pc "Do you have a source of old movies you haven't told anyone about?"
    else:
        pc "Mostly they stay in their rooms. Don't really speak much with them."
    jump school_class_lunch_end

label school_class_lunch_cass_5:
    show cass at right1 with dissolve
    cass.name "How's the boys out there treating you?"
    pc "Huh? Fine. We just play some football together."
    cass.name "Yeah?"
    pc "Yes. What are you getting at?"
    cass.name "Wrestling with the boys. All hot and sweaty. You being the only girl..."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1 and player.desire > 80:
        $ player.face_surprised()
        pc "Oh you mean all showering together?"
        cass.name "What? Really?"
        $ player.face_happy()
        pc "Or are you talking about the masturbation competitions?"
        cass.name "Err..."
        pc "There was that one time we all got naked and..."
        cass.name "Okay ok. No need to tease me."
    else:
        pc "I don't know what kind of idea you have about what goes on out there."
    $ player.face_normal()
    jump school_class_lunch_end

label school_class_lunch_cass_6:
    show cass worried at right1 with dissolve
    cass.name "..."
    pc "..."
    pc "You ok?"
    cass.name "Yeah..."
    pc "What happened?"
    cass.name "..."
    cass.name "Just these fucking busses..."
    pc "Oh?"
    jump school_class_lunch_end

label school_class_lunch_cass_7:
    show cass at right1 with dissolve
    cass.name "So, rumour says you have been flashing your arse out in the park."
    pc "Yeah, been doing dance shows to busk for some money."
    cass.name "I've seen your dance clothes. Bit dangerous isn't it?"
    pc "Well, we don't do it so late and there is a bunch of us. Nothing should get out of hand."
    cass.name "Hmm, hope not"
    jump school_class_lunch_end

label school_class_lunch_cass_8:
    show cass at right1 with dissolve
    cass.name "What is that [name]?"
    pc "Haven't a clue, I was late and this is all they had."
    cass.name "Looks like puke."
    pc "Doesn't taste much better either."
    jump school_class_lunch_end

label school_class_lunch_cass_9:
    show cass at right1 with dissolve
    cass.name "..."
    pc "What's wrong with you?"
    cass.name "Huh?"
    pc "You look like a zombie."
    cass.name "Oh..."
    cass.name "I walked here this morning. Had to get up really early and it was exhausting."
    pc "Looking to get more exercise?"
    cass.name "Fuck no. I was trying to avoid having half the bus feel me up."
    pc "Oh."
    cass.name "*Sigh*"
    jump school_class_lunch_end

label school_class_lunch_cass_10:
    show cass at right1 with dissolve
    cass.name "How's pub work?"
    pc "The pub?"
    pc "Well, if you thought the bus was bad, get the same type of people drunk then the bus feels like a breeze."
    cass.name "Oh? That bad?"
    pc "Well, at least they tip."
    $ randomnum = renpy.random.randint(1, 50)
    if randomnum == 1 and player.desire > 80:
        cass.name "That before or after they have had their way with you?"
        $ player.face_surprised()
        pc "..."
        pc "Money always before..."
        $ player.face_normal()
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
