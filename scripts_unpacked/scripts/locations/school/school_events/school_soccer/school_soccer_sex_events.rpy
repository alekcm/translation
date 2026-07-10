define school_field_soccer_sex_offer_rules = None

label school_field_soccer_sex_offer_picker:
    if robin_here() and not "soccerboys_knows_pc_sex" in robin.list:
        pcm "Maybe I should wait until [robin.name] has gone..."
        jump travel
    if school_field_soccer_sex_offer_rules == None:
        jump school_field_soccer_sex_offer_intro
    elif not school_soccer_sex_rules():
        jump school_field_soccer_sex_offer_update_rules
    else:



        if player.hygiene <= 30:
            jump school_field_soccer_sex_offer_shower
        else:
            jump school_field_soccer_sex_offer




label school_field_soccer_sex_offer_shower:
    pc "Umm... I need a shower. Someone want to join and help me out?"
    $ school_soccer_pick_boy("lust")
    $ npc_race_picker(tempname, tempname)
    if tempname == drake:
        drake.name "Sure [name]. Let's go."
        nate.name "Have fun!"
    elif tempname == dan:
        dan.name "Mmm, I'll help."
    else:
        nate.name "Whoo. Let's go [name]. I'll make you all sparkly."

    $ walk(loc_school_locker_old)
    pause 0.5
    pc "Mm, want to watch me undress?"
    tempname.name "Mmm."
    pc "Ha. Perv!"
    $ pc_striptease()
    show sb_pose_showbreasts tounge with dissolve
    pc "You like?"
    tempname.name "Fuck yes. Lemme see your ass."
    hide sb_pose_showbreasts
    show sb_pose_lookback
    with dissolve
    pc "Mmm?"
    tempname.name "Gonna look a lot nicer with my cock in there."
    pc "Then let's go and you can."
    hide sb_pose_lookback with dissolve
    $ shower_scene_start()
    $ renpy.show(renpy.random.choice(["shower", "shower_back"]))
    $ renpy.with_statement(dissolve)
    $ player.shower()
    if not tempname == nate:
        if renpy.showing("shower"):
            show shower hold with dissolve
        elif renpy.showing("shower_back"):
            show shower_back hold with dissolve
        pc "Mmmm..."
        if renpy.showing("shower"):
            show shower grope with dissolve
        elif renpy.showing("shower_back"):
            show shower_back grope with dissolve
        if tempname == drake:
            jump school_field_soccer_play_end_shower_sex_offer_drake1
        else:
            jump school_field_soccer_play_end_shower_sex_offer_dan1
    else:
        if renpy.showing("shower"):
            show shower stand with dissolve
        elif renpy.showing("shower_back"):
            show shower_back man_front with dissolve
        jump school_field_soccer_play_end_shower_sex_offer_nate1




label school_field_soccer_sex_alone_start:
    $ having_sex(5)
    pc "Hmmm..."
    $ dialouge = WeightedChoice([
    ("You like a girl with big tits?", If (player.breasts == 3 , 1,0)),
    ("You like a girl with small tits?", If (player.breasts == 1 , 1,0)),
    ("You like my tits while I am wearing this?", If (c.clevage , 1,0)),
    ("You like looking at my huge milk tits when I wear this?", If (c.clevage and player.pregnancy >= 2, 1,0)),
    ("You like my tits like this when I don't wear a bra?", If (c.clevage and c.bra == 0, 1,0)),
    ("You like my ass when I wear something so tight?", If (c.ass , 1,0)),
    ("You like it when I wear clothes that show off my pregnant belly?", If (player.preg_knows and c.belly, 1,0)),
    ("You like it when I wear clothes that shows off to everyone how you knocked me up?", If (player.preg_knows and c.belly and tempname.preg_knows, 1,0)),
    ("You like it when I wear such revealing clothes?", If (c.slutty , 1,0)),  
    ])
    pc "[dialouge]"
    tempname.name "Mmm. Prefer it when you wear nothing though."
    pc "Want me to do a striptease for you?"
    tempname.name "Of course!"
    $ pc_striptease()
    $ renpy.scene()
    show sb_pose_showbreasts happy
    with dissolve
    pc "Mmm, like what you see?"
    tempname.name "Oooh."
    tempname.name "Can't wait to have you bent over and see my cock in you."
    pc "Oh? From this angle?"
    tempname.name "Mmm."
    $ randomnum = renpy.random.randint(0, player.desire)
    if randomnum < 60:
        jump school_field_soccer_sex_offer_cont_knees
    else:
        jump school_field_soccer_sex_offer_cont_wall




label school_field_soccer_sex_offer_cheat:
    "This is a repeatable scene you can initiate once you have become really friendly with the soccer boys."
    $ walk(loc_school_field_back)
    jump school_field_soccer_sex_offer

label school_field_soccer_sex_offer:

    if player.isbroken:
        pc "Um, anyone want to use me?"
    elif player.has_perk(perk_preg_want) and not player.preg_knows:
        pc "So, who wants to have another go at making me a mother?"
    else:
        pc "Anyone want to go and have some fun?"
    if not school_soccer_pick_boy("lust") > 40:
        $ player.face_worried()
        pc "..."
        pc "No one?"
        drake.name "You keep wearing us out [name]. Give us some time to recover would you?"
        pc "I suppose..."
        jump travel
    $ school_soccer_pick_boy("lust")
    $ npc_race_picker(tempname, tempname2)
    tempname.name "Won't say no to that."
    if weather_var > 2 or not t.timeofday == "night":
        if weather_var == 3:
            pc "Let's go to the lockers out of the rain."
        elif weather_var == 4:
            pc "My tits will freeze off out here, let's go to the lockers."
        elif not t.timeofday == "night":
            pc "Let's go to the lockers. Don't want to be flashing my arse in broad daylight."
        else:
            pc "Come on, in here."
        $ walk(loc_school_locker_old)

    elif (robin_here() and not "soccerboys_can_sex" in robin.list) or not all([nate.sex, drake.sex, dan.sex]):
        pc "Come on, let's go somewhere out of the way."
        tempname.name "Lead the way."
        $ walk(renpy.random.choice([loc_school_locker_old, loc_bushes]))

    if loc_cur == loc_school_field_back:
        pc "Hmmm..."
        if c.nude:
            show sb_pose_lookback happy with dissolve
            pc "Like it when I go around nude for you lot?"
            nate.name "Fuck yes!"
            $ player.spank()
            if not tempname == nate:
                pc "Oi, no touching the goods. My ass belongs to [tempname.name]."
            else:
                pc "Oi, tease!"
        else:
            pc "Want me to do a striptease for you boys?"
            nate.name "Fuck yes!"
            $ player.spank()
            if not tempname == nate:
                pc "Oi, no touching the goods. My ass belongs to [tempname.name]."
            else:
                pc "Oi, tease!"
            $ pc_strip_upper(slow=True)
            show sb_pose_showbreasts happy with dissolve
            pc "Mmm, like what you see boys?"
            dan.name "Oooh."
            drake.name "Oh yeah!"
            if player.has_perk(perk_preg_want):
                pc "Want to see these get huge and leaking milk?"
                drake.name "It's you who wants that you crazy bint."
                pc "Maybe [tempname.name] will make it happen."
            else:
                pc "Mmm, thought you might. Bunch of perverts probably love seeing them bounce."
                nate.name "Especially while you are being fucked."
                pc "Oh, then soon."
            $ pc_strip_lower(slow=True)
            hide sb_pose_showbreasts
            show sb_pose_lookback happy
            with dissolve
            pc "How about from this angle?"
            tempname.name "Gonna be seeing more of you from that angle when my cock is in you."
            pc "Oh, prefer it when your thing is poked inside me?"
            tempname.name "Mmm."
            pc "From behind like this?"
    else:

        pc "Hmmm..."
        if c.nude:
            pc "Mmm. Like it when I wear nothing?"
        else:
            $ dialouge = WeightedChoice([
            ("You like my tits while I am wearing this?", If (c.clevage , 1,0)),
            ("You like looking at my huge milk tits when I wear this?", If (c.clevage and player.pregnancy >= 2, 1,0)),
            ("You like my tits like this when I don't wear a bra?", If (c.clevage and c.bra == 0, 1,0)),
            ("You like my ass when I wear something so tight?", If (c.ass , 1,0)),
            ("You like it when I wear clothes that show off my pregnant belly?", If (player.pregnancy >= 2 and c.belly, 1,0)),
            ("You like it when I wear clothes that shows off to everyone how you knocked me up?", If (player.pregnancy >= 2 and c.belly and tempname.preg_knows, 1,0)),
            ("You like it when I wear such revealing clothes?", If (c.slutty , 1,0)),
            ])
            pc "[dialouge]"
            tempname.name "Mmm. Prefer it when you wear nothing though."
            pc "Want me to do a striptease for you?"
            tempname.name "Of course!"
            $ pc_striptease()
        show sb_pose_showbreasts happy with dissolve
        pc "Mmm, like what you see?"
        tempname.name "Oooh."
        tempname.name "Can't wait to have you bent over and see my cock in you."
        pc "Oh? From this angle?"
        tempname.name "Mmm."

        $ randomnum = renpy.random.randint(0, player.desire)
        if randomnum < 60:
            jump school_field_soccer_sex_offer_cont_knees
        else:
            jump school_field_soccer_sex_offer_cont_wall

