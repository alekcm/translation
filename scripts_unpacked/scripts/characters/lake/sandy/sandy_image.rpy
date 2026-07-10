init python:
    def sandy_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.hour in irange(8,20):
            cur_location = loc_boardwalk
        elif t.time_from_to(07.00, 22.00) and people_beach():
            cur_location = loc_pier
        elif not sandy.showing and people_nude_beach_vball_canplay() and sandy.hour_number < 8: 
            cur_location = loc_beach_gym
        elif t.time_from_to(21.00, 02.00) and people_beach():
            cur_location = loc_beach_fire
        
        return npc_here_check(location, cur_location, where)

layeredimage sandy_body_layered:
    always "sandy_base"
    if sandy.heavy_preg:
        "sandy_base_preg_2"
    elif sandy.showing:
        "sandy_base_preg_1"

layeredimage sandy_outfit_bikini:
    if sandy.heavy_preg:
        "sandy_outfit_bikini_2"
    else:
        "sandy_outfit_bikini_0"

layeredimage sandy_outfit_standard:
    if people_nude_beach_vball_canplay() and loc(loc_beach_gym):
        "sandy_outfit_nude"
    else:
        "sandy_outfit_bikini"

layeredimage sandy:
    at sprite_highlight("sandy")
    always "sandy_body_layered"
    group outfit auto:
        attribute standard default

    group face auto:
        attribute neutral default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
