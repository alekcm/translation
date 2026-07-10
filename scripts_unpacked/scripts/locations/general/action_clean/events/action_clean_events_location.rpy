label action_clean_event_toilet_1:
    pcm "Please don't be anything weird in the toilets."
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pcm "Nasty fuckers."
    jump action_clean_event_picker

label action_clean_event_toilet_2:
    pcm "Fuck, this place reeks..."
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pcm "Ugh, I'm going to need a shower after this..."
    jump action_clean_event_picker

label action_clean_event_bathroom_1:
    pcm "Dirty mirror, floor, probably toilet as well..."
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pcm "Someone else needs to clean this place next time..."
    pcm "Who am I kidding, it will be me again."
    jump action_clean_event_picker

label action_clean_event_bedroom_1:
    pcm "Might as well give my own room a clean since I am here."
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pcm "[oskar.name] hopefully won't complain that I cleaned my own room to lower the rent."
    jump action_clean_event_picker


label action_clean_event_motel_1:
    $ male_npc_create()
    $ tempname = motelman
    show male_generic nude at right1 with dissolve
    $ player.face_shock()
    pc "Ah, sorry!"
    if not numgen(0,3):
        $ player.set_whore_price(0)
        tempname.name "Don't go, suck it for £[player.soldprice]?"
        if player.check_whore_agree_choice(request="oral"):
            jump whore_sex_start
        else:
            pc "Sorry mate, I'm just gonna clean."
            jump action_clean_event_picker
    jump action_clean_event_picker

label action_clean_event_motel_2:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    guy "Nice room service."
    pc "Don't mind me..."
    jump action_clean_event_picker

label action_clean_event_motel_3:
    $ male_npc_create()
    $ tempname = motelman
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    $ renpy.scene()
    show sb_standbehind
    with hpunch
    tempname.name "Nice. Bitch at the front sent me some fun."
    pc "Get off. I am the cleaner."
    if player.check_fight():
        hide sb_standbehind with hpunch
        "I struggle out of his arms and leave the room."
        jump action_clean_event_picker
    else:
        if numgen():
            tempname.name "Not here selling yourself?"
            if player.check_whore():
                pc "How much?"
                $ player.set_whore_price(0)
                tempname.name "£[player.soldprice] for you?"
                if player.check_whore_agree_choice():
                    jump whore_sex_start
                else:
                    pc "Sorry mate, I'm just gonna clean."
                    hide sb_standbehind with dissolve
                    jump action_clean_event_picker
        else:
            "I try to struggle off the guy but he isn't having it."
            if danger_gen(30,1) and player.check_victim():
                $ player.sex_forced(rapist)
                jump whore_street_sex_forced_attack_position
            else:
                tempname.name "Hmm, okay."
                hide sb_standbehind
                show male_generic nude at right1
                with dissolve
                tempname.name "Sorry darlin'. Thought you were sent fer me."
                pc "Sure..."
    jump action_clean_event_picker

label action_clean_event_motel_4:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    $ renpy.scene()
    with dissolve
    $ force_return = True
    call mira_whore_discover from _call_mira_whore_discover
    jump action_clean_event_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
