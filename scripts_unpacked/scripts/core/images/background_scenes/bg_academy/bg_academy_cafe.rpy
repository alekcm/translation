layeredimage bg_school_cafe_people_layer:
    if drake_here() and not renpy.showing("drake"):
        "bg_school_cafeteria_people_drake"
    if nate_here() and not renpy.showing("nate"):
        "bg_school_cafeteria_people_nate"
    if dan_here() and not renpy.showing("dan"):
        "bg_school_cafeteria_people_dan"
    if robin_here() and not renpy.showing("robin"):
        "bg_school_cafeteria_people_robin"


    if t.wkday in weekdays and t.hour in (10,11,13,14,15):
        "bg_school_cafeteria_people_girlalone"
    if t.wkday in weekdays and t.hour in (8,12,14):
        "bg_school_cafeteria_people_girlboy"
    if t.wkday in weekdays and t.hour in (8,12,14) and girl_dummy_3.showing:
        "bg_school_cafeteria_people_girlboypreg"
    if t.wkday in weekdays and t.hour == 12:
        "bg_school_cafeteria_people_girlwalk"
    if t.wkday in weekdays and t.hour == 12 and girl_dummy_1.showing:
        "bg_school_cafeteria_people_girlwalkpreg"
    if t.wkday in weekdays and t.hour in (8,12,13,14,15,16):
        "bg_school_cafeteria_people_guyfar"
    if t.wkday in weekdays and t.hour in (11, 12, 14,15,16):
        "bg_school_cafeteria_people_guyfarback"
    if rachel_here() and not renpy.showing("rachel"):
        "bg_school_cafeteria_people_rachel"
    if svet_here() and not renpy.showing("svet"):
        "bg_school_cafeteria_people_svet"
    if t.wkday in weekdays and t.hour in (8,12,15):
        "bg_school_cafeteria_people_girlsleft"
    if t.wkday in weekdays and t.hour in (8,12,14,15):
        "bg_school_cafeteria_people_girlsright"
    if not renpy.showing("dani"):
        "bg_school_cafe_people_dani_layer"
    if not renpy.showing("anabel"):
        "bg_school_cafe_people_anabel_layer"
    if not renpy.showing("cass"):
        "bg_school_cafe_people_cass_layer"
    if not renpy.showing("mira"):
        "bg_school_cafe_people_mira_layer"

layeredimage bg_school_cafe_people_cass_layer:
    if cass_here(loc_school_cafe):
        "bg_school_cafeteria_people_cass"
    if cass_here(loc_school_cafe) and cass.showing:
        "bg_school_cafeteria_people_casspreg"
layeredimage bg_school_cafe_people_mira_layer:
    if mira_here(loc_school_cafe):
        "bg_school_cafeteria_people_mira"
    if mira_here(loc_school_cafe) and mira.showing:
        "bg_school_cafeteria_people_mirapreg"
layeredimage bg_school_cafe_people_dani_layer:
    if dani_here(loc_school_cafe):
        "bg_school_cafeteria_people_dani"
    if dani_here(loc_school_cafe) and dani.showing:
        "bg_school_cafeteria_people_dani_preg"
layeredimage bg_school_cafe_people_anabel_layer:
    if anabel_here(loc_school_cafe):
        "bg_school_cafeteria_people_anabel"
    if anabel_here(loc_school_cafe) and anabel.showing:
        "bg_school_cafeteria_people_anabel_preg"

image bg_school_cafe_layer:
    get_background_filename("school_cafeteria", True, False)
    bg_tint_transform()

layeredimage bg_school_cafe:
    always "bg_school_cafe_layer"
    always "bg_school_cafe_people_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
