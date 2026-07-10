label school_field_soccer_darematch_picker:
    if not school_soccer_quest_dare_preg_warning and player.pregnancy >= 2:
        jump school_field_soccer_darematch_preg_intro
    if renpy.has_label("school_field_soccer_darematch_chain" + str(school_soccer_quest_betmatch["match_count"])):
        jump expression "school_field_soccer_darematch_chain" + str(school_soccer_quest_betmatch["match_count"])
    elif player.pregnancy >= 2:
        jump school_field_soccer_darematch_play_preg
    else:
        jump school_field_soccer_darematch_play

label school_field_soccer_darematch_challenge:



    if weather_var == 3:
        pcm "Hmm, don't think I want to be running round the pitch in the pissing rain."
        jump travel
    pc "So who's up for playing?"
    if not school_soccer_dare_canplay():
        drake.name "Not another one [name]. Relax and drink some beers."
        pc "Ugh..."
        jump travel
    $ school_soccer_pick_boy()
    tempname.name "Sure, I'm up for it."

    if player.pregnancy >= 2:
        jump school_field_soccer_darematch_play_preg
    else:
        jump school_field_soccer_darematch_play

label school_field_soccer_darematch_preg_intro:
    $ school_soccer_quest_dare_preg_warning = True
    nate.name "How you going to play like that?"
    $ player.face_meek()
    pc "Ugh..."
    $ player.face_neutral()
    pc "I just want to mess about and have fun."
    dan.name "I don't mind playing in your place. Good excuse to get a bit more exercise. You are still paying out the forfeits though."
    pc "And the winnings?"
    dan.name "Yeah you can have that as well."
    pc "Great. So let's play! Well, I watch. You play."
    jump school_field_soccer_darematch_picker

label school_field_soccer_darematch_chain0:
    $ school_soccer_quest_betmatch["match_count"] +=1
    tempname.name "Feeling brave?"
    pc "Sure. What do you normally put up? Last match was £100"
    tempname.name "Sure that will do."
    if player.cash < 100:
        pc "Err..."
        tempname.name "Not got that much?"
        pc "..."
        jump school_field_soccer_darematch_chain1
    pc "Okay then, let's go. Best to 5?"
    tempname.name "Ok, let's go."
    jump school_field_soccer_darematch_play

label school_field_soccer_darematch_chain1:
    $ school_soccer_quest_betmatch["can_challenge"] = True
    $ school_soccer_quest_betmatch["match_count"] += 1
    tempname.name "Betting money is boring. How about we do dares?"
    pc "Dares...?"
    tempname.name "Yeah, like a forfeit. Do something stupid or embarrassing."
    if c.nude:
        pc "I'm standing here naked so not sure what more you can dare me to do, but whatever, let's go for a dare."
        jump school_field_soccer_darematch_play
    if player.check_sex_agree(3, exhibitionist=True):
        pc "Why do I get the feeling with you lot, my dares will wind up with me losing clothes?"
        tempname.name "Maybe not. I can think of a few other things."
        pc "Yeah right..."
        pc "Well, whatever, sure. Let's go for a dare."
        jump school_field_soccer_darematch_play
    else:
        pc "Dares? Ones where I wind up naked no doubt..."
        tempname.name "Maybe not. I can think of a few other things."
        pc "Yeah right. I think I will pass on that for now."
        tempname.name "Suit yourself."
        jump school_field_soccer_hangout_conv_end

label school_field_soccer_darematch_dare_picker:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_dare_nocheck", 30),
    ("school_field_soccer_hangout_dare_easy", If (player.check_sex_agree(1, notif=False) and school_soccer_quest_betmatch["match_total"] > 0,100,0)),
    ("school_field_soccer_hangout_dare_normal", If (player.check_sex_agree(2, notif=False) and school_soccer_quest_betmatch["match_total"] > 3,80,0)),
    ("school_field_soccer_hangout_dare_hard", If (player.check_sex_agree(3, notif=False) and school_soccer_quest_betmatch["match_total"] > 6,60,0)),
    ("school_field_soccer_hangout_dare_vhard", If (player.check_sex_agree(4, notif=False) and school_soccer_quest_betmatch["match_total"] > 9,40,0)),
    ])
    jump expression rand_choice

label school_field_soccer_hangout_dare_nocheck:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_dare_nocheck_1", 1),
    ("school_field_soccer_hangout_dare_nocheck_2", 1),
    ])
    jump expression rand_choice

label school_field_soccer_hangout_dare_veasy:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_dare_veasy_1", If (c.skirt and c.pants, 1, 0) ),
    ("school_field_soccer_hangout_dare_veasy_2", If (c.top, 1, 0) ),
    ("school_field_soccer_hangout_dare_veasy_3", 1),
    ("school_field_soccer_hangout_dare_veasy_4", 1),
    ("school_field_soccer_hangout_dare_veasy_5", 1),
    ])
    jump expression rand_choice

label school_field_soccer_hangout_dare_easy:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_dare_easy_1", If(not c.cansee_breasts,1,0)),
    ("school_field_soccer_hangout_dare_easy_2", If(not writing.face,1,0)),
    ("school_field_soccer_hangout_dare_easy_3", If(not writing.forehead,1,0)),
    ("school_field_soccer_hangout_dare_easy_4", If(not writing.chest,1,0)),
    ("school_field_soccer_hangout_dare_easy_5", If(not writing.belly,1,0)),
    ("school_field_soccer_hangout_dare_easy_6", If(not "work" in tab_top and pub_waitress.timesworked,1,0)),
    
    ])
    jump expression rand_choice

label school_field_soccer_hangout_dare_normal:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_dare_normal_1", If(not c.underwear or c.nude,1,0)),
    ("school_field_soccer_hangout_dare_normal_2", If(not c.nude,1,0)),
    ("school_field_soccer_hangout_dare_normal_3", If(not c.cansee_breasts,1,0)),
    ("school_field_soccer_hangout_dare_normal_4", If(not c.cansee_breasts,1,0)),
    ("school_field_soccer_hangout_dare_normal_5", 1),
    ("school_field_soccer_hangout_dare_normal_6", If(robin_here(),1,0)),

    ])
    jump expression rand_choice

label school_field_soccer_hangout_dare_hard:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_dare_hard_1", 1),
    ("school_field_soccer_hangout_dare_hard_2", 1),
    ("school_field_soccer_hangout_dare_hard_3", 1),
    ("school_field_soccer_hangout_dare_hard_4", 1),
    ("school_field_soccer_hangout_dare_hard_5", 1),
    ("school_field_soccer_hangout_dare_hard_6", 1),
    
    ("school_field_soccer_hangout_dare_hard_8", If(robin_here(),1,0)),
    ])
    jump expression rand_choice

label school_field_soccer_hangout_dare_vhard:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_dare_vhard_1", 1),
    ("school_field_soccer_hangout_dare_vhard_2", 1),

    ])
    jump expression rand_choice


