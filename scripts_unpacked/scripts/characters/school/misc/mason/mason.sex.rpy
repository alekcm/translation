label mason_sex_picker:
    if not "sex_progress_counter" in mason.dict:
        $ mason.dict["sex_progress_counter"] = 0

    jump expression WeightedChoice([   
    
    ("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"]), If(renpy.has_label("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"])) and mason.want_sex() and not loc(loc_bedroom), 100, 0)),

    
    ("mason_sex_general_blowquick_1", If(not renpy.has_label("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"])) and mason.dict["sex_progress_counter"] < 15 and mason.want_sex(), 100, 0)),
    ("mason_sex_general_sexquick_1", If(not renpy.has_label("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"])) and mason.dict["sex_progress_counter"] < 20 and mason.want_sex(), 100, 0)),
    ("mason_sex_general_mast_1", If(not renpy.has_label("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"])) and mason.dict["sex_progress_counter"] < 10 and mason.want_sex(), 100, 0)),
    
    
    ("mason_sex_nude_general", If(not renpy.has_label("mason_sex_walk_chain_" + str(mason.dict["sex_progress_counter"])) and mason.dict["sex_progress_counter"] > 15 and mason.want_sex(), 100, 0)),

    
    ("mason_tease_nude_general", If(not loc(loc_bedroom), 100, 0)), 
    ("mason_random_no_event", If(loc(loc_bedroom), 0, 100)),
    ])

label mason_sex_walk_chain_0:
    $ mason.dict["sex_progress_counter"] += 1
    pc "..."
    pc "Mister mushroom?"
    show mason at right6 with dissolve
    mason.name "Huh?"
    $ npc_race_picker(mason)
    $ player.sex_hand(mason)
    hide mason
    show sb_handjob
    with dissolve
    pc "What hard thing do we have here?"
    $ player.sex_cum(mason, "hand")
    show sb_handjob shock down worried
    $ player.face_worried()
    mason.name "Ahhhhh!"
    show sb_handjob neutral
    $ player.face_neutral()
    pc "Ooooh?"
    show sb_handjob up
    pc "That was a bit sooner than expected."
    mason.name "Sorry. Watching you girls... Y'know."
    show sb_handjob straight
    pc "Was already good to blow? Hehe."
    hide sb_handjob
    show mason nude at right5
    with dissolve
    pc "Well, it's not pointing at me any more."
    jump mason_sex_end_first

label mason_sex_walk_chain_1:
    $ mason.dict["sex_progress_counter"] += 1
    pc "..."
    pc "Ready for round two mister mushroom?"
    show mason at right6 with dissolve
    mason.name "I don't think..."
    $ npc_race_picker(mason)
    $ player.sex_hand(mason)
    hide mason
    show sb_blowjob up happy poke smile
    with dissolve
    pc "This pervert been keeping you pent up?"
    show sb_blowjob 2h down neutral with dissolve
    pc "Lets see how excited he has got looking at all the naked girls."
    show sb_blowjob up
    $ player.face_neutral()
    pc "So who would you rather put it in [mason.fname]?"
    pc "[zahra.name]? Or maybe would would prefer [sandy.name]?"
    if "nude_vball" in rachel.list:
        pc "I'm kinda shocked you haven't already poked [rachel.name]."
    else:
        pc "A lot of sexy girls for you to..."
    $ player.sex_cum(mason, "face")
    show sb_blowjob shock up with dissolve
    pc "Ooooh there you go!"
    show sb_blowjob frown eangry angry
    $ player.face_annoyed()
    pc "Right in my face..."
    hide sb_blowjob
    show mason nude at right5
    with dissolve
    pc "Well, have a good look at what you did."
    pc "Now I am walking the rest of the way with you on my face after you run off home."
    jump mason_sex_end_repeat

