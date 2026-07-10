label school_bully_bully_event_force_cheat:
    if school_bully_quest_bully_event_stage < 10:
        "The bully stage is less than the maximum. This will mean not all actions will be unlocked."
        "Do you want to set it to maximum?"
        menu:
            "Yes":
                $ school_bully_quest_bully_event_stage = 10
                "Set to maximum"
            "No":
                $ NullAction()
                "Left unchanged"


    $ randomnum = renpy.random.randint(1, 4)
    if randomnum == 1 and school_bully_quest_bully_event_stage >= 10:
        jump school_bully_bully_event_10
    elif randomnum == 2 and school_bully_quest_bully_event_stage >= 9:
        jump school_bully_bully_event_9
    elif randomnum == 3 and school_bully_quest_bully_event_stage >= 8:
        jump school_bully_bully_event_8
    else:
        jump school_bully_bully_event_7



label school_bully_bully_event_force_strip:
    $ school_pick_bully_lust()
    $ npc_race_picker(tempname, tempname2)
    show shane smile with dissolve:
        xzoom -1
    tempname.name "Watch and make sure no one comes."
    if tempname == marcus:
        shane.name "Gonna have some fun? Ok."
        hide shane with dissolve
    else:
        marcus.name "Heh. Right."
        hide marcus with dissolve
        show shane with dissolve:
            xzoom 1
    $ dialouge = WeightedChoice([
    ("Right. Come 'ere you little bitch.", 1),
    ("Gonna be spending some nice alone time together.", 1),
    ("Now that we are alone, we can have some fun.", 1),
    ("Alone now so best start showing you your place.", 1),
    ("Hmmm. Now how should I have my fun with you?", 1),
    ("Time for the little whore to get what she deserves.", 1),
    ])
    tempname.name "[dialouge]"

    $ player.sex_forced(tempname)

    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        $ c.top = 0
        $ c.bra = 0
        $ c.outfit = 0
        if tempname == shane:
            show shane at right6 with hpunch
        else:
            show marcus at right6 with hpunch
        $ player.face_shock()
        $ dialouge = WeightedChoice([
        ("Ah what the fuck!?", 1),
        ("What are you doing?", 1),
        ("Ah fuck!", 1),
        ("What the hell?!", 1),
        ("What the hell you think you're doing?", 1),
        ("Ha fuck!", 1),
        ])
        pc "[dialouge]"
        pause 0.5

        $ randomnum = renpy.random.randint(1, 3)
        if randomnum == 1:
            tempname.name "If you make me take off the rest, it's gonna hurt."
        elif randomnum == 2:
            $ pc_strip()
            with hpunch
            pc "Shit!"
        else:
            $ player.punch()
            pc "Ah fuck! What did you do that for?"
            $ pc_strip()
            with hpunch
            $ player.face_cry()
            pc "*SOB*"
    elif randomnum == 2:
        tempname.name "Clothes off! Now!"
        $ player.face_shock()
        pc "Wha..."
        $ player.punch()
        tempname.name "I said now."
    else:
        tempname.name "Clothes off! Now!"
        $ player.face_shock()
        pc "Wha... But..."
    if not player.check_nowill():
        if c.exposed:
            pcm "Fuck. I want to try and do a runner but all my clothes are here."
            if c.nude:
                pcm "Am I really going to make a break for it completly naked?"
            elif c.cansee_breasts:
                pcm "Am I really going to have to make a break for it with my tits out?"
            elif c.cansee_ass:
                pcm "Am I really going to have to make a break for it with my arse hanging out?"
            else:
                pcm "Am I really going to have to make a break for it like this?"
        else:
            pcm "I might be able to run away. But if he catches me..."

        call school_bully_sex_forced_runaway from _call_school_bully_sex_forced_runaway

    pc "*SOB*"
    $ player.face_cry()
    pause 0.5
    $ pc_striptease()

    $ player.face_meek()
    pc "..."
    return

    $ randomnum = renpy.random.randint(1, 20)

    if randomnum > 10 and school_bully_quest_bully_event_stage >= 7:
        jump school_bully_sex_forced_hand
    elif randomnum > 3 and school_bully_quest_bully_event_stage >= 8:
        jump school_bully_sex_forced_blow
    elif randomnum < 3 and school_bully_quest_bully_event_stage >= 9:
        jump school_bully_sex_forced_sex_vag
    elif randomnum == 3 and school_bully_quest_bully_event_stage >= 9:
        jump school_bully_sex_forced_sex_anal
    else:
        "This is an error and should never triger. You probably used a debug command so I am picking an event at random."
        if randomnum > 10:
            jump school_bully_sex_forced_hand
        elif randomnum > 3:
            jump school_bully_sex_forced_blow
        elif randomnum < 3:
            jump school_bully_sex_forced_sex_vag
        elif randomnum == 3:
            jump school_bully_sex_forced_sex_anal



label school_bully_sex_forced_hand:
    $ dialouge = WeightedChoice([
    ("Get on your knees and let's see what those hands can do.", 1),
    ("Put your fingers round my cock, bitch.", 1),
    ("Get down and work those hands.", 1),
    ("You are gonna wank me off and I don't want to hear any complaining.", 1),
    ("On your knees you little bitch.", 1),
    ("Good whore. Now on your knees. You are going to wank me off for free.", If (player.iswhore, 1, 0)),
    ("Now whore, get on your knees and give me a free handjob.", If (player.iswhore, 1, 0)),
    ])
    tempname.name "[dialouge]"
    if not (shane.naughty or marcus.naughty):
        $ player.face_worried()
        pc "What? What are you talking about?"
        tempname.name "You are gonna get on your knees, wrap those fingers round my cock and do what a whore like you is good for."
        pc "What the hell. That's going too far..."
        tempname.name "First time for everything you dumb cunt. Now do it or I'll make you leave here limping."
        if not player.check_nowill():
            pcm "Fuck no!"
            jump school_bully_sex_forced_runaway_attempt

    pc "..."
    $ player.sex_hand(tempname)
    hide shane
    hide marcus
    show sb_handjob frown worried down
    with dissolve

    $ dialouge = WeightedChoice([
    ("Bitch like you should get used to this. Your only use is to get a guy off.", 1),
    ("Good, right where you belong.", 1),
    ("Good, you know your place. Bitch like you is good for only one thing.", 1),
    ("That's better bitch!", 1),
    ("Good whore. Now show me why people pay for you to get them off.", If (player.iswhore, 1, 0)),
    ("Good little whore. Now show me how good a whore who fucks men off for a living is.", If (player.iswhore, 1, 0)),
    ])
    tempname.name "[dialouge]"
    show sb_handjob up
    pc "..."
    pcm "Fuck, how did it come to this...?"
    show sb_handjob down
    $ dialouge = WeightedChoice([
    ("Ah fuck yes, you little slut.", 1),
    ("Ah fuck you little slut. You were born to take cocks in you.", 1),
    ("Bet you are loving this. All bitches want to be dominated and put on their knees by me.", 1),
    ("Good bitch knows her place. Keep going and you might even make me happy.", 1),
    ("Ah good little bitch.", 1),
    ("Ah yes. Looks like you have enough practice. But you need to do better if you expect to make a living.", If (player.iswhore, 1, 0)),
    ("Is this the best a whore can do?", If (player.iswhore, 1, 0)),
    ])
    tempname.name "[dialouge]"

    $ randomnum = renpy.random.randint(1, 5)
    if randomnum == 5 and school_bully_quest_bully_event_stage >= 9:
        $ dialouge = WeightedChoice([
        ("Fuck you useless cunt. Come 'ere", 1),
        ("Ah fuck. Come 'ere. I'm gonna stick it in you.", 1),
        ("Come 'ere you cunt. Bout time I got my dick wet.", 1),
        ])
        tempname.name "[dialouge]"
        jump school_bully_sex_forced_sex_choice

    elif randomnum > 2 and school_bully_quest_bully_event_stage >= 8:
        $ dialouge = WeightedChoice([
        ("Ah yes that's good. But let's see those lips sucking me off.", 1),
        ("Now I want to put my cock in your mouth.", 1),
        ("Now open your mouth you little bitch.", 1),
        ("Now you are gonna suck on my cock and I don't want to hear any complaining.", 1),
        ("Good whore. Now you are going to suck me off. And don't think Imma give you any money for it!", If (player.iswhore, 1, 0)),
        ])
        tempname.name "[dialouge]"
        tempname.name "Come here."
        jump school_bully_sex_forced_blow_jump
    else:

        pcm "Come on... Come on..."
        tempname.name "Keep going you dirty whore!"
        pcm "Hurry up..."
        tempname.name "Ahh yes!"
        pcm "He's close. I had better hurry so he doesn't try and stick it somewhere else."
        tempname.name "Keep going bitch."
        $ randomnum = renpy.random.randint(1, 5)
        if randomnum == 1:
            tempname.name "Ah fuck! Come here!"
            $ renpy.scene()
            show sb_blowjob angry closed suck with hpunch
            $ player.sex_oral(tempname)
            jump school_bully_sex_forced_blow_cum
        show sb_handjob shock
        $ player.sex_cum(tempname, "hand")
        tempname.name "Ahhh fuck yes!!"
        tempname.name "You shitty fucking whore!"
        tempname.name "Mmmmmm..."
        pc "..."
        jump school_bully_sex_forcesex_end

