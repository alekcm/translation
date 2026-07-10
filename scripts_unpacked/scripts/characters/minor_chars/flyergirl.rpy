init python:
    def flyergirl_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not flyergirl.has_met and t.hour in workhours:
            cur_location = loc_market
        elif t.hour in workhours and flyergirl.hour_number > 1 and t.hour in workhours:
            cur_location = loc_market
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

layeredimage flyergirl:
    at sprite_highlight("flyergirl")
    always "flyergirl_base"
    if flyergirl.heavy_preg:
        "flyergirl_preg2"
    elif flyergirl.showing:
        "flyergirl_preg1"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
