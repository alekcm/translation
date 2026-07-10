init python:
    def check_pc_has_clothes():
        
        for key, value in wardrobe.inv:
            clothes_type = getattr(key, "clothes_tab")
            if c.cansee_breasts and clothes_type in ["top", "outfit", "bra", "bsuit"]:
                return True
            elif c.cansee_vag and clothes_type in ["bottom", "outfit", "pants", "bsuit"]:
                return True
        else:
            return False

label leave_house_checks:
    $ temp_var_1 = False
    call leave_house_checks_call from _call_leave_house_checks_call
    $ walk(temp_var_9, trans=If(temp_var_1, True, False))
    jump travel

label leave_house_checks_call:
    if player.tired <= 10:
        $ player.face_worried()
        pcm "I'm so tired that if I go out now I will end up falling asleep on the floor somewhere. So I had better stay at home."
        jump travel
    elif player.tired <= 20:
        $ player.brow = 3
        pcm "I probably shouldn't stay out for too long since I am so tired. Don't want to fall asleep on a bench or something."
        $ player.face_normal()

    if player.mood < 20:
        if t.hour in (6,7,8,9) and t.wkday in weekdays and calander_holiday == "" and not dis_school.locked:
            pcm "Uff, I feel so shitty and to make things worse, I have to go to school..."
        else:
            pcm "I hope I can find something to cheer me up out here."

    if c.exposed:
        if not check_pc_has_clothes():
            pcm "Fuck, I don't even have enough clothes to wear and I need to go out..."
        elif perk_exhib_weight(0) or perk_exhib_weight(1) or perk_exhib_weight(2):
            pcm "I can't go out there with my bits out..."
            if t.timeofday == "night":
                if not "leave_house_nude_warning" in perk_exhibitionist.list:
                    menu:
                        "It's night, no one will see me":
                            $ add_to_list(perk_exhibitionist.list, "leave_house_nude_warning")
                            return
                        "Stay home":
                            jump travel
                else:
                    pcm "I doubt anyone will see me at this time though."
                    return

            jump travel


    if "home" in tab_top or "temp" in tab_top:
        $ temp_var_1 = loc_cur
        if dis(dis_home):
            $ temp_var_1 = loc_bedroom

        if t.hour in (6,7,8,9) and school.inappropriate == False and t.wkday in weekdays and calander_holiday == "":
            pcm "Better change into my uniform before heading out."
            $ pc_dress_event("school", temp_var_1)
        elif t.hour in dark and party.inappropriate == False and player.confidence >= 40:
            pcm "Better change before heading out."
            $ pc_dress_event("party", temp_var_1)
        elif daily.inappropriate == False:
            pcm "Better change before heading out."
            $ pc_dress_event("daily", temp_var_1)
        else:
            $ walk(temp_var_1)
            $ player.face_worried()
            pcm "I can't go out wearing my pyjamas and I don't have an outfit set that I can go out in."
            menu:
                "Open my wardrobe":
                    $ player.face_normal()
                    call screen wardrobe_screen

                "Wear my school uniform" if school.inappropriate == False:
                    $ player.face_normal()
                    $ pc_dress_event("school", temp_var_1)

                "Wear my sports clothes" if sport.inappropriate == False:
                    $ player.face_normal()
                    $ pc_dress_event("sport", temp_var_1)
                "Just stay at home":

                    $ player.face_normal()
                    jump travel

    return


label leave_school_changingroom_checks_pool:
    $ loc_want = "school_pool"
    jump leave_school_changingroom_checks

label leave_school_changingroom_checks_gym:
    $ loc_want = "school_gym"
    jump leave_school_changingroom_checks

label leave_school_changingroom_checks_field:
    $ loc_want = "school_field"
    jump leave_school_changingroom_checks


label leave_school_changingroom_checks:
    jump travel
    if loc_to == "school_locker_old":
        jump expression loc_want + "_arrival"
    if c.exposed == True:
        $ player.face_worried()
        pc "I should put something more appropriate on."
        $ player.face_normal()
        jump travel
    elif "swim" in tab_top and loc_want != "school_pool":
        $ player.face_worried()
        pc "I can't walk around school wearing my swimsuit."
        $ player.face_normal()
        jump travel
    elif tab_top != "swim" and loc_want == "school_pool":
        $ player.face_worried()
        pc "I need to wear my swimming suit before entering the pool."
        $ player.face_normal()
        jump travel
    elif "home" in tab_top:
        $ player.face_worried()
        pc "I can't go around wearing my home clothes."
        $ player.face_normal()
        jump travel
    else:
        jump expression loc_want + "_arrival"

label force_outfit_swim:
    pcm "I need to change into my swimwear first."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