label school_field_soccer_hangout_dare_nocheck_1:
    tempname.name "Okay [name]. Do a lap around the field."
    pc "Your making me do more running? Ugh, ok..."
    $ walk(loc_school_field)
    $ player.face_exercise()
    show activity_run with dissolve
    "I start running around the field listening to the mocking taunts of the boys as I do so."
    hide activity_run
    $ walk(loc_school_field_back)
    pc "*Huff* *Huff*"
    pc "Happy?"
    tempname.name "Sure am."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_nocheck_2:
    tempname.name "Hmm, sing us a song [name]."
    pc "Really? Ok, whatever..."
    $ player.face_happy()
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        pc "♪ When the sun shines, we'll shine together ♪"
        pc "♪ Told you I'll be here forever ♪"
        pc "♪ Said I'll always be your friend ♪"
        pc "♪ Took an oath, I'ma stick it out 'til the end ♪"
    elif randomnum == 2:
        pc "♪ I wanna hold 'em like they do in Texas, please ♪"
        pc "♪ Fold 'em, let 'em hit me, raise it, baby, stay with me ♪"
        pc "♪ Love game intuition, play the cards with spades to start ♪"
        pc "♪ And after he's been hooked, I'll play the one that's on his heart ♪"
    else:
        pc "♪ Cause it makes me that much stronger ♪"
        pc "♪ Makes me work a little bit harder ♪"
        pc "♪ Makes me that much wiser ♪"
        pc "♪ So thanks for making me a fighter ♪"
    "I continue singing until the laughing and mockery drowns out my voice and decide to stop."
    nate.name "Whoo!"
    drake.name "Come on! More!"
    jump school_field_soccer_hangout_conv_end


label school_field_soccer_hangout_dare_veasy_1:
    tempname.name "Okay [name]. Take off your underwear and show them to us."
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "Oh? Okay."
        if c.outfit or c.bottoms:
            $ c.bottom = 0
            $ c.outfit = 0
            tempname.name "Err..."
            pc "These pants?"
            tempname.name "Yes?"
        "I slowly lower them down my legs, making sure everyone gets a good look."
        $ c.pants = 0
        pc "Here you go."
        tempname.name "Oooh nice."
        pc "Want to keep them?"
        if tempname == nate:
            tempname.name "Sure!"
            pc "Okay."
            $ wardrobe.drop_clothes("pants", notif_message="Gave away knickers")
            if drake_here():
                drake.name "What do you want her knickers for?"
                nate.name "She offered."
                if robin_here():
                    robin.name "Pervert."
                    robin.name "Going to find [nate.name] wearing them tomorrow or something."
                    drake.name "Haha!"
        else:
            tempname.name "No, it's fine."
            pc "Okay."
        tempname.name "Shouldn't you, err. Dress back up?"
        pc "Why?"
        tempname.name "No reason..."
    else:

        pc "Ugh, ok..."
        "I take off my pants from under my skirt, trying not to expose myself too much."
        pc "Here."
        if c.thong:
            tempname.name "Ohh, tiny ones."
        elif c.pants_primary_colour in ("pink", "hotpink") or  c.pants_secondary_colour in ("pink", "hotpink"):
            tempname.name "Oooh pink ones!"
        else:
            tempname.name "Nice!"
        $ c.pants = 0
    $ pc_set_temp_outfit()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_veasy_2:
    tempname.name "Okay [name], take your top off and just have your bra on."
    if player.check_sex_agree(3):
        pc "Ugh, not wearing a bra but whatever..."
        $ c.top = 0
        pc "Happy?"
        tempname.name "Fuck!"
    else:
        if c.clevage and not c.bra:
            pc "What? You can see I am not wearing a bra."
            tempname.name "What? Really?"
            pc "Don't act like you haven't noticed."
        elif not c.bra:
            pc "What? I don't have a bra on."
            tempname.name "What? Really?"
            pc "*Sigh*"
        else:
            pc "Ugh, sure."
        $ c.top = 0
        pc "There we go."
    tempname.name "Nice!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_veasy_3:
    $ dialouge = renpy.random.choice([
    "I love sucking on huge cocks",
    "I love cum on my face",
    "I love swallowing cum",
    "I want to take a huge cock in my arse",
    ])
    tempname.name "Hmmm, shout as loud as you can \"[dialouge]\""
    pc "Pervert..."

    $ player.face_shout()
    with hpunch
    pc "[dialouge!u]!!!!"
    $ player.face_neutral()
    pc "*Cough*"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_veasy_4:
    tempname.name "Hmm, let me spank you?"
    pc "Whaa?"
    pc "..."
    pc "Fine."
    tempname.name "Mmmm."
    $ player.spank()
    pc "Ah!"
    $ player.spank()
    pc "Waaa!"
    $ player.spank()
    pc "Ah okay ok!"
    $ player.spank()
    pc "Hey that's too much."
    tempname.name "Sure, don't act like you don't like it."
    pc "Shush!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_veasy_5:
    tempname.name "Hmm, make a perverted face."
    pc "Hmmm..."
    pc "..."
    $ player.face_orgasm()
    pc "Ahhhhh ♥"
    $ player.face_happy()
    pc "Good enough?"
    tempname.name "Err, yes..."
    jump school_field_soccer_hangout_conv_end


label school_field_soccer_hangout_dare_easy_1:
    tempname.name "Hmm, show us your tits."
    pc "How original..."
    $ pc_strip_upper(slow=True)
    show sb_pose_showbreasts with dissolve
    pc "Happy?"
    nate.name "Mmmm."
    drake.name "Nice!"
    hide sb_pose_showbreasts with dissolve
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_easy_2:
    tempname.name "Hmm, come here. I want to write something on your face."
    pc "..."
    tempname.name "Let's see..."
    $ writing.add_writing("face", "temp")
    tempname.name "Done!"
    pc "What did you put there?"
    tempname.name "I drew a little heart on your cheek."
    pc "Ugh..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_easy_3:
    tempname.name "Hmm, come here. I want to write something on your face."
    pc "..."
    tempname.name "Let's see..."
    $ writing.add_writing("forehead", "temp")
    tempname.name "Done!"
    pc "What did you put there?"
    tempname.name "Nothing much."
    pc "Ugh..."
    $ walk(loc_school_locker_old)
    pc "Hmmm..."
    if player.sold > 30:
        pc "Ah... Well... Okay then..."
    else:
        $ player.face_annoyed()
        pc "Ugh, arsehole."
    $ walk(loc_school_field_back)
    if not player.sold > 30:
        $ player.face_annoyed()
        pc "You arse!"
        tempname.name "Looks good on you."
        pc "Ugh!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_easy_4:
    tempname.name "Hmm, you like showing those tits off so how about I make an addition to them."
    pc "Huh?"
    tempname.name "I'll write something on your chest."
    pc "Ugh, sure..."
    tempname.name "Let's see..."
    $ writing.add_writing("chest", "temp")
    tempname.name "There we go..."
    pc "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_easy_5:
    tempname.name "Hmm, you like showing off your belly. Let me write something there."
    pc "Ugh, sure..."
    tempname.name "Let's see..."
    $ writing.add_writing("belly", "temp")
    tempname.name "There we go..."
    pc "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_easy_6:
    tempname.name "Go and dress in your bar girl outfit."
    pc "Really?"
    tempname.name "It's sexy!"
    pc "..."
    $ walk(loc_school_locker_old)
    pc "Perverts."
    $ pc_striptease()
    $ pub_waitress.work_dress()
    $ pc_strip()
    pause 0.5
    $ pc_dress_slow()
    pause 0.5
    $ walk(loc_school_field_back)
    pc "There we go."
    tempname.name "Nice!"
    if not c.socks:
        drake.name "Wasn't it supposed to come with socks as well?"
        pc "Some degenerate bought them off me so I don't have them."
        tempname.name "Oh wow."
        tempname.name "What about under the skirt?"
        if player.check_sex_agree(2):
            if c.pants:
                pc "Still have those on."
                nate.name "Aw."
            else:
                pc "Also bought..."
                nate.name "Fuck, I need to go hang out at the pub more."
                drake.name "Damn right!"
        else:
            pc "That's only for me to know."
            nate.name "Considering how short the skirt is, doubt you will be able to keep it a secret for long."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_easy_7:
    tempname.name "Go and dress in your dancers outfit."
    pc "Really?"
    tempname.name "It's sexy!"
    pc "..."
    $ walk(loc_school_locker_old)
    pc "Perverts."
    $ pc_striptease()
    $ school_dance_set_clothes()
    $ tab_top = "work"
    pause 0.5
    $ pc_dress_slow()
    pause 0.5
    $ walk(loc_school_field_back)
    pc "There we go."
    tempname.name "Nice!"
    nate.name "Not sure if that skirt could be any smaller. Guessing everyone in the audience knows what colour your pants are after 30 seconds."
    if c.thong:
        dan.name "Pink."
    else:
        dan.name "Black."
    pc "Already? Fuck!"
    jump school_field_soccer_hangout_conv_end


