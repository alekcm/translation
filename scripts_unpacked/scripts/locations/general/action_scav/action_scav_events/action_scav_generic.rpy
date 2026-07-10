init python:
    def item_chance(item, base_weight=10, multi=1, override=False, amount=1, not_have=False, degrade=False):
        global scav_item_found_list
        
        
        
        
        
        
        
        
        if degrade:
            multi = (multi + inv.qty(item))
        
        if override:
            total_weight = override
        else:
            total_weight = (base_weight + item.value) * multi
        if not numgen(0, total_weight):
            if not_have and ((item.clothes and wardrobe.qty(item)) or (not item.clothes and inv.qty(item))):
                return
            else:
                if item.clothes:
                    wardrobe.take(item, 1, all_notif=True) 
                else:
                    inv.take(item, amount)
                scav_item_found_list.append(item)

    def item_picker(scav=True):
        global scav_item_found_list
        
        if dis(dis_haven): 
            item_chance(item_abort_pill, degrade=True)
            item_chance(item_joy, degrade=True)
            item_chance(item_lebo, degrade=True)
            item_chance(item_map_pill, degrade=True)
            item_chance(item_brew, degrade=True)
            item_chance(item_cigs, amount=numgen(1,5), degrade=True)
            item_chance(item_pepperspray, degrade=True)
            item_chance(item_haven_lighter, override=600, not_have=True)
            item_chance(item_haven_fluid, override=600, not_have=True)
            if loc(loc_haven_lounge) and not inv.qty(item_haven_fluid) and haven_time_empty():
                item_chance(item_haven_fluid, override=1, not_have=True)
        
        else:
            
            
            
            item_chance(item_scrap_mag)
            item_chance(item_scrap_junk)
            item_chance(item_scrap_cloth)
            item_chance(item_scrap_book)
            item_chance(item_scrap_metal)
            item_chance(item_scrap_ele)
            
            
            item_chance(item_chis, override=250, not_have=True)
            item_chance(item_saw, override=250, not_have=True)
            item_chance(item_nailpolish, multi=2, not_have=True)
            item_chance(item_contacts, multi=2, not_have=True)
            item_chance(item_hairdye, multi=2, not_have=True)
            item_chance(item_felt_marker, multi=2, not_have=True)
            item_chance(item_perm_marker, multi=2, not_have=True)
            
            
            item_chance(item_beer, multi=5)
            item_chance(item_preg_test, multi=5, degrade=True)
            item_chance(item_tape, multi=5, degrade=True)
            item_chance(item_pepperspray, multi=3, degrade=True)
            
            item_chance(item_milkbottle_empty, multi=5, degrade=True)
            
            
            
            
            
            item_chance(item_abort_pill, multi=If(loc_cur.outside, 3, 1), degrade=True)
            item_chance(item_joy, multi=If(loc_cur.outside, 3, 1), degrade=True)
            item_chance(item_lebo, multi=If(loc_cur.outside, 3, 1), degrade=True)
            item_chance(item_map_pill, multi=If(loc_cur.outside, 3, 1), degrade=True)
            item_chance(item_wakeup, multi=If(loc_cur.outside, 3, 1), degrade=True)
            item_chance(item_cigs, multi=If(loc_cur.outside, 3, 1), amount=numgen(1,5), degrade=True)
            item_chance(item_milktab, multi=If(loc_cur.outside, 3, 1), not_have=True)
            
            
            
            if loc_cur.loc_type == "grass":  
                
                item_chance(item_choker_6, override=100, not_have=True)
            
            if dis(dis_revel):
                
                item_chance(renpy.random.choice(item_clothes_list), not_have=True)
                
                item_chance(item_beer)
                
                item_chance(item_joy, degrade=True)
                item_chance(item_lebo, degrade=True)
                
                
                item_chance(item_scrap_book)
            
            if dis(dis_beach):
                
                
                
                
                item_chance(item_scrap_seashell)
                item_chance(item_scrap_gem)
                item_chance(item_scrap_jewel)
                
                if not player.has_perk(perk_sucu):
                    
                    item_chance(item_sucu_pill, override=200, not_have=True)
                
                
                item_chance(item_abort_pill, degrade=True)
                item_chance(item_joy, degrade=True)
                item_chance(item_lebo, degrade=True)
                item_chance(item_map_pill, degrade=True)
            
            if dis(dis_truckstop):
                
                item_chance(renpy.random.choice(item_clothes_list), not_have=True)
                
                item_chance(item_pinkticket)
            
            if dis(dis_junkyard):
                
                
                item_chance(item_scrap_mag)
                item_chance(item_scrap_junk)
                item_chance(item_scrap_cloth)
                item_chance(item_scrap_metal)
                item_chance(item_scrap_ele)
            
            
            item_chance(renpy.random.choice(item_clothes_list), not_have=True)
        
        if scav:
            loc_cur.scav_last = t.minutes_total
        if scav_item_found_list:
            found = True
        else:
            found = False
        scav_item_found_list = []
        return found

    def check_walk_discover():
        if weightgen(10, t.day): 
            return
        
        if loc(loc_junk_1) and loc_highway_slum.visited and (loc_walk_junk_rails.locked):
            renpy.jump("loc_walk_rails_discover")
        if loc(loc_park_path) and loc_school.visited and loc_walk_park_forest.locked:
            renpy.jump("loc_walk_park_forest_discover")
        if loc(loc_park_gazebo) and loc_lake.visited and loc_walk_park_shrubs.locked:
            renpy.jump("loc_walk_park_lake_discover")


    def scav_discover_walk_park_academy():
        if loc(loc_park_path) and loc_school.visited and loc_walk_park_forest.locked:
            return True
    def scav_discover_walk_junk_slum():
        if loc(loc_junk_1) and loc_highway_slum.visited and (loc_walk_junk_rails.locked):
            return True
    def scav_discover_walk_park_lake():
        if loc(loc_park_gazebo) and loc_lake.visited and loc_walk_park_shrubs.locked:
            return True

    def scav_discover_remind_park():
        if dis(dis_park) and not all([wardrobe.qty(item_choker_6), loc_walk_park_forest.unlocked, loc_walk_park_shrubs.unlocked]):
            return True
    def scav_discover_remind_junk():
        if dis(dis_junkyard) and not loc_walk_junk_rails.unlocked:
            return True
    def scav_discover_remind_beach():
        if dis(dis_beach) and not (inv.qty(item_sucu_pill) or player.has_perk(perk_sucu)):
            return True


label scav_discover_remind_park_event:
    pcm "I'm sure there is something nice to find in the park. I should probably scav around and see."
    jump travel

label scav_discover_remind_junk_event:
    pcm "The junk yard is a perfect place to find something interesting. I should scav around and see what i can find."
    jump travel

label scav_discover_remind_beach_event:
    pcm "People do all manner of shady things around here. I bet there are some drugs I can find if I scav around."
    jump travel


define scav_item_found_list = []

label loc_generic_scavenge:
    $ quest_scav.workcycle = 1
    "I take a walk around looking for any random junk around the floor that might be of value."
    $ working(5)
    $ item_picker()
    pcm "[rlist.scav_search]"
    $ working(5)
    $ item_picker()
    pcm "[rlist.scav_search]"
    $ working(5)
    $ item_picker()
    pcm "[rlist.scav_search]"
    $ working(5)
    $ item_picker()
    pcm "Hmmm..."
    $ check_walk_discover()
    pcm "Phew, that's probably it for now."
    $ quest_scav.work()
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