label school_bully_sex_forced_blow:
    $ dialouge = WeightedChoice([
    ("Get on your knees and let's see those lips sucking me off.", 1),
    ("On your knees bitch. I want to put my cock in your mouth.", 1),
    ("Get down and open your mouth.", 1),
    ("You are gonna suck on my cock and I don't want to hear any complaining.", 1),
    ("On your knees you little bitch.", 1),
    ("Good whore. Now on your knees. You are going to suck me off for free.", If (player.iswhore, 1, 0)),
    ("Now whore, get on your knees and give me a free blowjob.", If (player.iswhore, 1, 0)),
    ])
    tempname.name "[dialouge]"
    pc "..."
    $ player.sex_oral(tempname)
    $ renpy.scene()
    show sb_blowjob angry eangry poke
    with dissolve
    $ dialouge = WeightedChoice([
    ("Bitch like you should get used to this. Plenty of guys are going to make use of you.", 1),
    ("Good, right where you belong.", 1),
    ("Good, you know your place. Bitch like you is good for only one thing.", 1),
    ("Cock in the mouth of a bitch like you is almost too good.", 1),
    ("That's better bitch!", 1),
    ("Good whore. Now show me why people pay for you to suck them off.", If (player.iswhore, 1, 0)),
    ("Good little whore. Now show me how good a whore who sucks men off for a living is.", If (player.iswhore, 1, 0)),
    ])
    tempname.name "[dialouge]"
label school_bully_sex_forced_blow_jump:

    if not renpy.showing("sb_blowjob"):
        $ player.sex_oral(tempname)
    show sb_blowjob suck closed with hpunch

    pcm "..."
    pcm "Fucking arsehole..."
    $ dialouge = WeightedChoice([
    ("Ah fuck yes, you little cock sucking slut.", 1),
    ("Ah fuck you little slut. You were born to take cocks in you.", 1),
    ("Bet you are loving this. All bitches want to be dominated and put on their knees by a man.", 1),
    ("Good bitch knows her place. Keep sucking and you might even make me happy.", 1),
    ("Ah good little bitch.", 1),
    ("Ah yes. Looks like you have enough practice. But you need to do better if you expect to make a living.", If (player.iswhore, 1, 0)),
    ("Is this the best a whore can do?", If (player.iswhore, 1, 0)),
    ])
    tempname.name "[dialouge]"

    show sb_blowjob suck up with dissolve

    $ dialouge = WeightedChoice([
    ("I should tie you down and invite the school to have you as free use. Bet someone like you would love that.", 1),
    ("Bet you are getting off on this you little cunt. Bitch like you knows no better than to please a cock.", 1),
    ("You belong on your knees.", 1),
    ("Ah you dirty little girl. Didn't even need to hit you. Bet you're happy to suck me off.", 1),
    ("Maybe next time I will come by the highway and get another freebie off you.", If (player.iswhore, 1, 0)),
    ("Keep going you dirty whore. Suck it and take what's inside.", If (player.iswhore, 1, 0)),
    ])
    tempname.name "[dialouge]"

    show sb_blowjob suck down with dissolve

    $ dialouge = WeightedChoice([
    ("Mmmfff.", 1),
    ("Ah! *Ugg*", 1),
    ("Mmmff. *Hyuk* *Hyuk*", 1),
    ("*Slurp*", 1),
    ("*Hyuk* *Hyuk* *Hyuk*", 1),
    ])
    pc "[dialouge]"

    $ randomnum = renpy.random.randint(1, 2)
    if randomnum == 1 and school_bully_quest_bully_event_stage >= 9:
        show sb_blowjob suck eangry worried with dissolve
        pcm "Huh? What's that other idiot doing?"
        pcm "Ah fuck!"
        $ renpy.scene()
        show sb_spitroast back cum blow worried
        with dissolve
        pc "Mmmmf!"
        tempname.name "keep sucking bitch."
        $ randomnum = renpy.random.randint(1, 5)
        if randomnum == 1:
            jump school_bully_sex_forced_spitroast_anal
        else:
            jump school_bully_sex_forced_spitroast_vag

    $ dialouge = WeightedChoice([
    ("Dirty little slut. Keep going!", 1),
    ("Ah fuck, keep going like that and I will cum in your filthy mouth.", 1),
    ("Yes, fuck! Keep going you fucking whore.", 1),
    ("*Huff* *Huff* *Huffff*", 1),
    ])
    tempname.name "[dialouge]"
    show sb_blowjob 2h with dissolve
    $ dialouge = WeightedChoice([
    ("I start to feel his cock tensing up and his movements become erratic. He is being much more aggressive now and grabbing my hair while thrusting into my mouth. Seems he is not far off...", 1),
    ("His groaning lets me know he is not far off cumming so I pick up the pace and blow him even faster than I was before to get this ordeal over with.", 1),
    ("He is gripping onto my head and thrusting quite aggressively now. I know he won't last much longer at this rate so I work his shaft harder with my hands to try and push him over the edge.", 1),
    ])
    "[dialouge]"

    $ randomnum = renpy.random.randint(1, 5)
    if randomnum <= 3 and school_bully_quest_bully_event_stage >= 9:
        $ dialouge = WeightedChoice([
        ("Ah stop. Stop. It's better if I finish while fucking you.", 1),
        ("Ah fuck. Haaa. This would be so much better if I have you bent over on my cock.", 1),
        ("Ah yes. Fuck I really should take one of your holes and finish in there.", 1),
        ])
        tempname.name "[dialouge]"
        $ dialouge = WeightedChoice([
        ("Come here. Bend over so I can stick it in you like a good little bitch.", 1),
        ("Turn around so I don't need to look at your crying face while I stick it in you.", 1),
        ("Come here you little bitch. I'm gonna fuck you like a shitty tramp.", 1),
        ])
        tempname.name "[dialouge]"
        pc "*SOB*"
        jump school_bully_sex_forced_sex_choice
