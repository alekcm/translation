init python:
    def neighbour_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if "sex" in neighbour.list:
            cur_location = loc_highway_slum_home
        
        elif t.hour in night:
            if neighbour.hour_number <= 3:
                cur_location = loc_motel
            elif neighbour.hour_number >= 8:
                cur_location = loc_highway
            else:
                cur_location = loc_highway_slum_street
        
        elif t.hour == 6: 
            cur_location = None
        
        else:
            cur_location = loc_highway_slum_home
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def neighbour_routine(mins):
        
        
        if not dis(dis_truckstop) or neighbour.dead:
            
            return
        
        for _ in range(mins):
            
            
            
            
            if not "sex_time" in neighbour.dict:
                neighbour.dict["sex_time"] = 0
            
            if not loc_highway_slum_home.locked and neighbour.dict["sex_time"] > 0 and abs(neighbour.dict["sex_time"] - t.minutes_total) > 6 and "sex" in neighbour.list and not numgen(0, 5000):
                add_to_list(neighbour.list, "dead_choke")
                neighbour.kill()
            if not loc_highway_slum_home.locked and t.hour == 9 and not numgen(0, 20000):
                add_to_list(neighbour.list, "dead_od")
                neighbour.kill()
            
            if neighbour.dict["sex_time"] < t.minutes_total or not t.hour in night:
                remove_from_list(neighbour.list, "sex")
            
            
            if not t.hour in night:
                remove_from_list(neighbour.list, "whoring")
            
            
            
            if t.hour in night: 
                add_to_list(neighbour.list, "whoring")
                if not numgen(0,15):
                    add_to_list(neighbour.list, "sex")
                    neighbour.dict["sex_time"] = numgen((t.minutes_total + 10), (t.minutes_total + 20))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
