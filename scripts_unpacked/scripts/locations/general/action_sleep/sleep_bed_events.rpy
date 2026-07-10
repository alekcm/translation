define alarm_hour = 7
define alarm_set = False

label bed_nap:
    $ go_sleep_prompt = False
    if player.has_perk(perk_sucu):
        pcm "No point in sleeping since it won't help me."
        jump travel
    $ player.face_sleep()
    $ dialouge = renpy.random.choice([
    "I decide to lay down and have a nap.",
    "I close my eyes for a bit and let myself doze off.",
    "I lay and let my eyes close and doze off for a bit."
    ])
    "[dialouge]"
    $ time_sleep(60)
    jump travel

label bed_sleep:
    $ temp_var_2 = player.cum_amount()
    if player.has_perk(perk_sucu):
        pcm "No point in sleeping since it won't help me."
        jump travel
    elif player.tired >= 80:
        pc "I'm not really tired. If I just want to relax I should go and do something else."
        jump travel
    $ go_sleep_prompt = False
    $ player.drink_finish()
    if dis(dis_partyhouse):
        pcm "Should just sleep like this..."
    elif "home" in tab_top or c.nude:
        $ dialouge = renpy.random.choice([
        "I get into bed and close my eyes.",
        "I lay down on the bed and close my eyes."
        ])
        "[dialouge]"
    elif not (home.inappropriate and home2.inappropriate):
        $ pc_strip()
        $ pc_dress("home")
        if c.nude:
            $ dialouge = renpy.random.choice([
            "I strip off and get into bed.",
            "I take off my clothes and lay down on the bed.",
            "After stripping off I lay down on the bed and close my eyes."
            ])
            "[dialouge]"
        else:
            $ dialouge = renpy.random.choice([
            "I change into my pyjamas and get into bed.",
            "I change into my sleeping clothes and lay down on the bed.",
            "After changing into my pyjamas I lay down on the bed and close my eyes."
            ])
            "[dialouge]"
    else:
        $ player.face_worried()
        pc "Ugh, I don't really have anything I can sleep in... Ah whatever, will just sleep in this."
    $ player.face_sleep()
    pause 0.1
    show screen blackout(100) with dissolve
    pause 0.5
    $ time_sleep_hour()
    jump bed_sleep_loop

label bed_sleep_loop:
    if not renpy.get_screen("blackout"):
        $ player.eye = 3
        show screen blackout() with dissolve
        pause 0.5
    if "pc_is_tied_up" in dani.list:
        $ time_sleep(numgen(15,60))
        jump dani_bedroom_tiedup_sleep_loop_picker
    $ renpy.scene()

    if player.tired > 96:
        jump bed_wake

    elif t.hour == alarm_hour - 1 and t.minute >= 45 and alarm_set:
        $ time_round_to_hour_sleep()
        jump bed_sleep_loop
    elif alarm_set and t.hour == alarm_hour and t.minute == 0:
        if player.drunk + player.high > 60:
            $ time_sleep(15)
            jump bed_sleep_loop
        elif player.tired <= 50:
            call bed_wake_alarm from _call_bed_wake_alarm

            menu:
                "Go back to sleep.":
                    $ time_sleep(5)
                    jump bed_sleep_loop
                "Get up":




                    jump bed_wake
        else:
            call bed_wake_alarm from _call_bed_wake_alarm_1
            jump bed_wake
    else:
        if not "men_amount" in loc_motel_room.dict:
            $ loc_motel_room.dict["men_amount"] = 0

        $ time_sleep(15)
        jump expression WeightedChoice([
        
        ("bed_sleep_loop", 100),

        
        ("bed_wake_morning_sickness", If (player.days_pregnant > 15 and not player.drunk > 70, 1,0)),
        ("bed_wake_drunk_sickness", If (player.days_pregnant > 15 and player.drunk > 70, 1,0)), 
        
        
        ("bed_wake_drunk_sickness", If (player.drunk > 70, 1,0)),

        
        ("bed_wake_jaylee_sex_picker", If (((t.hour == 6 and t.minute >= 45) or (t.hour == 7 and t.minute <= 15)) and jaylee_here(), jaylee.lust, 0)),
        
        

        
        ("dani_sleepover_wake_morning_picker", If (t.hour == 6 and dani_here() and loc(loc_bedroom_dani), 1000, 0)),
        
        ("dani_sleepover_wake_sleep_picker", If (dani_here() and loc(loc_bedroom_dani) and dani.lust > 80 and dani.inv.qty(item_strapon) and dani_yan_value() > 60, (dani.lust * 4), 0)),

        
        ("bed_sleep_pinkroom_loop", If (loc(loc_motel_pinkroom) and player.tired <= 80, 200, 0)),
        ("bed_sleep_pinkroom_wake_sex", If (loc(loc_motel_pinkroom) and player.tired >= 35, 200, 0)),

        
        ("dance_party_sleep_loop", If (dis(dis_partyhouse) and (player.tired <= 60 or player.drunk > 50), 200, 0)),
        ("dance_party_wake_sex", If (dis(dis_partyhouse) and (player.tired >= 60 or player.drunk < 40) and t.hour in (21,22,23,0,1,2,3,4,5), 200, 0)),

        
        ("random_event_generic_allure_flirt_motel_sleep_loop", If (loc_cur.man_amount and (player.tired <= 60 or player.drunk > 50), 10 * loc_cur.man_amount, 0)),
        ("random_event_generic_allure_flirt_motel_sleep_wake", If (loc_cur.man_amount and (player.tired >= 60 or player.drunk < 40), 300, 0)),
        
        
        ("robin_talk_pub_leave_motel_morning", If (t.hour == 6 and robin_here() and not dis(dis_home), 1000, 0)),
        
        
        ("bed_sleep_slum_wake_1", If(loc(loc_highway_slum_home), 2, 0)),
        ("bed_sleep_slum_wake_2", If (neighbour.alive and loc(loc_highway_slum_home) and neighbour_here(loc_highway_slum_home) and "sex" in neighbour.list and "sex_time" in neighbour.dict and not abs(neighbour.dict["sex_time"] - t.minutes_total) <= 6, 30, 0)), 
        ("bed_sleep_slum_wake_3", If(loc(loc_highway_slum_home), 2, 0)),
        ("bed_sleep_slum_wake_4", If(loc(loc_highway_slum_home), 5, 0)),
        
        
        
        ])