label school_bully_sex_forced_blow_cum:
    if not renpy.showing("sb_blowjob"):
        $ player.sex_oral(tempname)
    show sb_blowjob angry closed
    $ player.sex_cum(tempname, "mouth")
    $ dialouge = WeightedChoice([
    ("I feel his start to throb and push his cock deep in my mouth. He starts to cum and I feel his vile load squirting from his cock and into my mouth.", 1),
    ("He starts throbbing in my mouth and I feel disgust as he cums into my mouth.", 1),
    ("His cock starts to swell until he tenses up and releases his vile load in my mouth and I have no choice but to swallow most of it down.", 1),
    ("He throbs in my mouth and I feel the first wave fill me. I quickly resist the urge to puke as I swallow it down before another pulse shoots more on my tongue.", 1),
    ])
    "[dialouge]"
    show sb_blowjob eangry with dissolve
    tempname.name "Ahhhh! Yeeeeess..."
    tempname.name "Haaaa..."
    pc "Ubbb..."
    $ dialouge = WeightedChoice([
    ("Ah good little slut. Keep that on your face as a present.", 1),
    ("That's how a bitch should treat their betters. Next time I will give you a good fucking.", 1),
    ("Good. Swallow it down like the little cum whore you are.", 1),
    ])
    tempname.name "[dialouge]"
    show sb_blowjob poke ub with dissolve
    show sb_blowjob noman with dissolve
    $ dialouge = WeightedChoice([
    ("I watch as he pulls his trousers up and without giving me a second look he heads off, leaving me naked and alone.", 1),
    ("I sit there naked, holding back tears as he dresses and heads off without another word.", 1),
    ])
    "[dialouge]"
    $ player.face_puke()
    show sb_blowjob swallow down with dissolve
    pc "Bleh..."
    show sb_blowjob frown with dissolve
    pc "..."
    jump school_bully_sex_forcesex_end

label school_bully_sex_forced_sex_intro:
    $ dialouge = WeightedChoice([
    ("Come here. Bend over so I can stick it in you like a good little bitch.", 1),
    ("Turn around so I don't need to look at your crying face while I stick it in you.", 1),
    ("Come here you little bitch. I'm gonna fuck you like a shitty tramp.", 1),
    ])
    tempname.name "[dialouge]"
    pc "Wha...?"
    pc "*SOB*"
    jump school_bully_sex_forced_sex_choice

label school_bully_sex_forced_sex_choice:
    $ renpy.scene()
    if not player.check_nowill():
        with dissolve
        if player.vvirgin:
            pcm "Fuck. He's about to take me for the first time. It's now or never to get away from here."
        elif c.exposed:
            pcm "Fuck. I want to try and do a runner but all my clothes are here."
            pcm "Am I really going to have to make a break for it with my arse hanging out?"
        else:
            pcm "Last chance to get out of here. But if he catches me..."
        call school_bully_sex_forced_runaway from _call_school_bully_sex_forced_runaway_1
    show sb_againstwall2 cum wink frown worried
    with dissolve
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum == 1:
        jump school_bully_sex_forced_sex_anal
    else:
        jump school_bully_sex_forced_sex_vag

label school_bully_sex_forced_sex_vag:
    show sb_againstwall2 pokevaghand wink frown worried with dissolve
    $ dialouge = WeightedChoice([
    ("I feel his cock sliding between my lips as he wanks himself off a bit.", 1),
    ("I can feel him stroking his cock as the tip of his penis slides between my wet folds.", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 pokevag with dissolve
    if player.vvirgin:
        pcm "Fuck, he is poking me there. I don't want to lose my virginity to this dirty shit."
    elif player.cycle_conditions["stage"] == "ovulate" and not player.preg_knows:
        pcm "Fuck, right now is a dangerous time of the month. No chance [tempname.name] will bother to pull out..."
    elif not player.pregpills or not player.cycle_conditions["stage"] == "mens" or not player.preg_knows:
        pcm "Fuck, without protection this can be a bit dangerous. I don't want to end up pregnant here..."
        pcm "And not with [tempname.name]'s baby. Fuck..."
    if (not player.pregpills or not player.cycle_conditions["stage"] == "mens" or player.vvirgin) and not player.preg_knows:
        menu:
            "Beg him not to put it inside":
                if player.vvirgin:
                    pc "No please don't. I don't want my first time to be with you. Please don't put it in me..."
                elif player.cycle_conditions["stage"] == "ovulate" and not player.preg_knows:
                    pc "Please, now is a bad time of the month. Please don't put it inside me."
                elif not player.pregpills or not player.cycle_conditions["stage"] == "mens" and not player.preg_knows:
                    pc "Please don't. I am not on any protection and I don't want to be getting pregnant by you..."
                if player.check_speech(4):
                    tempname.name "*Tsk*"
                    tempname.name "Whatever. One hole is as good as another."
                    jump school_bully_sex_forced_sex_anal
                else:
                    tempname.name "Shut up cunt. You should be happy to take what I give you!"
                    $ player.punch()
                    pc "Nnng!"
            "Keep silent":
                pcm "I am not going to beg at this shit's feet..."
label school_bully_sex_forced_sex_vag_jump:
    $ dialouge = WeightedChoice([
    ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
    ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ])
    "[dialouge]"
    $ player.sex_vag(tempname)
    show sb_againstwall2 insidevag pain angry closed with hpunch
    $ dialouge = WeightedChoice([
    ("Ah! Fucking cunt!", 1),
    ("Ah this fucking arsehole!", 1),
    ("Ah fuck this shitty cunt.", 1),
    ("Nonononono...", 1),
    ])
    pcm "[dialouge]"
    $ randomnum = renpy.random.randint(1, 4)
    if randomnum == 1:
        $ renpy.scene()
        show sb_againstwall3 worried squint grit sex with dissolve
    pc "*SOB*"
    $ dialouge = WeightedChoice([
    ("I feel him start to take long and deep thrusts inside me. Pushing his cock balls deep into me before pulling almost all the way out, then ramming it back in again. ", 1),
    ("He takes it slow and rhythmically thrusts making sure I feel his disgusting cock in me. He paws at my tits as he does so and I just accept what is happening.", 1),
    ("He thrusts deeply into me before slowly sliding his cock out almost all the way. Then aggressively slams back into me in a quick and hard thrust.", 1),
    ])
    "[dialouge]"
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("He starts to get into it more and spanks me or reaches round to claw at my tits as he is thrusting deep inside me.", 1),
    ("He starts to build momentum and it's not long before I hear his body slapping against my ass with each thrust into me.", 1),
    ("He builds up speed as I try not to cry and it's not long until he is harshly gripping my sides and pulling me against his thrusting cock.", 1),
    ("He cares nothing for my wellbeing and just rams away as he pleases. Fucking me hard and fast while smacking me on the arse.", If (player.desire > 80, 1, 0)),
    ])
    "[dialouge]"
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    tempname.name "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Cunt!", 1),
    ("Fucking cunt!", 1),
    ("Disgusting shit!", 1),
    ("Should have tried to bite his cock off...",1),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("His breathing starts to become ragged and it seems like it will be over soon.", 1),
    ("His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit.", 1),
    ("He is thrusting faster now and squeezing at my arse. It seems like he won't last much longer.", 1),
    ])
    "[dialouge]"
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Yes, yes!", 1),
    ("Ahhhhh fuck yes.", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh I am close.", 1),
    ("Ahhhhh yes you dirty bitch.", 1),
    ])
    tempname.name "[dialouge]"
    $ renpy.scene()
    show sb_againstwall2 insidevag pain worried wink
    with dissolve
    if (not player.pregpills or not player.cycle_conditions["stage"] == "mens") or player.vvirgin or player.cycle_conditions["stage"] == "ovulate":
        menu:
            "Beg him not to cum inside.":
                show sb_againstwall2 wink shock with dissolve
                pc "Please no. Not inside. Pull out, pull out! Please!"
                if player.check_speech(4):
                    jump school_bully_sex_forced_sex_vag_pullout
                else:

                    $ player.punch()
                    show sb_againstwall2 closed pain with dissolve
                    tempname.name "Shut up bitch. Stop ruining it for me!"
            "Keep silent.":

                $ NullAction()

    $ dialouge = WeightedChoice([
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it you cunt.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Yes, yes!", 1),
    ("Ah yes you shitty bitch! I am going to fill you up.", 1),
    ("Ah get ready for carrying my baby, bitch!", 1),
    ("Haaa fuck I am going to knock you up like a dirty slut you are!", 1),
    ("Get ready for my baby you bitch.", 1),
    ("Ahhh yes take it deep inside. Hope you're feeling lucky.", 1),
    ("Better hope you are lucky cos I am going to fill you up!", 1),
    ("You dirty slut. Take me inside you.", 1),
    ("Ah fuck yes you filthy slut.", 1),
    ])
    tempname.name "[dialouge]"

    $ dialouge = WeightedChoice([
    ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
    ("His cock pulses inside me, unloading his cum deep inside me.", 1),
    ])
    "[dialouge]"

    $ player.sex_cum(tempname, "inside")
    $ dialouge = WeightedChoice([
    ("No plea...", 1),
    ("Fuck...", 1),
    ("Stop...", 1),
    ("*SOB* *SOB*", 1),
    ("Shit!", 1),
    ])
    pc "[dialouge]"
    show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 noman wink with dissolve
    tempname.name "Good little whore."
    $ player.spank()
    $ player.face_cry()
    pc "*SOB*"
    $ dialouge = WeightedChoice([
    ("I stand there with his cum dripping out of me and watch as he leaves.", 1),
    ("I try to hold back tears as I watch the cunt leave with his cum inside me dripping out.", 1),
    ("I try not to curse at him as he is leaving in case he comes and hits me. But internally I am screaming at him.", 1),
    ])
    "[dialouge]"
    jump school_bully_sex_forcesex_end

