init python:
    def terry_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not mason.has_met or not mason.active:
            cur_location = None
        elif "no_location" in mason.list: 
            cur_location = None 
        
        elif t.hour in irange(8, 15) and t.wkday in weekdays:
            cur_location = loc_school_gym
        elif people_nude_beach_vball_canplay(): 
            cur_location = loc_beach_gym
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def mason_here(location=None, where=False, class_loc=False):
        return terry_here(location, where, class_loc)

layeredimage mason_penis:
    if mason.want_sex():
        "mason_outfit_hard"
    else:
        "mason_outfit_soft"

layeredimage mason:
    at sprite_highlight("mason")

    always "mason_base"
    group face auto:
        attribute neutral default
    group outfit auto:
        attribute gym default
        attribute nude "mason_penis"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
