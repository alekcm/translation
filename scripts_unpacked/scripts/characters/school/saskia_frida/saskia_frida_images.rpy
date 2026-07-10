init python:
    def frida_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.hour in irange(8,15) and t.wkday in weekdays: 
            cur_location = loc_school_sewroom
        elif t.hour in irange(16,20) and t.wkday in weekdays and not (global_random_number % 2) == 0: 
            cur_location = loc_school_sewroom
        elif t.hour in irange (16, 20) and (global_random_number % 2) == 0 and t.wkday in weekdays: 
            cur_location = loc_market_stall_needle
        elif t.hour in irange(8,20) and t.wkday in weekend: 
            cur_location = loc_market_stall_needle
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)



    def saskia_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        
        if t.hour in irange(8,15) and location == loc_school_sewroom and t.wkday in weekdays: 
            cur_location = loc_school_sewroom
        elif t.hour in irange(8,20) and t.wkday in weekdays and (global_random_number % 2) == 0: 
            cur_location = loc_school_sewroom
        elif t.hour in irange (16, 20) and not (global_random_number % 2) == 0 and t.wkday in weekdays: 
            cur_location = loc_market_stall_needle
        elif t.hour in irange(8,20) and t.wkday in weekend: 
            cur_location = loc_market_stall_needle
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def saskia_frida_here(location=None):
        if any([saskia_here(location), frida_here(location)]):
            return True
        else:
            return False

layeredimage frida_body_layer:
    always "frida_base"
    if frida.heavy_preg:
        "frida_belly_2"
    elif frida.showing:
        "frida_belly_1"

layeredimage frida_outfit_uni_layer:
    if frida.heavy_preg:
        "frida_outfit_sailor_2"
    elif frida.showing:
        "frida_outfit_sailor_1"
    else:
        "frida_outfit_sailor_0"

layeredimage frida:

    always "frida_body_layer"

    group outfit:
        attribute nude null
        attribute no_outfit null
        attribute uni default "frida_outfit_uni_layer"

    group face auto:
        attribute neutral default

    always "frida_hair"


layeredimage saskia_body_layer:
    always "saskia_base"
    if saskia.heavy_preg:
        "saskia_belly_2"
    elif saskia.showing:
        "saskia_belly_1"

layeredimage saskia_outfit_uni_layer:
    if saskia.heavy_preg:
        "saskia_outfit_uni_2"
    elif saskia.showing:
        "saskia_outfit_uni_1"
    else:
        "saskia_outfit_uni_0"

layeredimage saskia:

    always "saskia_body_layer"
    group outfit:
        attribute nude null
        attribute no_outfit null
        attribute uni default "saskia_outfit_uni_layer"

    group face auto:
        attribute neutral default

    always "saskia_hair"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