label school_bully_sex_forced_sex_anal:
    show sb_againstwall2 pokeasshand with dissolve
    $ dialouge = WeightedChoice([
    ("He pokes at my ass and without much lube, tries to push it inside but is unable to.", 1),
    ("I feel him press against my asshole and try to put it inside me, but without any lube it has no chance of getting in.", 1),
    ("I feel him put the tip of his cock against my ass and press against it. But my asshole is dry and he has no chance of getting inside.", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 pokevaghand with dissolve
    $ dialouge = WeightedChoice([
    ("He then decides to rub against my pussy. Unfortunately it is not very wet so I am probably in for a painful time.", 1),
    ("He decides to try and lube his cock up by rubbing it between my legs. But since I am not wet he doesn't manage to lube up much.", 1),
    ])
    "[dialouge]"
    $ randomnum = renpy.random.randint(1, 15)
    if randomnum == 1:
        tempname.name "Ah fuck it..."
        jump school_bully_sex_forced_sex_vag_jump
    show sb_againstwall2 pokeasshand shock worried with dissolve
    $ dialouge = WeightedChoice([
    ("I then feel him poke at my asshole again. At least his cock feels somewhat slicker than before and may not be as harsh when he enters me..", 1),
    ("His cock then presses against my arse again. Hopefully he managed to lube up a bit...", 1),
    ])
    "[dialouge]"
    show sb_againstwall2 pokeass with dissolve
    $ dialouge = WeightedChoice([
    ("He applies pressure with his cock against me and slowly starts to enter. But it is still too dry to get fully in.", 1),
    ("He starts to try and push it in, but without enough lube he is having a hard time.", 1),
    ])
    "[dialouge]"
    "Until eventually..."
    $ player.sex_anal(tempname)
    show sb_againstwall2 insideass pain closed angry with hpunch
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Ah fuck it hurts!", 1),
    ("Ahhh! Shit!!", 1),
    ("Ahhh! Fuck that hurts!", 1),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Shut up bitch!", 1),
    ("Shut the fuck up!", 1),
    ("Be quiet!", 1),
    ])
    tempname.name "[dialouge]"
    $ randomnum = renpy.random.randint(1, 10)
    if randomnum == 1:
        $ player.punch()
    $ dialouge = WeightedChoice([
    ("The pain is overwhelming and I don't even try to stifle my sobs. I just close my eyes and hope it will be over as quick as possible.", 1),
    ("The pain is excruciating and I just cry as he fucks me. All I can do is hope it will be over soon.", 1),
    ("The pain of him entering me is unbearable and all I can do is cry and hope it will end soon.", 1),
    ])
    "[dialouge]"

    $ dialouge = WeightedChoice([
    ("His grip on me starts to get stronger and more painful as he gets more and more excited. His breathing is now getting more ragged with each thrust.", 1),
    ("His grip on my cheeks is now hard enough to leave marks on my skin as his thrusts start to become erratic. He is clearly enjoying this and may not last much longer.", 1),
    ("His hands are all over my body as he starts to put himself over the edge. His breathing becoming heavy and he starts to thrust much more aggressively into me.", 1),
    ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
    ])
    "[dialouge]"

    $ dialouge = WeightedChoice([
    ("He must be close. At least I hope he is.", 1),
    ("The way he is grunting it sounds like it might be over soon.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ahhh, I'm about to come!", 1),
    ("Ah fuck I am close...", 1),
    ("Fuck so good. I am not going to last much longer.", 1),
    ("Ah yes! I am cumming!", 1),
    ])
    tempname.name "[dialouge]"
label school_bully_sex_forced_sex_anal_jump:
    pc "*SOB*"
    $ player.sex_cum(tempname,"anal")
    tempname.name "Ahhhh fuck yes."
    $ player.spank()
    tempname.name "Haaaaaa..."
    pc "*SOB*"
    tempname.name "Ah fuck yes. Nice little bitch."
    show sb_againstwall2 pokeass with dissolve
    show sb_againstwall2 noman with dissolve
    $ dialouge = WeightedChoice([
    ("I sit on the floor and cry as he cleans himself up and leaves without another word.", 1),
    ("I break down and cry and the guy pays me no heed as he dresses and heads off.", 1),
    ("I sit down and sob as he dresses and leaves without saying anything more.", 1),
    ])
    "[dialouge]"
    jump school_bully_sex_forcesex_end

label school_bully_sex_forced_sex_vag_pullout:
    $ randomnum = renpy.random.randint(1, 2)
    if randomnum == 1:
        $ dialouge = WeightedChoice([
        ("Come here then you little bitch. Open your mouth.", 1),
        ("On your knees then you little whore. I will come in at least one of your holes.", 1),
        ("Come here then you fucking whore.", 1),
        ])
        tempname.name "[dialouge]"
        $ renpy.scene()
        $ player.sex_oral(tempname)
        show sb_blowjob closed angry suck
        with hpunch
        $ dialouge = WeightedChoice([
        ("Mmmfff.", 1),
        ("Ah! *Ugg*", 1),
        ("Mmmff. *Hyuk* *Hyuk*", 1),
        ("*Hyuk* *Hyuk* *Hyuk*", 1),
        ])
        pc "[dialouge]"
        jump school_bully_sex_forced_blow_cum
    else:
        tempname.name "*Tsk*"
        show sb_againstwall2 pokevaghand with dissolve
        show sb_againstwall2 pokeasshand with dissolve
        show sb_againstwall2 pokeass with dissolve
        $ player.sex_anal(tempname)
        show sb_againstwall2 insideass pain angry closed with hpunch

        $ dialouge = WeightedChoice([
        ("Ah fuck it hurts!", 1),
        ("Ahhh! Shit!!", 1),
        ("Ahhh! Fuck that hurts!", 1),
        ])
        pc "[dialouge]"
        jump school_bully_sex_forced_sex_anal_jump

label school_bully_sex_forced_spitroast_anal:
    $ dialouge = WeightedChoice([
    ("I feel him doing something behind me but not sure what.", 1),
    ("I can feel him stroking his cock and hitting it against my ass.", 1),
    ])
    "[dialouge]"
    tempname.name "Couldn't wait your turn?"
    tempname2.name "You will send her off crying when you're done so better have a go now."
    tempname.name "Whatever."
    pc "Mmmmfff!"
    tempname.name "Looks like [tempname2.name]'s gonna stuck you like a pig. Heh."
    tempname2.name "Gonna make her squeel like one as well."
    tempname.name "Oh?"
    pcm "Fuck!"
    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy2 pokeasshold blow head_forward
    with dissolve
    $ dialouge = WeightedChoice([
    ("I feel his cock poking at my arsehole. It seems that's where he is aiming to put it.", 1),
    ("I feel him press his cock against my arsehole while tanking himself off.", 1),
    ])
    "[dialouge]"
    show sb_doggy2 pokeass with dissolve
    $ dialouge = WeightedChoice([
    ("He applies pressure with his cock against me and slowly starts to enter. But it is still too dry to get fully in.", 1),
    ("He starts to try and push it in, but without enough lube he is having a hard time.", 1),
    ])
    "[dialouge]"
    "Until eventually..."

    show sb_doggy2 insideass head_back angry squint shock with hpunch
    $ player.sex_anal(tempname2)
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Ah fuck it hurts!", 1),
    ("Ahhh! Shit!!", 1),
    ("Ahhh! Fuck that hurts!", 1),
    ])
    pc "[dialouge]"

    call school_bully_sex_forced_spitroast_cont from _call_school_bully_sex_forced_spitroast_cont

    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy1 grit angry anal
    with dissolve
    tempname2.name "Ahh fuck, gonna make sure you take it all inside!"
    $ dialouge = WeightedChoice([
    ("Cunt!", 1),
    ("Fucking cunt!", 1),
    ("Disgusting shit!", 1),
    ("Should have tried to bite his cock off...",1),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He doesn't miss a beat and carries on fucking me.", 1),
    ("His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit.", 1),
    ("He is thrusting faster now and squeezing at my arse. It seems like he won't last much longer.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("His breathing starts to become ragged and it seems like it will be over soon.", 1),
    ("His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit.", 1),
    ("He is thrusting faster now and squeezing at my arse. It seems like he won't last much longer.", 1),
    ])
    "[dialouge]"
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Yes, yes!", 1),
    ("Ahhhhh fuck yes.", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh I am close.", 1),
    ("Ahhhhh yes you dirty bitch.", 1),
    ])
    tempname2.name "[dialouge]"
    $ player.sex_cum(tempname2,"anal")
    tempname2.name "Ahhhh fuck yes."
    $ player.spank()
    tempname2.name "Haaaaaa..."
    pc "*SOB*"
    tempname2.name "Ah fuck yes. Nice little bitch."
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    pcm "Fuckfuckfuck. Ass feels like it's on fire!"
    pc "Unnnng!"
    $ dialouge = WeightedChoice([
    ("I sit on the floor and cry as they clean themselves up and leave while laughing at me.", 1),
    ("I break down and cry and arseholes pay me no heed as they laugh at me and leave.", 1),
    ("I sit down and sob as they laugh at me while dressing up, then leave.", 1),
    ])
    "[dialouge]"
    jump school_bully_sex_forcesex_end

