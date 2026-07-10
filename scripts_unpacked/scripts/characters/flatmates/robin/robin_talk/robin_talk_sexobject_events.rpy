label robin_talk_sexobject_bought_intro:
    if not renpy.showing("robin"):
        show robin at right1
    pc "Hey, so I have been to the market and picked up a few bits."
    robin.name "Okay. Like what?"
    pc "Like for what we were talking about before. Make you all pretty."
    robin.name "Oh wow? Really?"
    pc "Yeah, let's go somewhere alone."
    robin.name "Oooh. Yeah!"
    $ walk(loc_bedroom)
    pc "So... Here you go."
    $ log.markdone("quest_robinslut_02")
    $ inv.drop(item_robin_package)
    $ wardrobe.take(item_outfit_11)
    $ wardrobe.take(item_pants_7)
    $ wardrobe.take(item_top_22)
    $ wardrobe.take(item_bottom_15)
    $ robin.dict["robin_talk_sexobject_last_outing"] = t.day

    "She takes the package and eagerly rips it open. Once she sees whats inside she takes a long pause..."
    show robin worried
    robin.name "Err..."
    robin.name "This is..."
    pc "A bit much?"
    show robin happy
    robin.name "It's fucking great! There is almost nothing here! And it's see through. SEE THROUGH!!!"
    pc "Err... So you like it?"
    robin.name "Thanks [name]! Not even sure a junkie whore would wear this. It's more than I could have asked for!"
    pc "Really? Err... Ok. Great."
    pc "Should we try it on then? I also got some makeup stuff in there so you can look more the part."
    show robin neutral
    robin.name "What's this stuff?"
    pc "Ah. I saw that and thought it was nice. It's spray for your hair."
    robin.name "Err, I don't have much hair."
    pc "I mean it colours your hair. Spray it on to colour it and wash it off in the morning."
    robin.name "And it's pink!"
    pc "Well, it's just a spray so you probably won't look bright pink unless you bleach. But it's good enough for a bit of fun."
    robin.name "Ok, well. Suppose I will change then."
    pc "Ok, shall I..."
    show robin nude with dissolve
    pc "Okay, doing it here then?"
    show robin thong with dissolve
    robin.name "Hmm, never wore something like these before. Go right up the crack of my arse."
    pc "Yeah, kinda the point."
    robin.name "Err, this is a top?"
    pc "It's a dress."
    robin.name "It is? How's it supposed to cover..."
    robin.name "It's not supposed to cover anything..."
    robin.name "Let's see..."
    show robin bimbo_nomakeup with dissolve
    robin.name "Err, doesn't cover my tits or arse."
    pc "Nope. Let's give these other bits a go."
    robin.name "Okay..."
    "I spend some time helping [robin.name] get her makeup done and spray her hair."
    show robin bimbo with dissolve
    pc "Hmm, might have went a bit overboard with the colours..."
    robin.name "Hmm, let's see how I look..."
    show robin_bimbo_pose_front with dissolve
    robin.name "Oh wow. I look like such a slut!"
    show robin happy
    robin.name "Right?"
    pc "Err. Pretty much."
    robin.name "You think it's safe to wear something like this though?"
    pc "What do you mean?"
    robin.name "Like, will it cause troubles?"
    pc "Yup. But by the sounds of things it's the kind you want to cause."
    robin.name "Ah! Yeah..."
    hide robin_bimbo_pose_front with dissolve
    robin.name "Okay. You put this one on while I try the other."
    pc "Okay. Why am I putting this on?"
    robin.name "I can't be the only one looking like a slut."
    pc "We are in my bedroom."
    if player.breasts == 3:
        robin.name "Yeah. But also I want to see how you manage to squeeze into it with those massive tits."
    else:
        robin.name "Yeah, but I want to see how you look in it anyway."
    pc "Right..."
    show robin thong with dissolve
    robin.name "Here."
    $ work.pants = 7
    $ work.outfit = 11
    $ work.outfit_primary_colour = "black"
    $ work.pants_primary_colour = "pink"
    $ work.pants_secondary_colour = "black"
    $ pc_striptease()
    $ tab_top = "work"
    $ pc_dress_slow()
    show robin slut with dissolve
    robin.name "Didn't think it could get worse than that dress, but this thing is basically see through."
    show robin_bimbo_pose_back slut with dissolve
    robin.name "Doesn't cover any of my arse either."
    pc "Yup. One thin strip of your underwear between you and a cock inside you."
    show robin neutral
    robin.name "Err..."
    pc "What?"
    hide robin_bimbo_pose_back with dissolve
    robin.name "I just realised..."
    robin.name "I asked to look sexy, well, like a bit of a slut..."
    pc "Mmm..."
    robin.name "I just realised that people are going to treat me like one."
    pc "Yeah... Wasn't that the point?"
    robin.name "Well, yes. But I was thinking being talked to like one. Ogled, talked to in such a way, that kind of thing."
    robin.name "The stuff I saw when I was in school."
    pc "Mmm?"
    robin.name "I didn't give much thought to what happens when they, we, are alone."
    pc "Ah. You have only seen it from the outside. But now..."
    robin.name "Yeah."
    robin.name "What should I do?"
    pc "Err, that's up to you."
    robin.name "..."
    robin.name "What do... Sluts... Normally do?"
    pc "Ah. Well, all people are different. Some just want the attention like you do and don't take it so far. Others, well... Others have a lot of \"fun\"."
    robin.name "Sex?"
    pc "Of course."
    robin.name "..."
    pc "That a problem?"
    show robin happy
    robin.name "Not at all. I'm just wondering how far to take it."
    pc "Err, what do you mean?"
    hide robin with dissolve
    pc "Err. Where are you going?"
    pc "..."
    pc "[robin.name]?"
    pc "..."
    $ add_to_list(robin.list, "no_location")
    $ walk(loc_kitchen)
    pc "[robin.name]?"
    $ walk(loc_common)
    pcm "Did she go outside? Can't see her anywhere in here..."
    $ walk(loc_kitchen)
    $ walk(loc_stairwell)
    pcm "Where did she go?"
    $ walk(loc_residential)
    $ remove_from_list(robin.list, "no_location")
    $ loiter(10)
    "I look around the area to see if I can find her, but no such luck."
    pcm "Well, if she got the bus, I will never find her. I'll just look around the park a bit before heading home."
    $ walk(loc_park)
    pcm "Hmmm, well not gonna look in every bush but can't seem to find her around anywhere."
    pcm "Ah well, whatever."
    $ walk(loc_residential)
    $ player.face_worried()
    distvoice "Ahhhh!"
    pcm "Huh? That was a voice..."
    $ player.face_annoyed()
    pcm "Fuck [robin.name]. If you got yourself killed already then I'll kick your corpse!"
    pcm "..."
    pcm "Dammit! I'm gonna end up killed myself if I go chasing after her."
    $ player.face_angry()
    pcm "I'll help whoever is killing you to kill you!"
    $ walk(loc_alley)
    $ player.face_worried()
    pc "Are you h..."
    $ player.face_shock()
    pcm "Oh?"
    show robin_bimbo_gangbang slut with dissolve
    pcm "Okay then..."
    $ player.face_neutral()
    $ player.face_shy()
    pcm "Looks like she..."
    robin.name "Oh fuck yes!"
    pcm "...like she is going full in with it..."
    robin.name "Haaa yes fuck me you cunts!"
    pcm "Wow..."
    pcm "Okay then. Guess no need to worry about her."
    $ male_npc_create_all()
    hide robin_bimbo_gangbang
    show male_generic at right6
    $ player.face_shock()
    with hpunch
    pc "Ah!"
    man "Sorry. Didn't mean to sneak up on you. Did call out for you but you didn't hear."
    $ player.face_neutral()
    $ player.face_shy()
    pc "Ah, was a bit focused on... Well, that."
    man "Yeah. You her friend?"
    pc "Yeah, the clothes give it away?"
    man "And the fact you are in the same alleyway."
    $ player.face_neutral()
    pc "Mmm. So why you chatting to me and not over there?"
    man "Girl comes over and jumps on the first dirty comment someone makes looks suspicious as hell. Wasn't gonna go over there and end up robbed with my dick out."
    $ player.face_evil()
    pc "Haha. Gimme ya money!"
    man "Heh, now I know it's just girls havin' fun, then okay, I'll get my dick out."
    $ player.face_neutral()
    pc "Sure she won't complain. Have fun."
    man "Ya want I could be sticking it in you?"
    pc "How romantic."
    man "Don't look like you girls are looking for romance."
    pc "Think it's the last thing she wants."
    man "So, you or her? Who should I stick it in?"
    if player.check_sex_agree_choice(2, "Come on then, I'll take it in me", "Stick it in her, have fun", exhibitionist=True):
        jump robin_talk_sexobject_bought_sex
    else:
        jump robin_talk_sexobject_bought_watch