label mason_sex_walk_chain_2:
    $ mason.dict["sex_progress_counter"] += 1
    $ player.face_happy()
    pc "Mister mushroooooooom. ♥"
    show mason at right6 with dissolve
    mason.name "Errm..."
    $ npc_race_picker(mason)
    $ player.sex_oral(mason)
    hide mason
    show sb_blowjob up happy poke smile
    with dissolve
    mason.name "Don't forget last time."
    pc "Look, no hands."
    show sb_blowjob tounge down with dissolve
    pc "Pervert mushroom."
    show sb_blowjob up
    $ player.face_neutral()
    mason.name "Ah, you are..."
    show sb_blowjob up smile with dissolve
    pc "I'm what?"
    pc "Hehe."
    show sb_blowjob tounge down with dissolve
    mason.name "Ah, if you..."
    mason.name "Shit!"
    show sb_blowjob suck angry up with hpunch
    $ player.sex_cum(mason, "mouth")
    pc "Mmmfff..."
    mason.name "Ahhh!"
    mason.name "You knew that would happen."
    show sb_blowjob frown happy with dissolve
    $ player.face_annoyed()
    pc "Maybe..."
    pc "At least this time you put it somewhere I don't need to clean."
    hide sb_blowjob
    show mason nude at right5
    with dissolve
    pc "Now shoo you coward."
    jump mason_sex_end_repeat

label mason_sex_walk_chain_3:
    $ mason.dict["sex_progress_counter"] += 1
    $ player.face_happy()
    $ npc_race_picker(mason)
    hide mason
    show sb_againstwall3 wink cum smile
    with hpunch
    pc "Oooh, you up to something back there? ♥"
    mason.name "You have been asking for trouble."
    pc "Think I have been asking for a lot more than just \"trouble\"."
    $ player.spank()
    pc "Ah, careful, you will blow your..."
    $ player.sex_cum(mason, "ass")
    mason.name "Ahhhhh!"
    show sb_againstwall3 happy
    pc "... blow you load..."
    mason.name "Haaaa!"
    pc "Hehe."
    hide sb_againstwall3
    show mason nude at right5
    with dissolve
    pc "This is becoming a regular thing. I think you need to get off a little next time before trying to poke me."
    mason.name "Mmmm. Maybe."
    jump mason_sex_end_repeat

label mason_sex_walk_chain_4:
    $ mason.dict["sex_progress_counter"] += 1
    $ player.face_happy()
    $ npc_race_picker(mason)
    hide mason
    show sb_doggy1 shock
    with hpunch
    "[mason.name] suddenly grabs me by the hips and pulls at me, making me fall over."
    pc "Ahhh! ♥"
    show sb_doggy1 poke neutral with dissolve
    pc "You going to manage it this time?"
    pc "Oooh, I think you are struggling already."
    pc "Hehe."
    $ player.sex_cum(mason, "anus")
    show sb_doggy1 anal with dissolve
    "He starts to cum before even putting it in me, But the cum acts as lube and allows him to slip inside my ass."
    if player.asex == 1:
        show sb_doggy1 shock
        pc "Ah fuck. Didn't expect you to put it up my arse!"
        mason.name "Ahhh fuck!"
        mason.name "Haaaaa!"
        pc "Ask next time. First time someone put something in there."
    else:
        pc "You almost managed it."
        mason.name "Ahhh fuck!"
        mason.name "Haaaaa!"
        pc "Wont be long until you get to fuck me proper."
    show sb_doggy1 poke with dissolve
    mason.name "Phew!"
    show sb_doggy1 noman with dissolve
    pc "Look what you did to my ass."
    pc "Im leaking your cum."
    "I wiggle my bum a bit to tease him some more, then get up."
    hide sb_doggy1
    show mason nude at right5
    with dissolve
    pc "Now my ass feels all squidgy."
    jump mason_sex_end_repeat

