define school_dance_quest_preg = False
define school_dance_quest_on_team = False
define school_dance_quest_show_count = 0

init python:
    def school_dance_has_main_clothes():
        
        if not wardrobe.qty(item_bottom_13) or not If(school_dance_quest_show_count >= 11,  wardrobe.qty(item_top_19),  wardrobe.qty(item_top_20)):
            return False
        return True

    def school_dance_missing_clothes():
        
        if not c.pants:
            return "pants"
        elif school_dance_quest_show_count < 11 and not c.bra:
            return "bra"
        elif school_dance_quest_show_count < 8 and not c.socks:
            return "socks"



    def school_dance_set_clothes(): 
        work.reset_clothes()
        if school_dance_quest_show_count >= 11:
            work.top = 19
        else:
            work.top = 20
        work.bottom = 13
        if school_dance_quest_show_count >= 11:
            work.bra = 0
        else:
            work.bra = 3
        
        if school_dance_quest_show_count >= 9 and player.has_perk(perk_commando) or "messy_wore_commando" in quest_dance.list:
            work.pants = 0
        elif school_dance_quest_show_count >= 11 or (school_dance_quest_show_count == 9 and "messy_wore_thong" in quest_dance.list and not dis(dis_school)):
            work.pants = 5
        else:
            work.pants = 3 
        
        if school_dance_quest_show_count >= 8:
            work.socks = 0
        else:
            work.socks = 1
        
        work.top_primary_colour = "white"
        work.bottom_primary_colour = "black"
        work.bra_primary_colour = "grey"
        work.bra_secondary_colour = "grey"
        if work.pants == 3:
            work.pants_primary_colour = "black"
            work.pants_secondary_colour = "black"
        else:
            work.pants_primary_colour = "pink"
            work.pants_secondary_colour = "pink"
        work.socks_primary_colour = "black"
        work.socks_secondary_colour = "black"
        for i in clothes_wardrobe_list:
            setattr(work, i + "primary_trans", "trans_normal")
            setattr(work, i + "secondary_trans", "trans_normal")
        work.socks_primary_trans = "trans_trans"

    def show_dance_image():
        if school_dance_quest_show_count < 2 or not "work" in tab_top:
            renpy.scene()
            renpy.show("activity_dance")
            renpy.with_statement(dissolve)
            return
        
        image_list = ["dance_girls_rachel", "dance_girls_svet", "dance_behind", "ps_dance", "activity_dance"]
        if not dani.dead:
            image_list.append("dance_girls_dani")
        if not (anabel.hate or "dance_event_refuse" in anabel.list):
            image_list.append("dance_girls_anabel")
        image_list_new = []
        for i in image_list:
            if not renpy.showing(i):
                image_list_new.append(i)
        renpy.scene()
        renpy.show(renpy.random.choice(image_list_new))
        renpy.with_statement(dissolve)

    def show_dance_pole_image(pc_only=False):
        image_list = []
        
        if not pc_only:
            
            if svet_here():
                add_to_list(image_list, ["svet_poledance_1", "svet_poledance_2", "dance_girls_svet"])
            if rachel_here():
                add_to_list(image_list, ["rachel_poledance_1", "dance_girls_rachel"])
            if dani_here():
                add_to_list(image_list, ["dani_poledance_2", "dance_girls_dani"])
                if not dani.showing:
                    add_to_list(image_list, "dani_poledance_1")
            if anabel_here():
                add_to_list(image_list, ["anabel_poledance_1", "dance_girls_anabel"])
        
        add_to_list(image_list, ["dance_behind", "ps_dance", "activity_dance"])
        image_list_new = []
        for i in image_list:
            if not renpy.showing(i):
                image_list_new.append(i)
        
        renpy.scene()
        renpy.show(renpy.random.choice(image_list_new))
        renpy.with_statement(dissolve)

    def show_dance_collect_image():
        image_list = ["dance_girls_anabel", "dance_girls_rachel", "dance_girls_dani", "dance_girls_svet", "dance_behind", "ps_dance", "activity_dance"]
        
        if not dani.dead:
            image_list.append("dance_girls_dani")
        if not anabel.hate:
            image_list.append("dance_girls_anabel")
        
        image_list_new = []
        for i in image_list:
            if not renpy.showing(i):
                image_list_new.append(i)
        renpy.scene()
        renpy.show(renpy.random.choice(image_list_new))
        renpy.with_statement(dissolve)

    def dance_hide_girls():
        add_to_list(dani.list, "no_location")
        add_to_list(svet.list, "no_location")
        add_to_list(anabel.list, "no_location")
        add_to_list(rachel.list, "no_location")

    def dance_unhide_girls():
        remove_from_list(dani.list, "no_location")
        remove_from_list(svet.list, "no_location")
        remove_from_list(anabel.list, "no_location")
        remove_from_list(rachel.list, "no_location")

    def school_dance_can_ask_join_team():
        if school_dance_quest_on_team == False and (player.fitness >= 30 or (player.pregnancy == 0 and t.day >= 10) or t.day >= 25 or (t.day > 10 and all([svet.has_met, rachel.has_met, dani.has_met, anabel.has_met]))):
            return True
        return False

    def school_dance_quest_show_count_cheat(amount):
        global school_dance_quest_show_count
        school_dance_quest_show_count += amount
        if school_dance_quest_show_count < 0:
            school_dance_quest_show_count = 0
        if school_dance_quest_show_count > 20:
            school_dance_quest_show_count = 0


    def school_dance_event_active():
        if t.wkday in ["Monday", "Tuesday", "Wednesday"] and t.hour in irange(13,16) and school_dance_quest_on_team:
            return True
        else:
            return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