label robin_talk_sexobject_bought_watch:
    man "Like watching do you?"
    pc "Na, I'm just here for some moral support."
    man "Don't think she needs much of that."
    pc "And to make sure she isn't murdered."
    man "Ah, well... Yeah. Doubt any of my mates are capable of that."
    pc "Never know who you'll run into in a dark alleyway."
    man "Mmm, today just a bunch of guys wanting to fuck a pair of sluts."
    pc "The best kind."
    man "Well, looks like some space is freeing up, so I'll go give it to her then."
    pc "Have fun."
    hide male_generic with dissolve
    pcm "Well, good job it's just a bunch of horny guys. She could have ended up in trouble running off like that."
    show robin_bimbo_gangbang nude with dissolve
    pcm "Though she might still end up in trouble the way they are filling her up..."
    "I end up standing there watching guy after guy fuck her. She doesn't seem to care what they do and just goes along with it."
    pcm "The guy's are treating her like a sex doll and have very little regard for her. Though it is just what she wanted so I guess she is happy about that."
    pcm "Yup, she is happy about it..."
    "I watch as they take their turns and fill up all her holes. She doesn't seem to have trouble taking them in the slightest."
    "But eventually the guy's have all shot their load in or on her, and are standing off smoking waiting for the last to finish up."
    "I get the odd smile or wink, but none approach me and keep a respectful distance."
    "Eventually they all head off, leaving [robin.name] a crumpled cum covered heap on the floor."
    $ robin.have_sex_milti(robinman, times=8)
    jump robin_talk_sexobject_bought_wrapup

