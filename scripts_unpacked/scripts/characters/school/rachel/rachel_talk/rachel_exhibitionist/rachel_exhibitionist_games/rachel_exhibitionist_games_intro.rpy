label rachel_talk_exhib_game_start:
    $ rachel.dict["rachel_talk_exhib_games_chain"] += 1
    rachel.name "Oh? So want to play do you?"
    pc "Well, I thought I would see what crazy stuff you had in mind."
    rachel.name "Nothing crazy. I just thought we would take turns telling each other something to do."
    pc "While naked?"
    rachel.name "Of course!"
    pc "Right..."
    rachel.name "I'm still scared though. So we can go easy at the start."
    pc "Okay. Any ideas?"
    rachel.name "Yeah I do!"
    rachel.name "Go upstairs to the library and get me a book."
    pc "Err... Why do I go first?"
    rachel.name "Because I had the idea. You should have thought of something for me to do."
    pc "..."
    jump rachel_talk_exhib_game_library

label rachel_talk_exhib_game_library:
    menu:
        "Go upstairs and get the book":
            $ NullAction()
        "Another time":
            rachel.name "Boring!"
            hide rachel with dissolve
            jump travel
    $ exhib_games_playgame(True)
    pc "Okay..."
    rachel.name "Good luck. Don't hurry!"
    pc "..."
    hide rachel with dissolve
    pcm "Digging my own grave here. It's her weird ideas and I am the one prancing around naked..."
    $ walk(loc_school_hallway)
    $ player.cover()
    pcm "Not like there is anyone in here anyway."
    pcm "Although the boys outside might come in here."
    pcm "They never do though."
    $ walk(loc_school_hallway_2f)
    pcm "..."
    pcm "Could just rush in there and grab it, but that's kind of not the point of the game."
    pcm "..."
    pcm "Ugh, well standing here doing nothing isn't much fun either..."
    $ walk(loc_school_library)
    pcm "Graveyard as always."
    pcm "Hmmm, don't really want to take a book since it would probably never return."
    pcm "I'll just take this flyer thing."
    $ player.left_hand = "flyer"
    pcm "..."
    $ player.face_happy()
    $ player.uncover()
    pcm "Lalalala..."
    pcm "I am naked..."
    pcm "In the library..."
    pcm "..."
    $ player.face_neutral()
    $ player.cover()
    pcm "Right..."
    $ walk(loc_school_hallway_2f)
    pcm "Go back to [rachel.name] I guess."
    $ walk(loc_school_hallway)
    pcm "Still no one here. This was easy."
    $ add_to_list(rachel.list, "streaking")
    $ walk(loc_school_gym)
    pcm "Hmm, where is she?"
    pc "[rachel.name]?"
    $ remove_from_list(rachel.list, "streaking")
    show rachel at right1 with dissolve
    rachel.name "Here I am."
    $ player.uncover()
    pc "Where did you go?"
    rachel.name "I was hiding."
    pc "Oh?"
    pc "Well, I went to the library."
    rachel.name "Really? Show me the book."
    pc "Well, didn't want to steal a book so I bought this."
    $ player.left_hand = ""
    rachel.name "Wow. You actually went?"
    pc "Well, that was the game. And I get to make you do something next time."
    rachel.name "Ah yeah you do. Better think of something then."
    pc "Right."
    hide rachel with dissolve
    pcm "Probably shouldn't think of something too extreme or she will do the same next turn."
    jump travel

