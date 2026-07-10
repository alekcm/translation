
image bg_school_classroom_layer:
    get_background_filename("school_classroom", True, False)
    bg_tint_transform()

layeredimage bg_school_classroom_people_layer:
    if t.wkday in weekdays and t.hour in (9,10,11,12,13,14,15):
        "bg_school_classroom_people_girlsittalk"
    if t.wkday in weekdays and t.hour in (10,11,13,14):
        "bg_school_classroom_people_girlcross"
    if t.wkday in weekdays and t.hour in (10,11,13,14,15):
        "bg_school_classroom_people_girlclose"
    if t.wkday in weekdays and t.hour in (12,15,16,17):
        "bg_school_classroom_people_boystand"
    if t.wkday in weekdays and t.hour in (8,12,13,14,15,16):
        "bg_school_classroom_people_girlstand"
    if t.wkday in weekdays and t.hour in (8,12,13,14,15,16) and girl_dummy_3.showing:
        "bg_school_classroom_people_girlstand_pregl"
    if t.wkday in weekdays and t.hour in (8,12,13,14,15,16) and girl_dummy_6.showing:
        "bg_school_classroom_people_girlstand_pregr"
    if t.wkday in weekdays and t.hour in (11,14,15,16):
        "bg_school_classroom_people_boyclose"
    if not renpy.showing("cass"):
        "bg_school_classroom_cass_layer"
    if not renpy.showing("mira"):
        "bg_school_classroom_mira_layer"
    if anabel_here() and not renpy.showing("anabel"):
        "bg_school_classroom_people_anabel"

layeredimage bg_school_classroom_cass_layer:  
    if cass_here(loc_school_classroom) and cass.showing:
        "bg_school_classroom_people_cass_preg"
    elif cass_here(loc_school_classroom):
        "bg_school_classroom_people_cass"

layeredimage bg_school_classroom_mira_layer:  
    if mira_here(loc_school_classroom) and mira.showing:
        "bg_school_classroom_people_mira_preg"
    elif mira_here(loc_school_classroom):
        "bg_school_classroom_people_mira"

image bg_school_classroom_people:
    "bg_school_classroom_people_layer"
    bg_tint_transform()

layeredimage bg_school_classroom:
    always "bg_school_classroom_layer"
    always "bg_school_classroom_people"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