label robin_talk_sexobject_bought_sex:
    $ npc_race_picker()
    pc "No point in me just standing here while she has all the fun."
    man "That's the spirit."
    $ player.spank()
    pc "Aie!"
    hide male_generic with dissolve
    $ player.grope()
    pc "Not wasting any time are you?"
    man "Gotta get it in you before my friends come have a turn."
    $ player.grope()
    pc "Who told you they will be getting a turn?"
    $ player.grope()
    man "Easy girl like you and your friend? Of course you're gonna give them a turn."
    pc "We'll see..."
    $ player.grope()
    man "Hah!"
    pc "So how you want to do this?"
    $ player.grope_end()
    $ player.spank()
    man "Against the wall there."
    pc "Ooh, romantic."
    $ pc_strip_under()
    show sb_againstwall3 wink slant with dissolve
    man "I'm a charmer."
    pc "Heh. I bet."
    show sb_againstwall3 mast with dissolve
    $ player.sex_location_offer()
    if player.want_sexlocation == 1:
        jump robin_talk_sexobject_bought_sex_vag
    else:
        jump robin_talk_sexobject_bought_sex_anal

label robin_talk_sexobject_bought_sex_vag:
    "I feel him rubbing his cock between my lips before putting pressure on me and sliding it inside me."
    show sb_againstwall3 poke with dissolve
    pc "Oooh..."
    $ player.sex_vag(robinman, quest_robinslut)
    show sb_againstwall3 sex up happy worried with dissolve
    pc "Huuuuuu..."
    "The man behind me doesn't ease into it and starts off at a furious pace."
    pc "Ah shit. Can take your time you know?"
    man "Thought a dirty girl like you would want it like this. Fucked like a highway whore."
    pc "Get me warmed up first, then you can."
    "He eases up a bit but still keeps a decent pace."
    $ player.spank()
    show sb_againstwall3 sex happy closed straight with dissolve
    pc "Mmmmm..."
    "I close my eyes and focus only on the cock penetrating me and making me feel good. His hands are all over my body but my mind pays attention to only one thing."
    "While he did ease up in the beginning, his pace is now picking up again. Fortunately I am more ready for it and can enjoy what he is doing to me."
    show sb_againstwall3 wink ag with dissolve
    pc "Fuck it feels to gooooood..."
    "At this point I am rocking my hips to meet his thrusts, so each of his thrusts is hitting me hard with a loud *slap* reverberating in the alley."
    pc "Fuck fuck keep going!"
    show sb_againstwall3 closed with dissolve
    man "Ahhh yeeessss..."
    pc "Keeeep... Nnnnggg..."
    pc "YES!"
    man "Come here!"
    $ player.face_shock()
    hide sb_againstwall3 with hpunch
    "He pulls me away from the wall and forces my head down. My legs are weak and my mind swimming with pleasure that I barely even register what he is doing."
    show sb_doggy1 shock vag with vpunch
    pc "Nnng!"
    $ player.spank()
    man "On your knees like a good bitch!"
    "He carries on fucking me at a fast pace and I get lost in the feeling of it all."
    show sb_doggy1 ag closed with dissolve
    man "Mmmm yes you dirty girl!"
    pc "Nnng yes!"
    pc "YES!"
    guy "Oh you found another one?"
    man "Mmm, bitches come in pairs."
    guy "Heh."
    man "Had fun with that one?"
    guy "Yeah. She is eager as hell."
    guy "Fellas! Another one here if you don't wanna wait your turn."
    show sb_doggy1 oh worried open with dissolve
    pcm "Oh shit."
    $ player.spank()
    "He keeps furiously fucking me and spanking me. Probably eager to get his fill before his friends join."
    show sb_doggy1 ag closed with dissolve
    pc "Mmmmmm!"
    pc "Fuck!"
    jump robin_talk_sexobject_bought_sex_spitroast

