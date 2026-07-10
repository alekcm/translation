label dani_sleepover_start:


    jump dani_sleepover_bed_picker

label dani_sleepover_first_time:
    $ add_to_list(loc_bedroom_dani.list, "slept_over")
    $ dani.dict["dani_times_slept_over"] += 1
    pc "Yeah, sure I will."
    dani.name "Not much room. But I think it's fine."
    pc "Snug as a bug in a rug."
    pc "Err, I don't really have anything to sleep in."
    dani.name "Nor do I and I live here."
    pc "Heh, right..."
    $ pc_strip_tops(True, temp=True)
    if c.nude:
        dani.name "Err... You are naked..."
        pc "I don't have any underwear."
        dani.name "Err... Okay..."
    elif c.exposed:
        dani.name "Errm... I thought you might have something that covered."
        pc "Not really."
    else:
        pc "This should do it."
        dani.name "Yup."
    dani.name "Good night [name]."
    pc "Night [dani.nname]."
    jump bed_sleep_loop





label dani_sleepover_bed_picker:

    if not "dani_times_slept_over" in dani.dict:
        $ dani.dict["dani_times_slept_over"] = 0
    if not "dani_yan_sex_progression" in dani.dict:
        $ dani.dict["dani_yan_sex_progression"] = 0
    if not "strapon_sex" in dani.dict:
        $ dani.dict["strapon_sex"] = 0


    if not dani.dict["dani_times_slept_over"]:
        jump dani_sleepover_first_time
    elif dani.dict["dani_times_slept_over"] == 1:
        pc "Prepared with some clothes this time."
        dani.name "Ah."

    $ dani.dict["dani_times_slept_over"] += 1
    $ dani_yan_remove(numgen(1,4))

    if not dani.can_sex:
        jump dani_sleepover_bed_join_sleep
    elif dani.can_sex and not dani.sex_les:
        jump dani_sleepover_bed_join_sex_firsttime

    jump expression WeightedChoice([
    
    

    ("dani_sleepover_bed_join_sleep", 1), 

    ("dani_sleepover_bed_join_kiss_sleep", If(dani.lust < 20, 500, 10)), 

    ("dani_sleepover_bed_join_sex_1", If(dani.lust >= 20, 100, 10)), 
    ("dani_sleepover_bed_join_sex_2", If(dani.lust >= 20, 100, 10)), 
    ("dani_sleepover_bed_join_sex_3", If(dani.lust >= 20, 100, 10)), 

    ("dani_sleepover_bed_join_strapon_sex_1", If(dani.lust >= 50 and dani_yan_value() >= 70 and dani.dict["strapon_sex"], 300, 0)), 
    ("dani_sleepover_bed_join_strapon_sex_2", If(dani.lust >= 50 and dani_yan_value() >= 70 and dani.dict["strapon_sex"], 300, 0)), 

    
    ("dani_sleepover_bed_join_sex_strapon_firsttime", If(dani.lust >= 20 and dani_yan_value() >= 40 and not dani.inv.qty(item_strapon) and dani.sex_les > 2, 5000, 0)), 
    ("dani_sleepover_bed_join_sex_roleplay_firsttime", If(dani.lust >= 20 and dani_yan_value() >= 60 and dani.inv.qty(item_strapon) and dani.sex_les > 2 and not dani.dict["strapon_sex"], 5000, 0)), 
    
    ])

label dani_sleepover_bed_join_sleep:
    hide dani with dissolve
    $ pc_striptease()
    $ pc_dress_slow("home")
    "I climb into bed with [dani.nname] and get comfortable."
    $ player.eye = 3
    show screen blackout(100) with dissolve
    pause 0.5
    $ time_sleep_hour()
    jump bed_sleep_loop



