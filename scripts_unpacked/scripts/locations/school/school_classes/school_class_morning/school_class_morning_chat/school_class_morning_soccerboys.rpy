label school_class_normal_soccerboys:
    $ rand_choice = WeightedChoice([
    ("school_class_normal_soccerboys_1", 1),
    ("school_class_normal_soccerboys_2", 1),
    ("school_class_normal_soccerboys_3", If(cass.isactive,1,0)),
    ("school_class_normal_soccerboys_4", 1),
    ("school_class_normal_soccerboys_5", 1),
    ("school_class_normal_soccerboys_6", If (player.allure>100,1,0)),
    
    
    
    

    ])
    jump expression rand_choice


label school_class_normal_soccerboys_1:
    show nate at right1 with dissolve
    pc "Morning."
    nate.name "Hey."
    pc "You alone? Where are the others?"
    nate.name "Drunk too much and still sleeping probably."
    pc "Ah."
    nate.name "Ugh. How about we skip the class and you suck my cock?"
    pc "Ugh, shut up you pervert."
    if player.check_sex_agree(5):
        pcm "Hmmm..."
        menu:
            "Meet you by the toilets":
                nate.name "Oh? Ok."
                hide nate with dissolve
                pcm "No one watching?"
                pcm "..."
                pcm "Nope, no one paying attention."
                $ walk(loc_school_hallway)
                pause 0.5
                $ walk(loc_school_toilet)
                pause 0.5
                pcm "Hmmm..."
                show nate at right1 with dissolve
                nate.name "It's empty. Come on."
                hide nate with dissolve
                pcm "Hopefully no one sees me..."
                $ walk(loc_school_toilet_boys)
                $ tempname = nate
                $ npc_race_picker(nate)
                jump school_field_soccer_sex_alone_start
            "Don't bother":
                $ NullAction()
    jump school_class_normal_end

label school_class_normal_soccerboys_2:
    show dan at right1 with dissolve
    pc "Morning [dan.name]."
    dan.name "Morning."
    pc "What you doing?"
    dan.name "Seeing how long it takes for the girl [nate.name] is talking to gets pissed off with him."
    pc "Hmmm."
    pc "Well, [nate.name]'s not that bad. As long as he doesn't say something stupidly perverted like he usually..."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        pc "Huh?"
        pc "Wait! Are they leaving together?"
        dan.name "Wow, looks like it."
        pc "Well. That's a shocker..."
    else:
        pc "Oh..."
        dan.name "She's pissed."
        pc "Ouch."
        pc "Idiot that he is..."
    jump school_class_normal_end

label school_class_normal_soccerboys_3:
    show nate at right1 with dissolve
    nate.name "Morning sexy."
    pc "Morning. What you doing?"
    nate.name "Trying to see what kind of pant's that redhead is wearing."
    pc "Ugh, leave [cass.name] alone, she's my friend."
    nate.name "Then why don't you introduce us?"
    pc "Yeah, really going to introduce her to the guy who's sitting here trying to look up her skirt."
    if player.preg_knows and nate.preg_current:
        pc "Plus she doesn't need you knocking her up like you did to me."
        if cass.days_pregnant > 55:
            nate.name "Looks like someone already knocked her up so no worries there."
            jump school_class_normal_end

    nate.name "Hmmm..."
    jump school_class_normal_end

label school_class_normal_soccerboys_4:
    show nate at right1
    show drake at right2
    with dissolve
    drake.name "... getting bigger?"
    nate.name "I think so."
    pc "Morning."
    drake.name "Morning [name]. So the girl over there. You know her?"
    pc "Seen her about but no, don't know her. Why?"
    drake.name "We are trying to work out if she is pregnant. It looks like she has been getting bigger and doubt it's over eating."
    if player.pregnancy >= 2:
        pc "Maybe. Not like it would be a suprise. So many girls here are pregnant, myself included."
    else:
        pc "Maybe. Not like it would be a suprise. So many girls here are pregnant."
    drake.name "I suppose."
    jump school_class_normal_end

label school_class_normal_soccerboys_5:
    show drake at right1
    show dan at right2
    with dissolve
    drake.name "... and started acting all weird, coming close to me and just standing there."
    dan.name "What did you do?"
    drake.name "Nothing. Just walked away from him. Not going to get in a tustle with a lunatic like that."
    dan.name "Good. People like that aren't all there in the head."
    drake.name "Yeah..."
    jump school_class_normal_end

label school_class_normal_soccerboys_6:
    show drake at right1 with dissolve
    pc "Morning."
    drake.name "Morning. Looking good. You didn't have to dress all nice just for me."
    if player.check_sex_agree(5):
        pc "For you? It's for anyone who wants to have a look."
        drake.name "Gonna let me have a much closer look?"
        pc "Hmm..."
        menu:
            "Sure. Let's go somewhere quiet":
                drake.name "Oh?"
                pc "More fun than being in here."
                drake.name "Right. Ok? So... Let's go."
                pc "Go to the toilets and I'll meet you there."
                hide drake with dissolve
                pcm "No one watching?"
                pcm "..."
                pcm "Nope, no one paying attention."
                $ walk(loc_school_hallway)
                pause 0.5
                $ walk(loc_school_toilet)
                pause 0.5
                pcm "Hopefully no one sees me..."
                $ walk(loc_school_toilet_boys)
                show drake at right1
                $ tempname = drake
                $ npc_race_picker(drake)
                jump school_field_soccer_sex_alone_start
            "Not really":


                pc "You can keep looking from a distance."
    else:
        pc "Don't flatter yourself."
    jump school_class_normal_end

label school_class_normal_soccerboys_7:
    with dissolve
    $ player.face_worried()
    pc "Morning. What are you doing down there?"
    dan.name "Uhhh. Drank too much..."
    pc "Ah."
    pc "Well..."
    pc "Good luck."
    jump school_class_normal_end

label school_class_normal_soccerboys_8:
    show drake at right1 with dissolve
    pc "Morning."
    drake.name "Hey. Morning."
    pc "..."
    pc "Why are you so quiet?"
    drake.name "Huh?"
    pc "Oh? Who you perving on?"
    drake.name "Err... No one."
    pc "Yeah right."
    jump school_class_normal_end

label school_class_normal_soccerboys_9:
    show dan at right1 with dissolve
    pc "Morning. Alone again?"
    dan.name "Yeah, [nate.name] ran off."
    pc "Oh?"
    dan.name "He got his hands on one of the school magazines and wanted some alone time."
    pc "Ugh, pervert."
    jump school_class_normal_end

label school_class_normal_soccerboys_10:
    show drake at right1
    show dan at right2
    with dissolve
    drake.name "... no helping him."
    pc "Morning."
    dan.name "I guess not. Morning [name]."
    pc "No helping who? Talking about [nate.name] arent you?"
    drake.name "Of course."
    pc "What's he done now?"
    drake.name "The same thing as always. Scaring the girls off."
    pc "Ah."
    jump school_class_normal_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
