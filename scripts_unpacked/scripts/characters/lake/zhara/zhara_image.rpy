init python:
    def zahra_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.time_from_to(09.00, 17.00) and people_beach():
            cur_location = loc_beach_gym
        elif not zahra.showing and people_nude_beach_vball_canplay() and zahra.hour_number < 6: 
            cur_location = loc_beach_gym
        elif t.time_from_to(17.00, 02.00) and people_beach():
            cur_location = loc_beach_fire
        
        return npc_here_check(location, cur_location, where)


layeredimage zahra_body_layered:
    always "zahra_base"
    if zahra.heavy_preg:
        "zahra_base_preg_2"
    elif zahra.showing:
        "zahra_base_preg_1"

layeredimage zahra_outfit_bikini:
    if zahra.heavy_preg:
        "zahra_outfit_swim_2"
    else:
        "zahra_outfit_swim_0"

layeredimage zahra_outfit_nude:
    always "zahra_breasts"

layeredimage zahra_outfit_standard:
    if people_nude_beach_vball_canplay() and loc(loc_beach_gym):
        "zahra_outfit_nude"
    else:
        "zahra_outfit_bikini"


layeredimage zahra:
    at sprite_highlight("zahra")
    always "zahra_body_layered"
    group outfit auto:
        attribute standard default

    group mouth auto:
        attribute neutral default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