label rachel_talk_exhib_game_doors:
    $ exhib_games_playgame(False)
    pc "Okay, your turn now."
    rachel.name "Okay. What do you want?"
    pc "Go to the main doors and press yourself against them until a guy walks past outside."
    rachel.name "Err, okay. What if he sees me?"
    pc "Hmm, then show off?"
    rachel.name "Okay... I'll try..."
    rachel.name "The doors are locked, right?"
    pc "Should be. You can try and open yourself and see."
    rachel.name "Okay."
    $ add_to_list(rachel.list, "streaking")
    hide rachel with dissolve
    pcm "Hmmm..."
    pcm "So I just wait here stark naked?"
    pcm "..."
    pcm "I'm gonna spy on her."
    show rachel_exhib_doors at right2
    $ walk(loc_school_hallway)
    pcm "Looks like she is going for it."
    pcm "Well, good. I don't want to be doing all this naked stuff while she doesn't play along."
    pcm "Maybe it can be fun."
    pcm "We are in here alone. Only the boys outside but they never come in here."

    if all([drake.sex, nate.sex, dan.sex]):
        pcm "What does it matter anyway? We have all had sex and been naked. So probably wouldn't even shock them."
    elif all([drake.seen_naked, nate.seen_naked, dan.seen_naked]):
        pcm "Well, not that it would matter much. They have all seen me naked."
    else:
        pcm "Even if they did, they would go away if I told them to."

    pcm "Probably more fun if they are there though. Then I risk getting caught."
    pcm "Without risk it's no different that being in your bedroom nude or something."
    pcm "Well, maybe not quite like that. But close..."
    pcm "..."
    pcm "Ah well. I'll just go back to the gym. Don't want [rachel.name] catching me."
    hide rachel_exhib_doors
    $ walk(loc_school_gym)
    pcm "..."
    pcm "Bit boring just waiting here alone."
    pcm "Maybe next time we should do something together."
    pcm "Ah, but it's her turn to pick what I do next time."
    pcm "..."
    $ player.uncover()
    $ player.face_happy()
    pc "Lalalala!"
    pcm "..."
    pcm "I know!"
    show ps_dance with dissolve
    pcm "Dancing is what [rachel.name] was doing when I caught her."
    pcm "Feels very different when you are butt naked."
    pcm "I can see why she was doing it."
    pcm "It's... Interesting."
    hide ps_dance
    show dance_behind
    with dissolve
    pcm "My bare ass in the wind."
    pcm "Well, no wind. Whatever."
    pc "Lalalala!"
    pcm "Hmmm..."
    pc "[rlist.singing_dialogue_1]"
    pc "[rlist.singing_dialogue_2]"
    pc "[rlist.singing_dialogue_3]"
    show rachel nude happy at right1 with dissolve
    pc "[rlist.singing_dialogue_4]"
    rachel.name "Having fun?"
    hide dance_behind
    $ player.face_shock()
    $ player.cover()
    with hpunch
    pc "Whaaaaaa!"
    pc "Fuck... Scare the life out of me!"
    rachel.name "Hahahaha!"
    pc "Ugh. Heart almost jumped out my chest..."
    $ player.cover_reset()
    $ player.face_neutral()
    pc "*Phew*"
    pc "So... What happened?"
    rachel.name "Ahh, nothing much."
    pc "No?"
    rachel.name "I stood there for ages and was getting bored. Then some guy walked past."
    pc "And?"
    rachel.name "And he walked past. Didn't even look or see me."
    pc "Ah, bit anti climactic."
    rachel.name "No, it was fun. I don't wanna run in the park yet."
    pc "Yet?"
    rachel.name "Eventually we will."
    pc "We!?"
    rachel.name "Yeah. Get us both dragged of. Loads of fun!"
    pc "Right..."
    pc "..."
    $ remove_from_list(rachel.list, "streaking")
    hide rachel with dissolve
    jump travel

