init python:

    def new_day(): 
        
        
        holiday_check() 
        player.stat_deg() 
        
        questlog_checks() 
        daily_checks() 
        bruise.heal() 
        blood.heal() 
        player.cycle() 
        npc_girls_newday_tick() 
        npc_active_routine_day() 
        npc_conversation_new_day() 
        rent_tick() 
        shops_restock() 
        player.hair_daily_grow() 

    def questlog_checks():
        if main_quest_02.isactive(): 
            if log.interactive("mq_02_passed_a") and (t.day - main_quest_01.missionvar2 > 0):
                main_quest_01.missionvar3 = 1 
                log.markdone("mq_02_passed_a")
            elif log.interactive("mq_02_a") and (t.day - main_quest_01.missionvar2 > 2):  
                
                main_quest_01.missionvar3 = 1 
                log.markdone("mq_02_a")
        if log.interactive("mq_04_b") and (main_quest_04.dict.get("wait") and t.day - main_quest_04.dict["wait"] > 0):
            log.markdone("mq_04_b")
        if log.interactive("mq_04_e") and t.day - main_quest_04.day_completed >= 2:
            log.markdone("mq_04_e")
        
        if log.completed("photo_02") and t.day - quest_photo.workedtoday >= 3:
            log.set_notdone("photo_02")
        
        if log.interactive("photo_intro_03") and t.day - quest_photo_intro.workedtoday >= 2:
            log.markdone("photo_intro_03") 
        if log.interactive("photo_intro_05") and t.day - quest_photo_intro.workedtoday >= 2:
            log.markdone("photo_intro_05") 
        if log.interactive("photo_intro_07") and t.day - quest_photo_intro.workedtoday >= 1:
            log.markdone("photo_intro_07")
        
        if log.interactive("photo_first_03") and t.day - quest_photo.workedtoday >= 2:
            log.markdone("photo_first_03")


    def daily_checks():
        global global_random_number
        global_random_number = numgen(1,10)
        
        if t.day > 28 and player.has_perk([perk_virgin, perk_tech_virgin]):
            player.remove_perk([perk_virgin, perk_tech_virgin])
            player.add_perk(perk_pure_virgin)
        perk_bimbo_queue()
        
        if not quest_gloryhole.active and t.day > 35: 
            for i in loc_list_all:
                if i.can_gloryhole and not i.has_gloryhole and not numgen(0,50):
                    i.has_gloryhole = True
                    if get_opposite_gender_room(i):
                        get_opposite_gender_room(i).has_gloryhole = True

    def weather_set():
        
        global weather_var 
        summer_weather = [1,1,1,1,1,1,1,1,1,2,2,3] 
        autumn_weather = [1,1,2,2,2,3,3,4]
        winter_weather = [2,4]
        spring_weather = [1,1,1,1,1,1,2,2,2,2,3]
        if t.day < 7:
            weather_var = 1
        elif t.month == "Summer":
            weather_var = renpy.random.choice(summer_weather)
        elif t.month == "Autumn":
            weather_var = renpy.random.choice(autumn_weather)
        elif t.month == "Winter":
            weather_var = renpy.random.choice(winter_weather)
        elif t.month == "Spring":
            weather_var = renpy.random.choice(spring_weather)

    def game_tick():
        global action_mirror_var, action_act_var, action_wardrobe_var, action_npc_var, action_shower_var, action_misc_var, action_bed_var
        
        player.cum_visible_check() 
        action_mirror_var = False
        action_npc_var = False
        action_shower_var = False
        action_misc_var = False
        action_bed_var = False
        if not action_act_var == loc_cur:
            action_act_var = False
        action_wardrobe_var = False
        player.check_effect_perks()
        writing.perk_checker()
        having_sex_tick()








    def talk_time_pass(event, interact=True, **kwargs):
        global talk_counter
        if talk_counter == "blocked" or not event == "end": 
            
            return
        talk_counter += 1
        if talk_counter >= 4:
            t.minute = 1
            talk_counter = 0

    def say_arguments_callback(who, interact=True, color="#fff"):
        global cheat_name_who, speaking_char
        
        cheat_name_who = who
        
        return (), { "interact" : interact, "what_color" : color }



    config.all_character_callbacks = [talk_time_pass, name_callback]

    def npc_race_setsame(race=False):
        
        global npc_race, npc_race2, npc_race3
        npc_race_picker_1(race)
        npc_race2 = npc_race
        npc_race3 = npc_race

    def npc_race_picker(race1=False,race2=False, race3=False):
        
        
        
        
        npc_race_picker_1(race1)
        npc_race_picker_2(race2)
        npc_race_picker_3(race3)

    def npc_race_picker_1(race1=False):
        global npc_race
        if race1 and isinstance(race1, Npc) and race1.skinbase:
            npc_race = race1
        else:
            if not numgen(0,2):
                npc_race = numgen(1,10)
            else:
                npc_race = numgen(1,4)

    def npc_race_picker_2(race2=False):
        global npc_race2
        if race2 and isinstance(race2, Npc) and race2.skinbase:
            npc_race2 = race2   
        else:
            if not numgen(0,2):
                npc_race2 = numgen(1,10)
            else:
                npc_race2 = numgen(1,4)

    def npc_race_picker_3(race3=False):
        global npc_race3
        if race3 and isinstance(race3, Npc) and race3.skinbase:
            npc_race3 = race3 
        else:
            if not numgen(0,2):
                npc_race3 = numgen(1,10)
            else:
                npc_race3 = numgen(1,4)

    def npc_race_switch(man1=None, man2=None):
        global npc_race, npc_race2, npc_race3
        if not man1:
            man1 = npc_race
        if not man2:
            man2 = npc_race2
        npc_race, npc_race2 = man2, man1

    def npc_name_switch():
        global tempname, tempname2
        name1 = tempname
        name2 = tempname2
        tempname = name2
        tempname2 = name1

    def npc_switch():
        npc_name_switch()
        npc_race_switch()

    def walk(location, time_amount=2, arrival=False, trans=True, loc_cur_block=False, outfit_block=False):
        travel_walk(location, time_amount, arrival, trans, loc_cur_block, outfit_block) 

    def exercise(tamount): 
        
        tamount = float(tamount)
        hunger = tamount / 5
        hygiene = tamount / 2
        allure = tamount / 15 * player.allure / 80
        if player.pregnancy == 2:
            tiredtotal = tamount / 15 * 3
        elif player.pregnancy == 3:
            tiredtotal = tamount / 15 * 4
        else:
            tiredtotal = tamount / 15 * 2
        
        if player.fitness < 20:
            moodtotal = tamount / 15 * -2
        elif player.fitness < 35:
            moodtotal = tamount / 15 * -1
        elif player.fitness >= 70:
            moodtotal = tamount / 15 * -0.2
        else:
            moodtotal = tamount / 15 * -0.5
        
        t.minute = int(tamount)
        
        
        player.add_hygiene(hygiene)
        player.add_hunger(hunger)
        player.add_tired(-tiredtotal)
        
        player.add_mood(moodtotal)
        player.add_desire(allure)
        if tamount >= 180: 
            player.add_fitness()
            player.add_fitness()
            player.add_fitness()
        elif tamount >= 120:
            player.add_fitness()
            player.add_fitness()
        elif tamount >= 60:
            player.add_fitness()
        else:
            randomnum = renpy.random.randint(1, 60)
            if randomnum < tamount:
                player.add_fitness()
        loiter_love((tamount / 4))
        
        
        return

    def stroll(tamount): 
        
        tamount = float(tamount)
        hunger = tamount / 15
        
        allure = tamount / 15 * player.allure / 80
        if player.pregnancy == 2:
            tiredtotal = tamount / 15 * 1.5
        elif player.pregnancy == 3:
            tiredtotal = tamount / 15 * 2
        else:
            tiredtotal = tamount / 15
        
        moodtotal = tamount / 15
        
        t.minute = int(tamount)
        
        
        player.add_hygiene(hunger)
        player.add_hunger(hunger)
        player.add_tired(-tiredtotal)
        player.add_mood(-moodtotal)
        player.add_desire(allure)
        if player.hygiene <= 20:
            player.add_mood(-moodtotal)

    def relax(tamount, who=None): 
        tamount = float(tamount)
        hunger = tamount / 15
        hygiene = tamount / 20
        allure = tamount / 15 * player.allure / 80
        tiredtotal = tamount / 30
        
        moodtotal = tamount / 10
        
        t.minute = int(tamount)
        
        
        player.add_hygiene(hygiene)
        player.add_hunger(hunger)
        player.add_tired(-tiredtotal)
        player.add_mood(moodtotal)
        player.add_desire(allure)
        if player.hygiene <= 20:
            player.add_mood(-moodtotal / 2)
        loiter_love(tamount, who)
        
        
        
        
        
        
        
        return

    def loiter(tamount=20, who=None):
        player.add_mood(tamount / 5)
        relax(tamount, who)

    def loiter_love(tamount=20, who=None):
        
        if who:
            if not isinstance(who, list):
                who = [who]
            for i in who:
                i._love += int(tamount)
        else:
            npc_hangout_love(tamount)

    def npc_hangout_love(tamount=20):
        
        for person in diary_people_list:
            if person._original_name.lower() + "_here" in globals() and globals()[person._original_name.lower() + "_here"]():
                person._love += int(tamount)

    def npc_check_here():
        who_list = []
        for person in diary_people_list:
            if person._original_name.lower() + "_here" in globals() and globals()[person._original_name.lower() + "_here"]():
                who_list.append( person._original_name.lower())
        return who_list

    def npc_any_here(where=None, exclude=None): 
        if where == None:
            where = loc_cur
        
        if not isinstance(exclude, list):
            exclude = [exclude]
        
        g = globals()
        
        for person in diary_people_list:
            if person in exclude:
                continue
            
            func_name = person._original_name.lower() + "_here"
            func = g.get(func_name)
            
            if func:
                if isinstance(func(class_loc=True), District):
                    
                    
                    if where in func(class_loc=True).locs and where.population > 2:
                        return person._original_name.lower()
                elif func(where):
                    return True
        else:
            return False

    def having_sex_tick(): 
        if player.having_sex:
            if player.beingraped:
                if not numgen(0,10):
                    if numgen():
                        bruise.belly += 1
                    if numgen():
                        bruise.chest += 1
                    if numgen():
                        bruise.face += 1
                if not numgen(0,5):
                    bruise.bruise_ass(0.2)
            else:
                if not numgen(0,100):
                    if numgen():
                        bruise.belly += 1
                    else:
                        bruise.chest += 1
                if not numgen(0,40):
                    bruise.bruise_ass()
        return

    def having_sex(tamount): 
        tamount = float(tamount)
        hunger = tamount / 5
        hygiene = tamount / 2
        allure = tamount / 15 * player.allure / 80
        tiredtotal = tamount / 15 * 2
        moodtotal = tamount / 15 * -0.5
        
        t.minute = int(tamount)
        
        
        player.add_hygiene(hygiene)
        player.add_hunger(hunger)
        player.add_tired(-tiredtotal)
        
        player.add_mood(moodtotal)
        player.add_desire(allure)
        return

    def working(tamount): 
        tamount = float(tamount)
        hunger = tamount / 10
        hygiene = tamount / 5
        allure = tamount / 15 * player.allure / 120
        if player.pregnancy == 2:
            tiredtotal = tamount / 15 * 2
        elif player.pregnancy == 3:
            tiredtotal = tamount / 15 * 2.5
        else:
            tiredtotal = tamount / 15 * 1.5
        
        moodtotal = tamount / 8
        
        t.minute = int(tamount)
        
        
        player.add_hygiene(hygiene)
        player.add_hunger(hunger)
        player.add_tired(-tiredtotal)
        player.add_mood(-moodtotal)
        player.add_desire(allure)
        if player.hygiene <= 20:
            player.add_mood(-moodtotal)
        if numgen(0,300) < tamount:
            player.add_fitness()

    def time_working_to(hours,mins):
        minstotal = mins - t.minute
        if not t.minute == mins:
            if minstotal < 0:
                minstotal = abs(minstotal)
                working(60 - minstotal)
            else:
                working(minstotal)
        elif not t.hour == hours:
            working(hours * 60)
        if t.hour == hours and t.minute == mins:
            return
        else:
            time_working_to(hours, mins)

    def time_round_to_hour():
        
        totalMinutes = 60
        totalMinutes -= t.minute
        t.minute = totalMinutes
        allure = totalMinutes / 15 * player.allure / 10
        stotal = totalMinutes / 15
        hunger = totalMinutes / 15
        player.add_hygiene(hunger)
        player.add_hunger(hunger)
        player.add_tired(-stotal)
        player.add_mood(-stotal)
        player.add_desire(allure)
        return

    def time_advance_to(hours, mins):
        if not t.minute == mins:
            t.minute = 1
        elif not t.hour == hours:
            t.hour = 1
        
        if t.hour == hours and t.minute == mins:
            return
        else:
            time_advance_to(hours, mins)

    def time_sleep(amount):
        
        t.minute = amount
        tired = int(amount / 7)
        player.add_tired(tired)
        hunger = amount / 15
        hygiene = amount / 10
        player.add_hunger(hunger)
        player.add_hygiene(hygiene)

    def time_round_to_hour_sleep():
        
        totalMinutes = 60
        totalMinutes -= t.minute
        t.minute = totalMinutes
        tired = int(totalMinutes / 7)
        player.add_tired(tired)
        hunger = totalMinutes / 15
        hygiene = totalMinutes / 10
        player.add_hunger(hunger)
        player.add_hygiene(hygiene)

    def time_sleep_hour():
        totalMinutes = 60
        t.minute = totalMinutes
        tired = int(totalMinutes / 7)
        player.add_tired(tired)
        hunger = totalMinutes / 15
        hygiene = totalMinutes / 10
        player.add_hunger(hunger)
        player.add_hygiene(hygiene)

    def time_sleep(timeamount):
        t.minute = timeamount
        tired = int(timeamount / 7)
        player.add_tired(tired)
        hunger = timeamount / 15
        hygiene = timeamount / 10
        player.add_hunger(hunger)
        player.add_hygiene(hygiene)

    def time_sleep_rough():
        timeamount = renpy.random.randint(120, 240)
        time_sleep(timeamount)
        player.add_mood(-(timeamount / 10))
        player.add_hygiene(100)
        player.face_sleep()

    def time_round_to_half_hour():
        if t.minute >= 30:
            totalMinutes = 60
            totalMinutes -= t.minute + 30
            t.minute = totalMinutes
            return
        else:
            totalMinutes = 30
            totalMinutes -= t.minute
            t.minute = totalMinutes
        allure = totalMinutes / 15 * player.allure / 10
        stotal = totalMinutes / 15
        hygiene = totalMinutes / 10
        player.add_hunger(stotal)
        player.add_hygiene(hygiene)
        player.add_tired(-stotal)
        player.add_mood(-stotal)
        player.add_desire(allure)
        return

    def makeup_strip():
        
        player.eyeshad_colour = 0
        player.blush_colour = 0

    def add_wardrobe(list, number):
        global owned_jacket, owned_outfit, owned_top, owned_bottom, owned_pants, owned_bra, owned_socks, owned_gloves, owned_hat
        if not number in list:
            list.append(number)

    def remove_wardrobe(alist, number, slot):
        global owned_jacket, owned_outfit, owned_top, owned_bottom, owned_pants, owned_bra, owned_socks, owned_gloves, owned_hat
        remove_from_list(alist, number)
        for i in (school,daily,sport,party,home):
            if getattr(i,slot) == number:
                setattr(i,slot,0)

    def spend_money(amount):
        player.cash -= amount

    def reset_call_stack():
        for _ in range(renpy.call_stack_depth()):
            renpy.pop_call()

    def holiday_check():
        global calander_holiday
        calander_holiday = ""























    def add_event_love_lust(who): 
        for i in who:
            randomnum = renpy.random.randint(5, 15)
            for _ in range(randomnum):
                i.talk_love_add()
                i.talk_lust_add

    def npc_conversation_new_day():
        
        if school_photo_shoots_done >= 3:
            add_to_list(school_photo_quest.list, "dani_photos")
            if "want_photos" in school_soccer_quest.conversation_topics and renpy.random.randint(1,10) == 1:
                add_to_list(school_soccer_quest.conversation_topics, "has_photos")
            
            if "has_photos" in school_soccer_quest.conversation_topics and "dani_photos" in school_photo_quest.list and renpy.random.randint(1,20) == 1:
                add_to_list(school_soccer_quest.conversation_topics, "has_dani_photos")
            
            if renpy.random.randint(1,10) == 1:
                add_to_list(school_photo_quest.list, "dani_tasteful")
            
            if renpy.random.randint(1,20) == 1:
                add_to_list(school_photo_quest.list, "dani_topless")
            
            if renpy.random.randint(1,35) == 1:
                add_to_list(school_photo_quest.list, "dani_nude")
            
            if dani.iswhore and renpy.random.randint(1,10) == 1:
                add_to_list(school_photo_quest.list, "dani_sex")
        
        for i in npc_girls:
            
            
            if i.is_unique and "rape" in i.conversation_topics and numgen():
                remove_from_list(i.conversation_topics, "rape")
            if i.is_unique and "lover" in i.conversation_topics and numgen():
                remove_from_list(i.conversation_topics, "lover")


    def npc_active_routine_day():
        
        set_attend_school()
        npc_consume_items()
        
        
        
        
        
        
        
        
        
        
        
        
        if cass.alive:
            if cass.inv.qty(item_poison) and not numgen(0,6):  
                cass.inv.drop(item_poison)
                shane.inv.take(item_beer_poison) 
                add_to_list(shane.list, "cass_poison")
            
            if "broken" in cass.list and not numgen(0, 20):
                cass.kill()
                cass.dead_message = "She seems to have vanished."
        
        if mira.alive:
            if log.interactive("mira_missing_08") and not numgen(0, 10):
                cass.inv.take(item_mira_intel)
            if "hospitalised" in mira.list and "rescue_date" in mira.dict and t.day > (mira.dict["rescue_date"] + 10):
                remove_from_list(mira.list, "hospitalised")
                add_to_list(mira.list, "rescued")
                mira.active = True
            if not quest_mira_missing.active and "kidnapped" in mira.list and not "rescued" in mira.list and (t.day - mira.dict["kidnap_date"]) >= 20:
                mira.kill()
                add_to_list(cass.list, "broken")
                mira.dead_message = "She seems to have went missing one day."
        
        if oskar.alive:
            if oskar.inv.qty(item_beer_poison) and not numgen(0,If("pc_broke_in" in loc_office_ll.list, 25, 7)):  
                oskar.inv.drop(item_beer_poison, oskar.inv.qty(item_beer_poison))
                oskar.dict["took_poison"] = t.day
            if "took_poison" in oskar.dict and oskar.dict["took_poison"] > 0:
                kill_chance_amount = (10 - ((t.day - oskar.dict["took_poison"]) - 10))
                
                if kill_chance_amount <= 0 or not numgen(0, kill_chance_amount):
                    oskar.kill()
                    dani_yan_max_add(-100) 
                    dani_yan_add(-dani_yan_value()) 
                    add_to_list(oskar.list, "dead_poisoned")
                    if oskar.rape:
                        oskar.dead_message = "I poisoned the rapist piece of shit!"
                    else: 
                        oskar.dead_message = "I killed the piece of shit!"
        else: 
            if oskar.days_dead >= 10 and not loc_office_ll.locked:
                
                loc_office_ll.locked = True



    def npc_active_routine_day_middle():    
        
        if rachel.alive:
            if not numgen(0,2) and "nude_vball" in loc_beach_hangout.list and weather_var in [1,2]:
                add_to_list(rachel.list, "playing_nude_vball")
            else:
                remove_from_list(rachel.list, "playing_nude_vball")

    def npc_active_routine_minute():
        if not mira.dead:
            if mira_here(dis_truckstop) and not numgen(0,40):
                add_to_list(mira.list, "whore_having_sex")
                mira.have_sex(punter, sold=True)
            elif "whore_having_sex" in mira.list and not numgen(0,10):
                remove_from_list(mira.list, "whore_having_sex")
        
        if not cass.dead:
            if cass_here(dis_truckstop) and not numgen(0,40):
                add_to_list(cass.list, "whore_having_sex")
                cass.have_sex(punter, sold=True)
            elif "whore_having_sex" in cass.list and not numgen(0,10):
                remove_from_list(cass.list, "whore_having_sex")
        
        if not robin.dead:
            school_soccer_npc_sex_robin_pick()
        if not rachel.dead:
            school_soccer_npc_sex_rachel_pick()

    def npc_active_routine_hour():
        
        
        if not jaylee.dead:
            if jaylee.days_pregnant > (global_pregnancy_length * 0.3):
                
                jaylee.active = True
            elif (t.wkday == "Thursday" and t.hour >= 9) or (t.wkday == "Friday" and t.hour <= 19):
                
                jaylee.active = False
            else:
                jaylee.active = True
        
        if not robin.dead: 
            remove_from_list(robin.list, "pub_leave_offer") 
            if t.hour == 7 and "slut_outing" in robin.list:
                remove_from_list(robin.list, "slut_outing")
            if t.hour == 22 and numgen(0,2) and robin.drunk > 50:
                add_to_list(robin.list, "common_passout")
            if "common_passout" in robin.list and t.hour in (0,1,2,3) and not numgen(0,3): 
                remove_from_list(robin.list, "common_passout")  
            if t.hour == 4 and "common_passout" in robin.list: 
                remove_from_list(robin.list, "common_passout")  
            if robin_here(loc_motel_room2): 
                robin.have_sex_milti(pubpatron, times=numgen(1,4))
        
        if not shane.dead:
            if shane.inv.qty(item_beer_poison) and not "poisoned" in shane.list:
                add_to_list(shane.list, "poisoned")
                shane.dict["took_poison"] = t.day
                shane.inv.drop(item_beer_poison, 100)
            if "took_poison" in shane.dict and t.day - shane.dict["took_poison"] >= 10:
                kill_chance_amount = (10 - ((t.day - shane.dict["took_poison"]) - 10))
                
                if kill_chance_amount <= 0 or not numgen(0, kill_chance_amount):
                    shane.kill()
                    marcus.kill()
                    add_to_list(shane.list, "dead_poisoned")
                    add_to_list(marcus.list, "dead_poisoned")
                    if "cass_poison" in shane.list:
                        shane.dead_message = "I helped " + cass.name.name + " kill the piece of shit!"
                        marcus.dead_message = "I helped " + cass.name.name + " kill the piece of shit!"
                    else:
                        shane.dead_message = "I killed the piece of shit!"
                        marcus.dead_message = "I killed the piece of shit!"
                    shane.dead_location = "In hell I hope."
                    marcus.dead_location = "Rotting somewhere."


    def set_attend_school():
        if not mira.dead:
            if ((mira.love >= 100 and t.day >= 32) or t.day >= 56) and mira.active and not ("kidnapped" in mira.list or "kidnapped_fail" in mira.list):
                quest_mira_missing_kidnap()
            if "rescued" in mira.list and not mira.active:
                mira.active = True
        if not cass.dead:
            if school_bully_quest_bully_cass_target and not shane.dead and not numgen(0,8):
                cass.active = False
            else:
                cass.active = True
        
        
        if t.day in irange(school_soccer_quest_bully_remove["vanished_date"], school_soccer_quest_bully_remove["vanished_date"]+3):
            drake.active = False
            nate.active = False
            dan.active = False
        elif not all([drake.active, nate.active, dan.active]):
            drake.active = True
            nate.active = True
            dan.active = True

    def npc_consume_items():
        for i in npc_all:
            if i.inv.qty(item_beer):
                i.inv.drop(numgen(1, i.inv.qty(item_beer)))
            elif i.inv.qty(item_joy):
                i.inv.drop(item_joy)
                if i == dani:
                    dani_yan_remove(numgen(5,15))

    def npc_desire_raise():
        for i in npc_unique:
            if not numgen(0, i.lust):
                i.add_lust(5)

    def npc_drunk():
        
        
        
        
        
        for person in npc_all:
            if person._original_name.lower() + "_here" in globals() and isinstance(globals()[person._original_name.lower() + "_here"](class_loc=True), Location) and globals()[person._original_name.lower() + "_here"](class_loc=True).drinking_location:
                
                person.add_drunk() 
            elif person.drunk:
                person.remove_drunk(25) 

    def npc_list_names(alist):
        all_list = []
        for i in alist:
            all_list.append(i.name)
        return all_list

    def npc_girls_newday_tick(ignore_timer=False): 
        if not t.day < 14 or ignore_timer: 
            npc_girls_protection()
            npc_girls_check_pregnancy()
            npc_girls_random_preg()
            npc_girls_newday_tick_events()
            npc_girls_lover_preg()
            npc_girls_whore_preg()

    def npc_girls_protection():
        
        for i in npc_girls:
            if not numgen(0,150):
                i.inv.take(item_map_pill)
            if not numgen(0, 300) and not i.inv.qty(item_abort_pill):
                i.inv.take(item_abort_pill)
            if i.iswhore:
                if not numgen(0,60) and i.inv.qty(item_abort_pill) <= 2:
                    i.inv.take(item_abort_pill)
                if not numgen(0,20) and i.inv.qty(item_map_pill) <= 3:
                    i.inv.take(item_map_pill)

    def npc_girls_newday_tick_events(): 
        
        
        if cass.alive:
            
            if school_bully_quest_bully_cass_target and not shane.dead: 
                npc_girls_regular_preg(cass, renpy.random.choice([shane,marcus]), high_range=2, forced=True, block_spray=True)
        
        if mira.alive:
            if "kidnapped" in mira.list and not "rescued" in mira.list:
                mira.inv.empty() 
                for _ in range(numgen(2,6)):
                    mira.have_sex(mira_kidnapper, forced=True)
        
        if rachel.alive:
            npc_girls_regular_preg(rachel, busgroper, 1, 30)
            npc_girls_regular_preg(rachel, renpy.random.choice([shane,marcus]), high_range=10, forced=True, block_spray=True)
            if school_dance_quest_show_count > 3 and sum([drake.love,nate.love,dan.love]) > 80: 
                npc_girls_regular_preg(rachel, renpy.random.choice([drake,nate]))
                npc_girls_regular_preg(rachel, dan, 1, 15)
            if "using_gloryhole" in rachel.list and t.wkday in weekdays:
                npc_girls_gloryhole_preg(rachel) 
            if "can_bitch" in rachel.list and rachel.noon_number <= 3:
                npc_girls_regular_preg(rachel, wolf)
        
        if dani.alive:
            
            if "dani_sex" in school_photo_quest.list:
                npc_girls_regular_preg(dani, felix, 1, 15)
            if "pub_started_working" in dani.dict and dani.dict["pub_started_working"] > 0 and t.day >= dani.dict["pub_started_working"] and "willwork_pub" in dani.list:
                remove_from_list(dani.list, "willwork_pub")
                remove_from_list(trixie.list, "asked_about_dani")
                add_to_list(dani.list, "working_pub")
            if "pub_started_working" in dani.dict and dani.dict["pub_started_working"] > 0 and t.day >= dani.dict["pub_started_working"] + 10:
                npc_girls_regular_preg(dani, pubpatron, 1, 3, sold=True)
                if loc_pub_toilet_girls.has_gloryhole: 
                    npc_girls_gloryhole_preg(dani) 
            
            if dani.has_met: 
                
                dani_alone_academy_day_picker() 
                
                
                if "freakout_blocked" in dani.list: 
                    dani_yan_max_add(-5) 
                else:
                    dani_yan_add(2) 
                    if dani.hate: 
                        dani_yan_max_add(5) 
                    if dani_not_hanging_with_anabel(): 
                        dani_yan_add(2) 
                    if not numgen(0,10): 
                        dani_yan_max_add(1)
                    
                    
                    
                    if dani.rape: 
                        for _ in range(dani.rape):
                            if not numgen(0,10):
                                dani_yan_max_add(1) 
                    if dani.sold: 
                        for _ in range(dani.sold):
                            if not numgen(0,25):
                                dani_yan_max_add(1)
                    
                    if dani.sex_les:
                        
                        
                        dani_yan_add(numgen(0,2))
                    if dani.sex_les and player.showing:
                        
                        if not numgen(0,3):
                            dani_yan_max_add(1)
                            dani_yan_add(numgen(0,5))
                    for i in [rachel, robin, anabel, cass, mira]:
                        if dani.sex_les and i.love > 80 and not numgen(0,3):
                            
                            dani_yan_max_add(1)
                            dani_yan_add(numgen(1,4))
                    
                    
                    if pubpatron in dani.sex_who_class and not "added_yan_for_pub_sex" in dani.list:
                        
                        add_to_list(dani.list, "added_yan_for_pub_sex")
                        dani_yan_max_add(20)
                    if ghman in dani.sex_who_class and not "added_yan_for_gloryhole" in dani.list:
                        
                        add_to_list(dani.list, "added_yan_for_gloryhole")
                        dani_yan_max_add(20)
                    if partyman in dani.sex_who_class and not "added_yan_for_vip" in dani.list:
                        
                        add_to_list(dani.list, "added_yan_for_vip")
                        if dani.iswhore:
                            dani_yan_max_add(20)
                        else:
                            dani_yan_max_add(40)
                    
                    if dani.showing:
                        if not numgen(0,5):
                            dani_yan_max_add(1)
                        if dani.pregnant_who == oskar:
                            dani_yan_max_add(2)
                    if anabel.hate:
                        dani_yan_max_add(3)
                        dani_yan_add(numgen(3,10))
                    if oskar.dead:
                        
                        dani_yan_max_add(-numgen(1,8))
                        dani_yan_add(-numgen(3,10))
        
        if anabel.alive:
            anabel_alone_academy_day_picker()
            
            if dani.dead and "dead_anabel_knows" in dani.list:
                if not numgen(0, 20):
                    anabel.kill("I am not sure what happened to her, but I haven't seen her around for some time.")
                
                elif numgen():
                    anabel.active = False
                else:
                    anabel.active = True
        
        
        
        if robin.alive:
            if "soccerboys_can_sex" in robin.list:
                npc_girls_regular_preg(robin, renpy.random.choice([drake,nate]))
                npc_girls_regular_preg(robin, dan, 1, 15)
            if "pc_know_want_bussex" in robin.list:
                npc_girls_regular_preg(robin, busgroper, 1, 5) 
            if "oskar_sex" in robin.list:
                npc_girls_regular_preg(robin, oskar, 1, 3) 
            if "robin_talk_pub_chain" in robin.dict and robin.dict["robin_talk_pub_chain"] >= 15 and global_random_noon_number >= 9:
                npc_girls_regular_preg(robin, pubpatron, 1, 2) 
            if "can_bitch" in robin.list and robin.noon_number <= 2:
                npc_girls_regular_preg(robin, wolf) 
        
        if jaylee.alive:
            npc_girls_regular_preg(jaylee, ashon, high_range=4)
        
        for i in npc_girls:
            if i.is_unique and not i.stay_virgin and not i.iswhore:
                npc_girls_regular_preg(i, busgroper, 1, 70)

    def npc_girls_lover_preg(): 
        for i in npc_girls:
            if not i.stay_virgin and not i.iswhore:
                if i.isslut and not numgen(0, 4):
                    i.have_sex(lover)  
                    add_to_list(i.conversation_topics,"lover")
                elif not numgen(0, 10):
                    i.have_sex(lover)
                    add_to_list(i.conversation_topics,"lover")

    def npc_girls_regular_preg(girl, boy, low_range=1, high_range=5, forced=False, sold=False, block_spray=False): 
        if numgen(low_range, high_range) == 1:
            if forced:  
                girl.rape += 1
            
            girl.have_sex(boy, forced=forced, block_spray=block_spray, sold=sold)  
            add_to_list(girl.conversation_topics, boy.setname.lower())  
            add_to_list(boy.conversation_topics,girl.setname.lower())

    def npc_girls_whore_preg(): 
        for i in npc_girls:
            if not numgen(0,50) and not i.stay_virgin:
                i.have_sex(highpayer, sold=True)
        for i in npc_girls_whore:
            if i == mira and "kidnapped" in mira.list and not "rescued" in mira.list:
                continue
            for _ in range(numgen(1,5)):
                i.have_sex(punter, sold=True)

    def npc_girls_gloryhole_preg(who): 
        for _ in range(numgen(1,3)):
            who.have_sex(ghman, sold=True, vaginal=False, anal=False)
        if not numgen(0, 5):
            who.have_sex(ghman, sold=True)

    def npc_girls_check_pregnancy():
        global npc_girls, npc_girls_pregnant
        for i in npc_girls:
            if getattr(i, "is_pregnant") and i not in npc_girls_pregnant:
                add_to_list(npc_girls_pregnant,i)
            if not getattr(i, "is_pregnant") and i in npc_girls_pregnant:
                remove_from_list(npc_girls_pregnant,i)
        
        for i in npc_girls_pregnant: 
            i.preg_pass_day()  

    def npc_girls_random_preg():
        for i in npc_girls:
            if renpy.random.randint(0, 30) == 1:
                i.have_sex(rapist, forced=True)
                add_to_list(i.conversation_topics,"rape")

    def men_location_degrade():
        for i in loc_list_all:
            i.man_degrade()

    def get_and_return_label_list(what_label):
        label_list = []
        label_number = 0
        for _ in range():
            label_number += 1
            if renpy.has_label(what_label + str(label_number)):
                label_list.append(what_label + str(label_number))
            else:
                return label_list



    def add_to_list(alist, what):
        if not isinstance(what,list):
            what = [what]
        for i in what:
            if not i in alist:
                alist.append(i)

    def remove_from_list(alist, what):
        if not isinstance(what, list):
            what = [what]
        for i in what:
            while i in alist:
                alist.remove(i)

    def any_in_list(alist, what):
        if not isinstance(what, list):
            what = [what]
        for i in what:
            if i in alist:
                return True
        else:
            return False
    def hide_npc(who):
        
        if not isinstance(who,list):
            who = [who]
        for i in who:
            add_to_list(i.list, "no_location")

    def unhide_npc(who):
        
        if not isinstance(who,list):
            who = [who]
        for i in who:
            remove_from_list(i.list, "no_location")

    def npc_here_check(location, cur_location, where, text_desc=""): 
        if where:
            if text_desc:
                return text_desc
            elif cur_location:
                if isinstance(cur_location, District):
                    return cur_location.npc_desc
                else:
                    return cur_location.desc
            
            
            
            
            else:
                return "Unknown"
        
        if isinstance(location, District):
            location = location.locs
        if not isinstance(location, list):
            location = [location]
        if isinstance(cur_location, District):
            cur_location = cur_location.locs
        if not isinstance(cur_location, list):
            cur_location = [cur_location]
        
        for i in location:
            if i in cur_location:
                return True
        
        return False

    def reset_temp_vars():
        global temp_var_1, temp_var_2, temp_var_3, temp_var_4, temp_var_5, temp_var_6, temp_var_7,temp_var_8, temp_var_9, temp_var_10
        temp_var_1 = False
        temp_var_2 = False
        temp_var_3 = False
        temp_var_4 = False
        temp_var_5 = False
        temp_var_6 = False
        temp_var_7 = False
        temp_var_8 = False
        temp_var_9 = False
        temp_var_10 = False

    def roundup_10(amount, var):
        number = int(math.ceil(amount / 10.0)) * 10
        var = number
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