label school_field_soccer_hangout_dare_normal_1:
    $ school_soccer_quest_dare_clothes["under"] = t.day
    tempname.name "Strip down to your undies and stay that way."
    if not (c.bra or c.pants):
        pc "And if I'm not wearing any?"
        tempname.name "Then even better for us."
        pc "Ugh."

    pc "..."
    $ pc_strip_tops(slow=True)
    if not (c.bra or c.pants):
        $ player.face_meek()
        tempname.name "Oh fuck. Wow."
        nate.name "Jackpot!"
    elif c.thong:
        tempname.name "Oh nice pants. Might even be better than if you didn't have any."
    else:
        pc "Happy?"
        tempname.name "Very!"
    $ pc_dress_slow()
    $ pc_set_temp_outfit()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_normal_2:
    tempname.name "Do a lap in your underwear."
    if not (c.bra or c.pants):
        pc "And if I'm not wearing any?"
        tempname.name "Then even better for us."
        pc "Ugh."

    pc "..."
    $ pc_strip_tops(slow=True)
    if not (c.bra or c.pants):
        $ player.face_meek()
        tempname.name "Oh fuck. Wow."
        nate.name "Jackpot!"
    elif c.thong:
        tempname.name "Oh nice. Can see her bare arse anyway"
    $ walk(loc_school_field)
    $ player.face_exercise()
    show activity_run with dissolve
    "I start running around the pitch and try to ignore the jeering coming from their mouths."
    pc "Dirty perverts the lot of you!"
    drake.name "You are the one naked in front of a bunch of guys."
    nate.name "She's a pervert!"
    pc "Ugh."
    "I finally make it back to where I started."
    hide activity_run
    $ walk(loc_school_field_back)
    $ player.face_neutral()
    pc "There we go."
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_normal_3:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    tempname.name "Get your tits out and do a lap."
    if c.outfit:
        pc "Err, I'm wearing a dress."
        tempname.name "I can see that."
        if not c.pants:
            pc "And I have no pants on."
            tempname.name "Oh?"
            tempname.name "Nude it is then."
            pc "Arsehole!"
            tempname.name "Might be getting a look at yours."
    pc "..."
    $ pc_strip_upper(slow=True)
    pc "Dirty perverts the lot of you!"
    drake.name "You are the one naked in front of a bunch of guys."
    nate.name "She's a pervert!"
    pc "Ugh."
    "I finally make it back to where I started."
    $ player.face_neutral()
    pc "There we go."
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_normal_4:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    $ school_soccer_quest_dare_clothes["topless"] = t.day
    tempname.name "Okay [name]. For the rest of the night, you need to stay topless."
    pc "What? The rest of the night?"
    tempname.name "Yup!"
    pc "Ok..."
    $ pc_strip_upper(slow=True)
    $ pc_set_temp_outfit()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_normal_5:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_handjob")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    tempname.name "How about you use your hands and give me some relief."
    pc "Huh?"
    tempname.name "Wank me off."
    $ player.face_shock()
    pc "Seriously?"
    tempname.name "The loser has to pay up."
    $ player.face_meek()
    pc "Ugh..."
    $ player.face_neutral()
    pc "Right..."
    pc "Come on then. Get it out."
    $ npc_race_picker(tempname)
    $ player.sex_hand(tempname)
    show sb_handjob ballrub with dissolve
    pc "Bet you couldn't wait to make me do this."
    if school_soccer_quest_boys_know["slut"]:
        tempname.name "You're such a slut I bet you was looking forward to this."
    elif school_soccer_quest_boys_know["whore"]:
        tempname.name "You say it like others haven't paid you to do worse things."
    else:
        tempname.name "I don't see you saying no."
    pc "Heh."
    show sb_handjob mast down with dissolve
    pc "What are friends for if not to give a helping hand?"
    tempname.name "Ha, that's the spirit."
    pc "It's so warm..."
    "I stroke [tempname.name]'s cock with a nice rhythm and it seems he's enjoying it by the sounds he is making."
    $ dialouge = WeightedChoice([
    ("Ah yes, like that.", 1),
    ("Fuck, you know what you are doing don't you?", If (player.hsex > 15,1,0)),
    ("Mmm, had a lot of practice haven't you?", If (school_soccer_quest_boys_know["slut"], 1, 0)),
    ("Can see why people pay you to do this.", If (school_soccer_quest_boys_know["whore"], 1, 0)),
    ])
    tempname.name "[dialouge]"
    show sb_handjob up
    pc "Having fun?"
    tempname.name "Ah, fuck yes! Keep going."
    show sb_handjob down
    pc "Oooh, you are leaking. Getting close?"
    pc "Ah, it's throbbing!"
    tempname.name "Ahh, keep going."
    tempname.name "Ahhhhhhhhh..."
    tempname.name "Yes!!"
    pc "Oooh, here it comes."
    $ player.sex_cum(tempname, "hand")
    tempname.name "Ahhhhh!"
    tempname.name "Yes!"
    tempname.name "Fuck. That was nice!"
    show sb_handjob up
    pc "Mmmm. Now my hand is all messy."
    tempname.name "*Phew*"
    hide sb_handjob with dissolve
    if player.isslut:
        "I get off my knees and lick [tempname.name]'s cum off my hands while sorting out my clothes."
    else:
        "I get up off my knees and start wiping away the mess on my hand while sorting out my clothes."
    $ pc_dress()
    $ player.cum_clean_outside()
    pc "Enjoy the show you perverts?"
    if not tempname == nate:
        nate.name "Fuck yes!"
    if not tempname == drake:
        drake.name "Damn right!"
    if not tempname == dan:
        dan.name "Yup."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_normal_6:
    tempname.name "Hmm, from now on you have to call [robin.name] something nice."
    robin.name "Oh? I like this."
    $ robin._nname = rlist.name_cute_upper
    tempname.name "Call her [robin.nname] from now on."
    robin.name "Oooh..."
    pc "Ok. [robin.nname]."
    jump school_field_soccer_hangout_conv_end


