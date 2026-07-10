define school_field_soccer_intro = False
define school_field_running_intro = False

define school_random_event_returner = False
init python:

    def school_class_morning_active(): 
        if t.wkday in weekday and t.hour in irange(8,11) and calander_holiday == "":
            return True
        else:
            return False

    def school_class_lunch_active(): 
        if t.wkday in weekday and t.hour == 12 and calander_holiday == "":
            return True
        else:
            return False

    def school_class_gym_active(): 
        if t.wkday in weekday and t.hour == 13 and calander_holiday == "":
            return True
        else:
            return False

    def school_morning():
        
        if t.hour == 9:
            stroll(120 + (60 - t.minute))
            player.add_int()
            player.add_int()
            player.add_int()
        elif t.hour == 10:
            stroll(60 + (60 - t.minute))
            player.add_int()
            player.add_int()
        else:
            stroll(60 - t.minute)
            player.add_int()

    def school_lunch():
        relax(60 - t.minute)
        player.eat()

    def school_gym():
        exercise(60 - t.minute)

    def school_closing():
        if not school_open_hours():
            if school_soccer_quest_backentrance["used"] and (outside or loc_cur == loc_school_locker_old):
                return
            else:
                renpy.jump("school_closing")

    def school_class_hours():
        if t.hour in irange(8,14) and t.wkday in weekdays:
            return True
        else:
            return False

    def school_open_hours():
        if t.hour in irange(8,19):
            return True
        else:
            return False

    def school_people_present(): 
        if t.wkday in weekdays and calander_holiday == "" and t.hour in irange(8,16):
            return True
        else:
            return False



    def school_dance_trope_present(): 
        if (t.wkday in weekdays and t.hour in irange(14,16)) or (t.wkday == "Sunday" and t.hour in irange(10,16)):
            return True 
        else:
            return False

    def school_dance_girls_present(): 
        if (t.wkday in weekdays and (t.hour in irange(13,17) or t.hour in (9,10))) or (t.wkday in weekend and t.hour in irange(12,15)):
            return True
        else:
            return False



    def school_soccer_playing(): 
        
        if ((t.wkday in weekdays and t.hour in irange(14,16)) or (t.wkday in weekend and t.hour in irange(10,16))) and not weather_var >= 3 and not t.day in irange(school_soccer_quest_bully_remove["vanished_date"],school_soccer_quest_bully_remove["vanished_date"]+3):
            return True
        else:
            return False

    def school_soccer_hangingout(): 
        if t.wkday in weekdays:
            hangout_hours = (irange(14,23))
        else:
            hangout_hours = (irange(11,23))
        hangout_hours.append(0)
        hangout_hours.append(1)
        if t.hour in hangout_hours and not t.day in irange(school_soccer_quest_bully_remove["vanished_date"], school_soccer_quest_bully_remove["vanished_date"]+3) and not school_soccer_playing():
            return True
        else:
            return False

    def school_soccer_love_check(amount): 
        if max(drake.love, nate.love, dan.love) >= amount:
            return True
        else:
            return False

    def school_soccer_end_play(amount=1): 
        drake.add_love(amount)
        nate.add_love(amount)
        dan.add_love(amount)

    def school_soccer_hangout_offer(): 
        if sum([drake.love, nate.love, dan.love]) > 40 and school_soccer_quest_hangout_prompt == False:
            return True
        else:
            return False

    def school_soccer_dare_canplay(): 
        if not school_soccer_quest_betmatch["match_day"] == t.day:
            school_soccer_quest_betmatch["match_count"] = 0
            school_soccer_quest_betmatch["match_day"] = t.day
        
        school_soccer_quest_betmatch["match_count"] += 1
        
        if school_soccer_quest_betmatch["match_count"] > 2:
            return False
        else:
            school_soccer_quest_betmatch["match_total"] += 1
            return True

    def school_soccer_dare_win(amount=60): 
        check_amount = ((player.fitness + (player.allure / 10) + (player.confidence / 3)) - ((player.drunk / 3) + (100 - player.tired / 6)))
        if check_amount < 0:
            check_amount = 0
        randomnum = renpy.random.randint(0, amount)
        if check_amount > randomnum or randomnum < 3:
            return True
        else:
            return False

    def school_soccer_dare_should_undress(): 
        if not t.timeofday == "night":
            return False
        elif (school_soccer_quest_dare_clothes["nude"] == t.day or (school_soccer_quest_dare_clothes["nude"] == t.day+1 and t.hour in irange(0,5))) and not c.nude:
            return "nude"
        elif (school_soccer_quest_dare_clothes["topless"] == t.day or (school_soccer_quest_dare_clothes["topless"] == t.day+1 and t.hour in irange(0,5))) and not c.cansee_breasts:
            return "topless"
        elif (school_soccer_quest_dare_clothes["under"] == t.day or (school_soccer_quest_dare_clothes["under"] == t.day+1 and t.hour in irange(0,5))) and c.outerwear: 
            return "under"
        else:
            return False

    def school_soccer_pick_boy(condition=None): 
        global tempname, tempname2
        if condition == None:
            namelist = [drake,nate,dan]
            tempname = renpy.random.choice(namelist)
            namelist.remove(tempname)
            tempname2 = renpy.random.choice(namelist)
        elif condition == "lust":
            namelist = [drake,nate,dan]
            if drake.lust >= max(nate.lust, dan.lust):
                tempname = drake
            elif nate.lust >= max(drake.lust, dan.lust):
                tempname = nate
            else:
                tempname = dan
            namelist.remove(tempname)
            tempname2 = renpy.random.choice(namelist)
            return tempname.lust
        else:
            namelist = []
            for i in (drake,nate,dan):
                if getattr(i,condition): 
                    namelist.append(i)
            if not namelist: 
                return False
            else: 
                tempname = renpy.random.choice(namelist)
                namelist.remove(tempname)
                if namelist:
                    tempname2 = renpy.random.choice(namelist)
                return True

    def school_soccer_pick_new_boy(): 
        global tempname
        if tempname == drake:
            namelist = (nate,dan)
        elif tempname == nate:
            namelist = (drake,dan)
        else:
            namelist = (drake,nate)
        tempname = renpy.random.choice(namelist)

    def school_soccer_pick_other_boy(): 
        global tempname, tempname2
        namelist = [drake,nate,dan]
        namelist.remove(tempname)
        tempname2 = renpy.random.choice(namelist)

    def school_soccer_field_sex(): 
        if tempname.lust > 90 and not numgen(0,5) and school_soccer_quest_betmatch["can_challenge"] and t.timeofday == "night":
            renpy.jump("school_field_soccer_darematch_play_sex_picker")

    def school_soccer_isfather(father=None): 
        if father == None and (drake == player.preg_father_class or nate == player.preg_father_class or dan == player.preg_father_class):
            return True
        elif father == player.preg_father_class:
            return True
        else:
            return False

    def school_soccer_cansex(): 
        if sum([drake.love, nate.love, dan.love]) > 180 or all([drake.naughty, nate.naughty, dan.naughty]):
            return True
        else:
            return False

    def school_soccer_sex_rules(): 
        if not player.isbroken and school_field_soccer_sex_offer_rules == "broken":
            return False
        elif not player.has_perk([perk_preg_want, perk_creampie_lover]) and not player.preg_knows and school_field_soccer_sex_offer_rules == "inside":
            return False
        elif (player.isbroken or player.has_perk([perk_preg_want, perk_creampie_lover])) and school_field_soccer_sex_offer_rules == "careful":
            return False
        else:
            return True

    def school_soccer_tell_photos(): 
        if not "want_photos" in school_soccer_quest.conversation_topics and "nude" in school_photo_quest.list and renpy.random.randint(1,10) == 1:
            renpy.jump("school_field_soccer_hangout_conv_photo_private")

    def school_soccer_bully_vanish():
        if school_soccer_quest_bully_remove["vanished_date"] and t.day in irange(school_soccer_quest_bully_remove["vanished_date"], school_soccer_quest_bully_remove["vanished_date"] + 3):
            return True
        else:
            return False



    def school_bully_can_bully():
        if (loc(loc_school_field) and (school_soccer_playing() or school_soccer_hangingout())) or (loc(loc_school_gym) and school_dance_trope_present()) or not shane_here(dis_school) or school_soccer_quest_bully_remove["accepted"] or school_soccer_quest_bully_remove["vanished"] or shane.dead or ("took_poison" in shane.dict and t.day - shane.dict["took_poison"] >= 4):
            return False
        else:
            return True

    def school_pick_bully_lust():
        global tempname, tempname2
        if shane.lust >= marcus.lust:
            tempname = shane
            tempname2 = marcus
            return shane
        else:
            tempname = marcus
            tempname2 = shane
            return marcus

    def school_bully_adv_bully_stage(amount):
        global school_bully_quest_bully_event_stage 
        if school_bully_quest_bully_event_stage < amount + 1:
            school_bully_quest_bully_event_stage = amount + 1
        elif school_bully_quest_bully_event_stage == amount:
            school_bully_quest_bully_event_stage = amount + 2
        else:
            return

    def school_soccer_quest_bully_vanished_checker():
        if not school_soccer_quest_bully_remove["vanished"]:
            return False
        elif t.day - school_soccer_quest_bully_remove["vanished_date"] >= 15 and school_soccer_quest_bully_vanished_stage == 0:
            return True
        elif t.day - school_soccer_quest_bully_remove["vanished_date"] >= 18 and school_soccer_quest_bully_vanished_stage == 1:
            return True
        elif t.day - school_soccer_quest_bully_remove["vanished_date"] >= 22 and school_soccer_quest_bully_vanished_stage == 2:
            return True
        elif t.day - school_soccer_quest_bully_remove["vanished_date"] >= 25 and school_soccer_quest_bully_vanished_stage == 3:
            return True
        else:
            return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