label dani_sleepover_bed_join_sex_firsttime:
    $ player.sex_les(dani)
    dani.name "Oh, staying over?"
    pc "Sure, why..."
    hide dani
    show dani_kiss
    with hpunch
    pc "Mmmmff..."
    show dani_kiss pc_closed with dissolve
    dani.name "Mmmm..."
    show dani_kiss dani_open with dissolve
    dani.name "You know, you are the first girl I have kissed."
    pc "Okay..."
    dani.name "Mmmmm."
    $ pc_strip_upper(temp=True)
    show dani_kiss pc_open with dissolve
    pc "Taking it off?"
    dani.name "Why not?"
    dani.name "See what it's like with someone who isn't a dirty pervert."
    pc "I might still be a dirty pervert."
    $ pc_strip_lower(temp=True)
    dani.name "Well, lets see..."
    hide dani_kiss
    show sb_laykiss
    with dissolve
    "She presses against me and we both fall onto the bed as she continues to kiss me."
    pc "Looking like you might be the pervert here."
    dani.name "With you here, I think I might be."
    show sb_laykiss closed with dissolve
    "Her hands are all over me, pressing me close as she kisses me more aggressively and I can feel her rubbing her body against mine."
    "I relax and go along with it. Enjoying her hands roaming all over my body, rubbing my tits while she presses her thigh between my legs."
    "I am getting pretty excited with all this, and it seems so is [dani.nname] because she starts to reposition herself."
    hide sb_laykiss
    show sb_scissoring
    with dissolve
    pc "Mmm, this is new."
    dani.name "Oh? You like it?"
    pc "Dunno, but I think I'm about to find out."
    "We both rub ourselves against each other and I slip my hand down between my legs to rub myself."
    "[dani.nname] starts to do the same and we both lay there pleasuring ourselves and each other."
    show sb_laykiss closed
    hide sb_scissoring
    with dissolve
    dani.name "So much softer than the usual pervert."
    pc "Mmmm."
    "We kiss, touch each other and enjoy the moment."
    "We both start to breathe much heavier as we rub against each other, hands between our legs and getting ourselves off."
    "[dani.nname] kisses me way more aggressively and deeper, less of a kiss and more of a tongue invading every part of my mouth."
    "And not just my mouth, she licks my lips, nibbles on my ear and tries to press as much of her skin against mine as possible."
    dani.name "Haa fuck this is so much fun."
    "She pushes her tongue deep into my mouth while breathing heavily an bucks her hips against me."
    dani.name "Ha fuck I am going to cum."
    pc "Mmm, pervert. Do it."
    "We both rub ourselves more as we kiss and she presses herself against me."
    $ player.sex_cum(dani)
    dani.name "Mmmmmm..."
    pc "Ahhh thats nice."
    dani.name "Much better than the usual pervert."
    "We lay together calming down, and eventually drift off to sleep together."
    jump bed_sleep_loop

label dani_sleepover_bed_join_sex_strapon_firsttime:
    $ dani.inv.take(item_strapon)
    $ player.sex_les(dani)
    $ pc_striptease(temp=True)
    show dani happy
    dani.name "By the way, I bought something."
    pc "More wine?"
    dani.name "No, something better. Hold on..."
    show dani at left3 with dissolve
    dani.name "Where was it..."
    dani.name "Ah."
    show dani nude with dissolve
    pc "Showing me your ass?"
    dani.name "..."
    show dani strapon with dissolve
    show dani crazy at right5 with dissolve
    show dani happy with dissolve
    $ player.face_meek()
    pc "Oh wow!"
    $ player.face_shock()
    pc "Where the hell did you get that thing?"
    dani.name "I stumbled on it in the market."
    $ player.face_worried()
    pc "It's... Bumpy?"
    dani.name "It is."
    show dani crazy with dissolve
    hide dani
    $ player.face_shock()
    show sb_onback strapon dani_kiss
    with hpunch
    pc "Ah."
    dani.name "Hope you are ready for it."
    pc "Err, probably not..."
    "[dani.nname] kisses me as I feel her rubbing something between my legs."
    "it generally feels nice, even if I am a bit worried about where she plans to put it."
    pc "There is no way that giant thing is fitting in me."
    dani.name "A slut like you can't handle it?"
    pc "Huh?"
    dani.name "Thought you would take this easy."
    pc "Sure, if I want to die."
    show sb_onback dani_lay_open look_right relaxed with dissolve
    dani.name "It's not that big."
    pc "Then I'll wear it and you bend over."
    show sb_onback dani_down dani_lay_mast with dissolve
    dani.name "Hmmm, it is kinda big isn't it?"
    show sb_onback pout look_down
    pc "Maybe should have got a smaller one?"
    show sb_onback look_right neutral dani_smile
    dani.name "Well it's not like there was much choice. Have to take what you can get."
    pc "Well I am not taking that thing!"
    dani.name "Shame. I thought it would be fun."
    pc "..."
    dani.name "I'll just wait until you are asleep and poke you with it."
    show sb_onback worried pout
    pc "Errr... Right. Sure."
    dani.name "Haha."
    dani.name "Goodnight [name]."
    pc "You are going to sleep with that thing?"
    dani.name "Can't be bothered to change."
    show sb_onback dani_lay_closed dani_sleep with dissolve
    pc "Okay, goodnight."
    show sb_onback look_closed pout
    show screen blackout() with dissolve
    jump bed_sleep_loop