label school_field_soccer_hangout_dare_hard_1:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    tempname.name "Hmm, strip and run around the pitch."
    pc "..."
    $ pc_striptease()
    tempname.name "Whooo! Looking good!"
    show sb_pose_lookback with dissolve
    pc "Perverts!"
    tempname.name "You are the naked one. Pervert."
    pc "*Sigh*"
    hide sb_pose_lookback with dissolve
    $ walk(loc_school_field)
    "I endure the whooping as I undress and start running around the pitch. Their perverted comments about my bouncing breasts never seem to cease and finally I get back to where I started."
    $ walk(loc_school_field_back)
    pc "There you go..."
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_hard_2:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    $ school_soccer_quest_dare_clothes["nude"] = t.day
    tempname.name "Take your clothes off and keep them off for the rest of the evening."
    pc "Keep them off?"
    tempname.name "While you are here, yes. No one else but us will see you."
    pc "Right..."
    $ pc_striptease()
    pc "There we go"
    $ pc_set_temp_outfit()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_hard_3:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    tempname.name "Hmm, put your dancers clothes on and do a dance for us."
    tempname.name "A dance that ends in you naked."
    pc "What? Really?"
    tempname.name "Yup!"
    pc "Right..."
    pc "I'll go change."
    $ school_dance_set_clothes()
    $ pc_dress_event("work", loc_school_locker_old, loc_school_field_back)
    tempname.name "Oooh."
    pc "Ready?"
    tempname.name "Oh yes!"
    show dance_front nodani with dissolve
    pc "♪ When the sun shines, we'll shine together ♪"
    $ c.top = 0
    $ c.bra = 0
    show dance_front with dissolve
    pc "♪ Told you I'll be here forever ♪"
    $ c.socks = 0
    $ c.bottom = 0
    show dance_front with dissolve
    pc "♪ Said I'll always be your friend ♪"
    $ c.pants = 0
    show dance_front with dissolve
    pc "♪ Took an oath, I'ma stick it out 'til the end ♪"
    "I keep dancing and singing while the boys cheer me on. Eventually the song comes to an end and I stop dancing."
    dan.name "Nice show!"
    drake.name "Wow."
    hide dance_front with dissolve
    $ player.face_happy()
    pc "Shush you perverts."
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_hard_4:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    tempname.name "Let's see... Take your clothes off and do some sexy poses for us."
    pc "Ok..."
    $ pc_striptease()
    show sb_pose_showbreasts with dissolve
    pc "Like looking at these do you?"
    pc "Bunch of perverts the lot of you."
    "I can't even make out what the boys are saying as they are all cheering me on at the same time."
    hide sb_pose_showbreasts
    show sb_pose_lookback
    with dissolve
    pc "How about from this angle? Like a look at my bum?"
    $ player.spank()
    pc "Mmm, like that do you? Like me spanking my ass?"
    $ player.spank()
    "I still can't make out what they are saying but I decide I have held up my end of the bargain so decide to get dressed."
    hide sb_pose_lookback
    pc "That's enough you dirty lot."
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_hard_5:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    tempname.name "Take your clothes off and let each of us write something on your body."
    pc "All of you? Right..."
    $ pc_striptease()
    nate.name "Ok..."
    $ writing.add_writing_random()
    drake.name "Let's see..."
    $ writing.add_writing_random()
    dan.name "Hmmm..."
    $ writing.add_writing_random()
    dan.name "There we go."
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_hard_6:
    $ npc_race_picker(tempname)
    tempname.name "Hmm, get on your knees and suck me off."
    $ player.face_shock()
    pc "What!?"
    tempname.name "You heard me loser."
    if robin_here() and not "soccerboys_knows_pc_sex" in robin.list:
        robin.name "Wow, going to the extreme here..."
        $ add_to_list(robin.list, "soccerboys_seen_dare_blowjob")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    $ player.face_meek()
    pc "Ugh..."
    $ player.face_neutral()
    pc "Right..."
    show sb_blowjob with dissolve
    "I get down on my knees in front of the other boys and prepare to blow [tempname.name]."
    tempname.name "Good girl, here you go."
    $ randomnum = renpy.random.randint(1, 10)
    if randomnum == 1:
        $ player.spank()
        show sb_blowjob face closed frown angry with vpunch
        pc "Ah!"
        show sb_blowjob up neutral straight with dissolve
        pc "You arse!"
        show sb_blowjob 1h with dissolve
        tempname.name "Don't pretend you don't like it."
        show sb_blowjob poke down with dissolve
    pc "Mmm..."
    show sb_blowjob poke 1h with dissolve
    if not numgen(0,40):
        show sb_blowjob closed laugh angry with dissolve
        pc "♪ If you wanna be my lover, you gotta get with my friends. ♪"
        tempname.name "What, [name]... No!"
        pc "♪ Make it last forever, friendship never ends. ♪"
        tempname.name "What the fuck..."
        pc "♪ If you wanna be my lover, you have got to give. ♪"
        tempname.name "Ugh."
        pc "♪ Taking is too easy, but that's the way it is. ♪"
        $ randomnum = renpy.random.randint(1, 10)
        if randomnum == 1:
            show sb_blowjob 0h suck with vpunch
            pc "Mmmmfff!!"
            tempname.name "Best way to shut you up."
            show sb_blowjob eangry with dissolve
            pc "Mmmii maafff hammmmffnnn fffnnnn."
        else:
            show sb_blowjob noman up happy neutral with dissolve
            tempname.name "Give me my cock back."
            pc "Hey! I was having fun."
            tempname.name "Go sing with someone else's cock."
            pc "Spoilsport."
            hide sb_blowjob with dissolve
            $ pc_dress()
            jump school_field_soccer_hangout_conv_end

    show sb_blowjob suck 2h down happy with dissolve
    "I wrap my fingers around [tempname.name]'s cock and start wanking him off while sucking on it."
    tempname.name "Ah yes, that's the way!"
    if player.iswhore or player.isslut:
        tempname.name "Fuck you are good at this."
    show sb_blowjob poke neutral up with dissolve
    pc "Enjoying?"
    show sb_blowjob suck down with dissolve
    tempname.name "Fuck!"
    "He starts thrusting into my mouth in time with my head bobbing and eventually he is slowly fucking my mouth. I help him out by stroking his cock in time with his thrusts."
    tempname.name "Ah yes!"
    pc "*Mmmmff*"
    pc "*Hyuk* *Hyuk* *Hyuk*"
    tempname.name "Ah fuck yes!"
    tempname.name "You're gonna make me cum!"
    show sb_blowjob poke neutral up with dissolve
    pc "Face or mouth?"
    show sb_blowjob suck down with dissolve
    tempname.name "Ah fuck!"
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        tempname.name "Keep sucking!"
        pc "Mmmff."
        "I start to feel his cock tensing up and his movements become erratic. I know he is about to cum in my mouth."
        tempname.name "Ah yes keep goingggg..."
        tempname.name "Ah yes!!"
        $ player.sex_cum(tempname, "mouth")
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
        hide sb_blowjob with dissolve
    elif randomnum == 2:
        tempname.name "Open your mouth."
        show sb_blowjob poke swallow up with dissolve
        pc "Ik Is?"
        tempname.name "That's it!"
        show sb_blowjob down 2h with dissolve
        "I keep wanking him off while licking his cock, getting ready for him to cum in my mouth."
        $ player.sex_cum(tempname, "mouth")
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
        hide sb_blowjob with dissolve
    else:
        tempname.name "Your face."
        show sb_blowjob face swallow up 2h with dissolve
        "I lick the shaft of his cock while wanking him off with my hand, getting ready for him to come over my face."
        $ player.sex_cum(tempname, "face")
        show sb_blowjob closed with dissolve
        tempname.name "Ah fuck yes!!!"
        tempname.name "Yesss!"
        tempname.name "Ah shit. That was good."
        show sb_blowjob up laugh with dissolve
        pc "Like what you see?"
        tempname.name "Perfect!"
        show sb_blowjob noman neutral with dissolve
        hide sb_blowjob with dissolve
    "I get up off my knees and start wiping away the mess on my face while sorting out my clothes."
    $ pc_dress()
    $ player.cum_clean_outside()
    pc "Enjoy the show you perverts?"
    if not tempname == nate:
        nate.name "Fuck yes!"
    if not tempname == drake:
        drake.name "Damn right!"
    if not tempname == dan:
        dan.name "Yup."

    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_hard_8:
    tempname.name "Give [robin.name] a nice big lesbian kiss."
    pc "Really?"
    robin.name "How do I get dragged into this?"
    nate.name "Kiss kiss kiss!"
    drake.name "Haha."
    pc "Ugh..."
    show robin_kiss with dissolve
    nate.name "Oooooh!"
    drake.name "Nice!"
    nate.name "Go go go!"
    hide robin_kiss with dissolve
    pc "Happy?"
    tempname.name "Yup."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_hard_7:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_shower")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    $ npc_race_picker(tempname, tempname)
    tempname.name "Hmm, I am all sweaty after that. How about we go have a shower together?"
    pc "Ok."
    $ walk(loc_school_locker_old)
    pause 0.5
    pc "Err, going to just stand there and watch me undress?"
    tempname.name "Ladies first."
    pc "Ha. Perv!"
    $ pc_striptease()
    pc "There we go. You coming?"
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
        tempname.name "Bet you were hoping for this."
        pc "Had worse outcomes. This way I end up clean at the end at least."
        tempname.name "Not if I can help it."
        jump school_field_soccer_play_end_shower_sex_offer_nate1


