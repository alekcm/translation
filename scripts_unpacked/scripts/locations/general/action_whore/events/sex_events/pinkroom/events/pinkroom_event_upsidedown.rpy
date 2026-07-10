label pinkroom_customer_event_upsidedown:
    tempname.name "Hey [rlist.name_cute]. How about we put these loops to good use and tie you up?"
    if not inv.qty(item_bdsm):
        pc "Err, I don't have anything to use to tie up."
        tempname.name "No worries. I do."
        pc "Oh? Great..."
    else:
        pc "Err, sure. I have some stuff we can use."
    $ inv.take(item_pinkticket, 4)
    tempname.name "Great."
    "I head over to the bed and get out the straps I have. The guy starts positioning and tying me up."
    pc "Err, this isn't easy."
    tempname.name "But looks hot as fuck."
    pc "Ung! Ow! Alllmost..."
    show sb_upsidedown with dissolve
    tempname.name "There we go..."
    pc "Gonna have all the blood rush to my head."
    if inv.qty(item_blindfold) and not player.has_perk(perk_blind):
        tempname.name "I see you have one of these? I'll put that on as well."
        $ player.add_perk(perk_blind)
        show sb_upsidedown
        pc "Ah, okay..."
    elif not inv.qty(item_blindfold) and not numgen(0,10):
        tempname.name "I have one of these, it will be more fun with it."
        $ inv.take(item_blindfold)
        $ player.add_perk(perk_blind)
        show sb_upsidedown
    if inv.qty(item_ballgag) and not player.has_perk([perk_gagged, perk_gagged_locked]):
        tempname.name "I'll put this on as well."
        $ player.add_perk(perk_gagged)
        show sb_upsidedown
        pc "Gagged muff"
    elif not numgen(0,10) and not player.has_perk([perk_gagged, perk_gagged_locked]):
        tempname.name "I have one of these as well, it will be fun."
        if numgen(0, 10):
            $ inv.take(item_ballgag)
            $ player.add_perk(perk_gagged)
            show sb_upsidedown
        else:
            $ inv.take(item_ballgag_locked)
            $ player.add_perk(perk_gagged_locked)
            show sb_upsidedown
        pc "Gagged muff"
    tempname.name "Mmmmm..."
    if not numgen(0,3):
        tempname.name "Sexy arse poking up like that."
        $ player.spank()
        show sb_upsidedown
        pc "Ah!"
        if player.gagged:
            tempname.name "I can't understand you."
            $ player.spank()
            show sb_upsidedown
            pc "something"
            tempname.name "More? Okay."
            show sb_upsidedown pain
            $ player.spank()
            show sb_upsidedown
            tempname.name "Don't worry, you won't leave here without a bright red arse."
            $ player.spank()
            show sb_upsidedown
            pc "Something"
            tempname.name "Yes, it is nice."
            $ player.spank()
            show sb_upsidedown
            tempname.name "Mmmm..."
            $ player.spank()
            show sb_upsidedown
        else:
            tempname.name "Like that do you?"
            show sb_upsidedown pain
            $ player.spank()
            show sb_upsidedown
            pc "Haaa!"
            pc "You really into this aren't you?"
            tempname.name "Of course. Can fuck any girl on the highway but only you pinkroom whores do the real fun things."
            $ player.spank()
            show sb_upsidedown
            pc "Ah!"
            tempname.name "Don't worry, I'll get to filling you up soon."
            $ player.spank()
            show sb_upsidedown
            tempname.name "Got to give you something to remember first."
            $ player.spank()
            show sb_upsidedown
            pc "Ahhh!"

    if inv.qty(item_buttplug) and not acc.anus and numgen():
        tempname.name "And what's this we have here?"
        tempname.name "Bad girl, you have been holding out on me."
        pc "Huh?"
        tempname.name "Well, not for much longer."
        "He takes my buttplug from my stuff, spits on it and presses it against my asshole."
        $ acc.anus = 1
        if not inv.qty(item_buttplug):
            $ inv.take(item_buttplug)
        pc "Haaaa!"
    elif not acc.anus and not numgen(0, 6):
        tempname.name "I can think of something that will make this ass a lot nicer."
        pc "Huh?"
        if player.blind:
            "I hear him walk away from me, then start rustling with something. I have no idea what it is, but he is coming towards me with it."
            "Without warning, I feel something hard and cold press against my arsehole making what it is somewhat obvious."
            "I feel it pressing into my arse and my hole stretching open. It's only when I feel myself relax against it's base that I realise it's a plug and not a dildo."
            $ acc.anus = 1
            if not inv.qty(item_buttplug):
                $ inv.take(item_buttplug)
            pc "Haaaa..."
            tempname.name "Good girl."
        else:
            "He heads over to his bag, takes something out, spits on it then comes over to me."
            "I didn't manage to see what it was, but the cold feeling of it pressing against my arsehole makes it somewhat obvious."
            "I feel it pressing into my arse and my hole stretching open. It's only when I feel myself relax against it's base that I realise it's a plug and not a dildo."
            $ acc.anus = 1
            if not inv.qty(item_buttplug):
                $ inv.take(item_buttplug)
            pc "Haaaa..."
            tempname.name "Good girl."
    $ player.spank()
    tempname.name "Now what should I do with you, all tied up with your ass in the air?"
    if not numgen(0,2) and not player.gagged:
        tempname.name "Maybe you should get me ready with your mouth first."
        pc "Not like I can refuse like this."
        tempname.name "That's right."
        show sb_upsidedown blow down with dissolve
        $ player.sex_oral(tempname, quest_temp)
        pc "[rlist.blowjob_muffle]"
        tempname.name "[rlist.having_sex_man_yes]"
        "I end up just laying back while he uses my mouth as a hole to gently fuck. It's not a bad sensation, even if I am upside down."
        "His hands are constantly on my ass and now and then his fingers or even his tongue probes ones of my holes."
        if numgen():
            "Without warning, he gets a little more excited and presses his cock deeper into my mouth "
            show sb_upsidedown blowdeep closed with dissolve
            pc "[rlist.blowjob_muffle]"
            "It feels like he is going so deep that his cock is now fucking my throat."
            "I can barely breathe like this and without a care, he keeps pushing his cock deep down my throat."
            if numgen(0,30):
                "Just as I can feel myself truly starting to choke, he slowly eases out."
                show sb_upsidedown blow down with dissolve
                "While his cock isn't fully out of my mouth, I am able to breathe a little through my nose at least."
                show sb_upsidedown blowdeep closed closed with hpunch
                "Then again without warning, he shoves it back down my throat..."
                pcm "Fuck!"
                pc "*Ack*"
                if not numgen(0,10):
                    jump pinkroom_customer_event_upsidedown_cum_blowdeep
                elif not numgen(0,20):
                    "This is a pass out event. Sammy will choke, wake up and be in the train branch"
                "Rest not written"
        else:
            "Less blow branch"
    if acc.anus and player.gagged:
        tempname.name "Well, two of you holes are already occupied, so only leaves one left."
    elif acc.anus:
        tempname.name "Your ass is already full up, so I think I will fuck you in the pussy."
        tempname.name "Both of your holes filled up, I bet you would like that."
        pc "Maybe..."
    else:
        tempname.name "Two little holes here looking right at me begging to be filled."
        tempname.name "Would you prefer it up your arse or in the pussy?"
    pc "Mmmm."
    jump expression WeightedChoice([
    ("pinkroom_customer_event_upsidedown_sex_anal", If(not acc.anus, 2, 0)),
    ("pinkroom_customer_event_upsidedown_sex_vag", 5), 
    ])

