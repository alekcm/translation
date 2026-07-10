label whore_street_sex_tied_laying:
    $ npc_race_setsame()
    tempname.name "Hey [rlist.name_cute]. How about we put these loops to good use and tie you up?"
    if not inv.qty(item_bdsm):
        pc "Err, I don't have anything to use to tie up."
        tempname.name "No worries. I do."
        pc "Oh? Great..."
    else:
        pc "Err, sure. I have some stuff we can use."
    $ inv.take(item_pinkticket, 4)
    tempname.name "Great."
    "I take the straps off him, lay on the bed and he helps me tie my arms and legs to the posts."
    show sb_onback look_up tied with dissolve
    pc "Err, I think that's tight enough."
    tempname.name "There we go..."
    if inv.qty(item_blindfold) and not player.has_perk(perk_blind):
        tempname.name "I see you have one of these? I'll put that on as well."
        $ player.add_perk(perk_blind)
        show sb_onback
        pc "Ah, okay..."
    elif not inv.qty(item_blindfold) and not numgen(0,10):
        tempname.name "I have one of these, it will be more fun with it."
        $ inv.take(item_blindfold)
        $ player.add_perk(perk_blind)
        show sb_onback
    if inv.qty(item_ballgag) and not player.has_perk([perk_gagged, perk_gagged_locked]):
        tempname.name "I'll put this on as well."
        $ player.add_perk(perk_gagged)
        show sb_onback
        pc "Gagged muff"
    elif not numgen(0,10) and not player.has_perk([perk_gagged, perk_gagged_locked]):
        tempname.name "I have one of these as well, it will be fun."
        if numgen(0, 10):
            $ inv.take(item_ballgag)
            $ player.add_perk(perk_gagged)
            show sb_onback
        else:
            $ inv.take(item_ballgag_locked)
            $ player.add_perk(perk_gagged_locked)
            show sb_onback
        pc "Gagged muff"
    tempname.name "Mmmmm..."

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
        tempname.name "Mmm, maybe I should help you feel much more full up?"
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
            "He looks at me and smiles while showing me what he had. It's a buttplug."
            pc "Why do you just happen to have one of those?"
            tempname.name "Something special for fun with girls like you."
            "He puts his hands between my legs and I feel it pressing into my arse and my hole stretching open. It pops it's way into my arse and I relax around it's stem."
            $ acc.anus = 1
            if not inv.qty(item_buttplug):
                $ inv.take(item_buttplug)
            pc "Haaaa..."
            tempname.name "Good girl."
    $ player.spank()
    show sb_onback man_left with dissolve
    tempname.name "Now what should I do with you, all tied up and helpless?"
    if not numgen(0,2) and not player.gagged:
        tempname.name "Maybe you should get me ready with your mouth first."
        pc "Not like I can refuse like this."
        tempname.name "That's right."
        show sb_onback no_man_left facefuck look_down with dissolve
        $ player.sex_oral(tempname, quest_temp)
        pc "[rlist.blowjob_muffle]"
        tempname.name "[rlist.having_sex_man_yes]"
        "I end up just laying back while he uses my mouth as a hole to gently fuck. It's not a bad sensation and something I might even like to do normally."
        "His hands are running through my hair, holding my head and making sure my mouth matches pace with his trusts."
        if numgen():
            "Without warning, he gets a little more excited and presses his cock deeper into my mouth "
            show sb_onback facefuck_deep look_closed with dissolve
            pc "[rlist.blowjob_muffle]"
            "It feels like he is going so deep that his cock is now fucking my throat."
            "I can barely breathe like this and without a care, he keeps pushing his cock deep down my throat."
            if numgen(0,15):
                "Just as I can feel myself truly starting to choke, he slowly eases out."
                show sb_onback facefuck look_down with dissolve
                "While his cock isn't fully out of my mouth, I am able to breathe a little through my nose at least."
                show sb_onback facefuck_deep look_closed with hpunch
                "Then again without warning, he shoves it back down my throat..."
                pcm "Fuck!"
                pc "*Ack*"
                if not numgen(0,10):
                    jump whore_street_sex_tied_laying_cum_blowdeep
                elif danger_gen(20,1):
                    "He keeps deep fucking my throat and I try to take it and wait for him to pull out again."
                    "But he just keeps going and I am really struggling to breathe..."
                    with hpunch
                    "I start to try to move my head or arms, but I am too stuck in place to do anything."
                    with vpunch
                    "He keeps fucking me."
                    with hpunch
                    pcm "Fuck fuck fuck! Can't breathe!"
                    show screen blackout(50) with vpunch
                    pcm "Get off get off get off get off!"
                    "He keeps fucking me deep in my throat and I cannot stop him."
                    show screen blackout(100) with dissolve
                    show sb_onback no_facefuck look_closed
                    jump pinkroom_customer_event_train_wakeup_train

            show sb_onback facefuck look_down with dissolve
            show sb_onback man_left no_facefuck look_up with dissolve
            "He slides out of my mouth and off of me, which let's me catch my breath."
            pc "Not so rough next time."
            tempname.name "Don't worry, I'll be putting it deep somewhere else next."
        else:
            "He facefucks me for a while and I get into the flow of it. I try to move my head in time with his thrusts."
            show sb_onback man_left no_facefuck with dissolve
            "Then he slides out of me and stands off to the side."
            pc "Not done already are you?"
            tempname.name "Nope. But I think I will put it somewhere else now."
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
    ("whore_street_sex_tied_laying_sex_anal", If(not acc.anus, 2, 0)),
    ("whore_street_sex_tied_laying_sex_vag", 5), 
    ])