label rachel_exhib_game_cafe:
    $ exhib_games_playgame(True)
    rachel.name "Okay. Go to the cafeteria, get something to eat, sit and eat it and don't leave."
    pc "Err, okay."
    rachel.name "You can't leave no matter what until you have finished."
    pc "Should be fine."
    rachel.name "Big windows in there."
    pc "True..."
    hide rachel
    $ walk(loc_school_hallway)
    pcm "Hmmm..."
    pcm "Do they even have food at this time in there?"
    $ walk(loc_school_cafe)
    pcm "..."
    pcm "This place is much colder when it's empty."
    pcm "And when I am naked..."
    pcm "Right, no food. Of course..."
    pcm "Well, I guess I just sit here then?"
    show sb_sitting worried with dissolve
    pcm "How long should I sit here? I was supposed to eat but nothing to eat..."
    pcm "Big windows, but at this time there is no one to even look in them."
    pcm "Hmmm..."
    hide sb_sitting with dissolve
    pcm "I wonder..."
    show activity_windowshow_front nosale with dissolve
    if drake.has_met:
        pcm "I wonder if the boys are out there."
        if drake_here(loc_school_field_back):
            pcm "Ah, I can see them..."
            pcm "Just about."
            if robin_here(loc_school_field_back):
                pcm "Looks like [robin.name] is there too."
                if all([drake.sex, nate.sex, dan.sex]):
                    pcm "Bitch, having fun with them without me..."
        else:
            pcm "Don't think I can see them."
            pcm "Wait, hope that doesn't mean they are in here or something..."
            pcm "Probably not. Went home drunk I guess."
    else:
        pcm "Don't imagine anyone is out there."
        pcm "Wonder if those boys are still playing."
        pcm "Doubt it, probably too late."
    pcm "Ah well..."
    hide activity_windowshow_front with dissolve
    pcm "Suppose I'll just wait..."
    show sb_sitting worried with dissolve
    pcm "..."
    pcm "Ass is cold on this chair."
    "I just sit around with nothing much to do. I can't imagine anyone but [rachel.name] coming inside so I am not really worried."
    $ relax(5)
    pcm "Would be more interesting if there was something to do."
    pcm "Think next time I'll have to give [rachel.name] an task to do so she isn't just sitting around bored."
    pcm "..."
    pcm "Ah well, this is long enough."
    hide sb_sitting with dissolve
    pcm "Suppose I'll go back."
    $ walk(loc_school_hallway)
    $ add_to_list(rachel.list, "streaking")
    $ walk(loc_school_gym)
    pcm "..."
    pc "[rachel.name]?"
    show rachel at right1 with dissolve
    $ remove_from_list(rachel.list, "streaking")
    rachel.name "You did it?"
    pc "Yeah."
    rachel.name "How was it?"
    pc "Kinda boring actually. Staying in one place isn't much fun."
    pc "And no food in there at this time. So I just sat there."
    rachel.name "Oooh yeah. Didn't think of that."
    pc "Next time something more fun."
    rachel.name "Ooh, sound fun."
    pc "Mmm."
    hide rachel nude with dissolve
    jump travel

label rachel_exhib_game_thinking:
    $ exhib_games_playgame(False)
    pc "So I was thinking. Last time I just sat there doing nothing."
    rachel.name "Yeah."
    pc "So maybe something a little more interesting?"
    rachel.name "Okay. What do you think?"
    pc "Hmmm..."
    pc "How about you sneak round the back entrance and out of the school..."
    rachel.name "Out of the school?!"
    pc "And come to the front doors where I will be watching. Do a pose then come back."
    rachel.name "Out of the school? Into the street?"
    pc "Yeah, but it's just along the wall. I don't think anyone will see you."
    rachel.name "They might."
    pc "Maybe."
    rachel.name "..."
    rachel.name "Okay."
    rachel.name "Scary..."
    pc "Oh, be careful of the boys out there."
    rachel.name "Forgot about them."
    pc "I'll be watching the fun in case they catch you."
    rachel.name "Will you save me if they do?"
    pc "..."
    pc "No."
    rachel.name "Haha!"
    $ add_to_list(rachel.list, "streaking")
    hide rachel with dissolve
    $ walk(loc_school_hallway)
    $ walk(loc_school_cafe)
    $ remove_from_list(rachel.list, "streaking")
    pcm "I think I can see the boys from here."
    show activity_windowshow_front nosale with dissolve
    pcm "Where are they?"
    if robin_here(loc_school_field_back):
        pcm "There they are. [robin.name] as well."
    else:
        pcm "Ah, I see them."
    pcm "Doesn't look like they are paying attention."
    pcm "It's dark out there so can't imagine they will see [rachel.name]."
    pcm "..."
    pcm "Okay, she has probably made it past by now."
    hide activity_windowshow_front with dissolve
    pcm "Let' see if she made it to the doors."
    $ walk(loc_school_hallway)
    pcm "Hmmmm..."
    pcm "Just realised this is almost a dare for me as well. Last time I told [rachel.name] to go to the doors and now that's that I am doing."
    pcm "Whatever."
    pcm "Where is she?"
    pcm "Hope she didn't bump into someone."
    pcm "Or maybe I should hope she did?"
    pcm "I suppose running around like this is all about risking getting caught."
    pcm "What should we do if we do get caught?"
    if quest_wolfgang.active:
        pcm "[rachel.name]'s story of the girl in the park sound like those wolf guys so probably not as bad as it sounds."
        pcm "But either way we would be getting dragged off into the bushes."
    else:
        pcm "[rachel.name]'s story of the girl in the park obviously wasn't someone having fun running around naked."
        pcm "But no doubt they would still want us to go in the bushes with them."
    pcm "..."
    if player.check_sex_agree(4):
        pcm "Could be kinda fun."
    else:
        pcm "Not sure I am ready to be doing that."
    pcm "Oh?"
    $ player.face_happy()
    show rachel_pose_peace with dissolve
    pc "Hahaha!"
    pc "You make it!"
    rachel.name "I did!"
    pc "Looking good!"
    rachel.name "Thanks! No one is here."
    pc "Gonna stand there until someone is?"
    rachel.name "Maybe!"
    rachel.name "No..."
    rachel.name "Haha! Fun!"
    hide rachel_pose_peace with dissolve
    $ player.face_neutral()
    pc "Hahaha!"
    pcm "Well, she did it."
    pcm "Brave."
    $ walk(loc_school_cafe)
    show activity_windowshow_front nosale with dissolve
    pcm "Let's see if I can catch her."
    pcm "..."
    pcm "Too dark to see anything."
    pcm "Hmmm..."
    pcm "..."
    pcm "Is that...?"
    pcm "No. Not her..."
    pcm "..."
    if nate.has_met:
        pcm "Hold on? Is [nate.name] looking at me?"
    else:
        pcm "Hold on? Is that one of the boys looking at me?"
    pcm "Na, too dark. He shouldn't me able to see me."
    hide activity_windowshow_front
    show rachel nude happy at right1
    $ player.spank()
    $ player.face_shock()
    pc "Ahhhhh!"
    pc "Fuck! Almost had heart attack."
    rachel.name "Haha!"
    $ player.face_neutral()
    rachel.name "I saw you by the window as I was sneaking in so thought I would have fun."
    pc "Wait. Isn't it too dark to see in here?"
    rachel.name "Huh? No. It's like a TV screen since it's dark out there and bright in here."
    pc "Ah..."
    pcm "Fuck!"
    rachel.name "I'll think of something for you next time."
    pc "Okay."
    hide rachel with dissolve
    jump travel

