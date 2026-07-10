label action_sleep_jump:
    if player.has_perk(perk_sucu):
        show screen blackout(50) with dissolve
        $ player.face_shock()
        hide screen blackout with hpunch
        $ player.face_annoyed()
        pcm "Ugh! I am exhausted, but sleeping won't help..."
    elif loc_cur.get_district() == dis_home or loc(loc_residential):
        pcm "Ugh! I am exhausted. I need to just go to bed."
        $ walk(loc_bedroom)
        jump bed_sleep
    elif loc_cur.get_district() == dis_junkyard and not loc_junk_trailer.locked:
        pcm "Ugh! I am exhausted. I need to just go to bed."
        $ walk(loc_junk_trailer)
        jump bed_sleep
    elif dis(dis_slum) and loc_highway_slum_home.open():
        pcm "Ugh! I am exhausted. I need to just go to bed."
        $ walk(loc_highway_slum_home)
        jump bed_sleep
    elif dis_cur == dis_haven:
        jump haven_tired_trigger
    elif loc(loc_motel_pinkroom) or loc(loc_motel_shower) and loc_from == loc_motel_pinkroom:
        pcm "Ugh! I am exhausted. I need to just go to bed."
        $ walk(loc_motel_pinkroom)
        jump bed_sleep
    elif dis(dis_partyhouse):
        pcm "Ugh! I am exhausted. I really should have got some sleep before coming here."
        $ walk(loc_party_bedroom1)
        jump bed_sleep
    elif loc_cur in dis_misc.locs:
        pcm "Ugh! I am exhausted. I need to rest for a bit."
    else:
        pcm "Ugh! I am exhausted. I need to find somewhere to rest for a bit."
    if inv.qty(item_wakeup):
        menu:
            "Take some Wakeup":
                call item_wakeup_action from _call_item_wakeup_action_1
                jump travel
            "Find somewhere to sleep":
                $ NullAction()
    if not loc_cur in dis_misc.locs:
        $ travel_sleep_location()
        pause 0.5
        pcm "Hmm, somewhere a bit safer..."
        $ travel_isolate()
        pcm "Should be quiet enough here."
    "I find somewhere to curl up and it's not long before I drift off."
    $ player.face_sleep()
    show screen blackout() with dissolve
    $ time_sleep_rough()
    pause 1
    $ rand_choice = WeightedChoice([
    ("sleep_rough_wake_common", 100),
    ("sleep_rough_wake_rare", 25),
    ("sleep_rough_wake_vrare", If(danger_weight(), 5, 0)),
    ("random_event_generic_wakedrunk", If(player.check_drunk(5, notif=False), player.drunk, 0)),
    ])
    jump expression rand_choice

label world_tired_trigger_home:
    if player.tired < 3:
        jump action_sleep_jump
    elif player.tired < 10 and go_sleep_prompt == False:
        "I am so tired, had better go to bed soon."
        $ go_sleep_prompt = True
    jump travel


label world_tired_trigger:
    jump action_sleep_jump


label sleep_rough_wake_common:
    $ rand_choice = WeightedChoice([
    ("sleep_rough_wake_common_1", 100),
    ("sleep_rough_wake_common_2", 100),
    ("sleep_rough_wake_common_3", If(player.drunk > 70, player.drunk, 0)),
    ("sleep_rough_wake_common_4", 100),
    ("sleep_rough_wake_common_5", 100),
    ])
    jump expression rand_choice



label sleep_rough_wake_common_1:
    hide screen blackout with dissolve
    pause 0.5
    $ player.face_annoyed()
    pcm "Ugh, please let's not do that again."
    jump travel

label sleep_rough_wake_common_2:
    hide screen blackout 
    $ player.face_shock()
    with hpunch
    pc "Ah!!"
    $ player.face_worried()
    pc "..."
    pause 0.5
    $ player.face_annoyed()
    pcm "Ugh, please let's not do that again."
    jump travel