label school_field_soccer_sex_offer_cont_knees:
    $ having_sex(5)
    pc "How about we get you warmed up first?"
    hide sb_pose_showbreasts
    hide sb_pose_lookback
    show sb_blowjob
    with dissolve
    show sb_blowjob face 1h with dissolve
    pc "Like me on my knees with your cock in my hand?"
    tempname.name "Of course."
    $ randomnum = renpy.random.randint(1, 4)
    if randomnum == 1:
        show sb_blowjob poke tounge 1h with dissolve
        pc "Mmmm."
        show sb_blowjob face smile 1h with dissolve
        pc "Something nice in there waiting for me?"
        tempname.name "For you? Always."
        pc "Mmm good to know. ♥"
    elif randomnum == 2:
        show sb_blowjob poke tounge 1h with dissolve
        pc "Mmmm."
        show sb_blowjob down with dissolve
        pc "Something nice in there waiting for me?"
        show sb_blowjob 0h face closed frown with hpunch
        pc "Ah!"
        tempname.name "Always got something for you."
        show sb_blowjob up neutral with hpunch
        pc "That right?"
    elif randomnum == 3:
        show sb_blowjob poke tounge 1h with dissolve
        pc "Mmmm."
        show sb_blowjob closed suck angry 0h with hpunch
        pc "*HYUK*"
        show sb_blowjob up with dissolve
        pc "Mfffmfmfff..."
        tempname.name "Huh?"
        show sb_blowjob 1h face with dissolve
        pc "I said \"A little warning\"?"
        tempname.name "That's no fun."
    else:
        show sb_blowjob poke swallow 1h with dissolve
        pc "Ahhhhhh..."
        tempname.name "Bit early for that."
        show sb_blowjob laugh with dissolve
        pc "Mmm, just getting you warmed up for what's to come."
        tempname.name "Don't mind it in your mouth, but plenty of other places for it to go."
        if player.has_perk(perk_preg_want):
            pc "True, not going to get me pregnant if you cum in my mouth."
        else:
            pc "Hmm? Let's see then."
    show sb_blowjob down 1h poke neutral with dissolve
    jump school_field_soccer_sex_offer_sex_bj

label school_field_soccer_sex_offer_cont_wall:
    $ having_sex(5)
    $ renpy.scene()
    show sb_againstwall2
    with dissolve
    show sb_againstwall2 mast with dissolve
    pc "Putting something big in here hmmm?"
    show sb_againstwall2 pokevaghand with dissolve
    pc "Oooh, didn't think you would be poking me so soon."
    $ player.spank()
    pc "Oooh!"
    $ player.sex_location_offer()
    if player.want_sexlocation == 0:
        jump school_field_soccer_sex_offer_sex_bj
    elif player.want_sexlocation == 1:
        jump school_field_soccer_sex_offer_sex_vag
    else:
        jump school_field_soccer_sex_offer_sex_anal




label school_field_soccer_sex_offer_sex_bj:
    $ having_sex(5)
    pc "Mmmm ♥"
    $ player.sex_oral(tempname, school_soccer_quest)
    show sb_blowjob swallow with dissolve
    show sb_blowjob suck with dissolve
    "I try to take the full length of [tempname.name]'s cock in my mouth and start pleasuring him."
    $ dialouge = WeightedChoice([
    ("Mmmfff. Soo nice.", 1),
    ("Ah, more!", 1),
    ("Mmmff. So warm and nice.", 1),
    ("*Slurp*", 1),
    ("*Hyuk* *Hyuk* *Hyuk*", 1),
    ])
    pc "[dialouge]"

    $ school_soccer_pick_other_boy()
    $ temp_var_1 = tempname2.lust / 5 if loc_cur == loc_school_field_back else tempname2.lust / 2
    if t.timeofday == "night" and WeightedChoice([(True, temp_var_1),(False, 100)]):
        jump school_field_soccer_sex_offer_sex_spitroast



    show sb_blowjob 2h with dissolve
    $ dialouge = WeightedChoice([
    ("I start pumping him with my hands while bobbing my head back and forth on his cock, pretty much letting him facefuck me.", 1),
    ("I take his cock in both my hands and start working the shaft while still sucking and licking the tip of his cock.", 1),
    ("I get much more into it and take him in my hands, working the shaft while sliding my lips over his cockhead.", 1),
    ])
    "[dialouge]"
    tempname.name "Mmmmm fuck."
    show sb_blowjob up with dissolve
    $ dialouge = WeightedChoice([
    ("Let's put it somewhere warmer now.", 1),
    ("Think it's about time you bent over.", 1),
    ("Come here and let me fuck you.", 1),
    ("How about we change it up?", 1),
    ("Think somewhere else needs filled.", 1),
    ("Mmm, get up and bend over you little bitch.", 1),
    ])
    tempname.name "[dialouge]"
    $ player.sex_location_offer(
    diff=0,
    option1="Bend over",option2="Ask for anal", option3="Keep sucking",
    sex_vag_want="school_field_soccer_sex_offer_sex_vag",
    sex_anal="school_field_soccer_sex_offer_sex_anal",
    sex_other="school_field_soccer_sex_offer_sex_bj_cont",
    who=tempname.name
    )

label school_field_soccer_sex_offer_sex_bj_cont:
    $ having_sex(5)
    show sb_blowjob down with dissolve
    "I ignore him asking to fuck me and keep working his shaft and sucking on his cock. I'm not really interested in fucking him right now but wouldn't say no to having his cumming cock in my mouth."
    show sb_blowjob up
    pc "Mmmm ♥"
    show sb_blowjob down
    tempname.name "Ahhhh!"
    $ dialouge = WeightedChoice([
    ("It's clear from his reactions that he's enjoying himself so I continue to work at his cock and swirling my tongue around him inside my mouth.", 1),
    ("His actions make it clear he is having fun. I speed up working his shaft with my hands as I use my tongue to pleasure his cockhead.", 1),
    ("He rubs his fingers through my hair and tries to push his cock deeper into my mouth. I happily accept it and start working his shaft with my hands.", 1),
    ("He starts thrusting into my mouth in time with my head bobbing and eventually he is slowly fucking my mouth. I help him out by stroking his cock in time with his thrusts.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Mmmfff. Soo nice.", 1),
    ("Ah, more!", 1),
    ("Mmmff. So warm and nice.", 1),
    ("*Slurp*", 1),
    ("*Hyuk* *Hyuk* *Hyuk*", 1),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Sexy little slut. Keep going!", 1),
    ("Ah fuck, keep going like that and you will make me cum.", 1),
    ("Yes, fuck! Keep going...", 1),
    ("*Huff* *Huff* *Huffff*", 1),
    ])
    tempname.name "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I start to feel his cock tensing up and his movements become erratic. I know he is about to cum very soon.", 1),
    ("His groaning lets me know he is not far off cumming so I pick up the pace and blow him even faster than I was before.", 1),
    ("He is gripping onto my head and thrusting quite aggressively now. I know he won't last much longer at this rate so I work his shaft harder with my hands to try and push him over the edge.", 1),
    ])
    "[dialouge]"
    show sb_blowjob up laugh happy poke with dissolve
    pc "Someone's about to cum. ♥"
    tempname.name "Not far off."
    pc "Want to come over my face or in my mouth?"
    show sb_blowjob suck down with dissolve
    tempname.name "Ah fuck!"
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        tempname.name "Keep sucking!"
        jump school_field_soccer_sex_offer_sex_bj_cum_in
    elif randomnum == 2:
        tempname.name "Open your mouth."
        jump school_field_soccer_sex_offer_sex_bj_cum_out
    else:
        tempname.name "Your face."
        jump school_field_soccer_sex_offer_sex_bj_cum_face

label school_field_soccer_sex_offer_sex_bj_cum_in:
    $ having_sex(5)
    pc "Mmmff."
    "I start to feel his cock tensing up and his movements become erratic. I know he is about to cum in my mouth."
    tempname.name "Ah yes keep goingggg..."
    tempname.name "Ah yes!!"
    $ player.sex_cum(tempname, "mouth", school_soccer_quest)
    tempname.name "Ah fuck yes!!!"
    show sb_blowjob up with dissolve
    tempname.name "Yesss!"
    tempname.name "Ah shit. That was good."
    show sb_blowjob poke ub with dissolve
    show sb_blowjob noman with dissolve
    show sb_blowjob frown with dissolve
    show sb_blowjob swallow with dissolve
    pc "Ahhhh."
    tempname.name "Nice, swallowed it all up?"
    show sb_blowjob neutral with dissolve
    pc "Mmmm."
    jump school_field_soccer_sex_offer_sex_bj_wrapup

label school_field_soccer_sex_offer_sex_bj_cum_out:
    $ having_sex(5)
    show sb_blowjob poke swallow up with dissolve
    pc "Ik Is?"
    tempname.name "That's it!"
    show sb_blowjob down 2h with dissolve
    "I keep wanking him off while licking his cock, getting ready for him to cum in my mouth."
    $ player.sex_cum(tempname, "mouth", school_soccer_quest)
    tempname.name "Ah fuck yes!!!"
    show sb_blowjob up with dissolve
    tempname.name "Yesss!"
    tempname.name "Ah shit. That was good."
    show sb_blowjob poke ub with dissolve
    show sb_blowjob noman with dissolve
    show sb_blowjob frown with dissolve
    show sb_blowjob swallow with dissolve
    pc "Ahhhh."
    tempname.name "Nice, swallowed it all up?"
    show sb_blowjob neutral with dissolve
    pc "Mmmm."
    jump school_field_soccer_sex_offer_sex_bj_wrapup

label school_field_soccer_sex_offer_sex_bj_cum_face:
    $ having_sex(5)
    show sb_blowjob face swallow up 2h with dissolve
    "I lick the shaft of his cock while wanking him off with my hand, getting ready for him to come over my face."
    $ player.sex_cum(tempname, "face", school_soccer_quest)
    show sb_blowjob closed with dissolve
    tempname.name "Ah fuck yes!!!"
    tempname.name "Yesss!"
    tempname.name "Ah shit. That was good."
    show sb_blowjob up laugh with dissolve
    pc "Like what you see?"
    tempname.name "Perfect!"
    show sb_blowjob noman neutral with dissolve
    jump school_field_soccer_sex_offer_sex_bj_wrapup

label school_field_soccer_sex_offer_sex_bj_wrapup:
    $ having_sex(5)
    if school_class_hours():
        jump school_field_soccer_sex_offer_sex_wrapup_class
    $ randomnum = renpy.random.randint(1, 5)
    if loc_cur == loc_school_field_back and randomnum == 1:
        jump school_field_soccer_sex_offer_sex_buk
    else:
        hide sb_blowjob with dissolve
        tempname.name "That was fun."
        pc "Mmmm."
        $ renpy.scene()
        with dissolve
        if not ("exhibitionist_asked" in school_soccer_quest.conversation_topics and t.timeofday == "night"):
            $ pc_dress_slow()
        else:
            $ pc_set_temp_outfit()
        if loc_cur == loc_school_field_back:
            pc "Enjoy the show?"
            if not tempname == nate:
                nate.name "Sure did. It's a perfect look for you covered in cum."
            if not tempname == drake:
                nate.name "Who doesn't enjoy watching a naked perverted girl have fun?"
            if not tempname == dan:
                nate.name "Mmm, always fun watching you."
            pc "Heh."
        else:
            pc "Well, let's get back before that lot get bored."
            $ relax(20)
            $ walk(loc_school_field_back)
            pc "Still some beers left?"
            dan.name "Always."
        drake.name "Might wanna go clean up first though?"
        pc "Huh? Oh?"
        pc "Well, knowing you perverts you probably enjoy it."
        jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_offer_sex_wrapup_class:
    $ having_sex(5)
    tempname.name "That was fun."
    pc "Mmmm."
    $ renpy.scene()
    with dissolve
    $ pc_dress_slow()
    pc "Better get back before anyone notices we went missing."
    tempname.name "Right. I'll head in first."
    pc "Ok."
    if player.cum_visible_check():
        pcm "Better clean up before I leave."
        $ player.cum_clean_outside()
        pcm "There we go..."
    jump travel