label rachel_exhib_game_mast:
    $ exhib_games_playgame(True)
    rachel.name "Okay! I have a bad one for you."
    pc "A bad one?"
    rachel.name "Yup!"
    pc "Okay..."
    rachel.name "Go outside and have fun down there!"
    pc "What? Wait, you mean...?"
    rachel.name "You have to be outside."
    pc "Really?"
    rachel.name "Yup!"
    pc "..."
    pc "Okay..."
    rachel.name "Don't get caught by the boys!"
    pc "I'll point them in your direction if I do."
    rachel.name "Haha!"
    hide rachel with dissolve
    pcm "Right..."
    pcm "Outside..."
    pcm "That's a much tougher one..."
    $ walk(loc_school_hallway)
    pcm "Do I need to go out the school or just out the building?"
    pcm "The pitch area counts as outside doesn't it?"
    pcm "Either way, I am not going far. Either the bushes by the field or the bushes by the secret entrance."
    menu:
        "The field":
            $ temp_var_1 = "field"
        "The secret entrance":
            $ temp_var_1 = "entrance"
    pcm "Okay..."
    $ walk(loc_school_field)
    pcm "Dark so should be hidden."
    if temp_var_1 == "field":
        $ walk(loc_bushes)
    else:
        $ walk(loc_school_secret_entrance)
    pcm "Okay..."
    show sb_mast_stand with dissolve
    pcm "..."
    if t.month == "Winter":
        pcm "Be a lot nicer if I wasn't freezing my tits off..."
    elif weather_var == 3:
        pcm "Be a lot nicer if it wasn't pissing rain..."
    $ player.face_sleep()
    pc "Mmmm..."
    "I put my hand down between my slit and start to play with myself. Imagining nice things."
    call masturbate_fantasy_picker from _call_masturbate_fantasy_picker_4
    call expression rand_choice from _call_expression_23
    if not numgen(0,4) and loc(loc_school_secret_entrance):
        $ temp_var_1 = "stranger"
        pc "Haaaaaa..."
        $ tempname = streetpervert
        $ quest_temp = None
        $ male_npc_create_all()
        $ renpy.scene()
        show male_generic nude at right1
        with dissolve
        $ player.face_shock()
        pc "Ah fuck!"
        tempname.name "Don't mind me [rlist.name_cute]. Just enjoying the show."
        pc "Why are you naked?"
        tempname.name "Why are *you* naked?"
        pc "Err..."
        if player.check_sex_agree(4, exhibitionist=True):
            pc "Because I want to be."
            tempname.name "Looking at you, so do I."
            pc "Yeah, looking at your thing, looks like someone has been enjoying the show."
            tempname.name "Of course. Not every day you see a slut fingering herself in the bushes."
            pc "Well, good for you."
            tempname.name "Want some help?"
            pc "Huh?"
            tempname.name "Got something nicer here to put inside you."
            pc "Oh?"
            if player.check_sex_agree_choice(3, "Sure, why not", "No thanks"):
                $ temp_var_1 = "sex_stranger"
                pcm "The dare was \"until I finish\", would be cheating to not actually finish."
                pcm "..."
                pcm "Such a lame excuse."
                pc "Sure, why not?"
                tempname.name "Oh nice."
                $ event_end_interrupt_label = "rachel_exhib_game_mast_sex_stranger_end"
                jump whore_street_sex_sex_picker
            else:
                pc "Err, no thanks. Think I had better head off."
                tempname.name "Shame."
                pc "See ya."
                $ walk(loc_school_field)
                pcm "Not following me..."
                $ walk(loc_school_hallway)
                pcm "That was fucking scary. Can't believe a stranger caught me."
        else:
            pc "I... Err..."
            pc "See ya!"
            $ walk(loc_school_field)
            pcm "Not following me..."
            $ walk(loc_school_hallway)
            pcm "That was fucking scary. Can't believe a stranger caught me."
    else:

        pc "Haaaaaa..."
        $ player.sex_cum(nosex, "self")
        $ player.face_orgasm()
        pc "Ahhh yes yes!"
        pc "..."
        $ player.face_shame()
        pc "Fuuuu..."
        if temp_var_1 == "field" and nate.sex:
            $ add_to_list(nate.list, "exhib_seen")
            $ temp_var_1 = "nate"
            nate.name "Having fun?"
            hide sb_mast_stand
            show nate at right1
            $ player.face_shock()
            with hpunch
            pc "AHHHHHH!!!!"
            pc "Fuck!"
            pc "Fucking hell [nate.name]! You want to kill me?"
            pc "Jesus christ!"
            pc "..."
            $ player.face_annoyed()
            pc "What are you doing here?"
            nate.name "Saw you sneak off into the bushes so thought I would see what you were up to."
            pc "Ugh. Damn pervert."
            nate.name "Sure. I'm the pervert."
            nate.name "What are you up to anyway?"
            pc "None of your business!"
            hide nate
            $ walk(loc_school_field)
            pc "Idiot!"
            $ walk(loc_school_hallway)
            pcm "Fucking hell. My heart is pounding."
        else:

            pcm "..."
            hide sb_mast_stand with dissolve
            pcm "I think that's good enough."
            pcm "And no weirdos jumping out the bushes on me."
            $ walk(loc_school_field)
            pcm "No one looking for me..."
            $ walk(loc_school_hallway)
            pcm "That one was kind of scary."
    jump rachel_exhib_game_mast_return