label school_bully_sex_forced_spitroast_vag:
    $ dialouge = WeightedChoice([
    ("I feel him doing something behind me but not sure what.", 1),
    ("I can feel him stroking his cock and hitting it against my ass.", 1),
    ])
    "[dialouge]"
    tempname.name "Couldn't wait your turn?"
    tempname2.name "You will send her off crying when you're done so better have a go now."
    tempname.name "Whatever."
    pc "Mmmmfff!"
    tempname.name "Looks like [tempname2.name]'s gonna stuck you like a pig. Heh."
    pcm "Fuck!"
    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy2 pokevaghold blow head_forward
    with dissolve
    $ dialouge = WeightedChoice([
    ("I feel his cock sliding between my lips as he wanks himself off a bit.", 1),
    ("I can feel him stroking his cock as the tip of his penis slides between my wet folds.", 1),
    ])
    "[dialouge]"
    show sb_doggy2 pokevag with dissolve
    $ player.sex_vag(tempname2)
    show sb_doggy2 insidevag with dissolve
    $ dialouge = WeightedChoice([
    ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
    ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ])
    "[dialouge]"
    pc "Mmmff!"

    call school_bully_sex_forced_spitroast_cont from _call_school_bully_sex_forced_spitroast_cont_1

    $ renpy.scene()
    $ npc_race_switch()
    show sb_doggy1 no_head vag
    with dissolve
    tempname2.name "Ahh fuck, gonna make sure you take it all inside!"
    show sb_doggy1 head_down shock angry vag with dissolve
    $ dialouge = WeightedChoice([
    ("Cunt!", 1),
    ("Fucking cunt!", 1),
    ("Disgusting shit!", 1),
    ("Should have tried to bite his cock off...",1),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He doesn't miss a beat and carries on fucking me.", 1),
    ("His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit.", 1),
    ("He is thrusting faster now and squeezing at my arse. It seems like he won't last much longer.", 1),
    ])
    "[dialouge]"
    show sb_doggy1 grit
    $ dialouge = WeightedChoice([
    ("His breathing starts to become ragged and it seems like it will be over soon.", 1),
    ("His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit.", 1),
    ("He is thrusting faster now and squeezing at my arse. It seems like he won't last much longer.", 1),
    ])
    "[dialouge]"
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Yes, yes!", 1),
    ("Ahhhhh fuck yes.", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh I am close.", 1),
    ("Ahhhhh yes you dirty bitch.", 1),
    ])
    tempname2.name "[dialouge]"
    if player.preg_knows or player.cycle_conditions["stage"] == "mens":
        jump school_bully_sex_forced_spitroast_vag_cum_inside
    else:
        show sb_doggy1 shock worried with dissolve
        pcm "This is a bad time. I can't be carrying [tempname2.name]'s baby? Shit!"
        menu:
            "Beg him not to cum inside.":
                show sb_doggy1 shock with dissolve
                pc "Please no. Not inside. Pull out, pull out! Please!"
                if player.check_speech(4):
                    $ randomnum = renpy.random.randint(1,2)
                    if randomnum == 1:
                        jump school_bully_sex_forced_spitroast_vag_cum_pullout
                    else:
                        jump school_bully_sex_forced_spitroast_vag_cum_pullout_anal
                else:
                    $ player.punch()
                    show sb_doggy1 pain closed
                    tempname2.name "Shut up bitch. You don't have a choice here!"
                    jump school_bully_sex_forced_spitroast_vag_cum_inside
            "Keep silent.":

                jump school_bully_sex_forced_spitroast_vag_cum_inside

