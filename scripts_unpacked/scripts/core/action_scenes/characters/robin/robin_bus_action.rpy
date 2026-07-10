layeredimage robin_bus_grope_front_outfit_uni:
    always "robin_bus_grope_front_outfit_uni_base"
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_bus_grope_front_outfit_uni_preg_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_bus_grope_front_outfit_uni_preg_1"

layeredimage robin_bus_grope_front:
    always "robin_bus_grope_front_base"
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_bus_grope_front_belly_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_bus_grope_front_belly_1"

    if t.wkday in weekdays and t.hour in school_hours:
        "robin_bus_grope_front_outfit_uni"
    elif (global_random_number % 2):
        "robin_bus_grope_front_outfit_baggy"
    else:
        "robin_bus_grope_front_outfit_hoodie"
    always "robin_bus_grope_front_pole"


layeredimage robin_bus_grope_behind_outfit_uni:
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_bus_grope_behind_outfit_uni_preg_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_bus_grope_behind_outfit_uni_preg_1"
    always "robin_bus_grope_behind_outfit_uni_main"

layeredimage robin_bus_grope_behind_outfit_hoodie:
    always "robin_bus_grope_behind_outfit_hoodie_main"
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_bus_grope_behind_outfit_hoodie_preg_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_bus_grope_behind_outfit_hoodie_preg_1"

layeredimage robin_bus_grope_behind:
    always "robin_bus_grope_behind_bg"

    group man:
        attribute no_man default null
        attribute man "robin_bus_grope_behind_man_body"
        attribute grope "robin_bus_grope_behind_man_body"
        attribute no_grope "robin_bus_grope_behind_man_body"

    always "robin_bus_grope_behind_base"
    if robin.days_pregnant > (global_pregnancy_length * 0.75):
        "robin_bus_grope_behind_base_preg_2"
    elif robin.days_pregnant > (global_pregnancy_length * 0.3):
        "robin_bus_grope_behind_base_preg_1"

    if t.wkday in weekdays and t.hour in school_hours:
        "robin_bus_grope_behind_outfit_uni"
    elif (global_random_number % 2):
        "robin_bus_grope_behind_outfit_baggy_main"
    else:
        "robin_bus_grope_behind_outfit_hoodie"

    group man:
        attribute no_man default null
        attribute man null
        attribute grope "robin_bus_grope_behind_man_grope"
        attribute no_grope null

    if t.wkday in weekdays and t.hour in school_hours:
        if_not ["grope"] "robin_bus_grope_behind_outfit_uni_norm"
    elif (global_random_number % 2):
        if_not ["grope"] "robin_bus_grope_behind_outfit_baggy_norm"

    if t.wkday in weekdays and t.hour in school_hours:
        if_any ["grope"] "robin_bus_grope_behind_outfit_uni_grope"
    elif (global_random_number % 2):
        if_any ["grope"] "robin_bus_grope_behind_outfit_baggy_grope"
    else:
        if_any ["grope"] "robin_bus_grope_behind_outfit_hoodie_grope"

    always "robin_bus_grope_behind_frame"

image robin_bus_sex = LayeredImageProxy("robin_bus_sex_layered", Transform(align=(0.7, 0.0)))

layeredimage robin_bus_sex_layered:
    always "robin_bus_sex_bg"

    if t.wkday in weekdays and t.hour in school_hours:
        "robin_bus_sex_outfit_uni"
    elif (global_random_number % 2):
        "robin_bus_sex_outfit_baggy"
    else:
        "robin_bus_sex_outfit_hoodie"

    always "robin_bus_sex_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