label rachel_exhib_game_mast_sex_stranger_end:
    $ renpy.scene()
    show male_generic at right1
    with dissolve
    tempname.name "That was fun."
    pc "Sure was. But I'm gonna go now."
    tempname.name "Okay."
    hide male_generic
    $ walk(loc_school_field)
    pcm "Not following me is he?..."
    pcm "No, seems fine."
    $ walk(loc_school_hallway)
    pcm "That one was kind of scary."
    jump rachel_exhib_game_mast_return

label rachel_exhib_game_mast_return:
    $ walk(loc_school_gym)
    pc "I'm back."
    show rachel at right1 with dissolve
    rachel.name "How was it?"
    if temp_var_1 == "stranger":
        $ player.face_shock()
        pc "Scary. I got caught."
        rachel.name "You did?"
        pc "Yeah, I was standing there doing my thing, and just as I was close, I notice some naked man next to me wanking."
        show rachel happy
        rachel.name "Pfftt! Hahahahahahahahahaha!!!!!"
        $ player.face_sus()
        pc "Yeah yeah. Laugh it up."
        rachel.name "Hahaha!! What did you do?"
        $ player.face_normal()
        pc "Nothing. Kinda chatted a bit then I left."
        rachel.name "Amazing! Was it fun?"
        pc "Err, didn't think about that actually. Was more shocked I got caught."
        rachel.name "So nothing happened?"
        pc "Na, I left before things could get crazy."
        rachel.name "So fun."
    elif temp_var_1 == "sex_stranger":
        $ player.face_shock()
        pc "Fuck!"
        rachel.name "What?"
        pc "I got caught!"
        rachel.name "You did? By who?"
        pc "I was, y'know, doing my thing down there. At some point opened my eyes and some guy was standing near me, stark naked and wanking."
        show rachel happy
        rachel.name "Pfftt! Hahahahahahahahahaha!!!!!"
        $ player.face_sus()
        pc "Yeah yeah. Laugh it up."
        rachel.name "Hahaha!! What did you do?"
        $ player.face_happy()
        pc "I fucked him."
        rachel.name "Really?"
        pc "Yeah. We chatted for a bit and he offered to use his thing to help me down there."
        rachel.name "Oooh. Good idea."
        pc "Yeah, so he did. The dare was done and I told him goodbye."
        rachel.name "Haha. Wow that is amazing. Wish I was there now."
        pc "I'm sure the guy would have liked that."
        rachel.name "So fun."
    elif temp_var_1 == "nate":
        $ player.face_worried()
        pc "Err... I kinda got caught."
        rachel.name "Hahaha! Really? How?"
        pc "I was in the bushes, y'know, doing my thing."
        pc "And when I was done, [nate.name] was behind me."
        rachel.name "Wow! Really? What did he say?"
        pc "Nothing. I swore at him and left."
        pc "Almost had a heart attack when he called me."
        pc "Heart still feels like it might die."
        rachel.name "Hahaha! Wow that's amazing!"
        pc "Sure..."
        rachel.name "Did he see what you were doing?"
        pc "Knowing him, he was there the whole time."
        rachel.name "Ooooh. How fun!"
    else:
        pc "Fine, I went into the bushes round back and, y'know..."
        rachel.name "Did you finish the job?"
        pc "Yeah. I didn't cheat."
        rachel.name "Oooh. Good. Was it fun?"
        pc "Scary."
        pc "But yeah, kind of interesting."
        rachel.name "Yeah?"
        pc "Yeah, never done that before."
        rachel.name "Haha! Fun!"
    hide rachel with dissolve
    pcm "Fun indeed."
    jump travel