label school_field_soccer_hangout_dare_vhard_1:
    $ npc_race_picker(tempname)
    tempname.name "Ok, I am going for gold. Bend over naked [name], time for the loser to get fucked."
    pc "What? You serious?"
    if robin_here():
        robin.name "Wow!"
    tempname.name "I am. Unless you are a loser who is backing out?"
    pc "Fuck..."
    if player.vvirgin:
        pcm "Never had sex before. Am I really going to let [tempname.name] be my first?"
        menu:
            "There are worse ways to have my first time":
                $ NullAction()
            "No, this is too much":

                jump school_field_soccer_hangout_dare_vhard_1_backout
    elif not player.check_sex_agree(5):
        pcm "Having sex as a forfeit. A little extreme..."
        menu:
            "Undress and bend over":
                $ NullAction()
            "Back out of it.":
                jump school_field_soccer_hangout_dare_vhard_1_backout
    else:
        pcm "Damn pervert..."
        if not tempname.vsex:
            pcm "Well, was only a matter of time before [tempname.name] wanted to fuck me."
    pc "Ok, here we go..."
    $ pc_striptease()
    show sb_againstwall2 with dissolve
    pc "Getting a good view you perverts?"
    nate.name "Damn!"
    drake.name "Wow. Fuck."
    dan.name "..."
    if robin_here() and not "soccerboys_knows_pc_sex" in robin.list:
        $ add_to_list(robin.list, "soccerboys_seen_dare_sex")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
        robin.name "I can't believe what I am seeing..."
    pc "Well, gonna leave my arse hanging here or you going to do something?"
    tempname.name "Fuck yes!"
    show sb_againstwall2 cum with dissolve
    $ player.spank()
    pc "Ah!"
    tempname.name "Where do you want it?"
    if player.vvirgin:
        menu:
            "I'm still a virgin so use my arse instead":
                jump school_field_soccer_hangout_dare_vhard_1_anal
            "Have a go with my pussy":

                jump school_field_soccer_hangout_dare_vhard_1_vag
    else:
        menu:
            "Take me in the pussy":
                jump school_field_soccer_hangout_dare_vhard_1_vag
            "Use my arse":

                jump school_field_soccer_hangout_dare_vhard_1_anal

