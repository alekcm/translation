init python:
    def motel_recep_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.hour in irange(2,10):
            cur_location = loc_motel_room2 
        elif t.minute in irange(45,55):
            cur_location = loc_motel
        else:
            cur_location = loc_motel_lobby
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

layeredimage motel_recep:
    at sprite_highlight("motel_recep")
    always "motel_recep_base"
    if motel_recep.heavy_preg:
        "motel_recep_belly_2"
    elif motel_recep.showing:
        "motel_recep_belly_1"

    group face auto:
        attribute happy default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