label rachel_exhib_game_tease:
    $ exhib_games_playgame(False)
    pc "Okay, since you sent me outside to get caught, I have something risky for you."
    rachel.name "Oh? Scary!"
    pc "I want you to make a full circle around the pitch."
    rachel.name "That sounds easy."
    pc "Don't forget the boys are out there."
    rachel.name "Oh yeah..."
    pc "Not sure how you are going to manage not getting caught."
    rachel.name "Yeah..."
    rachel.name "Okay. I can do it."
    $ add_to_list(rachel.list, "streaking")
    hide rachel with dissolve
    pcm "Wow. I thought she might have tried to avoid that one."
    if any([dan.name in rachel.sex_who, nate.name in rachel.sex_who, drake.name in rachel.sex_who]):
        pcm "Although not like they haven't seen her naked already."
    else:
        pcm "Not even sure if she has met them before."
    pcm "Okay, let's see what she is up to."
    $ walk(loc_school_cafe)
    pcm "[rachel.name] said last time it's easy to see me from this window..."
    pcm "Whatever."
    show activity_windowshow_front nosale with dissolve
    pcm "Hmmm..."
    pcm "Can't see her near the doors, where is she?"
    $ player.face_happy()
    pcm "Oh shit!"
    hide activity_windowshow_front
    show rachel_exhib_run
    with dissolve
    pcm "She isn't even trying to hide!"
    pcm "Going at it full sprint."
    pcm "Haha, well at least as fast as she can run. How is she so bad at it?"
    pcm "No way the boys haven't seen her."
    pc "Hahaha!"
    pcm "Here she comes."
    hide rachel_exhib_run with dissolve
    $ walk(loc_school_hallway)
    pcm "..."
    show rachel happy at right1 with dissolve
    rachel.name "Haha! I did it!"
    pc "Yeah. Didn't expect you to just flat out run."
    rachel.name "I'm fed up hiding away. They can have a look."
    rachel.name "Bet it shocked them."
    pc "I bet it did."
    rachel.name "You're gonna be in trouble next time."
    pc "Uh oh."
    hide rachel with dissolve
    $ remove_from_list(rachel.list, "streaking")
    jump travel

