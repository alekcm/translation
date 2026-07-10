default sleep_oversleep = False
default sleep_gavebirth = False

label bedroom_nap:
    $ go_sleep_prompt = False
    $ player.eye = 3
    $ tab_top = "home"
    $ pc_dress()
    $ dialouge = renpy.random.choice([
    "I decide to lay down and have a nap.",
    "I change into my sleeping clothes and lay down on the bed.",
    "After changing into my pyjamas, I lay down on the bed to doze off."
    ])
    "[dialouge]"
    $ time_sleep(60)
    jump bedroom_wake

label bedroom_sleep:
    if player.tired >= 80:
        pc "I'm not really tired. If I just want to relax I should go and do something else."
        jump bedroom_screen
    $ go_sleep_prompt = False
    if "home" in tab_top:
        $ dialouge = renpy.random.choice([
        "You get into bed and close your eyes.",
        "You lay down on the bed and close your eyes."
        ])
        "[dialouge]"
    elif not home.inappropriate:
        $ tab_top = "home"
        $ pc_dress()
        $ dialouge = renpy.random.choice([
        "I change into my pyjamas and get into bed.",
        "I change into my sleeping clothes and lay down on the bed.",
        "After changing into my pyjamas I lay down on the bed and close my eyes."
        ])
        "[dialouge]"
    else:
        $ player.face_worried()
        pc "Ugh, I don't really have anything I can sleep in... Ah whatever, will just sleep in this."
    $ player.eye = 3
    show screen blackout(100) with dissolve
    pause 0.5
    $ time_sleep_hour()
    jump bedroom_sleep_loop

label bedroom_sleep_loop:

    if player.tired > 96:
        jump bedroom_wake

    elif t.hour == alarm_hour - 1 and t.minute >= 45:
        $ time_round_to_hour_sleep()
        jump bedroom_sleep_loop
    elif t.hour == alarm_hour and t.minute == 0:
        if player.drunk + player.high > 60:
            $ time_sleep(15)
            jump bedroom_sleep_loop
        elif player.tired <= 50:
            call bedroom_wake_alarm from _call_bedroom_wake_alarm

            if t.wkday in weekends:
                menu:
                    "It's the weekend. I can sleep some more.":
                        show screen blackout(100) with dissolve
                        $ time_sleep(15)
                        jump bedroom_sleep_loop
                    "Get up.":
                        jump bedroom_wake
            elif not calander_holiday == "":
                menu:
                    "It's a holiday today. I can sleep some more.":
                        show screen blackout(100) with dissolve
                        $ time_sleep(15)
                        jump bedroom_sleep_loop
                    "Get up.":
                        jump bedroom_wake
            else:

                menu:
                    "Be late for school and sleep some more.":
                        show screen blackout(100) with dissolve
                        $ time_sleep(15)
                        jump bedroom_sleep_loop
                    "Get up.":
                        jump bedroom_wake
        else:

            call bedroom_wake_alarm from _call_bedroom_wake_alarm_1
            jump bedroom_wake
    else:


        $ time_sleep(15)
        $ rand_choice = WeightedChoice([
        ("bedroom_sleep_loop", 100),
        ("bedroom_wake_morning_sickness", If (player.days_pregnant > 15 and not player.drunk > 70, 5,0)),
        ("bedroom_wake_drunk_sickness", If (player.days_pregnant > 15 and player.drunk > 70, 5,0)), 
        ("bedroom_wake_drunk_sickness", If (player.drunk > 70, 5,0)),
        
        ])
        jump expression rand_choice

label bedroom_wake_alarm:

    $ player.face_shock()
    $ player.inhib_sleep()
    hide screen blackout with hpunch
    $ player.face_angry()
    $ player.eye = 2
    pc "Uggggg... Damn alarm..."
    return

label bedroom_wake:
    if renpy.get_screen("blackout"):
        hide screen blackout with dissolve
    $ player.face_normal()

    if player.drunk or player.high:
        $ player.inhib_sleep()
        $ player.face_normal()
        if (player.drunk + player.high) > 15:
            $ player.face_puke()
            pc "Ugh, I'm gonna be feeling the effects of all that booze..."


    elif player.tired < 60:
        $ player.face_sad()
        pc "Ugh, I could do with staying in bed."


    jump travel

label bedroom_wake_morning_sickness:
    hide screen blackout with hpunch
    $ player.face_normal()
    $ player.mouth = 10
    pc "Fuck, I feel sick."
    $ walk(loc_bathroom)
    $ player.face_puke2()
    pc "Bleeeeh!"
    $ player.face_puke()
    pc "..."
    pc "Ugh."
    $ player.face_normal()
    if player.preg_knows == False and t.day < 50:
        pc "What the hell. I know it's a new body and all, but randomly puking?"
    elif player.preg_knows == False:
        pc "Ughhhh... This is new... Never randomly puked before. Might have to report it to [nik.name]."
    else:
        pc "Uff, suppose this is something I should have expected."
    jump travel

label bedroom_wake_drunk_sickness:
    hide screen blackout with hpunch
    $ player.face_normal()
    $ player.mouth = 10
    pc "Fuck, I feel sick."
    $ walk(loc_bathroom)
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