label dani_sleepover_bed_join_sex_roleplay_firsttime:
    $ dani.dict["strapon_sex"] += 1
    $ pc_striptease(temp=True)
    show dani happy
    dani.name "Mmmm..."
    show dani strapon with dissolve
    $ player.face_worried()
    pc "Getting that out again?"
    dani.name "Yup, I'm gonna fuck you like a dirty whore!"
    if dani.assault:
        pc "You pretty much raped me with that thing last time."
        dani.name "Ah, was just having a bit of fun."
        pc "..."
    else:
        pc "Huh?"
    show dani crazy with dissolve
    hide dani
    $ player.face_shock()
    show sb_bentover back worried oh
    with hpunch
    pc "Ah!"
    show sb_bentover dani_cum with dissolve
    pc "What are you doing back there?"
    dani.name "I'm gonna fuck you like a pub whore."
    pc "Err, you okay?"
    dani.name "I'm okay. I just want to try something."
    pc "..."
    show sb_bentover dani_poke with dissolve
    $ player.spank()
    dani.name "Sluts like us should be fucked like this."
    pc "Okay..."
    $ player.spank()
    dani.name "Bent over like the cheap whores we are."
    dani.name "Are you ready to be fucked?"
    pc "Err..."
    $ player.spank()
    dani.name "Doesn't matter, I'm going to fuck you anyway."
    $ player.sex_vag(dani)
    show sb_bentover dani_sex ooh forward
    pc "Ahh fuck it's so big."
    dani.name "Mmm, I'm sure you love something this big."
    pc "Ah fuck."
    dani.name "Dirty little slut."
    dani.name "Arse like this should be fucked all the time."
    show sb_bentover head_down with hpunch
    dani.name "You like this, slut?"
    dani.name "Stuck your head down there and eat that pillow!"
    with hpunch
    if player.showing:
        dani.name "Look at you you fat cunt! Let someone cum in you and give you that belly."
        dani.name "Bet there will be plenty more after this one."
    else:
        dani.name "Bet a dirty bitch like you wants a man to fill you up?"
        dani.name "Stick his baby in you then fuck off, leaving the rest to you."
    dani.name "If I could, I would cum in you like these fucks do with me."
    if dani.showing:
        dani.name "Look at my belly, look what they did to me!"
    else:
        dani.name "Always filling me up, making me risk their baby."
    $ player.spank()
    dani.name "Ahh, I should cum in you!"
    dani.name "Ah yeah!"
    $ dani.cum()
    dani.name "Yeah you bitch!"
    show sb_bentover dani_poke with dissolve
    dani.name "Mmmm, hope that was fun for you."
    show sb_bentover head_up back oh worried with dissolve
    pc "It was... Something..."
    hide sb_bentover
    show dani strapon at right5
    with dissolve
    dani.name "Err, I'm just kind of..."
    dani.name "Err..."
    dani.name "I'll go to bed now I think..."
    hide dani with dissolve
    pcm "That was..."
    jump travel



label dani_sleepover_bed_join_kiss_sleep:
    $ pc_striptease()
    dani.name "Oooh, striptease."
    pc "Get a good look while you can."
    $ pc_dress_slow("home")
    show dani_kiss with dissolve
    dani.name "Mmm, goodnight."
    "I climb into bed with [dani.nname] and get comfortable."
    $ player.eye = 3
    show screen blackout(100) with dissolve
    pause 0.5
    $ time_sleep_hour()
    jump bed_sleep_loop