label pinkroom_customer_event_upsidedown_sex_vag:
    show sb_upsidedown poke down ah with dissolve
    tempname.name "Think I will leave you with a leaking pussy."
    pc "Oh?"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ player.sex_vag(tempname, quest_temp)
    show sb_upsidedown vag down happy with dissolve
    $ player.face_excited()
    if player.blind:
        "He grips onto my ass and spreads my cheeks as I feel him fucking me in the pussy. I can't see what's happening but I can feel everything."
    else:
        "He grips onto my ass and gently fucks me. From this position I can see perfectly what he is doing as his cock slides in and out of me."
    "It's not the most comfortable of positions, but the guy likes it so I try to relax and enjoy the feeling of him fucking me."
    $ player.spank()
    "I feel so exposed like this. His cock in my pussy and his hands spreading my ass cheeks and him having a perfect view of everything."
    if not numgen(0,4) and not acc.anus:
        jump pinkroom_customer_event_upsidedown_sex_anal_switch
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "I lay here with my ass in the air taking everything he pumps inside me."
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    "In this position, I don't even feel anything leaking out after. Everything he pumps into me stays inside me."
    show sb_upsidedown poke neutral up with dissolve
    pc "Mmm, admiring your work?"
    tempname.name "It's a shame I can only fill you up once."
    pc "I'm a whore, fill me up as many times as you can afford."
    tempname.name "Haha."
    show sb_upsidedown noman with dissolve
    tempname.name "Phew."
    jump pinkroom_customer_event_upsidedown_sex_end

