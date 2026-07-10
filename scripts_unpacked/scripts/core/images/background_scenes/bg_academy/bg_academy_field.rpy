
image bg_school_field_layer:
    get_background_noshad_filename("school_field")
    bg_tint_transform()

layeredimage bg_school_field_people_hangingout_robin:
    if robin_here(loc_school_field_back) and not t.timeofday == "day" and "naked_for_boys" in robin.list:
        "bg_school_field_people_hangingout_robin_nude"
    elif robin_here(loc_school_field_back) and (global_random_number % 2):
        "bg_school_field_people_hangingout_robin_baggy"
    elif robin_here(loc_school_field_back):
        "bg_school_field_people_hangingout_robin_hoodie"

layeredimage bg_school_field_people_watch_mira_layer:
    always "bg_school_field_people_watch_mira"
    if mira.heavy_preg:
        "bg_school_field_people_watch_mira_preg2"
    elif mira.showing:
        "bg_school_field_people_watch_mira_preg1"

layeredimage bg_school_field_people_hangingout_mira:
    if mira_here(loc_school_field_back) and t.hour in (16,17):
        "bg_school_field_people_hangingout_mira_casual"
    elif mira_here(loc_school_field_back) and not t.hour in (16,17):
        "bg_school_field_people_hangingout_mira_whore"

layeredimage bg_school_field_people_hangingout_rachel:
    if rachel_here(loc_school_field_back) and t.timeofday == "day":
        "bg_school_field_people_hangingout_rachel_casual"
    elif rachel_here(loc_school_field_back) and not t.timeofday == "day":
        "bg_school_field_people_hangingout_rachel_nude"

layeredimage bg_school_field_people_layer: robin
    if school_soccer_playing():
        "bg_school_field_people_playing_boys"
    if school_soccer_playing() and mira_here(loc_school_field) and not renpy.showing("mira"):
        "bg_school_field_people_watch_mira_layer"
    if school_soccer_playing() and robin_here(loc_school_field) and not robin.days_pregnant > (global_pregnancy_length * 0.75) and not renpy.showing("robin"):
        "bg_school_field_people_playing_robin"
    elif school_soccer_playing() and robin_here(loc_school_field) and not renpy.showing("robin"):
        "bg_school_field_people_watch_robin"
    if school_soccer_hangingout():
        "bg_school_field_people_hangingout_boys"
    if school_soccer_hangingout() and robin_here(loc_school_field_back):
        "bg_school_field_people_hangingout_robin"
    if school_soccer_hangingout() and rachel_here(loc_school_field_back):
        "bg_school_field_people_hangingout_rachel"
    if school_soccer_hangingout() and mira_here(loc_school_field_back):
        "bg_school_field_people_hangingout_mira"

image bg_school_field_people_image:
    "bg_school_field_people_layer"
    bg_tint_transform()
layeredimage bg_school_field:
    always "bg_school_field_layer"
    always "bg_school_field_people_image"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
