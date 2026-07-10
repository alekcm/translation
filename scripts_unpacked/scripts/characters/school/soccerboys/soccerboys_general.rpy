init python:

    def drake_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not drake.has_met or not drake.active:
            cur_location = None
        elif t.wkday in weekdays and t.hour == 12:
            cur_location = loc_school_cafe
        elif school_soccer_hangingout() and "soccer_sex_robin" in drake.list and not "soccer_free_use" in robin.list: 
            if weather_var > 2 or t.month == "Winter":
                cur_location = loc_school_locker_old
            else:
                cur_location = loc_school_field_back_isolate
        elif school_soccer_playing(): 
            cur_location = loc_school_field
        elif school_soccer_hangingout(): 
            cur_location = loc_school_field_back
        elif t.hour in workhours:
            cur_location = dis_school
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def nate_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not nate.has_met or not nate.active:
            cur_location = None
        elif "no_location" in nate.list: 
            cur_location = None
        
        elif t.wkday in weekdays and t.hour == 12:
            cur_location = loc_school_cafe
        elif school_soccer_hangingout() and "soccer_sex_robin" in nate.list and not "soccer_free_use" in robin.list: 
            if weather_var > 2 or t.month == "Winter":
                cur_location = loc_school_locker_old
            else:
                cur_location = loc_school_field_back_isolate
        elif school_soccer_playing(): 
            cur_location = loc_school_field
        elif school_soccer_hangingout(): 
            cur_location = loc_school_field_back
        elif t.hour in workhours:
            cur_location = dis_school
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def dan_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not dan.has_met or not dan.active:
            cur_location = None
        elif t.wkday in weekdays and t.hour == 12:
            cur_location = loc_school_cafe
        elif school_soccer_hangingout() and "soccer_sex_robin" in dan.list and not "soccer_free_use" in robin.list: 
            if weather_var > 2 or t.month == "Winter":
                cur_location = loc_school_locker_old
            else:
                cur_location = loc_school_field_back_isolate
        elif school_soccer_playing(): 
            cur_location = loc_school_field
        elif school_soccer_hangingout(): 
            cur_location = loc_school_field_back
        elif t.hour in workhours:
            cur_location = dis_school
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