label school_field_soccer_hangout_dare_vhard_1_vag:
    if player.vvirgin:
        pc "But be gentle, it's my first time."
        tempname.name "First time?? Wow..."
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 pokevag
    $ player.spank()
    show sb_againstwall2 wink happy
    pc "Ah! ♥"
    tempname.name "Bet you were waiting for this to happen you dirty girl."
    pc "Shush."
    pc "Haa! ♥"
    $ player.sex_vag(tempname)
    show sb_againstwall2 insidevag closed ag worried with dissolve
    if player.virginbaby:
        "I feel [tempname.name]'s cock start to penetrate me. It is a strange feeling to be slowly spread and then start to feel it slide deeper."
        "I am not sure at what point I lost my virginity, but I do know at what point I felt completely stretched and full."
    else:
        "I feel [tempname.name] gently easing his cock deeper inside me. I am already quite wet so it finds little resistance and is welcomed inside."
    pc "Ahh fuck! ♥"
    tempname.name "Mmmmm. So warm."
    "I feel [tempname.name] gently thrusting in and out of me. I focus entirely on his cock pleasuring me and completely forget that there is an audience watching me get fucked."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        tempname.name "Ahhh!"
        $ player.sex_cum(tempname,"inside")
        show sb_againstwall2 shock worried open with dissolve
        "He presses into me as deep as he can and I feel his cock start to pulse inside me. No doubt making sure I take every drop he has to give me."
        pc "Ah I can feel you pumping in me. What the fuck?"
        tempname.name "Fuck ahhhh!"
        tempname.name "Yes!!!"
        pc "Hey, don't be all \"Yesing\" at me. You just came inside!"
        tempname.name "Fuck, sorry. I didn't expect to cum so quick."
        if not tempname == nate:
            nate.name "Well, that was anti climactic."
        else:
            drake.name "Well, that was anti climactic."
        show sb_againstwall2 pokevag with dissolve
        show sb_againstwall2 noman with dissolve
        pcm "Couldn't control himself and came right away..."
        pc "*Sigh*"
        hide sb_againstwall2 with dissolve
        $ pc_dress_slow()
        pcm "The pervert talks the talk, but couldn't do the walk..."
        jump school_field_soccer_hangout_conv_end

    if player.virginbaby:
        "Then it dawns on me. I am getting fucked for the first time, losing my virginity, while the others watch. I might have lost it to [tempname.name], but the others are witnessing it."
        "All 3 of my perverted friends are here for my first time."
    else:
        "I then realise that I am fucking one cock, but getting the other two off at the same time by acting in a live show porn movie for them."
    pc "Ahh yes! ♥"
    tempname.name "Ah fuck yes. You are lovin' it aren't you? Getting fucked with people watching."
    pc "Ha yes. You perverts enjoying as well? ♥"
    $ player.spank()
    pc "Haa!"
    tempname.name "Ah yes, I'm gonna cum!"
    menu:
        "Cum inside me!" if not player.has_perk(perk_preg_notwant):
            show sb_againstwall2 wink happy with dissolve
            tempname.name "Ah fuck yes! Don't be complaining if I knock you up!"
            pc "♥"
            "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
            tempname.name "Ahhh!"
            $ player.sex_cum(tempname,"inside")
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
            if player.has_perk(perk_preg_want) and not player.preg_knows:
                pc "Wonder if you managed to knock me up?"
                tempname.name "Don't say such things."
        "Pull out, pull out.":

            tempname.name "Mmm, I'll cover your arse with it. Don't wanna be knocking you up."
            pc "♥"
            "I feel him start to fuck me much faster and his breathing getting heavy. His hands now gripping hard into my ass cheeks which will no doubt leave a mark."
            tempname.name "Ahhh!"
            $ randomnum = renpy.random.randint(1, 10)
            if randomnum == 1:
                show sb_againstwall2 pokevaghand with dissolve
                $ player.sex_cum(tempname,"inside")
                show sb_againstwall2 shock open worried with dissolve
                "He quickly pulls out and starts masturbating while poking his cock against my pussy. I can then feel his warm wetness squirt against my lips and start running down my legs."
                show sb_againstwall2 frown with dissolve
                pc "Ah I can feel you cumming. Pull out more than that."
                tempname.name "Fuck ahhhh!"
                tempname.name "Yes!!!"
                pc "Idiot. Cumming like that can still be dangerous."
                tempname.name "Haaaaa!"
                pcm "He's not even listening..."
                tempname.name "Haa you dirty girl."
                show sb_againstwall2 open neutral with dissolve
                pc "Mmmm..."
                show sb_againstwall2 pokevag with dissolve
                show sb_againstwall2 noman with dissolve
                show sb_againstwall2 mast with dissolve
                pc "I am all leaking now."
                if player.has_perk(perk_preg_want) and not player.preg_knows:
                    pc "Wonder if you managed to knock me up?"
                    tempname.name "Don't say such things."
            else:

                show sb_againstwall2 cum with dissolve
                $ player.sex_cum(tempname,"pullout")
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

    pc "Mmmm."
    $ player.spank()
    pause 0.1
    show sb_againstwall2 shock with dissolve
    pc "Ah!"
    tempname.name "Unless you want someone else to take a turn, come and have a beer."
    show sb_againstwall2 neutral with dissolve
    pc "Mmm."
    hide sb_againstwall2 with dissolve
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_vhard_1_anal:
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
        $ player.sex_anal(tempname)
        pc "Haa fuck!"
    else:
        show sb_againstwall2 ag wink worried with dissolve
        "I feel him ease his way into my arse and feel myself stretching as he fills me up. He takes gentle thrusts with each one getting deeper and deeper until I can feel his body pressing against my ass."
        show sb_againstwall2 insideass with dissolve
        $ player.sex_anal(tempname)
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
    $ player.sex_cum(tempname,"anal")
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
    pc "*Sigh*"
    hide sb_againstwall2 with dissolve
    $ pc_dress_slow()
    pc "Ugh, I can feel you leaking down my leg."
    tempname.name "Here, take a beer."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_vhard_1_backout:
    pc "Sorry [tempname.name]. I am going to be a loser here."
    tempname.name "Ok, if you say so."
    tempname.name "LOSER!!!"
    pc "Yeah yeah..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_vhard_2:
    if robin_here():
        $ add_to_list(robin.list, "soccerboys_seen_dare_naked")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    tempname.name "I know, why don't you get yourself off in front of us?"
    $ player.face_worried()
    pc "What? Really?"
    tempname.name "Yup."
    $ player.face_annoyed()
    pc "Ugh. Right..."
    $ player.face_neutral()
    $ pc_striptease()
    show sb_againstwall2 mast with dissolve
    pc "*Sigh* How's this?"
    drake.name "Looks good from here."
    nate.name "Mmm, nice angle."
    nate.name "But you have to put some effort into it. You will be bent over here 'til you cum."
    drake.name "Or do it slow. Drinking a beer and looking at your naked ass is fine by us."
    pc "Damn perverts."
    show sb_againstwall2 closed worried with dissolve
    pcm "Best to pretend they are not here and just do what they are after."
    "With my eyes closed, I start touching between my legs and thinking of sexy thoughts to help get myself in the mood."
    "I know they all have their eyes on me. It should make me feel worse but instead it makes me feel quite excited knowing that they will probably wank off later to the thought of me doing this."
    pcm "Or maybe one of them will sneak up behind me with their hard cock..."
    show sb_againstwall2 pokevag with dissolve
    pcm "And slide it inside me..."
    show sb_againstwall2 insidevag with dissolve
    pcm "Mmm, and fuck me like a dirty whore. Maybe spank me a bit..."
    $ player.spank()
    pc "Haaa ♥"
    "I keep rubbing at my clit to the thoughts of someone fucking me from behind, getting hotter and hotter. Ignoring anything the perverts behind me have to say."
    "All I can think of is the imaginary cock inside me fucking me against the wall while the others watch."
    pcm "Mmmmmmm fuck!"
    pcm "Will you cum in me and risk knocking me up? Will you pull out? I don't care. You do as you wish."
    pcm "Haaaaaa."
    pcm "Yes fuck me!"
    $ player.sex_cum(nosex, "self")
    show sb_againstwall2 ag with dissolve
    pc "Ahhh fuck! ♥"
    pc "Ah yes yes!"
    pc "Mmmmmm..."
    pc "Phew..."
    show sb_againstwall2 open neutral straight noman with dissolve
    pc "Hmmm..."
    pc "That good for the show you dirty perverts."
    nate.name "Err, wow..."
    drake.name "Umm. Yes..."
    dan.name "..."
    pc "Right then."
    hide sb_againstwall2 with dissolve
    $ pc_dress_slow()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_darematch_play:
    $ walk(loc_school_field)
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

    call school_field_soccer_play_boys_picker from _call_school_field_soccer_play_boys_picker

    $ player.face_exercise()

    $ school_soccer_field_sex()

    call school_field_soccer_play_normal from _call_school_field_soccer_play_normal_2

    $ player.face_exercise()

    call school_field_soccer_play_boys_picker from _call_school_field_soccer_play_boys_picker_1

    $ player.face_exercise()

    $ school_soccer_field_sex()

    hide activity_soccer with dissolve

    $ walk(loc_school_field_back)
    if school_soccer_dare_win():
        $ player.face_happy()
        $ dialouge = WeightedChoice([
        ("Ah fuck. Good match.", 1),
        ("Dammit.", 1),
        ("Dammit. Couldn't concentrate with your tits bouncing all over the place", If (not c.bra, 1, 0)),
        ("Fuck, your ass swaying about is distracting...", If (c.ass, 1, 0)),
        ("Fuck, too busy trying to look up your skirt...", If (c.skirt, 1, 0)),
        ("Damn. Next time you need to dress properly. It's distracting.", If (c.exposed or c.inappropriate, 1, 0)),
        ("This is unfair. How am I supposed to play against your naked ass?", If (c.nude, 1, 0)),
        ])
        tempname.name "[dialouge]"
        jump school_field_soccer_darematch_play_won
    else:

        $ player.face_worried()
        if not school_soccer_quest_betmatch["can_challenge"]:
            pc "Fuck!"
            tempname.name "Language."
            tempname.name "Okay [name]. Pay up."
            pc "Ugh, sure..."
            $ player.add_money(-100)
            jump school_field_soccer_hangout_conv_end

        $ dialouge = WeightedChoice([
        ("Fuck. I lost...", 1),
        ("Ag, this oaf beat me...", 1),
        ("Dammit. Maybe I drunk too much...", If (player.drunk>70, 1, 0)),
        ])
        pc "[dialouge]"
        pc "Ok... What dare do you want me to do?"
        jump school_field_soccer_darematch_dare_picker