label school_field_soccer_sex_offer_sex_buk:
    $ having_sex(5)
    $ temp_var_1 = [dan,nate,drake]
    $ temp_var_1.remove(tempname)
    $ tempname = temp_var_1.pop()
    $ tempname2 = temp_var_1.pop()
    $ npc_race_picker(tempname)
    pc "Err, what are you two doing?"
    tempname.name "Well, he's finished and you are still on your knees. So come here."
    show sb_blowjob suck closed angry 0h with hpunch
    pc "Mmmmmfff!!"
    pcm "Damn perverts..."
    pcm "Well, I probably did tease them a but much, heh."
    show sb_blowjob down straight with dissolve
    "I just accept that I will be getting all three of them off this time round and start sucking off [tempname.name] even though I have already taken a load over me."
    pcm "Maybe I will have all 3 of them all over my face. Kind of hot. ♥"
    "[tempname.name] continues to roughly facefuck me and I put up no resistance. I try to bob my head in time with him pulling me down on his cock, but he is being too erratic."
    pcm "Were they wanking off the entire time watching me?"
    "My question is answered very sortly after as [tempname.name] starts grunting and sounds like he is very close to cumming."
    "He is probably saying something but I can't really hear him as his hands are clasped over my ears as he grips my head and forces my face further down on his cock."

    tempname.name "Ahhhhhh!!!"
    show sb_blowjob closed angry with dissolve
    $ player.sex_cum(tempname, "mouth", school_soccer_quest)
    pc "Mmmmmfff!"
    tempname.name "Haaaaaaa! Fuck yes [name] you slut!"
    tempname.name "Haaaa..."
    show sb_blowjob ub happy up poke with dissolve
    show sb_blowjob nopenis with dissolve
    show sb_blowjob frown with dissolve
    show sb_blowjob laugh with dissolve
    $ npc_race_picker(tempname2)
    pc "Well that was... Oh?"
    show sb_blowjob face with dissolve
    pc "You want a turn as..."
    $ player.sex_cum(tempname2, "face", school_soccer_quest)
    show sb_blowjob closed with dissolve
    "I am not even able to finish my sentence as my face is hit with another load of cum, so I just close my eyes and feel it as he pumps it on my face."
    show sb_blowjob up worried frown with dissolve
    pc "Ok, some warning there should have been nice."
    show sb_blowjob nopenis neutral happy with dissolve
    pc "Well, have a good look you degenerates."
    pc "I have all three of your cum on my face. Happy?"
    nate.name "No better sight. Should be like this always."
    drake.name "Is pretty hot seeing you like this."
    dan.name "Mmm, it is."
    show sb_blowjob happy with dissolve
    pc "Heh, though so you perverts."
    drake.name "Yeah, says the girl smiling while covered in cum."
    pc "What? I am innocent! You perverts ambushed me. ♥"
    nate.name "Yeah yeah."
    $ renpy.scene()
    with dissolve
    pc "Well, better get cleaned up."
    if not ("exhibitionist_asked" in school_soccer_quest.conversation_topics and t.timeofday == "night"):
        $ pc_dress_slow()
    else:
        $ pc_set_temp_outfit()
    pc "Though bet you lot would prefer it if I stayed like this wouldn't you?"
    nate.name "Sure, show everyone what kind of person you really are."
    pc "A victim!"
    nate.name "Yeah sure..."
    drake.name "Want a beer?"
    pc "Sure."
    jump school_field_soccer_hangout_conv_end




label school_field_soccer_sex_offer_sex_mast:
    "Possible scene where the boy just watches you get off yourself. He may not may not join mid fun."




label school_field_soccer_sex_offer_sex_vag:
    $ pc_striptease()
    if player.vvirgin:
        jump school_field_soccer_sex_offer_sex_vag_virgin
    hide sb_blowjob with dissolve
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 pokevag with dissolve
    $ player.spank()
    show sb_againstwall2 wink happy with dissolve
    pc "Ah! ♥"
    tempname.name "Such a dirty girl."
    $ dialouge = WeightedChoice([
    ("I'm hanging out and fucking a group of boys and you only just realised?", 1),
    ("Of course. Why else would I be hanging around with you lot?", 1),
    ("Like you didn't already know I am a slut.", If(school_soccer_quest_boys_know["slut"], 1, 0)),
    ("Well I am a whore. I just like giving you lot freebies.", If(school_soccer_quest_boys_know["whore"], 1, 0)),
    ("Well we have fooled around enough for you to know just how dirty.", If(tempname.naughty > 5, 1, 0)),
    ("I let you assfuck me and you are only just saying that now?", If(tempname.asex, 1, 0)),
    ("Always going to be dirty for the person who took my virginity", If(tempname.vvirgin, 1, 0)),
    ])
    pc "[dialouge]"
    $ player.spank()
    pc "Haa! ♥"
    $ player.sex_vag(tempname, school_soccer_quest)
    show sb_againstwall2 insidevag closed ag worried with dissolve

    "I feel [tempname.name] gently easing his cock deeper inside me. I am already quite wet so it finds little resistance and is welcomed inside."
    pc "Ahh fuck! ♥"
    tempname.name "Mmmmm. So warm."
    if loc_cur == loc_school_field_back:
        "I feel [tempname.name] gently thrusting in and out of me. I focus entirely on his cock pleasuring me and completely forget that there is an audience watching me get fucked."
    elif loc_cur == loc_bushes:
        "I feel [tempname.name] gently thrusting in and out of me. I focus entirely on his cock pleasuring me and don't even pay attention to the fact I am being fucked in the bushes like a drunken nightclub slut."
    else:
        "I feel [tempname.name] gently thrusting in and out of me. I focus entirely on his cock pleasuring me and just let it wash over me."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        jump school_field_soccer_sex_offer_sex_vag_cum_premature

    $ dialouge = WeightedChoice([
    ("I then realise that I am fucking one cock, but getting the other two off at the same time by acting in a live show porn movie for them.", If(loc_cur == loc_school_field_back, 1, 0)),
    ("It makes me excited to know that I am getting fucked in the bushes like a common whore while the other boys are probably listening to my moans just a few footsteps away.", If(loc_cur == loc_bushes, 1, 0)),
    ("It makes me excited thinking how the other boys know what we are doing in here and how much of a dirty girl they must think I am.", 1),
    ])
    "[dialouge]"
    pc "Ahh yes! ♥"
    if loc_cur == loc_school_field_back:
        tempname.name "Ah fuck yes. You are lovin' it aren't you? Getting fucked with people watching."
        pc "Ha yes. You perverts enjoying as well? ♥"
    else:
        tempname.name "Ah fuck yes. You are lovin' it aren't you? Fucked here like a dirty bitch."
        pc "Ha yes. Keep going! ♥"
    $ player.spank()
    pc "Haa!"
    tempname.name "Ah yes, I'm gonna cum!"

    $ player.sex_cum_location_offer(
    difficulty=1,
    cum_want="school_field_soccer_sex_offer_sex_vag_cum_in", 
    cum_notwant="school_field_soccer_sex_offer_sex_vag_cum_in_notwant", 
    cum_pullout="school_field_soccer_sex_offer_sex_vag_cum_pullout",
    cum_pullout_anal="school_field_soccer_sex_offer_sex_vag_cum_vagtoass", 
    cum_pullout_bj="school_field_soccer_sex_offer_sex_vag_cum_pullout_bj",  
    cum_pullout_poke="school_field_soccer_sex_offer_sex_vag_cum_poke",
    cum_bj="school_field_soccer_sex_offer_sex_vag_cum_pullout_bj_start",    
    )

label school_field_soccer_sex_offer_sex_vag_cum_pullout_bj:
    tempname.name "Haaa! Come here, get on your knees."
    jump school_field_soccer_sex_offer_sex_vag_cum_pullout_bj_start

label school_field_soccer_sex_offer_sex_vag_cum_pullout_bj_start:
    hide sb_againstwall2
    show sb_blowjob up poke
    with dissolve
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show sb_blowjob suck down with dissolve
        jump school_field_soccer_sex_offer_sex_bj_cum_in
    elif randomnum == 2:
        jump school_field_soccer_sex_offer_sex_bj_cum_out
    else:
        jump school_field_soccer_sex_offer_sex_bj_cum_face

label school_field_soccer_sex_offer_sex_vag_cum_in_notwant:
    $ having_sex(5)
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 wink happy with dissolve
    else:
        show sb_doggy1 open ag with dissolve

    $ dialouge = WeightedChoice([
    ("Pull out. I don't want you knocking me up again!", If (not player.has_perk(perk_preg_want) and not player.preg_knows and tempname.preg, 1,0)),
    ("Ha fuck, Not inside!", 1),
    ("Cum outside!", 1),
    ])
    pc "[dialouge]"
    pc "♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    $ player.sex_cum(tempname,"inside", school_soccer_quest)
    "He presses into me as deep as he can and I feel his cock start to pulse inside me. No doubt making sure I take every drop he has to give me."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 shock with dissolve
    pc "Ah I can feel you pumping in me. I told you outside!"
    tempname.name "Fuck ahhhh!"
    tempname.name "Yes!!!"
    pc "Idiot!"
    tempname.name "Haa you dirty girl."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 open neutral with dissolve
    else:
        show sb_doggy1 open neutral with dissolve
    pc "Mmmm..."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 pokevag with dissolve
        show sb_againstwall2 noman with dissolve
        show sb_againstwall2 mast with dissolve
    else:
        show sb_doggy1 poke with dissolve
        show sb_doggy1 noman with dissolve
    pc "I am all leaking now."
    if player.has_perk(perk_preg_want) and not player.preg_knows:
        pc "Wonder if you managed to knock me up?"
        tempname.name "Don't say such things."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup

label school_field_soccer_sex_offer_sex_vag_cum_in:
    $ having_sex(5)
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 wink happy with dissolve
    else:
        show sb_doggy1 open ag with dissolve

    $ dialouge = WeightedChoice([
    ("Ah keep going. Hope you don't knock me up again!", If (not player.has_perk(perk_preg_want) and not player.preg_knows and tempname.preg, 1,0)),
    ("Ah keep going. Hope you don't knock me up!", If (not player.has_perk(perk_preg_want) and not player.preg_knows and not tempname.preg, 1,0)),
    ("You already knocked me up so you can cum inside again.", If (tempname.preg_knows, 1,0)),
    ("I am already pregnant so come inside.", If (player.preg_knows, 1,0)),
    ("Ah yes, cum inside my fat belly.", If (player.pregnancy >= 2, 1,0)),
    ("Cum in me like a whore!", If (player.iswhore, 1,0)),
    ("Fuck. Fill me up like everyone else does!", If (player.isbroken , 1,0)),
    ("Ha fuck, don't stop!", 1),
    ("Keep going!", 1),
    ])
    pc "[dialouge]"
    pc "♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    $ player.sex_cum(tempname,"inside", school_soccer_quest)
    "He presses into me as deep as he can and I feel his cock start to pulse inside me. No doubt making sure I take every drop he has to give me."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 vhappy with dissolve
    pc "Ah I can feel you pumping in me."
    tempname.name "Fuck ahhhh!"
    tempname.name "Yes!!!"
    $ player.spank()
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum == 1:
        pc "Fuck, you like spanking me don't you?"
        tempname.name "With the way you tighten when I do, seems you love it as well."
        $ player.spank()
        if renpy.showing("sb_againstwall2"):
            show sb_againstwall2 closed with dissolve
        else:
            show sb_doggy1 closed with dissolve
        pc "Ha! ♥"
        tempname.name "See?"
        $ player.spank()
        pc "Ah fuck!"
    tempname.name "Haa you dirty girl."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 open neutral with dissolve
    else:
        show sb_doggy1 open neutral with dissolve
    pc "Mmmm..."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 pokevag with dissolve
        show sb_againstwall2 noman with dissolve
        show sb_againstwall2 mast with dissolve
    else:
        show sb_doggy1 poke with dissolve
        show sb_doggy1 noman with dissolve
    pc "I am all leaking now."
    if player.has_perk(perk_preg_want) and not player.preg_knows:
        pc "Wonder if you managed to knock me up?"
        tempname.name "Don't say such things."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup

label school_field_soccer_sex_offer_sex_vag_cum_poke:
    $ having_sex(5)
    $ dialouge = WeightedChoice([
    ("I'm gonna cum on your ass. Don't wanna be giving you another one of my kids!", If (not player.has_perk(perk_preg_want) and not player.preg_knows and tempname.preg, 1,0)),
    ("Mmm, I'm gonna cum all over that fat arse of yours!", If (player.pregnancy >= 2, 1,0)),
    ("Ahhh, let me cover you like the whore you are!", If (player.iswhore, 1,0)),
    ("Mmm, I'll cover your arse with it. Don't wanna be knocking you up.", If (not player.preg_knows, 1,0)),
    ("Mmm, I'm gonna cum all over your sexy ass.", 1),
    ("Ahh I'm gonna cover you with cum!", 1),
    ])
    tempname.name "[dialouge]"
    pc "♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 pokevaghand with dissolve
    else:
        show sb_doggy1 poke with dissolve
    $ player.sex_cum(tempname,"pullout", school_soccer_quest)
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 shock open worried with dissolve
    else:
        show sb_doggy1 worried open with dissolve
    "He quickly pulls out and starts masturbating while poking his cock against my pussy. I can then feel his warm wetness squirt against my lips and start running down my legs."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 frown with dissolve
    else:
        show sb_doggy1 shock with dissolve
    if not player.preg_knows:
        pc "Ah I can feel you cumming. Pull out more than that."
        tempname.name "Fuck ahhhh!"
        tempname.name "Yes!!!"
        pc "Idiot. Cumming like that can still be dangerous."
        tempname.name "Haaaaa!"
    else:
        pc "Mmm, I can still feel you putting it in me even though you pulled out."
        tempname.name "Fuck ahhhh!"
        tempname.name "Yes!!!"
        pc "If I wasnt already pregnant, you could knock me up like that."
        tempname.name "Haaaaa!"
    pcm "He's not even listening..."
    tempname.name "Haa you dirty girl."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 neutral with dissolve
    else:
        show sb_doggy1 neutral with dissolve
    pc "Mmmm..."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 pokevag with dissolve
        show sb_againstwall2 noman with dissolve
        show sb_againstwall2 mast with dissolve
    else:
        show sb_doggy1 poke with dissolve
        show sb_doggy1 noman with dissolve
    pc "I am all leaking now."
    if player.has_perk(perk_preg_want) and not player.preg_knows:
        pc "Wonder if you managed to knock me up?"
        tempname.name "Don't say such things."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup

label school_field_soccer_sex_offer_sex_vag_cum_pullout:
    $ having_sex(5)
    tempname.name "Mmm, I'll cover your arse with it. Don't wanna be knocking you up."
    pc "♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 cum with dissolve
    else:
        show sb_doggy1 poke with dissolve
    $ player.sex_cum(tempname,"pullout", school_soccer_quest)
    "He quickly pulls his cock out and I immediately feel his warmth splatter on my arse and start to run down between my cheeks and legs."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 vhappy with dissolve
    else:
        show sb_doggy1 oh with dissolve
    pc "Ah I can feel you putting it all over me."
    tempname.name "Fuck ahhhh!"
    tempname.name "Yes!!!"
    $ player.spank()
    tempname.name "Haa you dirty girl."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 open neutral with dissolve
    else:
        show sb_doggy1 open neutral with dissolve
    pc "Mmmm..."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 noman with dissolve
    else:
        show sb_doggy1 noman with dissolve
    pc "I am covered in it now."
    tempname.name "Good."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup

label school_field_soccer_sex_offer_sex_vag_cum_vagtoass:
    $ having_sex(5)
    tempname.name "Mmm, I'll cover your arse with it. Don't wanna be knocking you up."
    pc "♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 pokevaghand with dissolve
        show sb_againstwall2 pokeasshand with dissolve
        show sb_againstwall2 pokeass open shock with dissolve
    else:
        show sb_doggy1 poke open shock with dissolve
    pc "Err, what are..."
    $ player.sex_anal(tempname, school_soccer_quest)
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 insideass with dissolve
    else:
        show sb_doggy1 anal with dissolve
    pc "Haaa fuck what are you... Haaaaa ♥"
    "It's not like my ass is not used to having a man inside it, especially not [tempname.name]'s, so with his cock being covered in my juices and pre cum it doesn't take long for me to get used to the sudden penetration."
    "A good thing too, since because he is so close to cumming, he fucks me in the arse at a pretty rapid pace. Gripping onto my cheeks and fucking me deep right off the bat."
    pc "You sneaky git putting it up my arse! Ah fuck keep going!"
    tempname.name "Ahhhhhh!!"
    $ player.sex_cum(tempname,"anal", school_soccer_quest)
    $ if_showing("sb_againstwall2", "wink happy", "sb_doggy1", "open ah")
    tempname.name "Yes yes yeeeees!"
    pc "Oooooohhh!!"
    tempname.name "Haaaaaaa fuck so nice."
    pc "Mmmmm."
    tempname.name "*Pheeew*"
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 pokeass with dissolve
        show sb_againstwall2 noman with dissolve
    else:
        show sb_doggy1 poke with dissolve
        show sb_doggy1 noman with dissolve
    "He slides his cock out my ass and I feel a trickle of his cum leak out along with it."
    pc "Ah now I am all leaking. It's going to keep me all wet."
    $ player.spank()
    $ if_showing("sb_againstwall2", "shock", "sb_doggy1", "shock")
    tempname.name "You love it you dirty girl."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup

label school_field_soccer_sex_offer_sex_vag_cum_wrapup:
    $ having_sex(5)
    if school_class_hours():
        jump school_field_soccer_sex_offer_sex_wrapup_class
    pc "Mmmm."
    $ player.spank()
    pause 0.1
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 shock with dissolve
    else:
        show sb_doggy1 shock with dissolve
    pc "Ah!"
    $ randomnum = renpy.random.randint(1, 10)
    if loc_cur == loc_school_field_back and randomnum == 1:
        jump school_field_soccer_sex_offer_sex_vag_cum_wrapup_int
    tempname.name "Unless you want someone else to take a turn, come and have a beer."
    if renpy.showing("sb_againstwall2"):
        show sb_againstwall2 neutral with dissolve
    else:
        show sb_doggy1 neutral with dissolve
    pc "Mmm."
    $ renpy.scene()
    with dissolve
    if not ("exhibitionist_asked" in school_soccer_quest.conversation_topics and t.timeofday == "night"):
        $ pc_dress_slow()
    else:
        $ pc_set_temp_outfit()
    $ walk(loc_school_field_back)
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_offer_sex_vag_cum_wrapup_int:
    $ having_sex(5)
    tempname.name "Unless you want someone else to... Oh?"
    $ school_soccer_pick_new_boy()
    $ npc_race_picker(tempname)
    show sb_againstwall2 cum shock worried with dissolve
    tempname.name "Too late."
    if player.want_sexlocation == 1:
        jump school_field_soccer_sex_offer_sex_vag_cum_wrapup_int_vag
    else:
        jump school_field_soccer_sex_offer_sex_vag_cum_wrapup_int_anal