label bed_wake_alarm:

    $ player.face_shock()
    hide screen blackout with hpunch
    $ player.face_angry()
    $ player.eye = 2
    pc "Uggggg... Damn alarm..."
    return

label bed_wake:
    $ player.inhib_sleep()
    $ player.face_sleep()
    if renpy.get_screen("blackout"):
        hide screen blackout with dissolve
    $ player.face_normal()
    if player.drunk or player.high:
        $ player.face_normal()
        if player.has_perk(perk_hangover):
            $ player.face_puke()
            pcm "Ugh, I'm gonna be feeling the effects of all that booze..."
    elif player.tired < 60:
        $ player.face_sad()
        pcm "Ugh, I could do with staying in bed."
    if loc(loc_motel_pinkroom) and temp_var_1:
        pcm "Hmm, there are some tickets here. Did people pay for me while I was asleep?"
        $ inv.take(item_pinkticket, temp_var_1)
    elif player.cum_amount() > temp_var_2:
        $ player.face_meek()
        pcm "Ugh, I knew I should have slept somewhere better. Damn perverted men."
        if player.cum_locations["cum_vagin"]:
            pcm "I can even feel it leaking out of me..."
            if player.has_perk(perk_preg_notwant) and not player.has_perk(perk_period):
                pcm "Should probably look to get a pill or something in case I end up pregnant."
            elif player.cum_locations["cum_assin"]:
                pcm "Leaking out my ass as well."

    jump travel

label bed_wake_morning_sickness:
    hide screen blackout with hpunch
    $ player.face_normal()
    $ player.mouth = 10
    pc "Fuck, I feel sick."
    if loc_cur == loc_bedroom:
        $ walk(loc_bathroom)
    elif loc_cur == loc_junk_trailer:
        $ walk(loc_junk_2)
    $ player.face_puke2()
    pc "Bleeeeh!"
    $ player.face_puke()
    pc "..."
    pc "Ugh."
    $ player.face_normal()
    if not player.preg_knows and t.day < 50:
        pc "What the hell. I know it's a new body and all, but randomly puking?"
    elif not player.preg_knows:
        pc "Ughhhh... This is new... Never randomly puked before. Might have to report it to [nik.name]."
    else:
        pc "Uff, suppose this is something I should have expected."
    jump travel

label bed_wake_drunk_sickness:
    hide screen blackout with hpunch
    $ player.face_normal()
    $ player.mouth = 10
    pc "Fuck, I feel sick."
    if loc_cur == loc_bedroom:
        $ walk(loc_bathroom)
    elif loc_cur == loc_junk_trailer:
        $ walk(loc_junk_2)
    $ player.face_puke2()
    pc "Bleeeeh!"
    $ player.face_puke()
    pc "..."
    pc "Ugh."
    $ dialouge = renpy.random.choice([
    "Ugg, I should be more careful with how much I drink...",
    "Uhhhhhh. Never again...",
    "Ahhhh spinnnning...",
    ])
    pc "[dialouge]"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
