label school_dance_show_picker:
    if renpy.has_label("school_dance_show_" + str(school_dance_quest_show_count)):
        jump expression "school_dance_show_" + str(school_dance_quest_show_count)
    else:
        jump school_dance_show_repeatable_start


label school_dance_show_ask:
    pc "Should I join the [dancet] tonight?"
    menu:
        "Yes, join the girls.":
            if school_dance_quest_show_count >= 2:
                if not school_dance_has_main_clothes():
                    call school_dance_show_get_missing_clothes from _call_school_dance_show_get_missing_clothes
                $ school_dance_set_clothes()
                if not loc(loc_school_locker_girls):
                    $ walk(loc_school_locker_girls)
                if player.hygiene <= 50:
                    $ shower_scene("work")
                else:
                    $ pc_dress_event("work")
                if school_dance_missing_clothes():
                    if school_dance_missing_clothes() == "pants":
                        show sb_pose_upskirt with dissolve
                        pcm "Ugh, missing my underwear..."
                        pcm "Hope no one notices."
                        hide sb_pose_upskirt with dissolve
                    elif school_dance_missing_clothes() == "bra":
                        pcm "Missing my bra, hope they don't bounce around too much."
                    elif school_dance_missing_clothes() == "socks":
                        pcm "Don't have my tights..."
                        pcm "Oh well, they aren't that important."
            else:


                if not loc(loc_school_locker_girls):
                    $ walk(loc_school_locker_girls)
                if player.hygiene <= 50:
                    $ shower_scene("sport")
                else:
                    $ pc_dress_event("sport")

            jump school_dance_show_picker
        "Not today, I have other plans.":

            if player.hygiene <= 50:
                if not loc(loc_school_locker_girls):
                    $ walk(loc_school_locker_girls)
                $ shower_scene("daily")

            jump travel

label school_dance_show_get_missing_clothes:
    pcm "I don't have all my stuff. Hopefullt [svet.nname] has spares."
    "I look into the dance locker for replacements."
    pcm "There we go."
    $ wardrobe.take(item_bottom_13)
    if school_dance_quest_show_count >= 11:
        $ wardrobe.take(item_top_19)
    else:
        $ wardrobe.take(item_top_20)
    return

label school_dance_show_picker_cheat:
    "Warning. This cheat will not adjust the time. Normally you would start this event at around 3pm. Using this cheat will not use the correct time of day backgrounds."
    "It also bypasses stat checks so there is a chance you may be too tired to do this event properly."
    "Close the cheat menu now."
    $ walk(loc_school_locker_girls)
    jump school_dance_show_ask
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