label school_field_soccer_sex_offer_sex_vag_cum_wrapup_int_vag:
    $ having_sex(5)
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 pokevag with dissolve
    pc "[tempname.name]? Who said you could start poking me there?"
    $ player.spank()
    pc "Ah!"
    show sb_againstwall2 insidevag ag wink straight with dissolve
    $ player.sex_vag(tempname, school_soccer_quest)
    pc "Haaaaa..."
    pc "What is this. A fuck [name] train or something?"
    tempname.name "Sure. Why not?"
    tempname.name "Watching you already get fucked kind of got me excited so I waited my turn."
    pc "Perverts."
    tempname.name "Mmmm."
    pc "You already close?"
    tempname.name "Ahhh yeah, I was having fun watching you be a slut."
    pc "Ooh, playing with yourself while watching me?"
    tempname.name "Haaa! Fuck, come here, get on your knees."
    pc "Oh?"
    hide sb_againstwall2
    show sb_blowjob up poke
    with dissolve
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show sb_blowjob suck down with dissolve
        jump school_field_soccer_sex_offer_sex_bj_cum_in
    elif randomnum == 2:
        jump school_field_soccer_sex_offer_sex_bj_cum_out
    else:
        jump school_field_soccer_sex_offer_sex_bj_cum_face

label school_field_soccer_sex_offer_sex_vag_cum_wrapup_int_anal:
    $ having_sex(5)
    show sb_againstwall2 pokeasshand with dissolve
    show sb_againstwall2 pokeass with dissolve
    pc "[tempname.name]? Who said you could start poking me there?"
    $ player.spank()
    pc "Ah!"
    show sb_againstwall2 insideass ag wink straight with dissolve
    $ player.sex_anal(tempname, school_soccer_quest)
    pc "Haaaaa..."
    pc "What is this. A fuck [name] train or something?"
    tempname.name "Sure. Why not?"
    tempname.name "Watching you already get fucked kind of got me excited so I waited my turn."
    pc "Perverts."
    tempname.name "Mmmm."
    pc "You already close?"
    tempname.name "Ahhh yeah, I was having fun watching you be a slut."
    pc "Ooh, playing with yourself while watching me?"
    tempname.name "Ah yeah. Couldn't resist."
    pc "Mmmm, using me as your porn? Getting off..."
    $ player.sex_cum(tempname,"anal", school_soccer_quest)
    tempname.name "Ahhhhhhhhh!!!"
    pc "Oooh?"
    tempname.name "Take it in your arse you bitch!"
    pc "Mmmm, doesn't look like I have much choice."
    tempname.name "Haaaaaa..."
    pc "Mmm, that scratch an itch?"
    $ player.spank()
    tempname.name "It did."
    show sb_againstwall2 pokeass open straight neutral with dissolve
    show sb_againstwall2 noman with dissolve
    pc "Ah, I am leaking so much..."
    pc "*Sigh*"
    pc "Better have a beer ready for me."
    $ renpy.scene()
    with dissolve
    if not ("exhibitionist_asked" in school_soccer_quest.conversation_topics and t.timeofday == "night"):
        $ pc_dress_slow()
        pc "There we go."
    else:
        $ pc_set_temp_outfit()

    jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_offer_sex_anal:
    $ pc_striptease()
    $ having_sex(5)
    hide sb_blowjob with dissolve
    show sb_againstwall2 pokeasshand with dissolve
    if player.asex == 0:
        pc "Go slowly though, this is the first time taking it in the ass."
    elif player.asex < 5:
        pc "Be nice though. I haven't done this many times before."
    tempname.name "I'll use here to lube up a bit first."
    show sb_againstwall2 pokevaghand with dissolve
    pc "Ha!"
    "I feel him rubbing his cockhead between my lips to lube up his cock in preparation for putting it in my ass."
    if player.vvirgin:
        pc "Don't poke too deep. I don't want this to be my first time."
        tempname.name "Sure, don't worry."
    pc "Mmmm ♥"
    tempname.name "Enjoying being rubbed there. Maybe next time I'll take you deep here instead."
    pc "Next time..."
    show sb_againstwall2 pokeasshand with dissolve
    show sb_againstwall2 pokeass with dissolve
    tempname.name "Ready?"
    pc "Mmmm."
    if player.asex < 5:
        show sb_againstwall2 wink pain worried with dissolve
        "I feel him gently start to ease himself inside my ass as I try to keep relaxed to accommodate his cock. It's not easy though as I haven't had it here too often so it is fairly painful to start with."
        "He slowly and gently thrusts a little deeper each time as my ass relaxes some more to let him inside me."
        show sb_againstwall2 insideass with dissolve
        $ player.sex_anal(tempname, school_soccer_quest)
        pc "Haa fuck!"
    else:
        show sb_againstwall2 ag wink worried with dissolve
        "I feel him ease his way into my arse and feel myself stretching as he fills me up. He takes gentle thrusts with each one getting deeper and deeper until I can feel his body pressing against my ass."
        show sb_againstwall2 insideass with dissolve
        $ player.sex_anal(tempname, school_soccer_quest)
        pc "Ah fuck yes!"
    pc "Fuck! ♥"
    tempname.name "Mmmmm. Such a sexy ass."
    show sb_againstwall2 closed ag with dissolve
    "I close my eyes and just focus on the pleasure I am being given. It takes me a moment to remember that the others are watching [tempname.name] fuck me in the arse out here."
    show sb_againstwall2 wink with dissolve
    pc "You perverts having fun watching [tempname.name] fuck me in the arse?"
    $ player.spank()
    pc "Ahh! ♥"
    tempname.name "Be quiet."
    pc "Mmmm."
    $ player.spank()
    pc "♥"
    "[tempname.name] picks up the pace and fucks me a bit more roughly while gripping his fingers into my ass cheeks."
    "Through the fog of pleasure I realise he has got to the point where he is pulling out almost to the tip, then thrusting back inside with a slap as his cock is pushed to the hilt as his body slaps against my ass."
    pc "Fucking hell! ♥"
    $ player.spank()
    tempname.name "Ah fuck yes!"
    "Now he is pounding away at my arse with his hands locked onto my hips, pulling me as deep as possible onto his cock."
    show sb_againstwall2 closed
    "Despite being fucked in the ass with an audience, I feel the pleasure building up inside me as he fucks harder and harder."
    tempname.name "Ah yes!"
    pc "♥"
    $ player.sex_cum(tempname,"anal", school_soccer_quest)
    tempname.name "Ahhh fuck yes take it!"
    pc "Haaa yes. Fuuuck..."
    tempname.name "Haaaaa. Fuck that was good."
    pc "Mmmmm."
    show sb_againstwall2 pokeass open shock with dissolve
    pc "Ah slowly..."
    pc "Phew."
    show sb_againstwall2 noman neutral straight with dissolve
    pc "Fuck, I am going to be feeling that for a while."
    $ player.spank()
    pause 0.1
    show sb_againstwall2 pain closed
    tempname.name "And that."
    show sb_againstwall2 neutral open with dissolve
    pc "Idiot!"
    tempname.name "Come and celebrate your ass fucking with a beer."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup




label school_field_soccer_sex_offer_sex_vag_virgin:
    $ having_sex(5)
    hide sb_blowjob with dissolve
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 pokevag with dissolve
    $ player.spank()
    show sb_againstwall2 wink happy with dissolve
    pc "Ah! ♥"
    tempname.name "Such a dirty girl."
    pc "Be a bit gentle, this is my first time."
    tempname.name "I know, don't worry. I'll make you feel good."
    tempname.name "Hold on, a bit gentle?"
    pc "Some rough play is fine. ♥"
    $ player.spank()
    pc "Haa! ♥"
    tempname.name "Like this?"
    pc "Mmmmm."
    $ player.spank()
    pc "Hooo, you are gonna leave me with a red ass."
    tempname.name "Well, get ready for more than a red arse."
    pc "Oooh?"
    $ player.sex_vag(tempname, school_soccer_quest)
    show sb_againstwall2 insidevag closed ag worried with dissolve

    "I feel [tempname.name] gently easing his cock deeper inside me. I am already quite wet so despite it being my first time, it doesn't hurt as much as I expected it might."
    pc "Ahh fuck! ♥"
    tempname.name "Mmmmm. So warm."
    if loc_cur == loc_school_field_back:
        "I feel [tempname.name] gently thrusting in and out of me. I focus entirely on his cock pleasuring me and completely forget that there is an audience watching me lose my virginity."
    elif loc_cur == loc_bushes:
        "I feel [tempname.name] gently thrusting in and out of me. I focus entirely on his cock pleasuring me and don't even pay attention to the fact I am losing my virginity in the bushes like a drunken nightclub slut."
    else:
        "I feel [tempname.name] gently thrusting in and out of me. I focus entirely on his cock pleasuring me and just let it wash over me."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        jump school_field_soccer_sex_offer_sex_vag_cum_premature

    $ dialouge = WeightedChoice([
    ("I then realise that I am fucking one cock, but getting the other two off at the same time by acting in a live show porn movie for them.", If(loc_cur == loc_school_field_back, 1, 0)),
    ("It makes me excited to know that I am getting fucked in the bushes like a common whore while the other boys are probably listening to my moans just a few footsteps away.", If(loc_cur == loc_bushes, 1, 0)),
    ("It makes me excited thinking how the other boys know what we are doing in here and how much of a dirty girl they must think I am.", 1),
    ])
    "[dialouge]"
    pc "Ahh yes! ♥"
    if loc_cur == loc_school_field_back:
        tempname.name "Ah fuck yes. You are lovin' it aren't you? Getting fucked with people watching."
        pc "Ha yes. You perverts enjoying as well? ♥"
    else:
        tempname.name "Ah fuck yes. You are lovin' it aren't you? Fucked here like a dirty bitch."
        pc "Ha yes. Keep going! ♥"
    $ player.spank()
    pc "Haa!"
    tempname.name "Ah yes, I'm gonna cum!"
    $ player.sex_cum_location_offer(
    difficulty=1,
    cum_want="school_field_soccer_sex_offer_sex_vag_cum_in", 
    cum_notwant="school_field_soccer_sex_offer_sex_vag_cum_in_notwant", 
    cum_pullout="school_field_soccer_sex_offer_sex_vag_cum_pullout",
    cum_pullout_anal="school_field_soccer_sex_offer_sex_vag_cum_vagtoass", 
    cum_pullout_bj="school_field_soccer_sex_offer_sex_vag_cum_pullout_bj",  
    cum_pullout_poke="school_field_soccer_sex_offer_sex_vag_cum_poke",
    cum_bj="school_field_soccer_sex_offer_sex_vag_cum_pullout_bj_start",    
    )

