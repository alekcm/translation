init python:

    def haven_time_empty():
        if t.hour in [4,5,17,18]:
            return True
        else:
            return False

    def haven_time_safe():
        if t.hour in [6,7,8,9,10,11,12,13,14,15,16]:
            return True
        else:
            return False

    def haven_time_normal():
        if t.hour in [19,20,2,3]:
            return True
        else:
            return False

    def haven_time_danger():
        if t.hour in [0,1,21,22,23]:
            return True
        else:
            return False

    def haven_time_nohide():
        if t.hour in [23,0,1,2,3,4,5,6]:
            return True
        else:
            return False

    def haven_whore_pay():
        inv.take(item_brew, renpy.random.randint(0, 4))
        inv.take(item_cigs, renpy.random.randint(1, 20))
        inv.take(item_joy, renpy.random.randint(0, 2))
        inv.take(item_lebo, renpy.random.randint(0, 1))
        if not numgen(0,15):
            inv.take(item_map_pill, 1)
        if not numgen(0,15):
            inv.take(item_preg_test, 1)
        if not numgen(0,40):
            inv.take(item_abort_pill, 1)
        if not numgen(0,100):
            inv.take(item_pepperspray, 1)

    def haven_progress_triggers():
        if main_quest_05.active == 1:
            if loc_cur in (loc_haven_shower, loc_haven_utilities):
                return
            if haven_search_complete() and log.interactive("mq_05_b"):
                renpy.jump("haven_searched")
            
            if loc_cur == loc_haven_bedroom and not "bedroom_propt" in loc_haven_bedroom.list and haven_time_empty() and log.completed("mq_05_b"):
                renpy.jump("haven_bedroom_prompt")
            elif not log.interactive("mq_05_fire") and inv.qty(item_haven_lighter) and inv.qty(item_haven_fluid):
                renpy.jump("haven_notif_can_set_fire")
            elif not "tool_notif" in main_quest_05.conversation_topics and inv.qty(item_haven_crowbar):
                renpy.jump("haven_notif_tool")
            
            elif not "intel_first" in main_quest_05.conversation_topics and inv.qty(item_haven_intel):
                renpy.jump("haven_intel_first")
            elif not "intel_mid" in main_quest_05.conversation_topics and inv.qty(item_haven_intel) >= 6:
                renpy.jump("haven_intel_mid")
            elif not "intel_done" in main_quest_05.conversation_topics and inv.qty(item_haven_intel) >= 10:
                renpy.jump("haven_intel_done")
        return

    def haven_search_complete():
        room_list = [loc_haven_room1.visited, loc_haven_room2.visited, loc_haven_room3.visited, loc_haven_lounge.visited, loc_haven_bedroom.visited, loc_haven_storage.visited, loc_haven_shower.visited, loc_haven_utilities.visited, ]
        if all(room_list):
            return True
        else:
            return False

    def haven_intel_chance():
        global loc_to
        base = 13
        
        if haven_time_empty():
            return False
        
        elif loc(loc_haven_bed): 
            base = base * 1.5
        elif loc(loc_haven_room1): 
            
            if haven_time_danger():
                base = base * 0.8
            else:
                base = base * 1.2
        
        elif loc(loc_haven_room2): 
            base = base * 1.5
        
        elif loc(loc_haven_shower_stall):
            if haven_time_safe() or haven_time_normal():
                base = base * 1.1
            else: 
                base = base * 0.8
        
        else:
            if haven_time_danger():
                base = base * 0.5
            else:
                base = base * 0.8
        base = int(base)
        
        randomnum = renpy.random.randint(1, base)
        
        if randomnum == 1:
            return True
        else:
            return False

    def haven_random_event_can_trigger():
        if loc_cur in [loc_haven_bed, loc_haven_shower, loc_haven_shower_stall, loc_haven_landing, loc_haven_hallway_2f, loc_haven_hallway_1f, loc_haven_lounge] or haven_time_empty():
            
            return False
        elif loc_cur in [loc_haven_shower_stall, loc_haven_bed, loc_haven_bedroom, loc_haven_utilities] and haven_time_safe():
            
            return False
        else:
            return True

    def haven_random_event_noevent_weight():
        base_weight = 0
        if haven_time_empty():
            base_weight = 8000
        elif haven_time_safe():
            if loc_cur in [loc_haven_bed, loc_haven_bedroom, loc_haven_shower, loc_haven_shower_stall, loc_haven_utilities]:
                base_weight = 2500
            else:
                base_weight = 1500
        elif haven_time_normal():
            base_weight = 1500
        else: 
            base_weight = 300
        return base_weight

    def haven_random_event_room_weight(util=False, shower=False):
        global loc_cur
        if (util and not loc_cur == loc_haven_utilities) or (shower and not loc_cur == loc_haven_shower_stall):
            
            return 0
        
        if (not util and loc_cur == loc_haven_utilities) or (not shower and loc_cur == loc_haven_shower_stall):
            
            return 0
        
        if loc_cur.population == 2 and not (util or shower):
            return 0
        if loc_cur in (loc_haven_lobby, loc_haven_landing, loc_haven_hallway_1f, loc_haven_hallway_2f, loc_haven_bed):
            return 0
        if haven_time_empty():
            if loc_cur.population < 2: 
                return 5
            else:
                return 0
        
        elif loc_cur in (loc_haven_bed, loc_haven_bedroom, loc_haven_shower_stall, loc_haven_utilities) and haven_time_safe():
            
            return 0
        
        amount = ((player.drunk) + (player.desire / 4) + (If(player.isslut or player.iswhore, 20,0)) + (If(player.cum_visible, 50,0)) + ((100 - player.confidence) / 2) + ((100 - player.int) / 4))
        
        if haven_time_danger():
            amount = amount * 1.5
        elif haven_time_normal() or haven_time_safe():
            
            
            amount = amount
        if amount < 0:
            return 0
        return amount





    def haven_join_chance():
        if haven_time_empty():
            
            return False
        elif loc_cur in (loc_haven_bed, loc_haven_bedroom, loc_haven_shower_stall) and haven_time_safe():
            
            return False
        
        randomnum = renpy.random.randint(100, 1000)
        amount = ((player.desire / 4) + (player.drunk * 2) + ((100 - player.confidence) / 2) + ((100 - player.int) / 4) + (If(player.isslut, 20,0)) + (If(player.cum_visible, 50,0)))
        
        if loc_cur == loc_haven_room1: 
            if havenpeeper.dict.get("joined_room1") and havenpeeper.dict["joined_room1"] == 6: 
                amount += 25
            elif haven_time_safe():
                amount += 300
            elif haven_time_normal():
                amount += 150
            else:
                amount += 0
        
        
        
        elif haven_time_danger():
            amount += 300
        elif haven_time_normal() or haven_time_safe():
            
            
            amount += 75
        
        amount = amount * 2 
        if amount >= randomnum:
            return True
        else:
            return False
        return









    def haven_bedroom_search_caught():
        if not numgen(0,6):
            renpy.jump("haven_bedroom_search_caught")
        else:
            return


    def haven_bed_join_chance():
        if haven_join_chance():
            renpy.jump("haven_bed_sleep_join")
        else:
            return

    def haven_shower_join_chance():
        if haven_join_chance():
            renpy.jump("haven_shower_stall_join")
        else:
            return

    def haven_room1_join_chance():
        if haven_join_chance():
            renpy.jump("haven_room1_listen_join")
        else:
            return

    def haven_storage_join_chance():
        if haven_join_chance() and loc(loc_haven_storage):
            renpy.jump("haven_storage_join")
        else:
            return False

    def haven_storage_stool_join_chance():
        
        
        if haven_join_chance():
            renpy.jump("haven_storage_stool_join")
        elif haven_join_chance():
            renpy.jump("haven_storage_stool_join")
        elif haven_join_chance():
            renpy.jump("haven_storage_stool_join")

    def haven_storage_vent_join_chance():
        if haven_join_chance():
            renpy.jump("haven_storage_ventopen_join")
        else:
            return


    def haven_utilities_join_chance():
        if haven_join_chance() and loc(loc_haven_utilities):
            renpy.jump("haven_utilities_join")

    def haven_utilities_pry_join_chance():
        if haven_join_chance() and loc(loc_haven_utilities):
            renpy.jump("haven_utilities_pry_join")



    def haven_room2_listen():
        if haven_time_danger():
            randomnum = renpy.random.randint(1, 10)
        elif haven_time_empty():
            renpy.jump("haven_room2_listen_noinfo")
        else:
            randomnum = renpy.random.randint(1, 40)
        
        if randomnum == 1:
            renpy.jump("haven_room2_listen_goodinfo")
        elif randomnum > 35:
            renpy.jump("haven_room2_listen_noinfo")
        else:
            renpy.jump("haven_room2_listen_genericinfo")

    def haven_shower_listen():
        if haven_time_safe() or haven_time_normal():
            randomnum = renpy.random.randint(1, 30)
        
        if haven_time_danger():
            randomnum = renpy.random.randint(1, 10)
        else:
            renpy.jump("haven_shower_listen_noinfo")
        
        if randomnum == 1:
            if haven_time_safe():
                renpy.jump("haven_shower_listen_goodinfo_girls")
            else:
                renpy.jump("haven_shower_listen_goodinfo")
        elif randomnum > 35:
            renpy.jump("haven_shower_listen_noinfo")
        else:
            if haven_time_safe():
                renpy.jump("haven_shower_listen_genericinfo_girls")
            else:
                renpy.jump("haven_shower_listen_genericinfo")

    def shower_listen_masturbate():
        if player.check_sex_agree(4, notif=False) and (haven_time_normal() or haven_time_danger()) and player.check_horny(): 
            renpy.jump("haven_room1_listen_masturbate")

    def haven_can_set_fire():
        if log.interactive("mq_05_fire") and inv.qty(item_haven_lighter) and inv.qty(item_haven_fluid) and log.completed("mq_05_b"):
            return True
        else:
            return False

    def haven_guard_hours():
        if t.hour in [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
            return True
        else:
            return False

    def haven_guard_smoking():
        if t.hour in (8,10,12,14,16,18) and t.minute in irange(30,60) and havengateguard.inv.qty(item_haven_lighter):
            return True
        else:
            return False

    def haven_days():
        amount = t.day - main_quest_05.dict["day_entrance"]
        return amount

    def haven_drink_brew():
        
        inv.drop(item_brew, 1)
        player.add_perk(perk_drinking_brew_1, mins=10)
        randomnum = renpy.random.randint(1, 10)
        amount = randomnum + 40
        
        player.add_drunk(amount) 
        if player.mood < 25:
            player.add_mood(25 - player.mood) 
        player.add_tired(-10) 
        if player.confidence <= 20 and randomnum == 1:
            player.add_conf(1)
        renpy.show_screen("drink")
        if player.prop == "beerr":
            player.prop = ""
        elif player.prop == "beerb":
            player.prop = "beerl"
        elif player.prop == "beerl":
            player.prop = ""
        if player.cum_locations["cum_mouth"] == True:
            player.cum_locations["cum_mouth"] = False
        player.spike_chance()
        player.spike_chance() 

    def haven_sleep_sex_loop(who=None, amount=11):
        if who == None:
            who = havenman
        randomnum = 0
        while randomnum < amount:
            player.sex_forced(who, main_quest_05)
            player.sex_vag(who, main_quest_05)
            where = renpy.random.choice(["stomach", "pullout", "pullout",  "inside", "inside", "inside", "inside", "inside", "chest", "chest", "face", "face"])
            
            player.sex_cum(who, where, main_quest_05)
            
            player.sex_hideaction()
            relax(15)
            randomnum = renpy.random.randint(1, amount)
        
        else:
            return

    def haven_pay(amount):
        
        if inv.qty(item_cigs) > amount:
            inv.drop(item_cigs, amount)
            return
        else:
            var1 = inv.qty(item_cigs)
            inv.drop(item_cigs, var1)
            var2 = (amount - var1)
            inv.drop(item_brew, var2)
            return

    def haven_gained_intel(intel):
        inv.take(item_haven_intel)  
        log.find("mq_05_info", next=False)


    def haven_complete_questlog(slave=False):
        for i in ("mq_05_upstairs","mq_05_info","mq_05_fire","mq_05_pipes","mq_05_pipesbreak","mq_05_guard","mq_05_sprinklers"):
            if log.interactive(i):
                log.deactivate(i) 
        
        if log.completed("Haven"):
            
            
            return
        if not log.interactive("mq_05_c"):
            log.activate("mq_05_c")
        log.complete_quest("mq_05_c") 
        if slave:
            log.assign("Slave")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