label dani_sleepover_bed_join_sex_1:
    $ pc_striptease(temp=True)
    $ player.sex_les(dani)
    dani.name "Mmm, getting ready for me are you?"
    pc "Just getting ready for bed."
    dani.name "I know."
    show dani_kiss with hpunch
    "[dani.nname] kisses me for a bit and then pushes me onto the bed."
    hide dani_kiss
    show sb_bentover head_down
    with hpunch
    show sb_bentover head_up back worried oh with dissolve
    pc "Ohh?"
    pc "What are you up to you pervert?"
    show sb_bentover dani_lick ooh forward straight with dissolve
    pc "Oooh fuck! That's what you want to do?"
    $ player.spank()
    pc "Ah!"
    show sb_bentover head_down with dissolve
    pc "Fucking hell. Ah shit."
    "I stay there, ass in the air with my head in the pillow feeling what [dani.nname] is doing behind me."
    "She doesn't seem just content with one of my holes and tries to lick or stick her tongue in either one."
    "It doesn't feel bad, so I relax and let her do what she wants."
    show sb_bentover head_up back ooh with dissolve
    pc "Ah fuck, you are going to make me..."
    $ player.spank()
    pc "Haa!"
    show sb_bentover head_up closed ag with dissolve
    $ player.sex_cum(dani)
    pc "Ahhhhhhh!"
    pc "Fuck!"
    $ player.spank()
    pc "Huuuu..."
    show sb_bentover no_dani back oh worried with dissolve
    pc "Haa, you finished back there."
    dani.name "Yup, just admiring the view now."
    pc "Well, enjoy it."
    "I wiggle my ass for [dani.nname], then roll over and lay down."
    hide sb_bentover
    show sb_onback relaxed look_up neutral
    with dissolve
    pc "Coming to bed now?"
    show sb_onback look_right dani_lay_closed dani_smile with dissolve
    pc "That was interesting."
    dani.name "Tasty."
    pc "Hehe."
    $ player.eye = 3
    show sb_onback dani_closed look_closed
    show screen blackout(100) with dissolve
    pause 0.5
    $ time_sleep_hour()
    jump bed_sleep_loop


label dani_sleepover_bed_join_sex_2:
    $ pc_striptease(temp=True)
    $ player.sex_les(dani)
    dani.name "Mmm, getting ready for me are you?"
    pc "Just getting ready for bed."
    dani.name "I know."
    show dani_kiss with hpunch
    dani.name "Mmmmm."
    jump dani_sex_bedroom_laykissing

label dani_sleepover_bed_join_sex_3:
    $ pc_striptease(temp=True)
    $ player.sex_les(dani)
    dani.name "Mmm, getting ready for me are you?"
    pc "Just getting ready for bed."
    dani.name "I know."
    show dani_kiss with hpunch
    dani.name "Mmmmm."
    jump dani_sex_bedroom_mast

label dani_sleepover_bed_join_strapon_sex_1:
    $ pc_striptease(temp=True)
    $ player.sex_les(dani)
    dani.name "Mmm, getting ready for me are you?"
    pc "Just getting ready for bed."
    dani.name "I know."
    show dani_kiss with hpunch
    dani.name "Mmmmm."
    jump dani_sex_bedroom_bentover_strapon

label dani_sleepover_bed_join_strapon_sex_2:
    $ pc_striptease(temp=True)
    $ player.sex_les(dani)
    dani.name "Mmm, getting ready for me are you?"
    pc "Just getting ready for bed."
    dani.name "I know."
    show dani_kiss with hpunch
    dani.name "Mmmmm."
    jump dani_sex_bedroom_onback_strapon





label dani_sleepover_wake_morning_picker:

    if not dani.can_sex:
        jump dani_sleepover_wake_morning_normal



    jump expression WeightedChoice([

    ("dani_sleepover_wake_morning_kiss", 20),

    ("dani_sleepover_wake_morning_sex", If(dani.lust > 40, 100, 0)),

    ("dani_bedroom_tiedup_start", If("strapon_sex" in dani.dict and dani.dict["strapon_sex"] > 4 and dani_yan_value() >= 100 and school_dance_quest_show_count >= 11, (dani_yan_value() - 80), 0)),

    ])

label dani_sleepover_wake_morning_normal:
    $ player.eye = 3
    show screen blackout(50) with dissolve
    dani.name "[name]... Wake up. It's morning."
    $ player.face_annoyed()
    pc "Ugh..."
    hide screen blackout with dissolve
    dani.name "Good morning."
    pc "Ugh, morning..."
    $ player.face_normal()
    jump travel

label dani_sleepover_wake_morning_kiss:
    $ dani_yan_remove(numgen(1,2))
    $ player.eye = 3
    show dani_kiss pc_closed
    show screen blackout(50) with dissolve
    dani.name "[name]... Wake up. It's morning."
    $ player.face_annoyed()
    show dani_kiss pc_open with dissolve
    pc "Ugh..."
    hide screen blackout with dissolve
    dani.name "Good morning."
    pc "Ugh, morning..."
    $ player.face_normal()
    hide dani_kiss with dissolve
    jump travel