label school_bully_sex_forced_spitroast_cont:
    $ dialouge = WeightedChoice([
    ("Shut up bitch!", 1),
    ("Shut the fuck up!", 1),
    ("Be quiet!", 1),
    ])
    tempname.name "[dialouge]"
    show sb_doggy2 pullhair head_forward with hpunch
    pc "Mmmff!"
    tempname.name "Don't try to get away."
    $ dialouge = WeightedChoice([
    ("Ah! Fucking cunt!", 1),
    ("Ah this fucking arsehole!", 1),
    ("Ah fuck this shitty cunt.", 1),
    ("Nonononono...", 1),
    ])
    pcm "[dialouge]"
    pc "*SOB*"
    $ dialouge = WeightedChoice([
    ("I feel him start to take long and deep thrusts inside me. Pushing his cock balls deep into me before pulling almost all the way out, then ramming it back in again. ", 1),
    ("He takes it slow and rhythmically thrusts making sure I feel his disgusting cock in me. He paws at my tits as he does so and I just accept what is happening.", 1),
    ("He thrusts deeply into me before slowly sliding his cock out almost all the way. Then aggressively slams back into me in a quick and hard thrust.", 1),
    ])
    "[dialouge]"
    "All the while [tempname.name] in front of me pulls at my hair to force his cock deeper into my mouth."
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("Sandwiched between them, i can hardly get a breath and I hope it will all be over soon.", 1),
    ("The rythmic motion of them fucking me means that when one is on the way out, the other is pushing in deeper. I try my best to just wait it out.", 1),
    ])
    "[dialouge]"
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    tempname2.name "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Cunt!", 1),
    ("Fucking cunt!", 1),
    ("Disgusting shit!", 1),
    ])
    pcm "[dialouge]"
    shane.name "Like most whores around here. Perfectly fine once you put something in their mouth to shut them up."
    marcus.name "Heh"
    $ dialouge = WeightedChoice([
    ("His breathing starts to become ragged and it seems like it will be over soon.", 1),
    ("His thrusting and pawing at my body has become more aggressive and it sounds like he might be reaching his limit.", 1),
    ("He is thrusting faster now and squeezing at my arse. It seems like he won't last much longer.", 1),
    ])
    "[dialouge]"
    $ player.face_cry()
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
    show sb_spitroast angry closed sex blow
    with dissolve
    tempname2.name "Make the bitch swallow it."
    tempname.name "Of course!"
    tempname.name "Ahhhh!"
    $ player.sex_cum(tempname, "mouth")
    $ player.beingraped = True
    $ dialouge = WeightedChoice([
    ("I feel his start to throb and push his cock deep in my mouth. He starts to cum and I feel his vile load squirting from his cock and into my mouth.", 1),
    ("He starts throbbing in my mouth and I feel disgust as he cums into my mouth.", 1),
    ("His cock starts to swell until he tenses up and releases his vile load in my mouth and I have no choice but to swallow most of it down.", 1),
    ("He throbs in my mouth and I feel the first wave fill me. I quickly resist the urge to puke. I end up swallowing it down as another pulse shoots more into my mouth.", 1),
    ])
    "[dialouge]"
    tempname.name "Ahhhh! Yeeeeess..."
    tempname.name "Haaaa..."
    pc "Ubbb..."
    $ dialouge = WeightedChoice([
    ("Ah good little slut. Make sure to drink it all down.", 1),
    ("That's how a bitch should treat their betters. Next time I will be the one fucking you.", 1),
    ("Good. Swallow it down like the little cum whore you are.", 1),
    ])
    tempname.name "[dialouge]"
    show sb_spitroast up mast shock with dissolve
    pc "Ugh!"
    pcm "Can finally breathe properly."
    tempname.name "The bitch is all yours. I'll mind the door."
    pcm "Fuck."
    return

label school_bully_sex_forced_spitroast_vag_cum_inside:
    $ dialouge = WeightedChoice([
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it you cunt.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Yes, yes!", 1),
    ("Ah yes you shitty bitch! I am going to fill you up.", 1),
    ("Ah get ready for carrying my baby, bitch!", 1),
    ("Haaa fuck I am going to knock you up like a dirty slut you are!", 1),
    ("Get ready for my baby you bitch.", 1),
    ("Ahhh yes take it deep inside. Hope you're feeling lucky.", 1),
    ("Better hope you are lucky cos I am going to fill you up!", 1),
    ("You dirty slut. Take me inside you.", 1),
    ("Ah fuck yes you filthy slut.", 1),
    ])
    tempname2.name "[dialouge]"
    $ player.sex_cum(tempname2, "inside")
    show sb_doggy1 grit closed
    $ dialouge = WeightedChoice([
    ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
    ("His cock pulses inside me, unloading his cum deep inside me.", 1),
    ])
    "[dialouge]"
    tempname2.name "Ahhh take it all you shitty whore!"
    tempname2.name "Haaaaa!"

    $ dialouge = WeightedChoice([
    ("No plea...", 1),
    ("Fuck...", 1),
    ("Stop...", 1),
    ("*SOB* *SOB*", 1),
    ("Shit!", 1),
    ])
    pc "[dialouge]"
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    tempname2.name "Good little whore."
    $ player.spank()
    $ player.face_cry()
    pc "*SOB*"
    show sb_doggy1 open
    $ dialouge = WeightedChoice([
    ("I stay there with their cum dripping out of me and watch as the both of them leave laughing to each other.", 1),
    ("I try to hold back tears as I watch the cunts leave with their cum still inside me dripping out.", 1),
    ("I try not to curse at them as they are leaving in case one of them comes and hits me. But internally I am screaming at them.", 1),
    ])
    "[dialouge]"
    jump school_bully_sex_forcesex_end

