layeredimage bg_revel_backstreet_people_dani:
    if dani.showing:
        "bg_revel_backstreet_people_dani_preg"
    always "bg_revel_backstreet_people_dani_base"
layeredimage bg_revel_backstreet_people_svet:
    always "bg_revel_backstreet_people_svet_base"
    if svet.showing:
        "bg_revel_backstreet_people_svet_preg"
layeredimage bg_revel_backstreet_people_rachel:
    always "bg_revel_backstreet_people_rachel_base"
    if rachel.showing:
        "bg_revel_backstreet_people_rachel_preg"
layeredimage bg_revel_backstreet_people_anabel:
    always "bg_revel_backstreet_people_anabel_base"
    if anabel.showing:
        "bg_revel_backstreet_people_anabel_preg"

image bg_revel_backstreet_scene:
    get_background_filename("revel_backstreet", winter=False, night=True)

layeredimage bg_revel_backstreet_layered:
    always "bg_revel_backstreet_scene"
    if anabel_here() and not renpy.showing("anabel"):
        "bg_revel_backstreet_people_anabel"
    if rachel_here() and not renpy.showing("rachel"):
        "bg_revel_backstreet_people_rachel"
    if dani_here() and not renpy.showing("dani"):
        "bg_revel_backstreet_people_dani"
    if svet_here() and not renpy.showing("svet"):
        "bg_revel_backstreet_people_svet"

image bg_revel_backstreet:
    "bg_revel_backstreet_layered"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
