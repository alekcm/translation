label robin_talk_pub_leave_motel:
    $ walk(loc_motel, trans=False)
    $ renpy.scene()
    if renpy.get_screen("blackout"):
        hide screen blackout with dissolve
    show robin at right5 with dissolve
    robin.name "The guys got us a room, let's go."
    hide robin with dissolve
    $ walk(loc_motel_room2)
    $ male_npc_create_all()
    show male_generic at right1 with dissolve
    show robin at left1
    show male2_generic at right2
    with dissolve
    tempname.name "This is going to be fun."
    robin.name "I hope so."
    $ renpy.scene()
    with dissolve
    $ player.sex_man_amount = numgen(5,20)
    $ loc_motel_room2.man_amount = player.sex_man_amount
    $ event_end_interrupt_label = "robin_talk_pub_leave_motel_sex_end"
    jump whore_street_sex_group_start_picker

label robin_talk_pub_leave_motel_sex_end:
    if player.tired < 20 or player.drunk > 80:
        $ pc_set_temp_outfit()
        if not renpy.showing("sb_onback"):
            $ renpy.scene()
            show sb_onback relaxed
            with dissolve
        else:
            show sb_onback relaxed
            with dissolve
        if robin_here():
            "I am exhausted after all that and lay down to rest and I see [robin.name] is jut as worn out as I am."
            show sb_onback robin_lay_open look_right with dissolve
            robin.name "That was fun."
            pc "Mmmmm..."
            if loc_cur.man_amount:
                robin.name "Guy's better not complain if we steal the bed."
                show sb_onback robin_sleep with dissolve
            "I close my eyes and start to drift off."
            show sb_onback look_closed with dissolve
            $ player.eye = 3
            show screen blackout() with dissolve
            jump bed_sleep_loop
        else:
            "I can barely keep my eyes open after all that, and slowly drift off to sleep while in bed with the guy."
            $ player.eye = 3
            show screen blackout() with dissolve
            jump bed_sleep_loop
    else:

        if robin_here():
            pcm "Uff, looks like the guys are worn out."
            "I try to catch my breath for a bit then slowly wobble to my feet."
            $ renpy.scene()
            with dissolve
            show robin nude cum at right6 with dissolve
            robin.name "Ugh, I am sore all over."
            pc "And leaking."
            robin.name "I know. I can feel them running down my legs."
            if t.hour == 5:
                pc "looks like the guys are heading off."
                show male3_generic at right1 with dissolve
                tempname.name "Sorry girls, work and all that. It was fun though."
                pc "It was, c'ya."
                hide male3_generic with dissolve
                robin.name "I'm gonna head off home now. You coming?"
                menu:
                    "Yeah, let's go":
                        pc "Sure, let's go."
                        $ pc_dress_slow()
                        $ remove_from_list(robin.list, "slut_outing")
                        show robin standard with dissolve
                        robin.name "Feel so dirty heading home covered in cum."
                        pc "Heh, yeah."
                        jump robin_goto_home
                    "No, you go ahead":

                        pc "Think I'll have a shower first. You not going to?"
                        robin.name "Na, more fun going home like this. I'll shower when I get back."
                        show robin outing with dissolve
                        pc "You whore."
                        robin.name "Heh, have fun."
                        hide robin with dissolve
                        $ remove_from_list(robin.list, "slut_outing")
                        jump travel

            robin.name "What do you want to do now?"
            pc "Not sure, guys are worn out but I am not tired."
            robin.name "Want to head home together?"
            menu:
                "Sure, let's go home":
                    $ pc_dress_slow()
                    $ remove_from_list(robin.list, "slut_outing")
                    show robin standard with dissolve
                    robin.name "Feel so dirty heading home covered in cum."
                    pc "Heh, yeah."

                    jump robin_goto_home
                "No, I'll do something else":

                    pc "I don't think I will be heading home."
                    robin.name "Okay, then I'll just hang out with these guys."
                    $ pc_dress_slow()
                    pc "Have fun."
                    robin.name "You too."
                    hide robin with dissolve
                    $ walk(loc_motel)
                    jump travel
        else:
            jump pub_drink_motel_sex_end

label robin_talk_pub_leave_motel_morning:
    $ remove_from_list(robin.list, "slut_outing")
    show robin at right6
    $ player.eye = 3
    if player.tired < 60:
        show screen blackout(50) with dissolve
        robin.name "Wake up!!!"
        $ player.face_annoyed()
        pc "Ugh..."
        hide screen blackout with dissolve
        pc "What?"
    else:
        $ player.face_neutral()
        hide screen blackout with dissolve
    robin.name "It's morning [name]."
    if loc_cur.man_amount:
        robin.name "I'm heading home now. Unless you want to stay with these guys, get dressed."
    else:
        robin.name "I'm heading home now. The guys have already left."
    pc "Ugh..."
    if player.tired < 80:
        menu:
            "Get up":
                $ NullAction()
            "Go back to sleep":

                pc "You go, I'll stay here."
                robin.name "Okay, c'ya."
                hide robin with dissolve
                "I close my eyes and go back to sleep."
                jump bed_sleep_loop

    pc "Okay..."
    pc "Ugh... Still suffering from last night."
    robin.name "Yeah, same."
    $ pc_dress_slow("party")
    pc "Okay, I'm ready."
    hide robin with dissolve
    $ walk(loc_cur.get_district().hub)
    show robin at left1 with dissolve
    robin.name "Wanna get the bus home together?"
    menu:
        "Yeah, let's go":
            jump robin_goto_home
        "No, you go ahead":
            robin.name "Okay, be safe."
            hide robin with dissolve
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