label school_bully_sex_forced_spitroast_vag_cum_pullout_anal:
    tempname2.name "Tsk!"
    show sb_doggy1 poke with dissolve
    pause 0.5
    $ player.sex_anal(tempname2)
    show sb_doggy1 anal shock open with hpunch
    pc "AAAAAAAAAAAAAAHHHHHHHHHHHHHH HHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!! FUUUUUCCCCCCCCCKKKKKKK!!!!!!!!!"


    pc "THAFUCKAREYOUDOING?!?!!!??!?!?!?!?"
    pc "Shit fuck fuck fuck."
    show sb_doggy1 grit
    $ player.sex_cum(tempname2,"anal")
    tempname2.name "Ahhhh fuck yes."
    $ player.spank()
    tempname2.name "Haaaaaa..."
    pc "*SOB*"
    tempname2.name "Ah fuck yes. Nice little bitch."
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    pcm "Fuckfuckfuck. Ass feels like it's on fire!"
    pc "Unnnng!"
    $ dialouge = WeightedChoice([
    ("I sit on the floor and cry as they clean themselves up and leave while laughing at me.", 1),
    ("I break down and cry and arseholes pay me no heed as they laugh at me and leave.", 1),
    ("I sit down and sob as they laugh at me while dressing up, then leave.", 1),
    ])
    "[dialouge]"
    jump school_bully_sex_forcesex_end

label school_bully_sex_forced_spitroast_vag_cum_pullout:
    tempname2.name "Tsk!"
    show sb_doggy1 poke ah with dissolve
    $ player.sex_cum(tempname2,"pullout")
    tempname2.name "Ahhhh fuck yes."
    $ player.spank()
    tempname2.name "Haaaaaa..."
    pc "*SOB*"
    tempname2.name "Ah fuck yes. Nice little bitch."
    show sb_doggy1 poke with dissolve
    show sb_doggy1 noman with dissolve
    $ dialouge = WeightedChoice([
    ("I sit on the floor and cry as they clean themselves up and leave while laughing at me.", 1),
    ("I break down and cry and arseholes pay me no heed as they laugh at me and leave.", 1),
    ("I sit down and sob as they laugh at me while dressing up, then leave.", 1),
    ])
    "[dialouge]"
    jump school_bully_sex_forcesex_end

label school_bully_sex_forcesex_end:
    $ renpy.scene()
    with dissolve
    $ player.face_cry()
    $ dialouge = WeightedChoice([
    ("Arseholes! The both of them.", 1),
    ("Fucking cunts!", 1),
    ("Horrible shits!", 1),
    ])
    pc "[dialouge]"
    pc "*SOB*"
    pause 1
    $ pc_dress()
    $ player.face_wail()
    pc "Whaaaaa!"
    $ player.face_cry()
    pc "*SOB*"
    pc "I can't believe that just happened..."
    pc "..."
    jump random_event_school_end_picker

label school_bully_sex_forced_sold_intro:
    $ dialouge = WeightedChoice([
    ("Got some admirers here that wouldnt mind having a go this time. Whore like you is probably used to it anyway.", 1),
    ("Gonna put that arse of yours to work where it belongs. Some people here are interested in you and I could do with the money.", 1),
    ("Gonna put you to work bitch. Not that it's much different to usual.", 1),
    ])
    shane.name "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Get against the wall and stick your arse out. If you even think about opening your eyes, you might not leave here with them still in your skull.", 1),
    ("Against the wall and close your eyes. Open them and you lose them. Got it?", 1),
    ])
    shane.name "[dialouge]"
    if not player.check_nowill():
        pc "What. The hell do you..."
        $ player.punch()
        pc "Nnng!"
        shane.name "Another word gets another punch."
        pcm "Fuck fuck fuck!"
        if not player.check_nowill():
            pcm "The cunt wants to put me up for sale? Fuck fuck!"
            call school_bully_sex_forced_runaway from _call_school_bully_sex_forced_runaway_2
    $ player.face_cry()
    pc "*SOB*"
    shane.name "Go on bitch!"
    show sb_againstwall3 closed grit
    show screen blackout(50)
    with dissolve
    marcus.name "{color=#b3b3b3}Come in, she's ready.{/color}"
    guy "{color=#b3b3b3}Yeah? It's ok?{/color}"
    marcus.name "{color=#b3b3b3}Yeah, have fun.{/color}"
    pcm "Fuck fuck fuck!"
    pcm "..."
    pcm "What's going on?"
    show sb_againstwall3 poke with dissolve
    pcm "Shit!"
    pcm "Should have tried to run away..."
    $ player.sex_vag(shanewhore)
    show sb_againstwall3 sex with dissolve
    pcm "Fuck fuck fuck!"
    pcm "Not happening not happening..."
    "I try to ignore what is happening behind me and take my mind to a nicer place to get through this."
    "It is not easy though with him gripping onto me and slamming inside me."
    "I hear him calling me names while he thrusts into me. I am not sure if he knows he is raping me or if he thinks I am willing."
    "Not that it matters. I just try to think happy thoughts and get through this whole ordeal."
    $ player.sex_cum(shanewhore, "inside")
    guy "{color=#b3b3b3}Ahhh fuck yes!{/color}"
    guy "{color=#b3b3b3}Haaaa...{/color}"
    show sb_againstwall3 poke with dissolve
    show sb_againstwall3 noman with dissolve
    show sb_againstwall3 wink pout
    hide screen blackout
    with dissolve
    pcm "Is it over?"
    shane.name "{color=#b3b3b3}You're next. Go on.{/color}"
    pcm "Next? Fuck!"
    show sb_againstwall3 closed
    show screen blackout(50)
    with dissolve
    pc "*SOB*"
    show sb_againstwall3 poke with dissolve
    guy "{color=#b3b3b3}Ah you came inside? Ugh.{/color}"
    guy "{color=#b3b3b3}Can I fuck her arse?{/color}"
    shane.name "{color=#b3b3b3}Yeah whatever. Go wild. She loves it.{/color}"
    guy "{color=#b3b3b3}Nice.{/color}"
    $ player.sex_anal(shanewhore)
    show sb_againstwall3 sex grit with dissolve
    pc "Nnng!"
    pcm "FUUUUCK!!!!!"
    pcm "Hurts!"
    pcm "Owowowowowoowwwww!"
    show screen blackout(75) with dissolve
    show screen blackout(50) with dissolve
    "I try to block out the pain by gritting my teeth and just hope for it to be over soon."
    "The guy behind me doesn't make it easy though. He cares little for making it gentle and does what he pleases with little regard for my ass."
    "I try to block out what is happening, and manage to do it until he gets much rougher..."
    $ player.sex_cum(shanewhore, "anus")
    guy "{color=#b3b3b3}Fuck yes!!{/color}"
    guy "{color=#b3b3b3}Ahhhhh...{/color}"
    guy "{color=#b3b3b3}Mmmmmmmm...{/color}"
    show sb_againstwall3 poke with dissolve
    show sb_againstwall3 noman with dissolve
    show sb_againstwall3 wink pout
    pcm "Please be over please be over..."
    shane.name "{color=#b3b3b3}And you? Come on, money first.{/color}"
    pcm "It's not..."
    show screen blackout(100) with dissolve
    $ player.sex_vag(shanewhore)
    show sb_againstwall3 sex closed grit with dissolve
    show screen blackout(50) with dissolve
    pc "Nnng."
    show screen blackout(75) with dissolve
    show screen blackout(50) with dissolve
    "They keep going..."
    pcm "Block it out block it out..."
    guy "C'mere!"
    $ renpy.scene()
    hide screen blackout
    show sb_standbehind ah
    with hpunch
    pc "What are you doing?"
    $ tempname = shanewhore
    $ quest_temp = None
    $ player.sex_holes = ["vag"]
    $ event_end_interrupt_label = "school_bully_sex_forced_sold_repeat_end"
    $ player.sex_man_amount = numgen(2,10)
    jump whore_street_sex_group_standing_cont




    $ player.sex_cum(shanewhore, "inside")
    guy "{color=#b3b3b3}##### ### ###### ### #######.{/color}"
    show sb_againstwall3 poke with dissolve
    show sb_againstwall3 noman with dissolve
    jump school_bully_sex_forced_sold_repeat_choice