label school_field_soccer_darematch_play_preg:
    pc "So who wants to play in my place?"
    if not tempname == dan:
        dan.name "Yeah, let's go [tempname.name]."
    else:
        $ randomnum = renpy.random.randint(0, 1)
        if randomnum == 1:
            drake.name "Right, let's go [tempname.name]."
        else:
            nate.name "Oh? Right. Ok."
    "I stand and watch the boys play, helpless to do anything except cheer."
    $ player.face_happy()
    pc "GO GO GO!"
    if school_soccer_dare_win():
        $ player.face_happy()
        $ dialouge = WeightedChoice([
        ("Ah fuck. Good match.", 1),
        ("Dammit.", 1),
        ])
        tempname.name "[dialouge]"
        jump school_field_soccer_darematch_play_won
    else:

        $ dialouge = WeightedChoice([
        ("Fuck. I lost...", 1),
        ("Shit...", 1),
        ])
        pc "[dialouge]"
        pc "Ok... What dare do you want me to do?"
        jump school_field_soccer_darematch_dare_picker

label school_field_soccer_darematch_play_won:
    $ walk(loc_school_field_back)
    tempname.name "Ugh."
    $ player.face_happy()
    $ dialouge = renpy.random.choice([
    "Show me the money!",
    "Pay up loser.",
    "Hand it over.",
    "Come on, give it up.",
    ])
    pc "[dialouge]"
    tempname.name "Yeah yeah, here."
    $ player.face_neutral()
    $ player.add_money(100)
    jump travel

label school_field_soccer_darematch_play_sex_picker:
    if school_soccer_quest_dare_pitchsex["first"] == False:
        jump school_field_soccer_darematch_play_sex1

label school_field_soccer_darematch_play_sex1:
    $ npc_race_picker(tempname)
    tempname.name "Ah fuck this. Come 'ere [name]."
    pc "Huh?"
    if c.bottom or c.outfit or c.pants:
        $ pc_strip_lower()
        $ player.face_shock()
        with hpunch
        pc "Ah, what the hell?"
    tempname.name "You've been asking for this showing yourself off all over the pitch!"
    $ player.face_shock()
    $ pc_strip()
    hide activity_soccer
    show sb_doggy1 worried shock
    with hpunch
    pc "What the hell are you up to?"
    tempname.name "Your ass has been teasing me all match so I'm gonna punish it!"
    show sb_doggy1 neutral
    pc "Not my fault you are too much of a pervert to take your eyes off it."
    tempname.name "Not your fault but now your problem."
    if not player.check_sex_agree(4):
        pc "Ok, very funny but this is going too far."
        tempname.name "Hmm, you sure?"
        $ player.spank()
        pc "Ah!"
        $ player.spank()
        pc "Mmmm..."
        tempname.name "Still sure?"
        if not player.check_sex_agree(4):
            pc "I am sure."
            hide sb_doggy1 with dissolve
            $ pc_dress_slow()
            pc "No taking me on the pitch today thank you."
            pc "Does mean you forefeit the match though so pay up you dirty pervert."
            jump school_field_soccer_darematch_play_won
    pc "Damn pervert. Pushing over a poor innocent naked girl on the pitch."
    $ player.spank()
    pc "Ah! ♥"
    pc "Violence now is it?"
    $ player.spank()
    tempname.name "Be quiet!"
    tempname.name "Come here."
    show sb_doggy1 poke ah with dissolve
    pc "Waaa?"
    if player.desire >= 90 and player.check_drunk(3):
        jump school_field_soccer_darematch_play_sex1_vag
    else:
        menu:
            "This has gone too far":
                pc "Okay seriously, this is too much."
                hide sb_doggy1 with dissolve
                tempname.name "Ah fuck. If you say so."
                $ player.spank()
                pc "Ah, idiot."
                $ pc_dress_slow()
                pc "Let's drink instead and calm that cock of yours down."
                pc "You did forefeit the match though so pay up you dirty pervert."
                jump school_field_soccer_darematch_play_won

            "Not in my pussy" if player.check_anal_agree():
                jump school_field_soccer_darematch_play_sex1_anal
            "Keep silent":

                jump school_field_soccer_darematch_play_sex1_vag

