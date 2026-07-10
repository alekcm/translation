init python:

    def paige_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        
        
        
        
        if t.hour in irange(8,21):
            cur_location = loc_checkpoint_lobby
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)


layeredimage paige_body_layer:
    always "paige_base"
    if paige.heavy_preg:
        "paige_base_belly_2"
    elif paige.showing:
        "paige_base_belly_1"

layeredimage paige_outfit_uni_layer:
    always "paige_outfit_uni"
    if paige.heavy_preg:
        "paige_outfit_uni_2"
    elif paige.showing:
        "paige_outfit_uni_1"


layeredimage paige:
    at sprite_highlight("paige")
    always:
        "paige_body_layer"
    group face auto:
        attribute frown default
    group outfit:
        attribute uni default "paige_outfit_uni_layer"
        attribute nude "paige_outfit_nude"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