label robin_talk_sexobject_bought_sex_anal:
    man "Oh dirty girl. Want me to ass fuck you do you?"
    if player.has_perk(perk_buttslut):
        pc "Of course. I love it in the bum."
    elif not player.preg_knows:
        pc "Sure. And stops you from giving me a baby."
    else:
        pc "Sure, it can be fun."
    "I feel him rubbing his cock between my lips before pressing it against my arsehole and putting pressure on it."
    show sb_againstwall3 poke with dissolve
    pc "Oooh..."
    $ player.sex_anal(robinman, quest_robinslut)
    show sb_againstwall3 sex up happy worried with dissolve
    if player.asex < 5:
        show sb_againstwall3 grit worried sex with dissolve
        man "Ah fuck it's so tight!"
        pc "Nnnng fuck fuck!"
    else:
        show sb_againstwall3 sex up happy worried with dissolve
        man "Ah fuck yes!"
    pc "Huuuuuu..."
    "The man behind me doesn't ease into it and starts off at a furious pace."
    pc "Ah shit. Can take your time you know?"
    man "Thought a dirty girl like you would want it like this. Fucked like a highway whore."
    pc "Get my arse warmed up first, then you can."
    "He eases up a bit but still keeps a decent pace."
    $ player.spank()
    show sb_againstwall3 sex happy closed straight with dissolve
    pc "Mmmmm..."
    "I close my eyes and focus only on the cock penetrating me and making me feel good. His hands are all over my body but my mind pays attention to only one thing."
    "While he did ease up in the beginning, his pace is now picking up again. Fortunately I am more ready for it and can enjoy what he is doing to me."
    show sb_againstwall3 wink ag with dissolve
    pc "Fuck it feels to gooooood..."
    "At this point I am rocking my hips to meet his thrusts, so each of his thrusts is hitting me hard with a loud *slap* reverberating in the alley."
    pc "Fuck fuck keep going!"
    show sb_againstwall3 closed with dissolve
    man "Ahhh yeeessss..."
    pc "Keeeep... Nnnnggg..."
    pc "YES!"
    man "Come here!"
    $ player.face_shock()
    hide sb_againstwall3 with hpunch
    "He pulls me away from the wall and forces my head down. My legs are weak and my mind swimming with pleasure that I barely even register what he is doing."
    show sb_doggy1 shock anal with vpunch
    pc "Nnng!"
    $ player.spank()
    man "On your knees like a good bitch!"
    "He carries on fucking my ass at a fast pace and I get lost in the feeling of it all."
    show sb_doggy1 ag closed with dissolve
    man "Mmmm yes you dirty girl!"
    pc "Nnng yes!"
    pc "YES!"
    guy "Oh you found another one?"
    man "Mmm, bitches come in pairs."
    guy "Heh."
    man "Had fun with that one?"
    guy "Yeah. She is eager as hell."
    guy "Fellas! Another one here if you don't wanna wait your turn."
    show sb_doggy1 oh worried open with dissolve
    pcm "Oh shit."
    $ player.spank()
    "He keeps furiously fucking my arse and spanking me. Probably eager to get his fill before his friends join."
    show sb_doggy1 ag closed with dissolve
    pc "Mmmmmm!"
    pc "Fuck!"
    jump robin_talk_sexobject_bought_sex_spitroast

