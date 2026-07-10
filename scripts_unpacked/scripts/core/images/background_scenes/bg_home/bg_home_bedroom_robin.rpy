image bg_bedroom_robin_lighton_layer:
    get_background_filename("bedroom_robin_lighton", False, False)
    bg_tint_transform()
image bg_bedroom_robin_lightoff_layer:
    get_background_filename("bedroom_robin_lightoff", False, False)
    bg_tint_transform()

layeredimage bg_bedroom_robin_robin_oskar_blowjob:
    always "bg_bedroom_robin_blowjob_base"
    if robin.showing:
        "bg_bedroom_robin_blowjob_base_preg"
    if (global_random_number % 2):
        "bg_bedroom_robin_blowjob_baggy"
    else:
        "bg_bedroom_robin_blowjob_hoodie"

layeredimage bg_bedroom_robin_robin_oskar_missionary:
    always "bg_bedroom_robin_missionary"
    if robin.heavy_preg:
        "bg_bedroom_robin_missionary_preg"

layeredimage bg_bedroom_robin_robin_oskar_sex:
    if t.minute < 10:
        "bg_bedroom_robin_robin_oskar_blowjob"
    elif t.minute > 20 and not robin.showing:
        "bg_bedroom_robin_prone"
    else:
        "bg_bedroom_robin_robin_oskar_missionary"

layeredimage bg_bedroom_robin_window:
    if (t.timeofday == "night" or t.hour in (6,7)) and robin.showing:
        "bg_bedroom_robin_robin_window_pj_preg"
    elif (t.timeofday == "night" or t.hour in (6,7)):
        "bg_bedroom_robin_robin_window_pj"

    elif (global_random_number % 2) and robin.showing:
        "bg_bedroom_robin_robin_window_baggy_preg"
    elif (global_random_number % 2):
        "bg_bedroom_robin_robin_window_baggy"

    elif robin.showing:
        "bg_bedroom_robin_robin_window_hoodie_preg"
    else:
        "bg_bedroom_robin_robin_window_hoodie"

layeredimage bg_bedroom_robin_robin:
    if oskar_here():
        "bg_bedroom_robin_robin_oskar_sex"
    elif t.time_from_to(00.00, 06.00):
        "bg_bedroom_robin_robin_sleep"
    else:
        "bg_bedroom_robin_window"

image bg_bedroom_robin_robin_layer:
    "bg_bedroom_robin_robin"
    bg_tint_transform()

layeredimage bg_bedroom_robin:
    if (robin_here() and not t.time_from_to(00.00, 06.00)) or "light_on" in loc_bedroom_robin.list:
        "bg_bedroom_robin_lighton_layer"
    else:
        "bg_bedroom_robin_lightoff_layer"

    if robin_here() and not renpy.showing("robin"):
        "bg_bedroom_robin_robin_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
