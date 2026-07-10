init python:

    def felix_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not felix.has_met or not felix.active:
            cur_location = None
        
        
        elif loc_school_darkroom.open(): 
            cur_location = loc_school_darkroom
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)


layeredimage felix:
    at sprite_highlight("felix")
    always "felix_main"

    group face auto:
        attribute smile default
    always "felix_hair"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