label school_field_soccer_sex_offer_sex_vag_virgin_cum_out:
    $ having_sex(5)
    tempname.name "Mmm, shame. Would be so nice to cum in your virgin pussy."
    pc "Not a virgin anymore. ♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    show sb_againstwall2 cum with dissolve
    $ player.sex_cum(tempname,"pullout", school_soccer_quest)
    "He quickly pulls his cock out and I immediately feel his warmth splatter on my arse and start to run down between my cheeks and legs."
    show sb_againstwall2 vhappy with dissolve
    pc "Ah I can feel you putting it all over me."
    tempname.name "Fuck ahhhh!"
    tempname.name "Yes!!!"
    $ player.spank()
    tempname.name "Haa you dirty girl."
    show sb_againstwall2 open neutral with dissolve
    pc "Mmmm..."
    show sb_againstwall2 noman with dissolve
    pc "I am covered in it now."
    tempname.name "Good."
    jump school_field_soccer_sex_offer_sex_vag_virgin_cum_wrapup

label school_field_soccer_sex_offer_sex_vag_virgin_cum_in:
    $ having_sex(5)
    show sb_againstwall2 wink happy with dissolve
    pc "♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    $ player.sex_cum(tempname,"inside", school_soccer_quest)
    "He presses into me as deep as he can and I feel his cock start to pulse inside me. No doubt making sure I take every drop he has to give me."
    show sb_againstwall2 vhappy with dissolve
    pc "Ah I can feel you pumping in me."
    tempname.name "Fuck ahhhh!"
    tempname.name "Yes!!!"
    $ player.spank()
    pc "Fuck, you like spanking me don't you?"
    tempname.name "With the way you tighten when I do, seems you love it as well."
    $ player.spank()
    show sb_againstwall2 closed with dissolve
    pc "Ha! ♥"
    tempname.name "See?"
    $ player.spank()
    pc "Ah fuck!"
    tempname.name "Haa you dirty girl."
    show sb_againstwall2 open neutral with dissolve
    pc "Mmmm..."
    show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 noman with dissolve
    show sb_againstwall2 mast with dissolve
    pc "I am all leaking now."
    jump school_field_soccer_sex_offer_sex_vag_virgin_cum_wrapup

label school_field_soccer_sex_offer_sex_vag_virgin_cum_wrapup:
    $ having_sex(5)
    if school_class_hours():
        jump school_field_soccer_sex_offer_sex_wrapup_class
    pc "Mmmm."
    $ player.spank()
    pause 0.1
    show sb_againstwall2 shock with dissolve
    pc "Ah!"
    tempname.name "Fuck that was good."
    show sb_againstwall2 neutral with dissolve
    pc "Mmm."
    $ renpy.scene()
    with dissolve
    if not ("exhibitionist_asked" in school_soccer_quest.conversation_topics and t.timeofday == "night"):
        $ pc_dress_slow()
    else:
        $ pc_set_temp_outfit()
    if loc_cur == loc_school_field_back:
        jump school_field_soccer_sex_offer_sex_vag_virgin_post_field
    else:
        jump school_field_soccer_sex_offer_sex_vag_virgin_post_notfield

label school_field_soccer_sex_offer_sex_vag_virgin_post_field:

    if not tempname == drake:
        drake.name "So finally a woman?"
        if player.cum_vagin:
            pc "Huh? Was one before. Just now I am one that is leaking cum."
        else:
            pc "Huh? Was one before. Just now I am one who has had [tempname.name]'s cock in her."
        drake.name "Won't be the last time I recon."
        pc "Pssh. Still got you two perverts to get through. ♥"
        drake.name "Heh, can't wait!"
        pc "Mmmm."
    else:
        nate.name "So [tempname.name] made you a woman? Who's next on your list?"
        pc "Shuch [nate.name]. Don't ruin the moment."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_offer_sex_vag_virgin_post_notfield:
    $ walk(loc_school_field_back)
    if not tempname == drake:
        drake.name "So finally a woman?"
        if player.cum_vagin:
            pc "Huh? Was one before. Just now I am one that is leaking cum."
            drake.name "Leaking? You let him cum in you?"
            pc "Sure why not? A time for many firsts."
            drake.name "Yeah, first time for a baby as well?"
            if player.cycle_conditions["stage"] == "mens":
                pc "Ah no worries, I am on my period as well so won't happen."
                drake.name "Oooh, period sex as well? Being adventurous."
            elif player.cycle_conditions["stage"] == "foll":
                pc "Ah no worries, my period just finished so should be safe."
                drake.name "Well, good luck."
            elif player.cycle_conditions["stage"] == "lut":
                pc "Ah no worries, my period is round the corner so should be safe."
                drake.name "Well, good luck."
            elif player.cycle_conditions["stage"] == "ovulate":
                pc "Yeah, probably a bad idea... But whatever."
                drake.name "Whatever?"
                pc "Eh what's to worry about. Better [tempname.name] knocking me up than some shitty rapist that there seems to be hundreds of round here."
                pc "Or some degenerate who offers me a bunch of money."
                pc "Have fun while I can. Lot of people out there who wants to make me miserable so I will enjoy it while I can."
                drake.name "Okay..."
        else:

            pc "Huh? Was one before. Just now I am one who has had [tempname.name]'s cock in her."
        drake.name "Won't be the last time I recon."
        pc "Pssh. Still got you two perverts to get through. ♥"
        drake.name "Heh, can't wait!"
        pc "Mmmm."
    else:
        nate.name "So [tempname.name] made you a woman? Who's next on your list?"
        pc "Shush [nate.name]. Don't ruin the moment."
    jump school_field_soccer_hangout_conv_end







label school_field_soccer_sex_offer_sex_spitroast:
    show sb_blowjob suck eangry worried with dissolve
    pcm "Huh? What's that?"
    pcm "Ah shit!"
    $ renpy.scene()
    $ npc_race_picker_2(tempname2)
    show sb_spitroast back cum blow worried
    with dissolve
    show sb_spitroast happy straight mast with dissolve
    pc "What are you up to pervert?"
    tempname2.name "No point in letting [tempname.name] have all the fun."
    if player.check_sex_agree(4):
        pc "Dirty boy."
    else:
        pc "Err... Who said you could jump in?"
        $ player.spank()
        tempname2.name "I did."
        pc "Ugh."
    $ player.sex_location_offer()
    show sb_spitroast down blow with dissolve
    if player.want_sexlocation == 1:
        jump school_field_soccer_sex_offer_sex_spitroast_vag
    elif player.want_sexlocation == 2:
        jump school_field_soccer_sex_offer_sex_spitroast_anal
    else:
        if tempname2.vsex > tempname2.asex:
            jump school_field_soccer_sex_offer_sex_spitroast_vag
        else:
            jump school_field_soccer_sex_offer_sex_spitroast_anal

label school_field_soccer_sex_offer_sex_spitroast_anal:
    $ dialouge = WeightedChoice([
    ("I feel him wanking behind me and hitting his cock against my arse.", 1),
    ("I can feel him stroking his cock and hitting it against my ass.", 1),
    ])
    "[dialouge]"
    "I decide to wiggle my bum around and rub it against his cock to tease him some more. His hand grips onto my arse cheek as he wanks off on my bum."
    "Now and then he slides his cock between my wet folds, no doubt looking to lube up a bit before fucking me in the arse."
    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy2 pokeasshold blow head_forward
    with dissolve
    "Eventually he settes on his mark and I feel his cockhead press against my arsehole."
    pc "Mmmmmm."
    show sb_doggy2 pokeass with dissolve
    "I gently ease back onto his cock, letting it slide up my arse at my own pace. First the tip and then gently down the length of his cock."
    show sb_doggy2 insideass with dissolve
    $ player.sex_anal(tempname2)
    pc "Mmmmmmmffff."

    call school_field_soccer_sex_offer_sex_spitroast_cont from _call_school_field_soccer_sex_offer_sex_spitroast_cont

    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy1 blow anal
    with dissolve
    $ player.spank()
    "I had almost forgotten about [tempname2.name] while taking [tempname.name]'s load. But he quickly reminds me with a slap to my arse and picking up the pace with fucking me."
    pc "Ahhh!"
    "With [tempname.name] done, he gets up and leaves me at the mercy of [tempname2.name] fucking me in the arse."
    show sb_doggy1 no_blow head_down ag closed worried with dissolve
    "His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit."
    show sb_doggy1 open
    tempname2.name "Ahhh I am close."
    $ player.sex_cum(tempname2,"anal")
    tempname2.name "Ahhhh fuck yes."
    $ player.spank()
    tempname2.name "Haaaaaa..."
    pc "Oooh!"
    tempname2.name "Ah fuck yes. Nice little arse to fuck."
    pc "How romantic!"
    show sb_doggy1 poke neutral with dissolve
    show sb_doggy1 noman with dissolve
    pc "*Phew*"
    pc "Unnnng! My arse is on fire now and I have you leaking out of me."
    tempname2.name "Mmmm, I can see it."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup

label school_field_soccer_sex_offer_sex_spitroast_vag:
    $ dialouge = WeightedChoice([
    ("I feel him wanking behind me and hitting his cock against my arse.", 1),
    ("I can feel him stroking his cock and hitting it against my ass.", 1),
    ])
    "[dialouge]"
    "I decide to wiggle my bum around and rub it against his cock to tease him some more. His hand grips onto my arse cheek as he wanks off on my bum."
    "Now and then he slides his cock between my wet folds, poking a little into me but not all the way."
    pcm "Tease."
    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy2 pokevaghold blow head_forward
    with dissolve
    pc "Mmmmmm."
    show sb_doggy2 pokevag with dissolve
    "Eventually he settes on his mark and I feel him press his cockhead into me and ease himself all the way inside."
    show sb_doggy2 insidevag with dissolve
    $ player.sex_vag(tempname2)
    pc "Mmmmmmmffff."

    call school_field_soccer_sex_offer_sex_spitroast_cont from _call_school_field_soccer_sex_offer_sex_spitroast_cont_1

    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy1 blow vag
    with dissolve
    $ player.spank()
    "I had almost forgotten about [tempname2.name] while taking [tempname.name]'s load. But he quickly reminds me with a slap to my arse and picking up the pace with fucking me."
    pc "Ahhh!"
    "With [tempname.name] done, he gets up and leaves me at the mercy of [tempname2.name] fucking me and clawing at my arse."
    show sb_doggy1 no_blow head_down ag closed worried with dissolve
    "His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit."
    show sb_doggy1 open
    tempname2.name "Ahhh I am close."

    $ npc_name_switch()

    $ player.sex_cum_location_offer("Keep silent", "Not inside", 0)
    if player.want_pullout:
        $ randomnum = renpy.random.randint(1,3)
        if randomnum == 1:
            jump school_field_soccer_sex_offer_sex_vag_cum_pullout
        elif randomnum == 2:
            jump school_field_soccer_sex_offer_sex_vag_cum_poke
        else:
            jump school_field_soccer_sex_offer_sex_vag_cum_vagtoass
    else:
        jump school_field_soccer_sex_offer_sex_vag_cum_in

