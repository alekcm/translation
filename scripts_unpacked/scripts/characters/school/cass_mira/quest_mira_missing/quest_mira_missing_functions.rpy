init python:

    def quest_mira_missing_kidnap():
        
        if mira.inv.qty(item_pepperspray):
            add_to_list(mira.list, "kidnapped_fail")
            return
        mira.active = False
        add_to_list(mira.list, "kidnapped")
        mira.dict["kidnap_date"] = t.day

    def quest_mira_missing_kidnap_whore_outfit_set():
        quest_mira_missing.top_primary_colour = "black"  
        quest_mira_missing.bottom_primary_colour = "black"
        
        for i in clothes_wardrobe_list:
            setattr(quest_mira_missing, i, 0)
        quest_mira_missing.top = 36
        quest_mira_missing.bottom = 28

    def quest_mira_whore_can_investigate():
        if quest_mira_missing.active and log.interactive("mira_missing_08"):
            return True
        else:
            return False

    def quest_mira_whore_whore_name_picker():
        global tempname
        people = []
        for person in [rose, kitty, charity, pursy]:
            if person._original_name.lower() + "_here" in globals() and globals()[person._original_name.lower() + "_here"]():
                people.append(person)
        if people:
            tempname = renpy.random.choice(people)
        else:
            tempname = whore

    def quest_mira_intel_weight():
        if (player.check_int(4, notif=False) or not numgen(0,50)) and quest_mira_whore_can_investigate():
            
            return True
        else:
            return False

    def quest_mira_intel_trigger(jump_loc="quest_mira_missing_intel_whore_customer_picker"):
        if quest_mira_whore_can_investigate() and weightgen(sum([quest_whore.sex, quest_mira_missing.sex, (quest_whore.osex / 2), (quest_mira_missing.osex / 2), 1]), 20) and dis(dis_truckstop) and player.allure > 200:
            renpy.call(jump_loc)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