label sleep_rough_wake_common_3:
    hide screen blackout 
    $ player.face_puke()
    pc "Ubb!!"
    $ player.face_puke2()
    pc "Bleeeeeh!"
    $ player.face_worried()
    pc "..."
    pause 0.5
    $ player.face_annoyed()
    pcm "Fuck. Drunk too much..."
    jump travel

label sleep_rough_wake_common_4:
    hide screen blackout with dissolve
    $ player.face_pain()
    pc "Ugh, my neck is killing me. This was not comfortable at all."
    jump travel

label sleep_rough_wake_common_5:
    hide screen blackout with dissolve
    pause 0.5
    $ player.face_pain()
    pcm "Ugh, what the hell. My clothes are a mess and I stink. Let's not do this again please."
    jump travel


label sleep_rough_wake_rare:
    $ randomnum = renpy.random.randint(10,40)
    $ player.add_mood(-randomnum)
    $ randomnum = renpy.random.randint(1,5)
    if randomnum == 5:
        $ pc_strip()
        $ player.face_cry()
        pause 3
        hide screen blackout with dissolve
        pc "Fuck, What the fuck! I go to sleep for 5 minutes and wake up without a scrap of clothing on!"
        pc "*SOB* *SOB*"
    else:

        if c.skirt == True and c.pants > 0:
            $ c.pants = 0
            pause 3
            hide screen blackout with dissolve
            pc "What the hell, someone stole my pants while I was asleep..."
            pc "I hope thats all they did. Doesn't feel like I was raped but they might have taken photos or something..."
        elif c.bra > 0 and c.top > 0:
            $ c.top = 0
            pause 3
            hide screen blackout with dissolve
            pc "What the hell, my top is gone! Fuck!"
        elif c.pants > 0 and c.bottom > 0:
            $ c.bottom = 0
            pause 3
            hide screen blackout with dissolve
            pc "What the fuck! Someone took my clothes. Damn, looks like if i slept any longer it would be more than my clothes gone."
            if player.vvirgin:
                pc "My virginity would almost certainly be claimed by whoever took my trousers."
        else:
            $ c.top = 0
            $ c.outfit = 0
            $ c.bottom = 0
            pause 3
            hide screen blackout with dissolve
            pc "Fuck! Someone stole all my clothes..."
            pc "*SOB*"
            if c.exposed == True:
                pc "Didn't even wear proper underwear either so now I am totally exposed."

    pc "I can't be walking around like this. I had better try to get home without anyone seeing me."
    jump travel

label sleep_rough_wake_vrare:
    jump expression WeightedChoice([
    ("sleep_rough_wake_vrare_1", 100),
    ("sleep_rough_wake_vrare_2", If(dis(dis_truckstop, from_check=True), 100, 0)),
    ])

label sleep_rough_wake_vrare_1:
    $ travel_isolate(trans=False)
    $ randomnum = renpy.random.randint(20,50)
    $ player.add_mood(-randomnum)
    $ player.face_cry()
    pause 1
    if c.skirt == True and c.pants > 0:
        $ c.pants = 0
        $ player.sex_cum(rapist, "pullout")
        $ player.sex_hideaction()
        hide screen blackout with dissolve
        pc "What the hell, someone stole my pants while I was asleep..."
        pc "I hope thats all they did. Doesn't feel like I was raped but they might have taken photos or something..."
        pc "Shit! I'm all sticky... Did they really...?"
    elif c.bra > 0 and c.top > 0:
        $ player.sex_cum(rapist, "chest")
        $ player.sex_hideaction()
        $ c.top = 0
        hide screen blackout with dissolve
        pc "What the hell, my top is gone! Fuck!"
        pc "Ugh, what the hell, did some pervert really come on me?"
    elif c.pants > 0 and c.bottom > 0:
        $ player.sex_cum(rapist, "pullout")
        $ player.sex_hideaction()
        $ c.bottom = 0
        hide screen blackout with dissolve
        pc "What the fuck! Someone took my clothes. Damn, looks like if I slept any longer it would be more than my clothes gone."
        if player.vvirgin:
            pc "My virginity would almost certainly be claimed by whoever took my trousers."
        pc "Ugh shit. Is that really...?"
    else:
        $ c.top = 0
        $ c.outfit = 0
        $ c.bottom = 0
        $ player.sex_cum(rapist, "chest")
        hide screen cum_action
        hide screen blackout with dissolve
        pc "Fuck! Someone stole all my clothes... And did he come on me?"
        pc "*SOB*"
        if c.exposed == True:
            pc "Didn't even wear proper underwear either so now I am totally exposed."

    pc "I need to get home somehow..."
    jump travel

