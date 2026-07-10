layeredimage mira_base_layer:
    always "mira_base"
    if mira.days_pregnant > (global_pregnancy_length * 0.7):
        "mira_base_belly2"
    elif mira.days_pregnant > (global_pregnancy_length * 0.3):
        "mira_base_belly1"

layeredimage mira_outfit_uni_layer:
    if mira.days_pregnant > (global_pregnancy_length * 0.7):
        "mira_outfit_uni_2"
    elif mira.days_pregnant > (global_pregnancy_length * 0.3):
        "mira_outfit_uni_1"
    else:
        "mira_outfit_uni_0"

layeredimage mira_outfit_whore_layer:
    if mira.days_pregnant > (global_pregnancy_length * 0.7):
        "mira_outfit_whore_2"
    elif mira.days_pregnant > (global_pregnancy_length * 0.3):
        "mira_outfit_whore_1"
    else:
        "mira_outfit_whore_0"

layeredimage mira_outfit_casual_layer:
    if mira.days_pregnant > (global_pregnancy_length * 0.7):
        "mira_outfit_casual_2"
    elif mira.days_pregnant > (global_pregnancy_length * 0.3):
        "mira_outfit_casual_1"
    else:
        "mira_outfit_casual_0"

layeredimage mira_outfit_hospital_layer:
    if "hospitalised" in mira.list and "rescue_date" in mira.dict and (mira.dict["rescue_date"] + 5) > t.day:
        "mira_bandages"
    always "mira_outfit_gown"

layeredimage mira_outfit_missing_layer:
    always "mira_base_layer"
    always "mira_outfit_nude"
    always "mira_face_worried"
image mira_outfit_missing_image:
    "mira_outfit_missing_layer"
    matrixcolor SaturationMatrix(0.2) * BrightnessMatrix(-0.5)

layeredimage mira_outfit_standard:
    if "hospitalised" in mira.list:
        "mira_outfit_hospital_layer"
    elif not mira.dead and "kidnapped" in mira.list and not "rescued" in mira.list:
        "mira_outfit_missing_image"
    elif mira.dead:
        "mira_outfit_nude"
    elif mira_here(dis_truckstop.locs) or "whore_having_sex" in mira.list:
        "mira_outfit_whore_layer"
    elif t.wkday in weekdays and (t.hour in school_hours or t.hour == 7):
        "mira_outfit_uni_layer"
    else:
        "mira_outfit_casual_layer"

layeredimage mira:
    at sprite_highlight("mira")
    always "mira_base_layer"

    group face auto:
        attribute neutral default

    group outfit:
        attribute standard default:
            "mira_outfit_standard"
        attribute whore:
            "mira_outfit_whore_layer"
        attribute casual:
            "mira_outfit_casual_layer"
        attribute uni:
            "mira_outfit_uni_layer"
        attribute nude:
            "mira_outfit_nude"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