label rachel_exhib_game_boys:
    $ add_to_list(school_soccer_quest.conversation_topics, "exhibitionist_asked")

    pc "Okay, what bad one do you have for me?"
    rachel.name "Go hang out with the boys."
    pc "Err..."
    if not school_soccer_hangingout():
        pc "I didn't see the boys out there though, I think we will have to try another day."
        rachel.name "Really?"
        hide rachel with dissolve
        jump travel
    $ exhib_games_playgame(False)
    rachel.name "Go over there and talk to them."
    if not drake.has_met:
        pc "I don't even know them!"
        rachel.name "Well go an say hello. You will make them happy."
    elif not loc_school_field_back.visited:
        pc "Shit, I haven't even hung out with them round there. It's all dark and isolated."
        rachel.name "Have fun!"
    elif not all([drake.seen_naked, nate.seen_naked, dan.seen_naked]):
        pc "Shit, this will be te first time they see me like this."
        rachel.name "Even better!"
    else:
        pc "Well, they have already seen me naked..."
        rachel.name "Awww. Then it wont be so scary."
    pc "Right... Okay then..."
    pc "..."
    hide rachel
    $ walk(loc_school_hallway)
    pcm "Just pretend it's normal."
    $ walk(loc_school_field)
    if robin_here(loc_school_field_back):
        pcm "Ah shit. [robin.name] is there as well..."
        pcm "The boys might find it fun, but her?"
        pcm "No choice. Sorry [robin.name]."
    pcm "Right..."
    $ player.uncover()
    pcm "Okay..."
    pcm "Just do it..."
    if drake.has_met:

        $ walk(loc_school_field_back)
    if not drake.has_met:
        $ drake.meet()
        $ nate.meet()
        $ dan.meet()
        $ walk(loc_school_field_back)
        $ loc_school_field_back.locked = False
        pc "Err, hi guys. Nice to meet you."
        drake.name "Err, hi."
        nate.name "Nice to meet you."
        dan.name "Same."
        drake.name "Got some beer if you want."
        pc "Ooh, that would be nice."
        dan.name "Here."
        pc "Thanks."
        drake.name "So... Err, what brings you round here?"
        pc "Ah, just seen you hanging around here and thought I would say hello."
        drake.name "I'm... Err... I'm guessing with how you're dressed, you are friends with the other girl."
        pc "[rachel.name], yeah."
        pc "I hope you don't mind."
        drake.name "Mind what?"
        nate.name "Not at all!"
        nate.name "More than welcome. Should invite your friend as well."
        pc "Ah, maybe another time. She would probably like it."
        nate.name "So would we."
        pc "Heh."
    elif not school_soccer_quest_hangout_prompt:
        pc "Err, hey guys."
        drake.name "Err, hey [name]."
        pc "You drinking beer round here?"
        drake.name "Yeah, interested?"
        pc "Sure am."
        nate.name "So, you are dressed nice."
        pc "Like it? Took ages to pick it out my wardrobe."
        nate.name "Sure, looks good on you."
        drake.name "The other girl not around?"
        pc "Na, she's probably hiding by the window watching me."
        drake.name "Ah. That's what's going on?"
        pc "Something like that."
        nate.name "Well, keep it up!"
    elif all([drake.sex, nate.sex, dan.sex]):
        pc "Hey."
        drake.name "Hey [name]."
        if robin_here():
            robin.name "Why are you naked?"
            nate.name "Shhhh! Don't ask questions."
            robin.name "What? But..."
            nate.name "Just enjoy."
            robin.name "Ugh, you're all bloody perverts!"
            nate.name "Yup!"
        else:
            nate.name "[rachel.name] going to be joining us as well?"
            pc "Maybe."
            drake.name "And hanging here becomes even more fun."
        pc "Perverts!"
        nate.name "..."
        drake.name "Errr..."
        dan.name "First time I've seen [nate.name] with no words."
    elif all([drake.seen_naked, nate.seen_naked, dan.seen_naked]):
        nate.name "Whoo! Go [name]!"
        pc "Hey."
        nate.name "Do we get a dance as well?"
        pc "Maybe one day."
        drake.name "Didn't get your clothes stolen or something did you?"
        pc "No. Just messing about."
        drake.name "Okay. Well thats good."
        nate.name "Your friend joining us?"
        pc "Maybe. She's hiding for now."
        drake.name "Her friend?"
        nate.name "Yeah, she has been doing weird stuff with [rachel.name]."
        drake.name "Oh, her."
        if robin_here():
            robin.name "What weird stuff?"
            nate.name "Dunno. They have been running around naked and doing whatever."
            robin.name "Really?"
            if "exhib_seen" in nate.list:
                nate.name "Yeah, I caught [name] in the bushes and saw [rachel.name] running around."
            else:
                nate.name "Yeah, saw [name] in the window watching [rachel.name] run around the pitch."
            robin.name "Wow!"
    elif any([drake.seen_naked, nate.seen_naked, dan.seen_naked]):
        pc "Hey guys."
        nate.name "Hey [name]. What brings your naked ass over here?"
        pc "Beer."
        nate.name "Sure."
        if robin_here():
            robin.name "Is this something she does often?"
            nate.name "Kinda. Her and [rachel.name] seem to be up to weird things."
            robin.name "Oh?"
        else:
            drake.name "So decided to come and say hello instead of sneaking around?"
            pc "Ah, you saw before?"
            drake.name "Yeah, sort of."
        pc "Well, going to give me a beer?"
        dan.name "Here."
    else:
        pc "Hey guys."
        drake.name "Err, hey [name]."
        if robin_here():
            robin.name "What crazy thing are you up to now?"
            pc "What do you mean?"
            robin.name "What do you mean \"what do you mean\"?"
            pc "Are you ok?"
            robin.name "What? Am I ok?"
            pc "Yeah?"
            robin.name "Ugh!"
            nate.name "Shhh [robin.name]. Enjoy the fun."
        else:
            pc "No beer?"
            dan.name "Here."
            pc "Thanks."
            drake.name "So, I was, err..."
            drake.name "Fuck, I forgot what I was talking about."
            nate.name "Don't think anyone cares any more."
    jump school_field_soccer_hangout_conv_end