label robin_talk_sexobject_bought_sex_spitroast:
    pervert "Oooh, think I'll join in with this one. That one is a bit full up."
    show sb_doggy1 blow with dissolve
    "The new guy gets in front of me with his dick out and I barely hesitate before putting it in my mouth."
    pervert "Good girl."
    man "Lucky finding these two."
    pervert "Fuck yeah!"
    hide sb_doggy1
    if player.want_sexlocation == 1:
        show sb_doggy2 blow head_forward insidevag
    else:
        show sb_doggy2 blow head_forward insideass
    with dissolve
    $ player.sex_oral(robinman, quest_robinslut)
    "The guy in front shoves his cock in my mouth while holding onto my head. Even if I wanted to protest, I wouldn't be able to."
    "But of course I have no intention of protesting so relax and let him fuck my face and just trying to suck in a bit of air whenever I am able to."
    "I end up getting pushed about a bit as I am roughly fucked from both ends by these perverts. My knees on the floor are scraping and I can hear them mocking me and calling me names."
    "I really don't care though. Me and [robin.name] ended up in this alleyway to get fucked like cheap sluts, and that is what is happening."
    if player.want_sexlocation == 1:
        $ player.sex_cum(robinman, "inside", quest_robinslut)
    else:
        $ player.sex_cum(robinman, "anal", quest_robinslut)
    "This guy's cock throbbing inside me barely registers as I am writhing in pleasure being treated like this."
    $ player.sex_cum(robinman, "mouth")
    "The guy filling my mouth is harder to ignore though and it makes breathing harder as I swallow him all down."

    show sb_doggy2 no_blow head_back wink worried happy
    with dissolve
    pc "Huuu fuck. You guys weren't messing about."
    $ player.spank()
    pervert "Just like you wanted."
    $ player.face_neutral()
    pc "There a reason your cock is still in me?"
    pervert "Just making sure you take everything I have to give."
    if player.want_sexlocation == 1 and player.preg_knows:
        pc "Already pregnant so not like you are going to knock me up."
    elif player.want_sexlocation == 1:
        pc "Trying to knock me up or something?"
    else:
        pc "Well whatever. Keep it warm in my arse all you want."
    show sb_doggy2 head_forward with dissolve
    pervert "Looks like they are done with your friend as well."
    pc "Yeah, looks like. Take your cock out so I can fix myself up."
    if player.want_sexlocation == 1:
        show sb_doggy2 pokevag with dissolve
    else:
        show sb_doggy2 pokeass with dissolve
    show sb_doggy2 noman with dissolve
    pervert "You sluts made a lot of men happy today."
    show sb_doggy2 head_back straight normal happy with dissolve
    pc "Yeah I bet."
    hide sb_doggy2
    show male_generic at right1
    with dissolve
    $ pc_dress_slow()
    pervert "Hopefully see you sluts around again."
    pc "Leaving already?"
    pervert "Yeah, looks like everyone is done and you two don't strike me as the type who want pillow talk."
    pc "Heh, not really. See you round."
    hide male_generic with dissolve
    "I look over to [robin.name] and she is just a cum covered crumpled heap on the floor."
    jump robin_talk_sexobject_bought_wrapup