label mason_sex_walk_chain_5:
    show mason at right5 with dissolve
    $ mason.dict["sex_progress_counter"] += 1
    $ player.spank()
    $ npc_race_picker(mason)
    pc "Ah!"
    pc "Looking for some fun?"
    hide mason
    show sb_standbehind happy
    with dissolve
    pc "Oooh, getting all handsy?"
    pc "Hehe. ♥"
    hide sb_standbehind
    show sb_againstwall3 wink happy cum
    with dissolve
    pc "You going to manage it this time?"
    mason.name "We will find out."
    show sb_againstwall3 mast with dissolve
    pc "Mmmm."
    show sb_againstwall3 poke with dissolve
    $ player.sex_vag(mason)
    show sb_againstwall3 sex with dissolve
    pc "Oooh you got it in."
    "[mason.name] manages to last a while, thrusting gently inside me while his hands explore my ass."
    "But as usual, he's a bit too excited..."
    mason.name "Ah fuck!"
    show sb_againstwall3 mast with dissolve
    show sb_againstwall3 cum with dissolve
    $ player.sex_cum(mason, "ass")
    mason.name "Ahhh fuck!"
    mason.name "Haaaaa!"
    pc "Mmmm."
    mason.name "So warm in there."
    show sb_againstwall3 noman with dissolve
    pc "Glad you had fun."
    hide sb_againstwall3
    show mason nude at right5
    with dissolve
    pc "..."
    pc "Aren't you going to run off now?"
    mason.name "Err, no. I'll still come with you."
    pc "Ooooh progress. Not a scaredy cat any more?"
    mason.name "Lets go."
    pc "Okay."
    show mason at left1 with dissolve
    return

label mason_sex_walk_chain_6:
    $ mason.dict["sex_progress_counter"] += 1
    $ player.face_happy()
    pc "[mason.pname] ♥"
    show mason at right5 with dissolve
    mason.name "Hmmm?"
    $ npc_race_picker(mason)
    $ player.sex_oral(mason)
    hide mason
    show sb_blowjob up happy poke smile
    with dissolve
    pc "Lets see now."
    show sb_blowjob tounge down with dissolve
    pc "Mmmmm."
    show sb_blowjob up 2h with dissolve
    $ player.face_neutral()
    pc "Lets have some fun."
    show sb_blowjob down suck with dissolve
    pc "Mmmmmff"
    mason.name "Mmmmm."
    show sb_blowjob up poke with dissolve
    pc "Not ready to blow?"
    mason.name "Not yet."
    show sb_blowjob down suck with dissolve
    "I manage to actually suck on his cock without him blowing right away. Looks like he is getting better."
    "But of course my aim is to make him blow, and I do everything I can to make that happen."
    "I continue to wank him off and play with him in my mouth until I can feel him leaking in my mouth."
    show sb_blowjob up
    mason.name "Ah fuck!"
    show sb_blowjob down
    $ player.sex_cum(mason, "mouth")
    mason.name "Ahhh yes!"
    pc "Mmmmf!"
    mason.name "Haaaaaa!"
    show sb_blowjob ub noman up with dissolve
    show sb_blowjob neutral with dissolve
    pc "Mmmmm. Much more fun like that."
    mason.name "I bet."
    hide sb_blowjob
    show mason nude at right5
    with dissolve
    pc "Running off or you coming with me?"
    mason.name "I'll come."
    pc "Well, you already did that. I can still taste it."
    show mason at left1 with dissolve
    return

label mason_sex_nude_general:
    $ tempname = mason
    $ quest_temp = None
    $ npc_race_picker(mason)
    $ event_end_interrupt_label = "mason_sex_general_end"
    pc "Mmm, how about I deal with that mushroom of yours?"
    show mason at right6 with dissolve
    mason.name "Sure."
    jump whore_street_sex_start_picker

label mason_sex_nude_general_end:
    $ renpy.scene()
    show mason nude at right6
    with dissolve
    pc "Hehe."
    mason.name "Lets keep going."
    show mason nude at left1
    return

label mason_tease_nude_general:
    jump expression WeightedChoice([   
    ("mason_tease_nude_1", 1),
    ("mason_tease_nude_2", 1),
    ])

label mason_tease_nude_1:
    hide mason
    show sb_pose_lookback happy tounge
    with dissolve
    pc "Getting a good look?"
    mason.name "I am."
    pc "Hehe."
    hide sb_pose_lookback
    show mason nude at left1
    with dissolve
    return

