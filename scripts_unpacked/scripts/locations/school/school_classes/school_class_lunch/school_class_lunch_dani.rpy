label school_class_lunch_dani:
    jump expression WeightedChoice([
    ("school_class_lunch_dani_1", If(pub_waitress.timesworked >= 8 and not "asked_pub_work" in dani.list and dani.love >= 30, 1, 0)),
    ("school_class_lunch_dani_2", If(school_bully_quest_bully_event_stage > 4 and not shane.dead, 1, 0)),  
    ("school_class_lunch_dani_3", If(school_bully_quest_bully_event_stage >= 10 and not shane.dead, 1, 0)),  
    ("school_class_lunch_dani_4", If(not "asked_pub_work" in dani.list, 1, 0)),
    ("school_class_lunch_dani_5", 1),
    ("school_class_lunch_dani_6", If(player.iswhore and not dani.iswhore, 1, 0)),
    
    
    
    
    ])


label school_class_lunch_dani_1:
    show dani school at right1 with dissolve
    $ add_to_list(dani.list, "asked_pub_work")
    dani.name "How's working at the pub? Debating if I should give it a shot."
    pc "Short skirt and horny men who are also drunk. Worse than the bus."
    dani.name "But what's the pay like?"
    if pub_waitress.sex:
        pc "Depends on if you let the drunks do what they want."
        dani.name "And if you do?"
        pc "Then the pay is pretty good."
    else:
        pc "Mostly tips. Get the guy's to like you and they tip better."
        dani.name "Oh?"
        pc "Mmmm..."
    jump school_class_lunch_end

label school_class_lunch_dani_2:
    show dani school at right1 with dissolve
    dani.name "Still having trouble with those idiots?"
    $ player.face_worried()
    pc "Yeah... Unfortunately."
    dani.name "Not anything you can do about it?"
    pc "What can I do?"
    dani.name "Dunno. But might be worth trying something before it goes too far."
    if shane.sex or marcus.sex:
        pc "Too late for that."
        dani.name "Ah... Sorry."
    else:
        pc "Mmmm..."
    jump school_class_lunch_end

label school_class_lunch_dani_3:
    show dani school at right1 with dissolve
    dani.name "I heard things got pretty bad with those arseholes?"
    $ player.face_worried()
    pc "You heard?"
    dani.name "Yeah... It true or just some shitty rumour?"
    if player.isslut or player.iswhore:
        pc "I was gang fucked by half the school..."
        pc "So yeah... Is true..."
    else:
        $ player.face_meek()
        pc "Not sure what you heard..."
        pc "But probably true..."
    dani.name "..."
    jump school_class_lunch_end

label school_class_lunch_dani_4:
    show dani school at right1 with dissolve
    dani.name "Thinking of looking for work at the motel."
    pc "What kind of work are they offering?"
    dani.name "That's the problem, I'm not sure."
    dani.name "They say it's as a night cleaner but I have heard rumours."
    pc "About what?"
    dani.name "That you clean in tiny clothes."
    pc "Ah..."
    if pub_waitress.timesworked >= 8:
        pc "Well, pretty normal if my bar outfit is anything to go by."
    dani.name "Yeah..."
    jump school_class_lunch_end

label school_class_lunch_dani_5:
    show dani school at right1 with dissolve
    dani.name "You managing to keep up with rent payments?"
    pc "I guess..."
    pc "You struggling?"
    dani.name "Depends on the definition of struggling..."
    if player.isslut or player.iswhore:
        pc "Making you pay in other ways?"
        dani.name "Yeah..."
        pc "Well, got to do what you need to. Better than homeless I guess."
        dani.name "I wonder."
    else:
        pc "Oh..."
    jump school_class_lunch_end

label school_class_lunch_dani_6:
    show dani school at right1 with dissolve
    dani.name "[name]..."
    pc "Yeah?"
    dani.name "..."
    dani.name "You make decent money... You know? With what you do."
    pc "Ah."
    pc "Well, not sure I would call it decent. But it's money I wouldn't earn otherwise."
    dani.name "..."
    jump school_class_lunch_end

label school_class_lunch_dani_7:
    show dani school at right1 with dissolve
    dani.name "Hey."
    pc "Hey. So you have been doing photo's with [felix.name] as well?"
    dani.name "Ah! How did you find out?"
    pc "[nate.name] who I hang out with is a pervert. He was trying to get hold of my photos and managed to get some of yours as well."
    dani.name "Ah really? Well I guess it was only a matter of time."
    dani.name "Wait! Your photos? You did extra ones as well?"
    pc "Of course. More money."
    dani.name "Mmmm. Well, glad I'm not the only one."
    $ add_to_list(school_photo_quest.conversation_topics, "dani_photos_dani_knows_pc_knows")
    jump school_class_lunch_end

label school_class_lunch_dani_8:
    show dani school at right1 with dissolve
    dani.name "The extra photos you took."
    pc "Yeah?"
    dani.name "You ever show anything off?"
    pc "You not seen the photos? Just ask [felix.name] and he will probably show you."
    if "sex" in school_photo_quest.list:
        pc "But yes. I had sex while [felix.name] took pictures."
    elif "bukkake" in school_photo_quest.list:
        pc "But yes, I wound up in a shoot where the boys I hang out with... Err... Put stuff on my face."
    elif "nude" in school_photo_quest.list:
        pc "But yeah, I have shown everything off in the photos."
    elif "topless" in school_photo_quest.list:
        pc "But yeah, I've had pictures of me topless taken."
    else:
        pc "But not gone too far yet. Just nudes with all the bits hidden."
    pc "What about you?"
    dani.name "Your pervert friend not tell you?"
    pc "Not in detail. Just that there were some of you in the private collection."
    if "dani_sex" in school_photo_quest.list:
        dani.name "..."
        dani.name "I have been having sex with [felix.name] while he takes pictures of it all."
        pc "Ooooh! Nice! I'm surprised I've even managed to see [nate.name] recently if that's the case. He would love those."
    elif "dani_nude" in school_photo_quest.list:
        dani.name "I've been fully nude on camera..."
        pc "Oh. Bet [nate.name] likes those photos."
    elif "dani_topless" in school_photo_quest.list:
        dani.name "I've been topless on camera but not done full nude."
        pc "Oh. Bet [nate.name] likes those photos."
    else:
        dani.name "I took clothes off but didn't show anything in the photos. Just some tasteful nude ones."
        pc "Oh? Pretty sure [nate.name] would love them anyway."
    dani.name "I bet."
    jump school_class_lunch_end

label school_class_lunch_dani_postdance:
    show dani school at right1 with dissolve
    dani.name "Hey."
    call dani_postdance_company_conv from _call_dani_postdance_company_conv
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