label whore_street_sex_tied_laying_sex_vag:
    show sb_onback no_man_left hump look_down ooh with dissolve
    tempname.name "Think I will leave you with a leaking pussy."
    pc "Oh?"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ player.sex_vag(tempname, quest_temp)
    show sb_onback happy with dissolve
    $ player.face_excited()
    if player.blind:
        "He grips onto my hips and pushes deep into my pussy. I can't see what's happening but I can feel everything."
    else:
        "He grips onto my hips and gently fucks me. From this position I can see perfectly what he is doing as his cock slides in and out of me."
    "It's not the most comfortable of positions, but the guy likes it so I try to relax and enjoy the feeling of him fucking me."
    "I feel so vulnerable tied up like this. His cock in my pussy and his hands on my hips, making sure to push deep into me."
    if not numgen(0,4) and not acc.anus:
        jump whore_street_sex_tied_laying_sex_anal_switch
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "I lay here spread eagle, taking everything he pumps inside me."
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    show sb_onback look_up pout with dissolve
    pc "Mmm, admiring your work?"
    tempname.name "It's a shame I can only fill you up once."
    pc "I'm a whore, fill me up as many times as you can afford."
    tempname.name "Haha."
    show sb_onback no_sex with dissolve
    tempname.name "Phew."
    jump whore_street_sex_tied_laying_sex_end

label whore_street_sex_tied_laying_sex_anal_switch:
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

label whore_street_sex_tied_laying_sex_anal:
    "Anal branch"
label whore_street_sex_tied_laying_blindgag_leave:

label whore_street_sex_tied_laying_cum_blowdeep:
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
    jump whore_street_sex_tied_laying_sex_end

label whore_street_sex_tied_laying_sex_end:
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
        pc "You could help."
        tempname.name "And miss the view of you struggling around?"
        $ working(5)
        show sb_onback relax relaxed with dissolve
        "Eventually I manage to get my myself untied."
        jump whore_street_sex_end

    tempname.name "Okay."
    "He leans over and unlocks some of the clasps, leaving me a bit of room to unlock the rest myself."
    "He sits there with a stupid grin on his face while watching me trying to untie myself."
    pc "You could help."
    tempname.name "And miss the view of you struggling around?"
    show sb_onback relax relaxed with dissolve
    "Eventually I manage to get my myself untied."
    pc "Have a last look."
    jump whore_street_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
