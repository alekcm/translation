init python:
    def bed_sleep_pinkroom_loop_funtion():
        global temp_var_1
        temp_var_1 = 0
        number = numgen(0,2)
        for _ in range(number):
            if not numgen(0, 2):
                temp_var_1 += 1
            if numgen() and not acc.anus:
                player.sex_anal(tempname, quest_temp)
                player.sex_cum(tempname, "anal", quest_temp)
            else:
                player.sex_vag(tempname, quest_temp)
                player.sex_cum(tempname, "inside", quest_temp)
        player.sex_hideaction()

label bed_sleep_pinkroom_loop:
    $ bed_sleep_pinkroom_loop_funtion()
    jump bed_sleep_loop

label bed_sleep_pinkroom_wake_sex:
    $ player.sex_vag(tempname, quest_temp)
    $ player.sex_hideaction()
    show sb_onback hump worried
    $ player.face_shock()
    hide screen blackout with hpunch
    $ player.face_angry()
    $ player.eye = 2
    "I wake up with a start and realise someone is having sex with me."
    show sb_onback look_up
    pc "Couldn't have waited until I at least wake up?"
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "inside", quest_temp)
    pc "Right... Good morning to you too..."
    show sb_onback no_sex with dissolve
    "I start wriggling my way from under him. He gets the hint and starts to dress and leave."
    hide sb_onback with dissolve
    pc "..."
    pc "Did he at least leave a ticket?"
    if not type(temp_var_1) == int:


        $ temp_var_1 = 0
    if numgen():
        $ temp_var_1 += 1
    if temp_var_1:
        if temp_var_1 == 1:
            pcm "Ah, here we go."
        else:
            pcm "Hmm, more than one here. Did I get some while I was asleep?"
        $ inv.take(item_pinkticket, temp_var_1)
    else:
        pcm "No, nothing..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