label pinkroom_customer_event_upsidedown_sex_anal_switch:
    show sb_upsidedown poke down neutral with dissolve
    "I feel him ease himself out of me. He hasn't cum yet so I am not sure what he is doing."
    pc "Did you cum?"
    tempname.name "Going to have fun in your other hole."
    pc "Oh?"
    "I feel him press his cock against my arsehole, and with all the juices from my pussy on his cock, he finds little resistance."
    show sb_upsidedown ass ag closed with dissolve
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"

label pinkroom_customer_event_upsidedown_sex_anal:
    "Anal branch"
label pinkroom_customer_event_upsidedown_blindgag_leave:

label pinkroom_customer_event_upsidedown_cum_blowdeep:
    with hpunch
    "Before I know it, he is shoving his cock even deeper into my mouth. Any more and I'll be choking on his balls as well."
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    pcm "Quickly before I choke to death!"
    $ player.sex_cum(tempname, "mouth", quest_temp)
    "I feel this cock deep in my throat start to throb and feel something going down inside me as well as up through my nose."
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.blowjob_muffle]"
    show sb_upsidedown blow down with dissolve
    show sb_upsidedown noman angry up with dissolve
    pc "*COUGH*"
    pc "Fuck! I can feel it up my nose."
    tempname.name "Good girl. Your throat makes a good hole to fuck."
    pc "Ugh."
    $ player.spank()
    pc "Ah!"
    pcm "..."
    jump pinkroom_customer_event_upsidedown_sex_end

label pinkroom_customer_event_upsidedown_sex_end:
    pc "Gonna untie me?"
    if not numgen(0,50):
        if player.blind:
            "I am not sure what he is doing, but sounds like he is rustling about the room."
            "I lay there waiting with my ass in the air for him to hurry up."
            pcm "..."
            pc "Come on. Untie me."
            "But there is silence now from the room..."
            pc "Please?"
            "Then I realise what has happened when I feel a breeze. The door is open!"
            pcm "Fuck, that bastard left me?"
            pcm "..."
            pc "Hello?"
            pc "Some help here?"
            jump pinkroom_customer_event_train_start_unknown
        else:
            "He doesn't answer and instead just starts getting dressed."
            pcm "..."
            pc "Come on. Untie me."
            pc "..."
            pc "Please?"
            "Without another look, he just heads out the door, leaving it wide open."
            pcm "Fuck!"
            pcm "..."
            pc "Hello?"
            pc "Some help here?"
            jump pinkroom_customer_event_train_start_unknown

    elif not numgen(0,5) and not player.gagged:
        tempname.name "Sure you don't want to stay like this?"
        pc "I think I need blood in other places, not just my head."
        tempname.name "I could leave you tied up here and leave the door open. Half the district will have some fun with you."
        if player.has_perk([perk_freeuse, perk_sucu, perk_slut], notif=True):
            pcm "That actually kinda sounds like fun..."
            pc "Err..."
            menu:
                "Sure, keep me like his":
                    pc "Errr..."
                    pc "..."
                    tempname.name "Oh? You like the sound of that?"
                    pc "No."
                    tempname.name "Sure..."
                    tempname.name "I'm going to leave now."
                    pc "..."
                    if player.blind:
                        "I hear him getting dressed. He seems to be taking a fair amount of time doing so. I assume he is giving me time to ask him to untie me."
                        "But I keep silent and eventually I hear him unlock and open the door."
                    else:
                        "He starts very slowly getting ready, looking at me waiting for me to ask him to untie me."
                        "But I keep quiet. As he leaves he looks back at me one more time and again I keep silent."
                    tempname.name "C'ya."
                    if player.blind:
                        "After he says goodbye, I don't hear anything more. Including not hearing the door shut behind him."
                        "The room getting a little colder let's me know that he left it wide open."
                    else:
                        "Before he walks away, I see him write something on the notice on the door and walk away leaving it wide open."
                    jump pinkroom_customer_event_train_start_unknown
                "No thanks":

                    pc "Na, I think I'd rather not become a cum toilet."
                    pcm "As fun as that sounds..."
        else:
            pc "No thanks. I'd rather choose who fucks me."


    elif not numgen(0,3):
        "He doesn't answer and instead lights a cigarette and sits there smoking while just watching me."
        "Eventually though, he comes over and undoes some of the straps. Not all of them but just enough that I could manage to free myself."
        "He sits there with a stupid grin on his face while watching me trying to untie myself."
        $ working(5)
        "Eventually I manage it though and roll over to a normal position where blood isn't rushing to my head."
        jump whore_street_sex_end

    tempname.name "Okay."
    "He leans over and unlocks some of the clasps, leaving me a bit of room to unlock the rest myself."
    "He sits there with a stupid grin on his face while watching me trying to untie myself."
    pc "You could help."
    tempname.name "And miss the view of you struggling around?"
    "Eventually I manage it though and roll over to a normal position where blood isn't rushing to my head."
    jump whore_street_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
