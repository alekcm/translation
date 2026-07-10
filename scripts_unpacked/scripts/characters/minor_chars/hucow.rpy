init python:
    def hucow_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.hour in workhours:
            cur_location = loc_market_stall_milk
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

layeredimage hucow:
    at sprite_highlight("hucow") 
    always "hucow_base"
    if hucow.heavy_preg:
        "hucow_belly2"
    elif hucow.showing:
        "hucow_belly1"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
