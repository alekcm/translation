layeredimage bg_school_gym_troupe_anabel:
    if anabel.showing:
        "bg_school_gym_people_anabel_nude_preg" 
    else:
        "bg_school_gym_people_anabel_nude"
    if school_dance_quest_show_count <= 5:
        "bg_school_gym_people_anabel_tights"
    if anabel.showing and school_dance_quest_show_count >= 8:
        "bg_school_gym_people_anabel_dance2_preg"
    elif school_dance_quest_show_count >= 8:
        "bg_school_gym_people_anabel_dance1"
    elif anabel.showing and school_dance_quest_show_count >= 2:
        "bg_school_gym_people_anabel_dance1_preg"
    elif school_dance_quest_show_count >= 2:
        "bg_school_gym_people_anabel_dance1"
    elif anabel.showing:
        "bg_school_gym_people_anabel_gym_preg"
    else:
        "bg_school_gym_people_anabel_gym"  
layeredimage bg_school_gym_troupe_rachel:
    if rachel.showing:
        "bg_school_gym_people_rachel_nude_preg" 
    else:
        "bg_school_gym_people_rachel_nude"
    if school_dance_quest_show_count <= 5:
        "bg_school_gym_people_rachel_tights"
    if rachel.showing and school_dance_quest_show_count >= 8:
        "bg_school_gym_people_rachel_dance2_preg"
    elif school_dance_quest_show_count >= 8:
        "bg_school_gym_people_rachel_dance1"
    elif rachel.showing and school_dance_quest_show_count >= 2:
        "bg_school_gym_people_rachel_dance1_preg"
    elif school_dance_quest_show_count >= 2:
        "bg_school_gym_people_rachel_dance1"
    else:
        "bg_school_gym_people_rachel_gym" 
layeredimage bg_school_gym_troupe_svet:
    if svet.showing:
        "bg_school_gym_people_svet_nude_preg" 
    else:
        "bg_school_gym_people_svet_nude"
    if school_dance_quest_show_count <= 5:
        "bg_school_gym_people_svet_tights"
    if svet.showing and school_dance_quest_show_count >= 8:
        "bg_school_gym_people_svet_dance2_preg"
    elif school_dance_quest_show_count >= 8:
        "bg_school_gym_people_svet_dance1"
    elif svet.showing and school_dance_quest_show_count >= 2:
        "bg_school_gym_people_svet_dance1_preg"
    elif school_dance_quest_show_count >= 2:
        "bg_school_gym_people_svet_dance1"
    elif svet.showing:
        "bg_school_gym_people_svet_gym_preg"
    else:
        "bg_school_gym_people_svet_gym" 
layeredimage bg_school_gym_troupe_dani:
    if dani.showing:
        "bg_school_gym_people_dani_nude_preg" 
    else:
        "bg_school_gym_people_dani_nude"
    if school_dance_quest_show_count <= 5:
        "bg_school_gym_people_dani_tights"
    if dani.showing and school_dance_quest_show_count >= 8:
        "bg_school_gym_people_dani_dance2_preg"
    elif school_dance_quest_show_count >= 8:
        "bg_school_gym_people_dani_dance1"
    elif dani.showing and school_dance_quest_show_count >= 2:
        "bg_school_gym_people_dani_dance1_preg"
    elif school_dance_quest_show_count >= 2:
        "bg_school_gym_people_dani_dance1"
    elif dani.showing:
        "bg_school_gym_people_dani_gym_preg"
    else:
        "bg_school_gym_people_dani_gym" 

layeredimage bg_school_gym_people_rachel:
    if rachel.showing:
        "bg_school_gym_people_rachel_idle_preg"
    else:
        "bg_school_gym_people_rachel_idle"
layeredimage bg_school_gym_people_svet:
    if svet.showing:
        "bg_school_gym_people_svet_idle_preg"
    else:
        "bg_school_gym_people_svet_idle"

layeredimage bg_school_gym_troupe_rachel_nude_1:
    if rachel.showing:
        "bg_school_gym_people_rachel_nude_preg" 
    else:
        "bg_school_gym_people_rachel_nude"
image bg_school_gym_layer:
    get_background_filename("school_gym", True, False)

layeredimage bg_school_gym_layered:
    always "bg_school_gym_layer"

    if school_dance_trope_present() and not renpy.showing("anabel") and anabel_here():
        "bg_school_gym_troupe_anabel"
    if svet_here() and school_dance_trope_present() and not renpy.showing("svet") and svet_here():
        "bg_school_gym_troupe_svet"
    elif svet_here() and not renpy.showing("svet"):
        "bg_school_gym_people_svet"
    if school_dance_trope_present() and not renpy.showing("dani") and dani_here():
        "bg_school_gym_troupe_dani"
    if rachel_here() and school_dance_trope_present() and not renpy.showing("rachel"):
        "bg_school_gym_troupe_rachel"
    elif rachel_exhib_stripping_show() and (t.hour % 2) == 0 and not renpy.showing("rachel"):
        "bg_school_gym_troupe_rachel_nude_1"
    elif rachel_exhib_stripping_show() and not renpy.showing("rachel"):
        "bg_school_gym_people_rachel_strip_idle"
    elif rachel_exhib_stripping_hide() and (t.hour % 2) == 0 and not renpy.showing("rachel"):
        "bg_school_gym_people_rachel_strip_hide1"
    elif rachel_exhib_stripping_hide() and not renpy.showing("rachel"):
        "bg_school_gym_people_rachel_strip_hide2"

    elif rachel_here() and not renpy.showing("rachel"):
        "bg_school_gym_people_rachel"
    if school_dance_girls_present():
        "bg_school_gym_people_dancers"

image bg_school_gym:
    "bg_school_gym_layered"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