label school_field_soccer_darematch_play_sex1_vag:
    with hpunch
    pc "Haaaa you are poking me!"
    tempname.name "Better be ready for more than just poking."
    with hpunch
    pc "Ah! ♥"
    pc "Fuck, here on the pitch in front of everyone?"
    tempname.name "Damn right. Punishment for using that body of yours to cheat me out of winning."
    $ player.spank()
    show sb_doggy1 closed oh
    pc "Ah fuuuu..."
    show sb_doggy1 vag tounge worried with hpunch
    $ player.sex_vag(tempname)
    pc "Ah fuck fuck yes!"
    show sb_doggy1 open
    if player.virgin_pregcheck:
        pc "You shitty cunt. Taking my virginity here in front of everyone!"
        tempname.name "You are a virgin?"
        pc "Haaa! Not any more ♥ You took it from me."
        tempname.name "Fucking hell. And they say you never forget your first. Out here on the pitch being watched by those two."
        pc "Mmmmmm. ♥"
    else:
        pc "You shitty cunt. Fucking me here in front of everyone!"
        tempname.name "About time as well. Showing off that arse while running around pretending to play."
        pc "Haaa, you perverts are too easy to tease."
    $ player.spank()
    pc "Ah fuck."
    pc "Keep going!"
    tempname.name "Dirty girl. Showing off that body when you play. Bet you love it even more being fucked in front of everyone."
    show sb_doggy1 closed
    pc "Haaa yes!"
    pc "Spank me more!"
    $ player.spank()
    tempname.name "Like this?"
    pc "Nng. Yes!"
    $ player.spank()
    tempname.name "Fuck you dirty girl. Would have done this sooner had I known how eager for it you are."
    $ player.spank()
    pc "♥"
    tempname.name "Fuck yes yes."
    tempname.name "Haaaa!"
    $ randomnum = renpy.random.randint(0, 1)
    if randomnum == 1:
        $ player.sex_cum(tempname,"inside")
        $ school_soccer_quest_dare_pitchsex["first"] = "vag_in_" + tempname.setname
        tempname.name "Fuck yes! Take it you bitch!"
        if player.preg_knows or player.has_perk(perk_preg_want) or not player.check_pullout():
            pc "Ah yes. Pump it in me!"
            tempname.name "Ahh fuck yes. Haaaa..."
            if player.preg_knows and player.preg_father_class.setname == tempname.setname:
                pc "You have already knocked me up, so pump more in me!"
            elif player.preg_knows and player.preg_father_class.setname in (drake.setname, nate.setname, dan.setname):
                pc "[player.preg_father_class.name] already knocked me up so don't hold back. Fill me up!"
            pc "Haaa..."
            if player.has_perk(perk_preg_want):
                pcm "Knock me up you arsehole!"
            pc "Mmmmmm..."
            tempname.name "Ahhhhhh..."
            show sb_doggy1 poke with dissolve
            $ player.spank()
            show sb_doggy1 pain
            pc "Ng!"
            show sb_doggy1 noman with dissolve
            pc "Phew..."
            jump school_field_soccer_darematch_play_sex1_end
        else:
            show sb_doggy1 shock open
            pc "Fuck no. Outside!"
            show sb_doggy1 poke with dissolve
            tempname.name "Ahh fuck yes. Haaaa..."
            $ player.cum_locations["cum_assout"] = True
            show sb_doggy1 closed neutral with dissolve
            pc "Haaa..."
            pcm "Arsehole!"
            pc "Mmmmmm..."
            tempname.name "Ahhhhhh..."
            $ player.spank()
            show sb_doggy1 pain
            pc "Ng!"
            show sb_doggy1 noman with dissolve
            pc "Phew..."
            jump school_field_soccer_darematch_play_sex1_end
    else:


        $ school_soccer_quest_dare_pitchsex["first"] = "vag_out_" + tempname.setname
        show sb_doggy1 poke with dissolve
        $ player.sex_cum(tempname,"pullout")
        tempname.name "Fuck yes! Take it you bitch!"
        pc "Ah yes. Put it all over me!"
        if player.has_perk(perk_preg_want):
            pcm "Should have came inside me, idiot!"
        tempname.name "Ahh fuck yes. Haaaa..."
        pc "Haaa..."
        if player.has_perk(perk_preg_want):
            pcm "No baby for me today..."
        pc "Mmmmmm..."
        tempname.name "Ahhhhhh..."
        $ player.spank()
        show sb_doggy1 pain
        pc "Ng!"
        show sb_doggy1 noman with dissolve
        pc "Phew..."
        jump school_field_soccer_darematch_play_sex1_end

label school_field_soccer_darematch_play_sex1_anal:
    $ school_soccer_quest_dare_pitchsex["first"] = "ass_in_" + tempname.setname
    with hpunch
    tempname.name "If you say so."
    pc "Haaaa you are poking me!"
    tempname.name "Better be ready for more than just poking."
    with hpunch
    pc "Ah! ♥"
    pc "Not in there..."
    tempname.name "Just getting my cock wet and ready for your arse."
    pc "Fuck, here on the pitch in front of everyone?"
    tempname.name "Damn right. Punishment for using that body of yours to cheat me out of winning."
    $ player.spank()
    show sb_doggy1 closed oh
    pc "Ah fuuuu..."
    $ player.sex_anal(tempname)

    if player.asex <= 5:
        show sb_doggy1 anal pain angry with hpunch
        pc "Ah fuck fuck!"
        pc "Nnng!"
    else:
        show sb_doggy1 anal tounge worried with hpunch
        pc "Ah fuck yes!"
        pc "Huuuuu!"

    show sb_doggy1 open
    pc "You shitty cunt. Ass fucking me here in front of everyone!"
    tempname.name "About time as well. Showing off that arse while running around pretending to play."
    pc "Haaa, you perverts are too easy to tease."
    tempname.name "And now your arse is paying the price for your teasing."
    $ player.spank()
    pc "Ah fuck."
    pc "Keep going!"
    tempname.name "Dirty girl. Showing off that body when you play. Bet you love it even more being fucked in front of everyone."
    show sb_doggy1 closed
    pc "Haaa yes!"
    pc "Spank me more!"
    $ player.spank()
    tempname.name "Like this?"
    pc "Nng. Yes!"
    $ player.spank()
    tempname.name "Fuck you dirty girl. Would have done this sooner had I known how eager for it you are."
    $ player.spank()
    pc "♥"
    tempname.name "Fuck yes yes."
    tempname.name "Haaaa!"
    $ player.sex_cum(tempname,"anal")
    tempname.name "Fuck yes! Take it you bitch!"
    pc "Ah yes. Pump it in me!"
    tempname.name "Ahh fuck yes. Haaaa..."
    pc "Haaa..."
    pc "Mmmmmm... I feel your cock pumping in my ass."
    tempname.name "Ahhhhhh..."
    show sb_doggy1 poke with dissolve
    $ player.spank()
    show sb_doggy1 pain
    pc "Ng!"
    show sb_doggy1 noman with dissolve
    pc "Phew..."
    jump school_field_soccer_darematch_play_sex1_end

label school_field_soccer_darematch_play_sex1_end:
    $ player.face_neutral()
    show sb_doggy1 neutral open with dissolve
    pc "Ahhh..."
    pcm "Ugh, can't be staying here with my arse out like a bitch..."
    pc "Hup..."
    hide sb_doggy1 with dissolve
    if player.has_perk(perk_exhibitionist) and "temp_outfit" in tab_top:
        pcm "Leaving me here with my arse in the air to go and boast about fucking me..."
    else:
        pcm "Right. Clothes? Did that arsehole really just piss off and go back to the beers?"
        pcm "Could have helped me find my clothes first before going off to boast over fucking me..."
        $ pc_dress_slow()
    $ walk(loc_school_field_back)
    if player.has_perk(perk_exhibitionist) and "temp_outfit" in tab_top:
        pc "Thanks for leaving me on the pitch all naked you arse!"
    else:
        pc "Thanks for helping me get my clothes you arse!"
    tempname.name "Got you a beer instead. Here."
    if robin_here() and not "soccerboys_seen_pitchsex" in robin.list:
        $ add_to_list(robin.list, "soccerboys_seen_pitchsex")
        $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
        robin.name "Wow [name]! Quite a show."
        $ player.face_shock()
        pc "Ah, you saw..."
        robin.name "If you told me this morning that I'd see [tempname.name] fucking you out on the pitch I'd have called you a liar."
        $ player.face_annoyed()
        pc "He's a violent criminal."
        robin.name "\"Spank me more! Oooh!\""
        $ player.face_shy()
        if "pc_know_want_bussex" in robin.list:
            pc "Quiet you bus deviant."
            robin.name "Ah!"
            nate.name "Wait, what?"
        else:
            pc "Shush!"
        pc "Anyway [tempname.name]. You lost, so pay up."
    else:
        pc "Beer? You lost the match so pay up."
    tempname.name "What? Lost?"
    pc "You assaulted your opponent and committed violence on her."
    tempname.name "Vio... Wha?"
    pc "Shhh. Just pay up."
    jump school_field_soccer_darematch_play_won
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