label sleep_rough_wake_vrare_2:
    if loc_motel_pinkroom.visited and (not numgen(0,5) or dis(dis_truckstop)):
        $ walk(loc_motel_pinkroom, trans=None)
        $ tempname = pinkroom_tiedtrain
        $ quest_temp = None
        $ renpy.show(renpy.random.choice(["sb_upsidedown vag up pain", "sb_doggy1 body_tied vag", "sb_onback hump worried look_up ah tied"]))
        $ pinkroom_customer_event_train_sex_sleep_loop_function(forced=True)
        $ player.add_mood(numgen(20, 50))
        $ inv.take(item_ballgag_locked)
        $ player.add_perk(perk_gagged_locked)
        $ pc_strip()
    else:

        $ travel_dump_location()
        $ tempname = guy_tiedtrain
        $ quest_temp = None
        show sb_doggy1 body_tied vag
        $ pinkroom_customer_event_train_sex_sleep_loop_function(forced=True)
        $ player.add_mood(numgen(20, 50))
        $ inv.take(item_ballgag_locked)
        $ player.add_perk(perk_gagged_locked)
        $ pc_strip()

    pause 1
    hide screen blackout with hpunch
    "I wake with a start and am confused about where I am. As why there seems to be a guy fucking me."
    pc "Something."
    pcm "What the fuck? What is in my mouth?"
    pc "Something."
    "I struggle about and realise I am tied up."
    pcm "How the fuck did this happen?"
    $ if_showing("sb_upsidedown", "closed", "sb_onback", "look_closed")
    $ player.sex_cum(tempname, "inside", quest_temp)
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    "The guy dismounts and dresses up. I had hoped he would untie me but no such luck."
    pcm "Fuck! I have no choice but to accept this..."
    $ player.sex_forced(tempname, quest_temp)
    $ temp_var_1 = 0
    jump pinkroom_customer_event_train_sex_loop

label sleep_rough_wake_drunk:
    $ randomnum = renpy.random.randint(1,5)
    $ npc_race = randomnum
    $ temp_var_1 = player.vvirgin
    $ player.sex_forced(rapist)
    $ player.sex_vag(rapist)
    $ pc_strip()
    show sb_assup closed frown worried sex
    $ player.eye = 3
    pause 1
    show screen blackout(50) with dissolve
    pc "Uuuugggggg..."
    show sb_assup squint sex with dissolve
    pc "Whhhhhhhaaaaaa..."
    rapist.fname "Ahhhh..."
    $ player.sex_cum(rapist, "inside")
    $ player.eye = 3
    rapist.fname "Ahhhaaaahhh........"
    show sb_assup closed sex with dissolve
    $ player.eye = 3
    pc "Oooowhaaaaaa..."
    show screen blackout(100) with dissolve
    $ time_sleep_rough()
    hide sb_assup
    pause 1
    hide screen blackout 
    $ player.face_shock()
    with hpunch
    pc "Ahhhhh..."
    pc "Fuck, Ahhhh! What the hell. My body is so fucking sore..."
    pc "Did...?"
    $ player.eye = 3
    pc "Ah fuck..."
    $ player.face_cry()
    if temp_var_1 == True:
        pc "Did I really lose my virginity to some shit while passed out?"
    pc "And where the fuck are my clothes...?"
    pc "*SOB* *SOB*"
    $ player.face_normal
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