label robin_talk_sexobject_bought_wrapup:
    $ player.face_worried()
    pcm "I should probably help her up. But think I will leave her to soak in what she has just done."
    pcm "Don't think she regrets it. But best give her time to contemplate..."
    "She spends a bit of time recovering, then fixes up her clothes a bit and heads over to me."
    show robin slut happy at right1 with dissolve
    robin.name "Hey..."
    robin.name "Ooh, shaky legs..."
    $ player.face_happy()
    pc "Heh, after all that I'm not surprised."
    robin.name "Yeah, give me a moment."
    pc "Take your time."
    $ player.face_annoyed()
    pc "And next time don't run off like that. Stick together so you don't end up dead in here."
    show robin worried
    robin.name "Ah, sorry. I got a bit carried away..."
    $ player.face_neutral()
    pc "Have fun?"
    show robin happy
    robin.name "Oh fuck yes. My arse is sore from being beaten and fucked, I have the taste of cum in my mouth and I can feel stuff leaking out of me."
    robin.name "Might even be bleeding somewhere..."
    robin.name "Best night I've had since all this shit went down."
    pc "Good to hear."
    if robinman.sex:
        robin.name "Saw you bent over as well."
        pc "Yeah, thought I would lighten your load for your first time."
        robin.name "Haha, lying slut."
        pc "Me? Noooooo..."
        robin.name "Hahaha!"
    else:
        robin.name "Left my arse to please all the men. Thought you would join in."
        pc "I wanted to keep an eye on things to make sure you were safe and nothing got out of hand."
        robin.name "Thanks."
        pc "No problem."
    pc "Your legs okay to walk home?"
    show robin neutral
    robin.name "Yeah, probably need a shower after all that."
    pc "Yeah, can't even count how many that was."
    $ walk(loc_residential)
    robin.name "Well, I stopped counting after all three of my holes were filled up. Actually hurt like hell but no way was I going to complain."
    pc "Haha, I can imagine. Fuck you really went to the extreme."
    robin.name "Think it was a bad idea?"
    pc "Are you happier now than you were before?"
    show robin happy
    robin.name "Not sure I could be happier!"
    pc "Then it wasn't a bad idea."
    $ walk(loc_stairwell)
    robin.name "Heh, thanks [name]. For, y'know. Supporting my dumb idea."
    pc "Ah always happy to throw my friend at a group of horny men and have her gang fucked."
    robin.name "Knowing you, I'm not even sure that's a joke. But thanks anyway."
    pc "Sure."
    robin.name "Now quick inside before anyone sees us..."
    pc "Not sure anyone cares..."
    $ walk(loc_kitchen, trans=vpunch)
    pc "Woah!"
    robin.name "Quick!"
    $ walk(loc_bathroom)
    pc "Okay, why here?"
    robin.name "To wash up."
    pc "Okay... Together?"
    robin.name "Yeah, I don't want the others to see this..."
    pc "Right, ok. Whatever."
    robin.name "Fuck I am full of their stuff. It's all leaking out."
    if robinman.sex:
        jump robin_talk_sexobject_bought_wrapup_lesbian
    else:
        jump robin_talk_sexobject_bought_wrapup_clean

