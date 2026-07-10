init python:
    def samira_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.time_from_to(14.00, 04.00):
            if rose.hour_number in (0,1,2): 
                cur_location = loc_highway
            elif rose.hour_number  in (3,4,5):
                cur_location = loc_motel
            elif rose.hour_number  in (6,7,8):
                cur_location = loc_truckstop
            else:
                cur_location = loc_highway_slum
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)
    def rose_here(location=None, where=False, class_loc=False):
        return samira_here(location, where, class_loc)

    def nilay_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.time_from_to(12.00, 02.00):
            if charity.hour_number in (0,1,2):
                cur_location = loc_highway
            elif charity.hour_number  in (3,4,5):
                cur_location = loc_motel
            elif charity.hour_number  in (6,7,8):
                cur_location = loc_truckstop
            else:
                cur_location = loc_highway_slum
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)
    def charity_here(location=None, where=False, class_loc=False):
        return nilay_here(location, where, class_loc)



    def vivian_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.time_from_to(14.00, 00.00):
            if pursy.hour_number in (0,1,2):
                cur_location = loc_highway
            elif pursy.hour_number  in (3,4,5):
                cur_location = loc_motel
            elif pursy.hour_number  in (6,7,8):
                cur_location = loc_truckstop
            else:
                cur_location = loc_highway_slum
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def pursy_here(location=None, where=False, class_loc=False):
        return vivian_here(location, where, class_loc)

layeredimage rose:
    at sprite_highlight("rose")  
    always "whore_1_base"
    if rose.heavy_preg:
        "whore_1_belly_2"
    elif rose.showing:
        "whore_1_belly_1"

layeredimage charity:
    at sprite_highlight("charity")
    always "whore_2_base"
    if charity.heavy_preg:
        "whore_2_belly_2"
    elif charity.showing:
        "whore_2_belly_1"

layeredimage pursy:
    at sprite_highlight("pursy")
    always "whore_4_base"
    if pursy.heavy_preg:
        "whore_4_belly_2"
    elif pursy.showing:
        "whore_4_belly_1"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
