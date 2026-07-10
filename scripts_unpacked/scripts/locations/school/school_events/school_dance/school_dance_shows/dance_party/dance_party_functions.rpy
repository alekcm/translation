init python:

    def dance_party_sleep_loop_funtion():
        global temp_var_1
        temp_var_1 = 0
        number = numgen(0,2)
        for _ in range(number):
            if not numgen(0, 2):
                temp_var_1 += 1
            if not numgen(0,3) and not acc.anus:
                player.sex_anal(partyman, quest_dancevip)
                player.sex_cum(partyman, "anal", quest_dancevip)
            else:
                player.sex_vag(partyman, quest_dancevip)
                player.sex_cum(partyman, "inside", quest_dancevip)
        player.sex_hideaction()

    def dance_party_serve_wine(drink=False):
        quest_dancevip.dict["wine_amount"] -= 1
        if quest_dancevip.dict["wine_amount"] <= 0:
            quest_dancevip.dict["wine_amount"] = 0
            player.left_hand = ""
        if drink:
            player.drink(spiked=True)

    def dance_party_empty_wine():
        quest_dancevip.dict["wine_amount"] = 0
        player.left_hand = ""

    def dance_party_get_wine():
        quest_dancevip.dict["wine_amount"] = 4
        player.left_hand = "wine_bottle"

    def dance_is_dancing():
        if t.hour in (21,22,23,0,1) and t.minute in irange(0,10):
            return True
        return False

    def dance_party_sex_init(jump_loc=""):
        global event_end_interrupt_label, tempname, tempname2, quest_temp
        
        player.set_whore_price(0)
        dance_party_empty_wine()
        player.grope_end()
        tempname = partyman
        tempname2 = partyman2
        quest_temp = quest_dancevip
        male_npc_create_all()
        event_end_interrupt_label = jump_loc

    def dance_make_girls_dance():
        add_to_list(dani.list, "dancing")
        add_to_list(anabel.list, "dancing")
        add_to_list(rachel.list, "dancing")
        add_to_list(svet.list, "dancing")

    def dance_stop_girls_dance():
        remove_from_list(dani.list, "dancing")
        remove_from_list(anabel.list, "dancing")
        remove_from_list(rachel.list, "dancing")
        remove_from_list(svet.list, "dancing")

    def dance_someone_having_sex():
        for i in [anabel,dani,rachel,svet]:
            if "party_sex" in i.list:
                return True
        else:
            return False

    def dance_pick_who_having_sex():
        girls_list = []
        for i in [anabel,dani,rachel,svet]:
            if "party_sex" in i.list:
                girls_list.append(i._original_name.lower())
        return random(girls_list)

    def dance_everyone_having_sex():
        if all(["party_sex" in anabel.list, "party_sex" in dani.list, "party_sex" in rachel.list, "party_sex" in svet.list]):
            return True
        else:
            return False

    def school_dance_waiting_party():
        if t.wkday == "Saturday" and t.hour == 21 and (log.interactive("quest_dancevip_01") or log.interactive("quest_dancevip_02") or log.interactive("quest_dancevip_04")) and not school_dance_at_party():
            return True
        else:
            return False

    def school_dance_at_party():
        
        if any([log.interactive("quest_dancevip_02"), log.interactive("quest_dancevip_03"), log.interactive("quest_dancevip_04")]):
            if t.wkday == "Saturday" and t.hour in (22,23):
                
                return True
            elif t.wkday == "Sunday" and t.hour in (0,1,2,3,4):
                
                return True
            elif t.wkday == "Saturday" and t.hour == 21 and dis(dis_partyhouse):
                
                return True
        
        return False

    def school_dance_party_time():
        
        if any([log.interactive("quest_dancevip_02"), log.interactive("quest_dancevip_03"), log.interactive("quest_dancevip_04")]) and ((t.wkday == "Saturday" and t.hour in (22,23)) or t.wkday == "Sunday" and t.hour in (0,1,2,3,4,5)):
            return True
        else:
            return False

    def school_dance_party_dancing():
        if school_dance_at_party() and t.hour % 2 == 0 and t.minute in irange(0,30):
            return True
        else:
            return False

    def school_dance_leave_party(who=[]):
        if not who:
            who = [dani, anabel, rachel, svet]
        if not isinstance(who, list):
            who = [who]
        for i in who:
            if i == anabel and quest_dancevip.dict["first_party"] and "party_sex" in anabel.list:
                pass
            elif not "party_sex" in i.list:
                add_to_list(i.list, "left_party")
                remove_from_list(i.list, ["topless", "nude", "party_sex"])

    def dance_min_tick():
        if school_dance_party_time():
            for i in [anabel,dani,rachel,svet]:
                
                if i == anabel and "dance_event_refuse" in anabel.list:
                    pass
                
                if not numgen(0,20):
                    
                    i.drink()
                
                if "party_sex" in i.list and not numgen(0,4):
                    
                    if quest_dancevip.dict["first_party"] and i == anabel:
                        i.have_sex(partyman, anal=False, preg_force=True)
                    else:
                        i.have_sex(partyman, anal_reduce=True)
                
                
                if "left_party" in i.list:
                    
                    pass
                
                elif i == anabel and quest_dancevip.dict["first_party"]:
                    
                    
                    
                    if weightgen(i.drunk, 1500) and i.tipsy:
                        add_to_list(i.list, "topless")
                    if weightgen(i.drunk, 2000) and i.wasted:
                        add_to_list(i.list, "nude")
                    
                    if not "party_sex" in i.list and ("bedroom" in loc_cur.name or not dis(dis_partyhouse)) and i.blackout:
                        
                        add_to_list(i.list, "topless")
                        add_to_list(i.list, "nude")
                        add_to_list(i.list, "party_sex")
                        i.have_sex(partyman, anal=False, preg_force=True)
                
                elif (i == rachel) or (i == dani and dani.iswhore):
                    
                    
                    if weightgen(i.drunk, 500) and i.tipsy:
                        add_to_list(i.list, "topless")
                    if weightgen(i.drunk, 1000) and i.tipsy:
                        add_to_list(i.list, "nude")
                    
                    if weightgen(i.drunk, 1000) and not "party_sex" in i.list and i.tipsy:
                        add_to_list(i.list, "party_sex")
                        if quest_dancevip.dict["first_party"] and i == rachel:
                            i.have_sex(partyman)
                        else:
                            i.have_sex(partyman, anal_reduce=True)
                    
                    if "party_sex" in i.list and weightgen(i.drunk, 1500):
                        remove_from_list(i.list, "party_sex")
                
                else:
                    
                    if weightgen(i.drunk, 1200) and i.tipsy:
                        add_to_list(i.list, "topless")
                    if weightgen(i.drunk, 1800) and i.wasted:
                        add_to_list(i.list, "nude")
                    
                    if weightgen(i.drunk, 2500) and not "party_sex" in i.list and "nude" in i.list and "topless" in i.list and i.wasted:
                        i.have_sex(partyman, anal_reduce=True)
                        add_to_list(i.list, "party_sex")
                    
                    if "party_sex" in i.list and weightgen(i.drunk, 1200):
                        remove_from_list(i.list, "party_sex")
                
                
                
                if t.hour == 4 and t.wkday == "Sunday" and any_in_list(i.list, ["topless", "nude", "party_sex", "left_party"]):
                    if weightgen(1, 20):
                        school_dance_leave_party(i)
                
                elif t.hour >= 5 and t.wkday == "Sunday":
                    
                    remove_from_list(i.list, ["topless", "nude", "party_sex", "left_party"])
                    if quest_dancevip.dict["first_party"] and partyman in anabel.sex_who_class:
                        add_to_list(anabel.list, "bad_end")
                    quest_dancevip.dict["first_party"] = False

    def dance_timeskip_cheat():
        while t.hour != 21:
            t.hour = 1
        while t.wkday != "Saturday":
            t.day = 1



label dance_party_vip_cheat:
    $ walk(loc_revel_backstreet)
    if not quest_dancevip.active:
        $ log.assign("Dance VIP show")

    $ wardrobe.take(item_top_19)
    $ wardrobe.take(item_bottom_13)
    $ wardrobe.take(item_pants_5)
    $ anabel.meet()
    $ dani.meet()
    $ rachel.meet()
    $ svet.meet()
    $ school_dance_quest_show_count = 13
    $ dance_timeskip_cheat()

    "This cheat breaks the dance troupe storyline by skipping to the last event."
    "Go and talk to the girls who you should be able to see in front of you."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