label robin_talk_sexobject_bought_wrapup_lesbian:
    pc "Yeah, tell me about it."
    robin.name "Oh, your friends finished inside as well?"
    pc "Yeah... Though I didn't have as many \"friends\" as you did."
    robin.name "Err... Can... Want me to help?"
    pc "Err... Help with what?"
    robin.name "Cleaning."
    pc "I don't think I need help with..."
    $ player.face_shock()
    hide robin
    show robin_cumlick_front slut
    with hpunch
    pc "Err... Woah!"
    pc "Ahhh ♥"
    pc "Waiii..."
    if player.check_sex_agree_choice(3, "Mmmmmm", "Stop!"):
        pc "Fuck!"
        pc "Err, what are you... That's my..."
        pc "Arrrrsssseeee!!!"
        hide robin_cumlick_front
        show robin_cumlick_behind
        with dissolve
        pc "Ah fuck, your fingers are in the wrong place!"
        robin.name "Mmmff, No fey are ot."
        pc "Ah you fucking slut!"
        pc "Fuck! ♥"
        "I lift my leg so [robin.name] can have better access and just enjoy what she is doing."
        "I am still a bit sensitive but [robin.name] finger fucking my arse is quickly getting me over the top."
        pc "Fuck [robin.name]! You are becoming such a whore!"
        robin.name "Uuut, ot oore."
        pc "Huh?"
        robin.name "A huut, ot a hore."
        pc "Ah, A slut?"
        "[robin.name] carries on licking my clit while fingering my arse, and I am close."
        "I grab [robin.name]'s hair and force her face into me as I hump her mouth."
        $ player.sex_cum(robin)
        pc "Haaa fuck!"
        pc "Fuck yes!"
        robin.name "Aaaann eeeefffff..."
        pc "Haaaa..."
        robin.name "Aaannt reeve!"
        pc "Ah shit."
        hide robin_cumlick_behind
        show robin slut happy at right1
        with dissolve
        robin.name "*Phew* Anymore and I might have collapsed on the floor."
        pc "Ha, sorry."
    else:
        pc "Hey. Come on! Shoo you horny bitch!"
        pc "Shoo!"
        hide robin_cumlick_front
        show robin slut happy at right1
        with dissolve
        robin.name "Oh? Not want the help?"
        pc "Calm down you horny monster."
        robin.name "Haha."

    robin.name "Here..."
    hide robin
    show robin_kiss bimbo
    with dissolve
    "[robin.name] kisses me and spits some stuff into my mouth. Not sure if it's cum, my juices or her own saliva."
    "But she keeps me in a liplock and I have no choice but to take what she is giving me."
    hide robin_kiss
    show robin slut happy at right1
    with dissolve
    pc "Ugh, you dirty bitch."
    robin.name "Yup, now let's clean up."
    pc "Yeah... Just this time... Never mind."
    jump robin_talk_sexobject_bought_wrapup_clean

label robin_talk_sexobject_bought_wrapup_clean:
    $ pc_striptease()
    show robin nude_makeup with dissolve
    $ shower_scene_start()
    $ shower_scene_wash("I jump in the shower and wash up with [robin.name].")
    show robin nude at right1 with dissolve
    robin.name "The hair stuff came out fine."
    pc "Shame. Would have been fun seeing you with pink hair."
    robin.name "Ha, yeah bet you would have had fun with it."
    $ pc_dress_slow("party")
    pc "..."
    pc "So you going to just stand there with your tits out or what?"
    robin.name "Ah, yeah..."
    show robin standard with dissolve
    robin.name "Thanks [name]."
    hide robin with dissolve
    pc "Sure..."
    jump travel

label robin_talk_sexobject_bought_aftermath:
    $ robin.isslut = True
    pc "So, been a bit since you rushed out and..."
    robin.name "Got railed by a bunch of strangers in an alleyway?"
    pc "I would have put it nicer, but sure."
    robin.name "Why nicer?"
    pc "Err, well I was going to ask if you were okay with it all... Don't regret what you did?"
    robin.name "Fuck no. I wanna do it again."
    pc "Oh?"
    robin.name "Yeah, though maybe next time we should go to the pub or something where it's safer."
    pc "Yeah probably. Not a good idea to jump on random guys hanging out in an alleyway."
    robin.name "Not sure what to do afterwards though. That motel safe?"
    pc "What, you want to bring a group of guys to the motel?"
    robin.name "Err, yeah?"
    pc "Why not just go there and whore then? Sure a bunch of guys will fuck you."
    robin.name "Eh, it's not the same. Being a whore is a job."
    pc "Ah, ok. I think I understand."
    robin.name "You do?"
    pc "Yeah, getting fucked by a group of guys because you want it is different from selling yourself."
    pc "One is being a degenerate and the other is work."
    robin.name "Wow, you do understand."
    pc "Slut!"
    robin.name "Yeah..."
    jump robin_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
