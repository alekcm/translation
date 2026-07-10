image bg_school_image:
    get_background_filename("school_exterior")
    bg_tint_transform()

layeredimage bg_school_exterior_people_layer:
    if t.wkday in weekdays and (t.time_from_to(07.30, 08.15) or t.hour == 15) and calander_holiday == "":
        "bg_school_exterior_people_girl1"
    if t.wkday in weekdays and (t.time_from_to(07.30, 08.15) or t.hour == 15) and calander_holiday == "" and girl_dummy_5.showing:
        "bg_school_exterior_people_girl1_preg"
    if t.wkday in weekdays and (t.time_from_to(07.30, 08.15) or t.hour == 15) and calander_holiday == "":
        "bg_school_exterior_people_girl2"
    if t.wkday in weekdays and (t.time_from_to(07.30, 08.15) or t.hour == 15) and calander_holiday == "" and girl_dummy_5.showing:
        "bg_school_exterior_people_girl2_preg"
    if not renpy.showing("cass"):
        "bg_school_exterior_cass_layer"
    if not renpy.showing("mira"):
        "bg_school_exterior_mira_layer"
    if not renpy.showing("dani"):
        "bg_school_exterior_dani_layer"
    if not renpy.showing("anabel"):
        "bg_school_exterior_anabel_layer"
    if not renpy.showing("rachel"):
        "bg_school_exterior_rachel_layer"

layeredimage bg_school_exterior_cass_layer:
    if cass_here(loc_school) and t.hour > 12 and cass.showing:
        "bg_school_exterior_people_cass_casual_preg"
    elif cass_here(loc_school) and t.hour > 12:
        "bg_school_exterior_people_cass_casual"
    elif cass_here(loc_school) and cass.showing:
        "bg_school_exterior_people_cass_uni_preg"
    elif cass_here(loc_school):
        "bg_school_exterior_people_cass_uni"
layeredimage bg_school_exterior_mira_layer:
    if mira_here(loc_school) and t.hour > 12 and mira.showing:
        "bg_school_exterior_people_mira_casual_preg"
    elif mira_here(loc_school) and t.hour > 12:
        "bg_school_exterior_people_mira_casual"
    elif mira_here(loc_school) and mira.showing:
        "bg_school_exterior_people_mira_uni_preg"
    elif mira_here(loc_school):
        "bg_school_exterior_people_mira_uni"

layeredimage bg_school_exterior_dani_layer:
    if dani_here() and dani.showing:
        "bg_school_exterior_people_dani_preg"
    elif dani_here():
        "bg_school_exterior_people_dani"
layeredimage bg_school_exterior_anabel_layer:
    if anabel_here() and anabel.showing:
        "bg_school_exterior_people_anabel_preg"
    elif anabel_here():
        "bg_school_exterior_people_anabel"

layeredimage bg_school_exterior_rachel_layer:
    if rachel_here(loc_school) and rachel.showing:
        "bg_school_exterior_people_rachel_preg"
    if rachel_here(loc_school):
        "bg_school_exterior_people_rachel"

image bg_school_people_image:
    "bg_school_exterior_people_layer"
    bg_tint_transform()

layeredimage bg_school:
    always "bg_school_image"
    always "bg_school_people_image"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
