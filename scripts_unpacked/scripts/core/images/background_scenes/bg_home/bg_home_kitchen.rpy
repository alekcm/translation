layeredimage bg_kitchen_emile:
    if t.time_from_to(22.00, 08.00):
        "bg_kitchen_emile_sitting"
    elif (global_random_number % 2):
        "bg_kitchen_emile_standing_dress"
    else:
        "bg_kitchen_emile_standing_casual"



layeredimage bg_kitchen_robin_base:
    always "bg_kitchen_robin_standing_body_base"
    if robin.heavy_preg:
        "bg_kitchen_robin_standing_body_preg2"
    elif robin.showing:
        "bg_kitchen_robin_standing_body_preg1"
layeredimage bg_kitchen_robin_outfit_hoodie:
    always "bg_kitchen_robin_standing_outfit_hoodie_base"
    if robin.heavy_preg:
        "bg_kitchen_robin_standing_outfit_hoodie_preg2"
    elif robin.showing:
        "bg_kitchen_robin_standing_outfit_hoodie_preg1"
layeredimage bg_kitchen_robin_outfit_baggy:
    always "bg_kitchen_robin_standing_outfit_baggy_base"
    if robin.heavy_preg:
        "bg_kitchen_robin_standing_outfit_baggy_preg2"
    elif robin.showing:
        "bg_kitchen_robin_standing_outfit_baggy_preg1"
layeredimage bg_kitchen_robin_outfit_uni:
    always "bg_kitchen_robin_standing_outfit_uni_base"
    if robin.heavy_preg:
        "bg_kitchen_robin_standing_outfit_uni_preg2"
    elif robin.showing:
        "bg_kitchen_robin_standing_outfit_uni_preg1"
layeredimage bg_kitchen_robin_outfit_pj:
    always "bg_kitchen_robin_standing_outfit_pj_base"
    if robin.heavy_preg:
        "bg_kitchen_robin_standing_outfit_pj_preg2"
    elif robin.showing:
        "bg_kitchen_robin_standing_outfit_pj_preg1"

layeredimage bg_kitchen_robin:
    always "bg_kitchen_robin_base"
    if t.wkday in weekdays and t.hour in school_hours:
        "bg_kitchen_robin_outfit_uni"
    elif t.timeofday == "night" or t.hour in (6,7):
        "bg_kitchen_robin_outfit_pj" 
    elif (global_random_number % 2):
        "bg_kitchen_robin_outfit_baggy"
    else:
        "bg_kitchen_robin_outfit_hoodie"

layeredimage bg_kitchen_layer:
    always "bg_kitchen_scene"
    if emile_here() and not renpy.showing("emile"):
        "bg_kitchen_emile"
    if robin_here() and not renpy.showing("robin"):
        "bg_kitchen_robin"

image bg_kitchen:
    "bg_kitchen_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
