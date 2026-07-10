layeredimage bg_common_emile_layer:
    if t.hour in irange(0,6):
        "bg_common_emile_sleep"
    elif t.timeofday == "night":
        "bg_common_emile_sit_pj"
    elif (global_random_number % 2):
        "bg_common_emile_sit_dress"
    else:
        "bg_common_emile_sit_casual"

layeredimage bg_common_robin_layer:
    if "common_passout" in robin.list and robin.showing:
        "bg_common_robin_sleep_preg"
    elif "common_passout" in robin.list:
        "bg_common_robin_sleep"

    elif t.timeofday == "night" and robin.showing: 
        "bg_common_robin_sit_pj_preg"
    elif t.timeofday == "night":
        "bg_common_robin_sit_pj"

    elif t.wkday in weekdays and t.hour in school_hours and robin.showing:
        "bg_common_robin_sit_uni_preg"
    elif t.wkday in weekdays and t.hour in school_hours:
        "bg_common_robin_sit_uni"

    elif (global_random_number % 2) and robin.showing:
        "bg_common_robin_sit_baggy_preg"
    elif (global_random_number % 2):
        "bg_common_robin_sit_baggy"

    elif robin.showing:
        "bg_common_robin_sit_hoodie_preg"
    else:
        "bg_common_robin_sit_hoodie"

layeredimage bg_common_layer:
    always "bg_common_scene"
    if emile_here() and not renpy.showing("emile"):
        "bg_common_emile_layer"
    if robin_here() and not renpy.showing("robin"):
        "bg_common_robin_layer"

image bg_common:
    "bg_common_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