label school_field_soccer_sex_offer_sex_spitroast_cont:
    tempname2.name "Ahh fuck!"
    pc "Mmmff!"
    tempname.name "Don't slow down [name]."
    "We eventually settle into a rythmn where my mouth has all of [tempname.name]'s cock in it, until [tempname2.name] pulls me down onto his cock and I take him all the way inside me."
    $ player.spank()
    "Sandwiched between them, I can hardly squeek out even a moan as I am fucked from the front and back. I just stick with the rythmn and enjoy what is happening to me."
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    tempname.name "[dialouge]"
    pc "Mmmfff!"
    "I can hear [tempname.name] breathing heavier and it seems like he is close to the edge."
    $ player.face_shy()
    $ dialouge = WeightedChoice([
    ("Yes, yes!", 1),
    ("Ahhhhh fuck yes.", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh I am close.", 1),
    ("Ahhhhh yes you dirty bitch.", 1),
    ])
    tempname.name "[dialouge]"
    $ renpy.scene()
    $ npc_race_switch()
    show sb_spitroast closed sex blow
    with dissolve
    tempname.name "Ah fuck!"
    show sb_spitroast happy up sex mast with dissolve
    pc "I can feel you getting close."
    tempname.name "Mmmm."
    if renpy.random.randint(1, 2) == 1:
        "I continue wanking him off so that I can feel him cum all over my lips and face."
        tempname.name "Want it over you do you?"
        pc "Mmm. I do. ♥"
        tempname.name "Haaaaaa..."
        pc "Mmm, give it to me."
        $ player.sex_cum(tempname, "face")
        tempname.name "Ahhhhhhhh!"
        "He starts to cum and I feel it squirting onto my face and running down over my lips and into my mouth."
        pc "Mmmm. That's a lot."
        tempname.name "Fuck that was nice!"
    else:
        show sb_spitroast sex blow with dissolve
        "I carry on sucking him knowing he is about to blow his load at any moment."
        tempname.name "Ah dirty girl wants it in her mouth?"
        pc "Mmmmm."
        tempname.name "Haaaaaa..."
        $ player.sex_cum(tempname, "mouth")
        tempname.name "Ahhhhhhhh!"
        "I feel his cock throbbing in my mouth and the taste of his cum on my tounge. I keep sucking and swallowing as he pumps more into me."
        pc "Mmmmmfff."
        tempname.name "Fuck that was nice!"
        show sb_spitroast up mast happy with dissolve
        pc "*Phew*"
        pc "Like that did you? ♥"

    return

label school_field_soccer_sex_offer_sex_spitroast_vag_cum_inside:
    $ having_sex(5)
    show sb_doggy1 closed ag with dissolve
    $ dialouge = WeightedChoice([
    ("Ah keep going. Hope you don't knock me up again!", If (not player.has_perk(perk_preg_want) and not player.preg_knows and tempname.preg, 1,0)),
    ("Ah keep going. Hope you don't knock me up!", If (not player.has_perk(perk_preg_want) and not player.preg_knows and not tempname.preg, 1,0)),
    ("You already knocked me up so you can cum inside again.", If (tempname.preg_knows, 1,0)),
    ("I am already pregnant so come inside.", If (player.preg_knows, 1,0)),
    ("Ah yes, cum inside my fat belly.", If (player.pregnancy >= 2, 1,0)),
    ("Cum in me like a whore!", If (player.iswhore, 1,0)),
    ("Fuck. Fill me up like everyone else does!", If (player.isbroken , 1,0)),
    ("Ha fuck, don't stop!", 1),
    ("Keep going!", 1),
    ])
    pc "[dialouge]"
    pc "♥"
    "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
    tempname.name "Ahhh!"
    $ player.sex_cum(tempname,"inside", school_soccer_quest)
    "He presses into me as deep as he can and I feel his cock start to pulse inside me. No doubt making sure I take every drop he has to give me."
    show sb_againstwall2 vhappy with dissolve
    pc "Ah I can feel you pumping in me."
    tempname.name "Fuck ahhhh!"
    tempname.name "Yes!!!"
    $ player.spank()
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum == 1:
        pc "Fuck, you like spanking me don't you?"
        tempname.name "With the way you tighten when I do, seems you love it as well."
        $ player.spank()
        show sb_doggy1 closed with dissolve
        pc "Ha! ♥"
        tempname.name "See?"
        $ player.spank()
        pc "Ah fuck!"
    tempname.name "Haa you dirty girl."
    show sb_doggy1 open neutral with dissolve
    pc "Mmmm..."
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    $ player.spank()
    pc "I am all leaking now."
    if player.has_perk(perk_preg_want) and not player.preg_knows:
        pc "Wonder if you managed to knock me up?"
        tempname.name "Don't say such things."
    jump school_field_soccer_sex_offer_sex_vag_cum_wrapup




label school_field_soccer_sex_offer_sex_vag_cum_premature:
    $ having_sex(5)
    tempname.name "Ahhh!"
    $ temp_var_1 = player.desire
    $ player.sex_cum(tempname,"inside", school_soccer_quest)
    $ player._desire = temp_var_1
    $ player.add_desire(15)
    show sb_againstwall2 shock worried open with dissolve
    "He presses into me as deep as he can and I feel his cock start to pulse inside me. No doubt making sure I take every drop he has to give me."
    pc "Ah I can feel you pumping in me. What the fuck?"
    tempname.name "Fuck ahhhh!"
    tempname.name "Yes!!!"
    pc "Hey, don't be all \"Yesing\" at me. You just came inside!"
    tempname.name "Fuck, sorry. I didn't expect to cum so quick."
    if loc_cur == loc_school_field_back:
        if not tempname == nate:
            nate.name "Well, that was anti climactic."
        else:
            drake.name "Well, that was anti climactic."
    show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 noman with dissolve
    pcm "Couldn't control himself and came right away..."
    pc "*Sigh*"
    $ renpy.scene()
    with dissolve
    $ randomnum = renpy.random.randint(1,3)
    if player.desire >= 100 and randomnum == 1 and not player.isbroken:
        jump school_field_soccer_sex_offer_sex_vag_cum_premature_horny
    else:
        if not ("exhibitionist_asked" in school_soccer_quest.conversation_topics and t.timeofday == "night"):
            $ pc_dress_slow()
        else:
            $ pc_set_temp_outfit()
        pcm "The pervert talks the talk, but couldn't walk the walk..."
        jump travel

label school_field_soccer_sex_offer_sex_vag_cum_premature_horny:
    $ having_sex(5)
    pcm "Still horny as shit..."
    $ school_soccer_pick_new_boy()
    $ npc_race_picker(tempname)
    if loc_cur == loc_school_field_back:
        pc "Hmmm..."
        pc "Come here [tempname.name]."
    else:
        pcm "Hmm..."
        $ walk(loc_school_field_back)
        tempname.name "That was quick. Why you still naked?"
        pc "Come here!"
    tempname.name "Ah!"
    show sb_blowjob poke down 1h with dissolve
    tempname.name "Haa fuck. Slow down you horny bitch, need to..."
    show sb_blowjob suck with dissolve
    tempname.name "Ooooohhh!!"
    "I don't even mess about with any pretence and suck on his cock like a starving whore while rubbing his balls with my free hand. I want him hard as quickly as possible and ready to fuck me."
    show sb_blowjob poke up with dissolve
    pc "Get ready to fuck me silly."
    show sb_blowjob suck down with dissolve
    tempname.name "Haa, ok..."
    "My mind is pretty much lost in the haze of desire and I try to swallow his cock right down to the hilt. Though I don't manage it, it is not through a lack of trying and [tempname.name] seems to be enjoying the attempt."
    tempname.name "Ah fuck you horny slut. Come here!"
    hide sb_blowjob
    show sb_againstwall2 pokevag ag wink
    with dissolve
    tempname.name "Ah, you are still leaking..."
    "I don't even let him finish what he was saying and push back on his cock. I am sopping wet and already stretched from before so there is little resistance in one push, he is hilt deep inside me."
    $ player.sex_vag(tempname, school_soccer_quest)
    show sb_againstwall2 insidevag with hpunch
    pc "Haaa fuck! ♥"
    $ player.spank()
    show sb_againstwall2 mast with dissolve
    pc "Fuck yes, beat my ass!"
    "I keep pressing my ass against [tempname.name] while he grips hold of me and beats my ass like a drum, I have no idea how long things go on like this as I am totally lost in the desperate pleasure he is giving me."
    $ player.spank()
    "He is relentless is his beating of me and I am loving every moment of it. I can feel a heat welling up inside of me and it is not long until I am about to explode."
    pc "Fuck yes I am almost there! Keep going!"
    tempname.name "Fuuuuuu!"
    $ player.spank()
    tempname.name "Ahhhhhh!"
    show sb_againstwall2 closed
    $ player.sex_cum(tempname,"inside", school_soccer_quest)
    pc "Fuck yes, Fuck fuck!"
    pc "Ahhhhhhhhhhh..."
    pc "Haaaaaa..."
    pc "*Phew*"
    show sb_againstwall2 open neutral with dissolve
    $ player.face_neutral()
    pc "That was amazing."
    tempname.name "You are telling me."
    show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 noman with dissolve
    pc "Ooooh, I need a beer after that..."
    $ renpy.scene()
    with dissolve
    if not ("exhibitionist_asked" in school_soccer_quest.conversation_topics and t.timeofday == "night"):
        $ pc_dress_slow()
    else:
        $ pc_set_temp_outfit()
    pc "*Huff*"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_offer_sex_sex_wrapup:


label school_field_soccer_sex_offer_update_rules:
    pc "So guys."
    nate.name "Uh oh."
    if player.isbroken:
        $ school_field_soccer_sex_offer_rules = "broken"
        $ player.face_meek()
        pc "Ummm, when we are having sex..."
        $ player.add_desire(100)
        pc "Can you treat me badly. Rough and spanking..."
        $ player.face_happy()
        pc "Use me like a cheap whore."
        $ player.add_desire(100)
        nate.name "Right."
        $ player.face_meek()
        pc "Please use me."
        nate.name "Okaaay..."
    elif player.preg_knows:
        $ school_field_soccer_sex_offer_rules = "inside"
        pc "So, since I am pregnant, I guess you guys can cum where you want until it's gone."
        nate.name "Well, won't say no to that."
    elif player.has_perk([perk_preg_want, perk_creampie_lover], notif=True):
        $ school_field_soccer_sex_offer_rules = "inside"
        $ player.face_happy()
        pc "Can you make sure to cum inside me?"
        nate.name "What? Really? Won't that... Y'know"
        $ player.face_excited()
        $ player.add_desire(100)
        if player.has_perk(perk_preg_want):
            pc "Yup ♥"
            nate.name "Fuck, right. If you say so."
        elif player.has_perk(perk_creampie_lover):
            pc "Hmm, let's hope it doesn't come to that."
            nate.name "Err, sure..."
    elif player.pregpills:
        $ school_field_soccer_sex_offer_rules = "careful"
        pc "So I am on the pill. Well, when I can afford it anyway."
        pc "I would prefer outside but we can have some fun and make a mess."
        nate.name "Right."
    else:
        $ school_field_soccer_sex_offer_rules = "careful"
        pc "And pull out. It's no fun if I end up pregnant by one of you lot."
        pc "Or better yet, I have an ass and mouth that can be used."
        nate.name "Right, I can deal with that."
    $ player.face_meek()
    pc "Good, so..."
    $ player.face_neutral()
    pc "Great."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_sex_offer_intro:
    pc "So guys..."
    drake.name "Huh?"
    pc "We have done some naughty things together."
    nate.name "Something I will not forget."
    pc "Yes, well... You guys are cute. And I know the way you look at me..."
    pc "So if you want, we can do it on a regular basis."
    drake.name "What? [name], are you sure you..."
    nate.name "Shut up [drake.name]. Idiot."
    nate.name "We would be happy to..."
    dan.name "Watch your words before you ruin it."
    nate.name "We would be happy to serve your needs and make you happy."
    dan.name "Good enough."
    pc "Idiot."
    if not player.isbroken:
        pc "But there are rules. Don't pressure me. I will offer, no asking."
        nate.name "Right."
    if player.isbroken:
        $ school_field_soccer_sex_offer_rules = "broken"
        $ player.face_meek()
        pc "So... Use me as you like. Rough... Spanking..."
        $ player.face_happy()
        pc "Use me like a cheap whore."
        $ player.add_desire(100)
        nate.name "Right."
        $ player.face_meek()
        pc "Please use me."
        nate.name "Okaaay..."
    elif player.has_perk([perk_preg_want, perk_creampie_lover], notif=True):
        $ school_field_soccer_sex_offer_rules = "inside"
        $ player.face_happy()
        pc "And make sure to cum inside me."
        nate.name "What? Really? Won't that... Y'know"
        $ player.face_excited()
        $ player.add_desire(100)
        if player.has_perk(perk_preg_want):
            pc "Yup ♥"
            nate.name "Fuck, right. If you say so."
        elif player.has_perk(perk_creampie_lover):
            pc "Hmm, let's hope it doesn't come to that."
            nate.name "Err, sure..."
    elif player.pregpills:
        $ school_field_soccer_sex_offer_rules = "relaxed"
        pc "And I am on the pill. Well, when I can afford it anyway."
        pc "I would prefer outside but we can have some fun and make a mess."
        $ player.add_desire(100)
        nate.name "Right."
    else:
        $ school_field_soccer_sex_offer_rules = "careful"
        pc "And pull out. It's no fun if I end up pregnant by one of you lot."
        if player.has_perk(perk_buttslut):
            pc "Or better yet, I love it in the arse. You can do what you want there."
        else:
            pc "Or better yet, I have a mouth that can be used."
        $ player.add_desire(100)
        nate.name "Right, I can deal with that."
    $ player.face_meek()
    pc "Good, so..."
    $ player.face_neutral()
    pc "Okay then..."
    $ walk(loc_school_field)
    pcm "Fuck. Admitting that to them has my heart pounding and my nipples as hard as a rock!"
    pcm "Fuck fuck."
    $ player.face_happy()
    pcm "I really told them..."
    pcm "Fuck I am so horny now."
    $ drake.add_lust(100)
    $ nate.add_lust(100)
    $ dan.add_lust(100)
    jump travel





label school_field_soccer_sex_group_start:
    "[tempname.name] doesn't waste much time and comes up behind me."
    $ tempname2 = school_soccer_npc_sex_rachel_boy_who()
    $ tempname3 = school_soccer_npc_sex_robin_boy_who()
    $ npc_race_picker(tempname, tempname2, tempname3)

    if "soccer_sex_robin" in robin.list and "soccer_sex_rachel" in rachel.list:
        show sb_tripplesex rachel robin pc
    elif "soccer_sex_robin" in robin.list:
        show sb_tripplesex robin pc
    else:
        show sb_tripplesex rachel pc right
    with dissolve
    pc "Starting to think we make these perverts way too happy."
    if "soccer_sex_robin" in robin.list:
        robin.name "Well, they do give us free beer."
    if "soccer_sex_rachel" in rachel.list:
        rachel.name "Really? I think we could do some more fun things."
    $ player.sex_vag(tempname)
    show sb_tripplesex happy
    pc "Haaaa!"
    if "soccer_sex_robin" in robin.list:
        robin.name "Oh? Got it in you?"
    if "soccer_sex_rachel" in rachel.list:
        rachel.name "Haha, feels nice."
    pc "Ha, yeah."
    $ player.spank()
    pc "Ai!"
    tempname.name "That wasn't even me."
    pc "Oh? Some other pervert spanking my ass?"
    if "soccer_sex_rachel" in rachel.list:
        rachel.name "Ha, not happy with just one of us? Grabbing your arse as well."
        rachel.name "Wonder if it's [tempname2.name]?"
        rachel.name "Stop touching [name] and keep touching me!"
        rachel.name "Pervert!"
    if "soccer_sex_robin" in robin.list:
        robin.name "Come on [tempname3.name], keep going."
        robin.name "Can't have [name] getting all the fun."
        pc "How am I getting all the fun?"
        robin.name "You are in the middle."
        pc "Err, okay..."
    "The boys keep fucking us and I can hear them talking dirty behind us."
    "I can also feel more than two hands touching me now and then, one pair pulling my ass against a cock, another hand over my body."
    pc "Wonder who will blow first?"
    if "soccer_sex_rachel" in rachel.list:
        rachel.name "C'mon [tempname2.name]! Be the first! Cum!"
    if "soccer_sex_robin" in robin.list:
        robin.name "Is it good or bad to cum first?"
        pc "Dunno..."
    if "soccer_sex_rachel" in rachel.list:
        rachel.name "First one leaking is the winner!"
        pc "Oh? So that's how it's going to be?"
    "The boys seem to slow down a bit, taking it more gently. Seems like they don't want to be the first."
    if "soccer_sex_rachel" in rachel.list:
        rachel.name "Come on pervrts! Fill us up!"
    if "soccer_sex_robin" in robin.list:
        robin.name "Trying to keep it slow. We don't have all day."
    "It isn't long before one of them gives up the race..."
    pc "Who is that grunting?"
    $ temp_var_1 = [tempname]
    if "soccer_sex_rachel" in rachel.list:
        $ add_to_list(temp_var_1, tempname2)
    if "soccer_sex_robin" in robin.list:
        $ add_to_list(temp_var_1, tempname3)
    $ temp_var_2 = random(temp_var_1)

    if temp_var_2 is tempname:
        pc "Oh, I think it's [tempname.name]!"
        if "soccer_sex_rachel" in rachel.list:
            rachel.name "Hey [tempname2.name]! [name] is gonna win! Hurry up."
        if "soccer_sex_robin" in robin.list:
            robin.name "Is that who I can hear?"
        tempname.name "Ahhh fuck!"
        $ player.sex_cum(tempname, "inside")
        tempname.name "Ahh yes!"
        if "soccer_sex_rachel" in rachel.list:
            rachel.name "Ah she won!"
        if "soccer_sex_robin" in robin.list:
            robin.name "Fill her up [tempname.name]!"
        pc "Haaa, I can feel him."
        if "soccer_sex_rachel" in rachel.list:
            rachel.name "Oh! I am getting mine now."
            pc "Yeah?"
            rachel.name "Mmm. He is pressing it all the way and pumping."
            pc "Haha, go [tempname2.name]!"
        if "soccer_sex_robin" in robin.list:
            robin.name "[tempname3.name] as well now."
            pc "Oooh."

    elif temp_var_2 is tempname2:
        rachel.name "I am a winner!!"
        pc "Oh? [tempname2.name] is the grunting one?"
        rachel.name "Ah I feel him!"
        rachel.name "Go [tempname2.name]!"
        pc "Haha."
        pc "Oh?"
        $ player.sex_cum(tempname, "inside")
        pc "Seems like [tempname.name] is also blowing his load."
        if "soccer_sex_robin" in robin.list:
            robin.name "[tempname3.name] as well now."
            pc "Oooh."
        rachel.name "Winner! Winner!"
        pc "Yeah yeah..."
    else:
        robin.name "Ahhh!"
        robin.name "It's [tempname3.name] grunting."
        pc "He cumming?"
        robin.name "Almost finished now."
        if "soccer_sex_rachel" in rachel.list:
            rachel.name "Aww [tempname2.name]. You were too slow."
        $ player.sex_cum(tempname, "inside")
        pc "Oh? Yeah [tempname.name] is blowing now."
        robin.name "Haha."
    if "soccer_sex_rachel" in rachel.list and "soccer_sex_robin" in robin.list:
        nate.name "Haaa. All three of you bent over and leaking cum."
        dan.name "Nice view."
        nate.name "Yeah."
    else:
        nate.name "Two bare arses leaking cum."
        drake.name "Yeah, not something you see every day."
    hide sb_tripplesex with dissolve
    pc "Well, that was fun."
    if robin_here():
        robin.name "Haha."
    if mira_here():
        mira.name "Wow, you lot end up doing worse things than girls on the highway."
    jump school_field_soccer_hangout_conv_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