label rachel_exhib_game_boys_rachel:

    pc "Right, I think you know what you are doing."
    rachel.name "Yeah..."
    if not school_soccer_hangingout():
        pc "I didn't see the boys out there though, I think we will have to try another day."
        rachel.name "Really?"
        hide rachel with dissolve
        jump travel
    $ exhib_games_playgame(True)
    pc "Okay."
    rachel.name "Wanna come with me?"
    pc "This is your dare. I will come after."
    rachel.name "Okay."
    $ add_to_list(rachel.list, "streaking")
    $ add_to_list(rachel.list, "soccerboys_hangout")
    hide rachel with dissolve
    pc "..."
    pcm "I'll give her some time to do this on her own."
    pcm "Guess I will spy on her."
    $ walk(loc_school_hallway)
    $ walk(loc_school_cafe)
    pcm "Let's see."
    show activity_windowshow_front nosale with dissolve
    pcm "I can see her."
    if robin_here(loc_school_field_back):
        pcm "Looks like [robin.name] is there as well."
    pcm "..."
    pcm "They are just chatting."
    $ relax(10)
    "I stand by the window just watching and seeing what's going on."
    pcm "Nothing out of the ordinary."
    pcm "Suppose I'll head over there as well then. No point hanging around here bored."
    hide activity_windowshow_front with dissolve
    $ walk(loc_school_hallway)
    $ remove_from_list(rachel.list, "streaking")
    $ walk(loc_school_field)
    pcm "Hope they don't do weird things with her."
    pcm "..."
    pcm "Who am I kidding. It should be the boys I am worried about."
    $ walk(loc_school_field_back)
    pc "Hey guys."
    rachel.name "Ah finally!"
    nate.name "You joining us as well?"
    pc "Sure, why not?"
    if robin_here():
        robin.name "You guys are up to some weird stuff."
        rachel.name "It's fun!"
    elif mira_here():
        mira.name "You guys are going to get into trouble."
        rachel.name "Right!"
    else:
        nate.name "Not that I am complaining."
        rachel.name "Have fun and look."
    $ log.markdone("quest_exhib_04")
    jump school_field_soccer_hangout_conv_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