label mason_tease_nude_2:
    hide mason
    show sb_pose_showbreasts down happy
    with dissolve
    pc "Being naked makes these things bounce around a lot more. Hope you don't mind."
    mason.name "Err, no..."
    show sb_pose_showbreasts forward up
    pc "Hehe."
    hide sb_pose_showbreasts
    show mason nude at left1
    with dissolve
    return

label mason_random_no_event:
    if cheats:
        "No event was triggered"
    return

label mason_sex_end_first:
    show mason gym with dissolve
    $ player.face_worried()
    pc "Why are you dressing?"
    mason.name "Err..."
    mason.name "Without being excited, I can't do this..."
    pc "Your adventure goes away with the horny?"
    mason.name "Something like that."
    mason.name "I have to go..."
    hide mason with dissolve
    $ player.face_annoyed()
    pc "Wait!"
    pc "Ugh..."
    pcm "Leaving me here all alone butt ass naked..."
    menu:
        "Dress up":
            $ pc_dress_slow("party")
        "Stay naked":
            $ NullAction()
        "Run around with the bitch collar" if wolfgang_play_location():
            if not acc.choker == 6:
                $ acc.choker = 6
                pc "Hehe."
            $ walk(loc_park)
            jump random_event_wolfgang_picker

    jump travel

label mason_sex_end_repeat:
    show mason gym with dissolve
    $ player.face_worried()
    mason.name "Err, sorry."
    pc "Yeah yeah. Run off home you scaredy cat."
    mason.name "Err..."
    mason.name "Bye."
    hide mason with dissolve
    $ player.face_annoyed()
    pcm "Always leaving me here all alone butt ass naked..."
    menu:
        "Dress up":
            $ pc_dress_slow("party")
        "Stay naked":
            $ NullAction()
        "Run around with the bitch collar" if wolfgang_play_location():
            if not acc.choker == 6:
                $ acc.choker = 6
                pc "Hehe."
            $ walk(loc_park)
            jump random_event_wolfgang_picker

    if wolfgang_play_location() and acc.choker == 6:
        pcm "I still have the bitch collar on. I will be jumped at this rate."
        menu:
            "Keep it on":
                $ NullAction()
            "Take it off":
                $ acc.choker = 0
                pcm "There we go."
    jump travel

label mason_sex_general_bedroom_tombola:
    jump mason_sex_picker

label mason_sex_general_mast_1:
    $ mason.dict["sex_progress_counter"] += 1
    $ player.face_happy()
    pc "[mason.pname] ♥"
    mason.name "Hmmm?"
    $ npc_race_picker(mason)
    pc "I have an idea"
    mason.name "Okay..."
    hide mason
    show sb_againstwall2
    with dissolve
    pc "Wanna watch me? ♥"
    show sb_againstwall2 mast with dissolve
    mason.name "Oh?"
    pc "See how long you can last when I don't even touch you."
    mason.name "Quite a view."
    pc "Mmm, want to come closer?"
    show sb_againstwall2 cum with dissolve
    pc "Don't be blowing too quickly."
    show sb_againstwall2 closed
    "I close my eyes and think of dirty things, knowing this pervert is behind me wanking off."
    call masturbate_fantasy_picker from _call_masturbate_fantasy_picker_5
    call expression rand_choice from _call_expression_28
    if not renpy.showing("sb_againstwall2"):

        $ npc_race_picker(mason)
        show sb_againstwall2 mast cum with dissolve
    mason.name "Ahh fuck!"
    $ player.sex_cum(mason, "pullout")
    mason.name "Haaaaaaa!!!"
    show sb_againstwall2 wink
    pc "Ah, letting it go already?"
    mason.name "Haaaaaa!"
    pc "I can feel it all warm."
    mason.name "Haaaa..."
    if not mason.sex:
        pc "One day you will manage to fuck me."
    hide sb_againstwall2
    show mason nude at right5
    with dissolve
    pc "Had your fun?"
    mason.name "It was nice."
    jump mason_sex_general_end

