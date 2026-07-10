init python:
    def erika_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.time_from_to(09.00, 17.00) and people_beach():
            cur_location = loc_beach_gym
        elif t.time_from_to(21.00, 22.00) and people_beach():
            cur_location = loc_pier
        elif not erika.showing and people_nude_beach_vball_canplay() and erika.hour_number < 5: 
            cur_location = loc_beach_gym
        elif t.time_from_to(17.00, 02.00) and people_beach():
            cur_location = loc_beach_fire
        
        return npc_here_check(location, cur_location, where)



layeredimage erika_body_layered:
    always "erika_base"
    if erika.heavy_preg:
        "erika_base_preg_2"
    elif erika.showing:
        "erika_base_preg_1"

layeredimage erika_outfit_bikini:
    if erika.heavy_preg:
        "erika_clothes_swim_2"
    elif erika.showing:
        "erika_clothes_swim_1"
    else:
        "erika_clothes_swim"

layeredimage erika_outfit_tee:
    if erika.heavy_preg:
        "erika_clothes_tee_2"
    elif erika.showing:
        "erika_clothes_tee_1"
    else:
        "erika_clothes_tee_0"

layeredimage erika_outfit_nude:
    always "erika_breasts"

layeredimage erika_outfit_standard:
    if people_nude_beach_vball_canplay() and loc(loc_beach_gym):
        "erika_outfit_nude"
    elif t.timeofday == "day":
        "erika_outfit_bikini"
    else:
        "erika_outfit_tee"

layeredimage erika:
    at sprite_highlight("erika")
    always "erika_body_layered"
    group outfit auto:
        attribute standard default

    group mouth auto:
        attribute neutral default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
