init python:
    def mateo_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.time_from_to(10.00, 15.00) and people_beach():
            cur_location = loc_beach_gym
        elif t.time_from_to(18.00, 02.00) and people_beach():
            cur_location = loc_beach_fire
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