label mason_sex_general_blowquick_1:
    $ mason.dict["sex_progress_counter"] += 1
    $ player.face_happy()
    pc "[mason.pname] ♥"
    show mason at right5 with dissolve
    mason.name "Hmmm?"
    $ npc_race_picker(mason)
    $ player.sex_oral(mason)
    hide mason
    show sb_blowjob up happy poke smile
    with dissolve
    pc "Lets see now."
    show sb_blowjob tounge down with dissolve
    pc "Mmmmm."
    show sb_blowjob up 2h with dissolve
    $ player.face_neutral()
    pc "Lets have some fun."
    show sb_blowjob down suck with dissolve
    pc "Mmmmmff"
    mason.name "Mmmmm."
    $ player.sex_cum(mason, "mouth")
    mason.name "Haaaaaaa!!!"
    pc "Mmmmf!"
    mason.name "Haaaaaa!"
    show sb_blowjob up poke with dissolve
    pc "Mmm, leaving a nice taste in my mouth."
    mason.name "Good that you like it."
    if not numgen(0,10):
        $ player.sex_oral(mason)
        show sb_blowjob down suck with dissolve
        mason.name "Ah, what are you?."
        show sb_blowjob up poke with dissolve
        pc "I wonder if someone as sensitive as you can go again?"
        show sb_blowjob down suck with dissolve
        "I carry on sucking him. He is still pretty hard from before and doesn't seem like he is going to go soft."
        show sb_blowjob up
        mason.name "Ah fuck!"
        show sb_blowjob down
        $ player.sex_cum(mason, "mouth")
        mason.name "Ahhh yes!"
        pc "Mmmmf!"
        mason.name "Haaaaaa!"
        show sb_blowjob ub noman up with dissolve
        show sb_blowjob neutral with dissolve
        pc "Lasted a bit longer that time."
        mason.name "Mmmm."
    jump mason_sex_general_end

label mason_sex_general_sexquick_1:
    $ mason.dict["sex_progress_counter"] += 1
    $ player.face_happy()
    pc "[mason.pname] ♥"
    mason.name "Hmmm?"
    $ npc_race_picker(mason)
    pc "Wanna have some fun?"
    mason.name "Huh?"
    show sb_doggy1 with dissolve
    pc "I can be one of your park bitches."
    mason.name "Oh?"
    pc "Come on."
    show sb_doggy1 poke with dissolve
    "I wiggle my bum for him as I feel him press against me."
    if mason.dict["sex_progress_counter"] < 10:
        $ player.sex_cum(mason, "pullout")
        mason.name "Haaaaaaa!!!"
        pc "Ah, letting it go already?"
        mason.name "Haaaaaa!"
        if mason.dict["sex_progress_counter"] < 5:
            pc "Putting it all on me?"
            mason.name "Haaaa..."
            if not mason.sex:
                pc "One day you will manage to fuck me."
            show sb_doggy1 noman with dissolve
        else:
            pc "Oooh?"
            $ player.sex_vag(mason)
            show sb_doggy1 vag with dissolve
            show sb_doggy1 oh
            pc "Oooh, putting it in?"
            $ player.sex_cum(mason, "inside")
            if mason.sex == 1:
                show sb_doggy1 shock
                pcm "Wait, I knew he was going to cum right away..."
                pcm "Means no chance he is going to be able to pull out."
                pcm "Need to remember that."
                pc "Managed to fuck me finally? ♥"
                mason.name "Mmmm."
            else:
                pc "Ooooh. Leaving something inside me again?"
                mason.name "Haaaa..."
                mason.name "That felt great."
            show sb_doggy1 poke with dissolve
            show sb_doggy1 noman with dissolve
            if mason.sex == 1:
                pc "You always leave your bitches leaking?"
                mason.name "Err, you are the first one."
                if not player.preg_knows:
                    pc "Well, better be careful. You might leave this bitch with a pup."
    jump mason_sex_general_end

label mason_sex_general_bedroom_end:
    $ renpy.scene()
    show mason nude at right5
    with dissolve
    pc "Now that you have used me for your fun, you can run off."
    mason.name "Thanks for the fun."
    show mason gym with dissolve
    pc "Get home safe."
    hide mason with dissolve
    jump travel

label mason_sex_general_end:
    if loc(loc_bedroom):
        jump mason_sex_general_bedroom_end
    else:
        jump mason_sex_end_repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