label dani_sleepover_wake_morning_sex:
    $ dani_yan_remove(numgen(1,4))
    $ player.eye = 3
    show sb_laykiss underwear
    $ pc_strip(temp=True)
    show screen blackout(50) with dissolve
    $ player.sex_les(dani)
    dani.name "Morning."
    pc "Mmm, nice way to wake up."
    show sb_laykiss closed
    hide screen blackout
    with dissolve
    "Her hands are all over me, pressing me close as she kisses me more aggressively and I can feel her rubbing her body against mine."
    "I relax and go along with it. Enjoying her hands roaming all over my body, rubbing my tits while she presses her thigh between my legs."
    show sb_laykiss naked with dissolve
    "I am getting pretty excited with all this, and it seems so is [dani.nname] because she starts to reposition herself."
    hide sb_laykiss
    show sb_scissoring
    with dissolve
    pc "Oooh."
    dani.name "Oh? You like it?"
    "We both rub ourselves against each other and I slip my hand down between my legs to rub myself."
    "[dani.nname] starts to do the same and we both lay there pleasuring ourselves and each other."
    show sb_laykiss closed
    hide sb_scissoring
    with dissolve
    pc "Mmmm."
    "We kiss, touch each other and enjoy the moment."
    "We both start to breathe much heavier as we rub against each other, hands between our legs and getting ourselves off."
    "[dani.nname] kisses me way more aggressively and deeper, less of a kiss and more of a tongue invading every part of my mouth."
    "And not just my mouth, she licks my lips, nibbles on my ear and tries to press as much of her skin against mine as possible."
    dani.name "Haa fuck this is so much fun."
    "She pushes her tongue deep into my mouth while breathing heavily an bucks her hips against me."
    dani.name "Ha fuck I am going to cum."
    pc "Ahh so am I!"
    "We both rub ourselves more as we kiss and she presses herself against me."
    $ player.sex_cum(dani)
    dani.name "Mmmmmm..."
    pc "Ahhh thats nice."
    hide sb_laykiss
    show dani nude at right5
    with dissolve
    dani.name "Nice way to start the day."
    show dani sleep with dissolve
    hide dani with dissolve
    jump travel


label dani_sleepover_wake_sleep_picker:

    jump expression WeightedChoice([
    ("bed_sleep_loop", 1000),

    ("dani_sleepover_wake_sleep_mast", If(dani.sex_les > 4 and dani.lust > 50 and dani_yan_value() > 30, 100, 0)),
    
    ("dani_sleepover_wake_sleep_strapon_sex", If("strapon_sex" in dani.dict and dani.dict["strapon_sex"], 100, 0)),
    ("dani_bedroom_tiedup_start", If("strapon_sex" in dani.dict and dani.dict["strapon_sex"] > 1 and dani_yan_value() >= 100 and school_dance_quest_show_count >= 11, (dani_yan_value() - 80), 0)), 

    ])