label school_bully_sex_forced_sold_repeat_choice:
    $ randomnum = renpy.random.randint(1, 9)
    if randomnum == 1:
        jump school_bully_sex_forced_sold_repeat_end
    if randomnum < 3:
        jump school_bully_sex_forced_sold_repeat_ass
    else:
        jump school_bully_sex_forced_sold_repeat_vag

label school_bully_sex_forced_sold_repeat_vag:
    pause 1
    show sb_againstwall3 poke with dissolve
    $ player.sex_vag(shanewhore)
    show sb_againstwall3 sex with dissolve
    $ dialouge = WeightedChoice([
    ("Nnng!", 1),
    ("*SOB*", 1),
    ("Fuck!", 1),
    ])
    pcm "[dialouge]"
    pause 1
    $ working(20)
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show sb_againstwall3 cum with dissolve
        $ player.sex_cum(shanewhore, "pullout")
        guy "{color=#b3b3b3}##### ### ###### ### #######.{/color}"
    else:
        $ player.sex_cum(shanewhore, "inside")
        guy "{color=#b3b3b3}##### ### ###### ### #######.{/color}"
        show sb_againstwall3 poke with dissolve
    show sb_againstwall3 noman with dissolve
    jump school_bully_sex_forced_sold_repeat_choice

label school_bully_sex_forced_sold_repeat_ass:
    pause 1
    show sb_againstwall3 poke with dissolve
    $ player.sex_anal(shanewhore)
    show sb_againstwall3 sex with dissolve
    $ dialouge = WeightedChoice([
    ("Nnng!", 1),
    ("*SOB*", 1),
    ("Fuck!", 1),
    ])
    pcm "[dialouge]"
    pause 1
    $ working(20)
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show sb_againstwall3 cum with dissolve
        $ player.sex_cum(shanewhore, "pullout")
        guy "{color=#b3b3b3}##### ### ###### ### #######.{/color}"
    else:
        $ player.sex_cum(shanewhore, "anus")
        guy "{color=#b3b3b3}##### ### ###### ### #######.{/color}"
        show sb_againstwall3 poke with dissolve
    show sb_againstwall3 noman with dissolve
    jump school_bully_sex_forced_sold_repeat_choice

label school_bully_sex_forced_sold_repeat_end:
    pc "..."
    pcm "Have they gone?"
    pcm "Fuuuck I am so sore..."
    $ player.face_cry()
    pc "*SOB*"
    jump school_bully_sex_forcesex_end

label school_bully_sex_forced_attack:

    $ player.punch()
    pc "Ahh!"
    $ player.punch()
    pause 0.2
    $ player.punch()
    pc "Stoooo..."
    jump school_bully_sex_ko

label school_bully_sex_ko:
    show screen blackout with dissolve
    pause 0.5
    hide shane
    hide marcus
    $ temp_var_1 = player.vvirgin
    $ player.sex_forced(shane)
    $ player.sex_vag(shane)
    $ player.sex_forced(marcus)
    $ player.sex_vag(marcus)
    $ player.sex_hideaction()
    $ tempname = random([shane, marcus])
    $ npc_race_picker(tempname)
    $ pc_strip()


    show sb_assup closed worried frown sex

    $ player.eye = 3
    show screen blackout(50) with dissolve
    pc "Uuuugggggg..."
    show sb_assup squint with dissolve
    pc "Whhhhhhhaaaaaa..."
    tempname.name "Ahhhh..."
    $ player.sex_cum(tempname, "inside")
    $ player.eye = 3
    tempname.name "Ahhhaaaahhh........"
    show sb_assup closed with dissolve
    $ player.eye = 3
    pc "Oooowhaaaaaa..."
    show screen blackout(100) with dissolve
    $ time_sleep_rough()
    hide sb_assup
    pause 0.5
    hide screen blackout with dissolve
    $ player.face_shock()
    pc "Ahhhhh..."
    pc "Fuck fuck!"
    pc "Did...?"
    pc "Ah fuck..."
    $ player.face_cry()

    if temp_var_1 == True:
        pc "Did those fuckers really take my virginity?"

    "I spot my clothes laying in a pile on the floor so I head over to pick them up."
    pc "*SOB* *SOB*"
    $ pc_dress()
    pc "..."
    pc "*SOB* *SOB*"
    pc "I can't believe that just happened..."
    pc "..."
    jump random_event_school_end_picker

label school_bully_sex_forced_runaway:
    if player.confidence >= 60:
        jump school_bully_sex_forced_runaway_attempt
    menu:
        "Try to run away":
            jump school_bully_sex_forced_runaway_attempt
        "Submit":
            pcm "I'll end up getting beaten up if I try to run away..."
            return

label school_bully_sex_forced_runaway_attempt:
    if player.check_fight(3):
        hide shane
        hide marcus
        $ walk(loc_school_hallway)
        $ player.face_exercise()
        with hpunch

        $ dialouge = WeightedChoice([
        ("I raise my hands to my top to look like I am about to undress, then quickly make a break for it and don't look back", 1),
        ("I spit in his face and quickly make a run for it. I keep going without looking back until I am somewhere much more public.", 1),
        ("I pretend to get ready to undress before quickly doing a runner. I keep going until I am somewhere with other people around.", 1),
        ])
        "[dialouge]"
        pcm "*Phew*"
        $ player.face_worried()
        pcm "Fuck..."
        $ player.face_cry()
        pcm "*SOB*"
        pcm "Thank fuck I got away..."

        jump random_event_school_end_picker
    else:

        if tempname == shane:
            show shane frown at right5
        else:
            show marcus frown at right5
        with hpunch
        $ dialouge = WeightedChoice([
        ("I raise my hands to my top to look like I am about to undress, then quickly make a break for it. But he was ready and trips my ankle as I try to run.", 1),
        ("I spit in his face and quickly make a run for it. But he was prepared for me and pushes me as I run and I end up tumbling over and hitting the floor.", 1),
        ("I pretend to get ready to undress before quickly doing a runner. He isn't fooled though and trips me as I try to run.", 1),
        ])
        "[dialouge]"

        $ player.punch()
        tempname.name "Right! You asked for it!"

        jump school_bully_sex_forced_attack
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