label dani_sleepover_wake_sleep_mast:
    $ dani_yan_remove(numgen(1,4))
    $ player.eye = 3
    show sb_onback dani_lay_mast dani_down look_closed pout relaxed
    $ pc_strip(temp=True)
    show screen blackout(50) with dissolve
    $ player.sex_les(dani)
    pcm "Is she..."
    show sb_onback look_right with dissolve
    pc "Pervert, waking me up."
    show sb_onback dani_neutral
    dani.name "Ah, thought you were sleeping."
    hide screen blackout with dissolve
    pc "I was..."
    dani.name "Ah, sorry."
    pc "No need to stop. Carry on."
    dani.name "Err, okay."
    show sb_onback dani_down neutral with dissolve
    pc "Dirty girl, touching yourself while I sleep next to you."
    dani.name "Mmm, I couldn't help it."
    pc "Mmmm..."
    "I lay there watching as [dani.nname] touches herself."
    if not player.check_horny():
        "I'm not very excited myself, but I am happy she is having some fun."
        dani.name "Ahh i'm close."
        pc "Already?"
        dani.name "Mmmm, I was having fun before you woke."
        pc "Ah."
        dani.name "Ahhh yes!"
        dani.name "Haaaa fuck yes!"
        $ dani.cum()
        dani.name "Ahhhh..."
        dani.name "That was fun."
        pc "Mmmmm..."
        "Now she has had her fun, I close my eyes and try and get back to sleep."
        show sb_onback look_closed
        show screen blackout(100) with dissolve
        pause 0.5
        $ time_sleep_hour()
        jump bed_sleep_loop
    else:
        show sb_onback dani_neutral with dissolve
        dani.name "Hmmmm."
        pc "What?"
        dani.name "Only me having fun?"
        pc "Well, I was sleeping."
        dani.name "Come here."
        show sb_onback dani_kiss with dissolve
        pc "Oh? Jumping on me now?"
        dani.name "No reason for only me to have fun."
        pc "Okay."
        "I slip my hand between my legs as well and start touching myself."
        show sb_onback mast relaxed with dissolve
        "I lay there masturbating while [dani.name] kisses, gropes and licks me all over."
        pc "Mmmm, this is nice. Keep going like this and I will cum."
        dani.name "That's the plan."
        "She gets a bit more aggressive with her affection, pushing her tongue in my mouth as I start to breathe heavier."
        "I let her do what she wants as I focus between my legs, slowly brining myself to climax."
        dani.name "Oh getting closer?"
        pc "Mmmm."
        dani.name "I want to look you in the eye as you cum!"
        "As I get closer, I look at her directly and I start to cum."
        pc "Ah fuck yes."
        pc "Ahhhhhhhh."
        $ player.sex_cum(dani)
        dani.name "Ah yes, let me see that face."
        pc "Ah, weirdo."
        dani.name "Your the pervert wanking in my bed."
        pc "Ah well, not any more."
        show sb_onback dani_lay_open relax with dissolve
        dani.name "That was fun."
        pc "Mmm, pervery waking me in the night."
        dani.name "Wont be the last time."
        "Now we have had our fun, I close my eyes and try and get back to sleep."
        show sb_onback look_closed
        show screen blackout(100) with dissolve
        pause 0.5
        $ time_sleep_hour()
        jump bed_sleep_loop

label dani_sleepover_wake_sleep_strapon_sex:
    $ dani_yan_remove(numgen(1,6))
    $ dani.dict["strapon_sex"] += 1
    $ player.eye = 3
    show sb_onback strapon dani_sex look_closed pout
    $ pc_strip(temp=True)
    show screen blackout(50) with dissolve
    $ player.sex_forced(dani)
    $ player.sex_les(dani)
    show sb_onback look_up worried with dissolve
    pc "Uuuhh..."
    dani.name "Dirty slut has woke up?"
    pc "What are you..."
    $ player.sex_vag(dani)
    hide screen blackout
    show sb_onback ah angry
    pc "Ah fuck!"
    pc "What the hell are you doing?"
    dani.name "Fucking a dirty little slut!"
    with hpunch
    dani.name "Take it you whore!"
    pc "That thing is huge, don't push it so..."
    with hpunch
    pc "Ung!"
    dani.name "Fuck yes you dirty bitch."
    pc "This is a bit much..."
    show sb_onback worried pout
    if player.iswhore:
        dani.name "How many guys have you sold yourself to?"
        dani.name "Let them fuck you like the shitty whore you are?"
        with vpunch
    else:
        dani.name "Dirty bitch, I bet you want these perverts we dacne for to fuck you like this."
        dani.name "Taken into the bushes and let the men have turns on you."
    if player.showing:
        dani.name "You even have a fat belly. What pervert did you let knock you up?"
    else:
        dani.name "I bet you will let them try and knock you up!"
    pcm "What the fuck, she is going a bit crazy."
    dani.name "I'm going to cum inside you."
    pc "Huh?"
    dani.name "Ahhh yeah you bitch!"
    dani.name "Take it inside."
    $ dani.cum()
    dani.name "Ahhh yeah you bitch!"
    pc "..."
    dani.name "Mmmmm..."
    show sb_onback dani_kiss with dissolve
    dani.name "Mmm, that was fun. You can go back to sleep now."
    pc "What the?"
    show sb_onback dani_lay_closed dani_smile look_right relaxed with dissolve
    dani.name "Good night."
    show sb_onback dani_sleep
    pc "..."
    pcm "Fucking hell..."
    hide sb_onback with dissolve
    pc "Did she just..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
