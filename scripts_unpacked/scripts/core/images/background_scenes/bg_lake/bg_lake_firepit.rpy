image bg_beach_firepit_people_fire_layer:
    "bg_beach_firepit_people_fire"
    bg_tint_transform()

layeredimage bg_beach_firepit_people_erika_layered:
    if erika.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_beach_firepit_people_erika_preg"
    else:
        "bg_beach_firepit_people_erika"

layeredimage bg_beach_firepit_people_sandy_layered:
    if sandy.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_beach_firepit_people_sandy_preg"
    else:
        "bg_beach_firepit_people_sandy"

layeredimage bg_beach_firepit_people_zahra_layered:
    if zahra.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_beach_firepit_people_zahra_preg"
    else:
        "bg_beach_firepit_people_zahra"

image bg_beach_firepit_layer:
    get_background_filename("beach_firepit", True, False)
    bg_tint_transform()

layeredimage bg_beach_fire:
    always "bg_beach_firepit_layer"
    always "bg_beach_fire_people_layer"

layeredimage bg_beach_fire_people:
    if t.hour_from_to(20,3) and people_beach():
        "bg_beach_firepit_fire"
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_2.hour_number > 3:
        "bg_beach_firepit_people_girl_lay"
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_1.hour_number > 4:
        "bg_beach_firepit_people_girl_sitfront"
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_4.hour_number < 6:
        "bg_beach_firepit_people_girl_sitpose"
    if t.hour_from_to(8,17) and weather_var <= 2 and not t.month == "Winter" and girl_dummy_3.hour_number > 3:
        "bg_beach_firepit_people_girl_standfar"
    if t.hour_from_to(9,20) and weather_var == 1 and girl_dummy_4.hour_number < 6:
        "bg_beach_firepit_people_girl_sitpose"
    if t.hour_from_to(8,17) and weather_var == 1 and global_random_hour_number < 6:
        "bg_beach_firepit_people_girl_topless"
    if t.hour_from_to(10,19) and weather_var <= 2 and not t.month == "Winter" and global_random_hour_number < 4:
        "bg_beach_firepit_people_man_pose"
    if t.hour_from_to(10,19) and weather_var <= 2 and not t.month == "Winter" and girl_dummy_6.hour_number < 8:
        "bg_beach_firepit_people_man_strech"
    if t.hour_from_to(10,19) and weather_var <= 2 and not t.month == "Winter" and girl_dummy_5.hour_number < 8:
        "bg_beach_firepit_people_man_walk"
    if t.hour_from_to(10,19) and weather_var <= 2 and not t.month == "Winter" and global_random_hour_number < 8:
        "bg_beach_firepit_people_girl_standclose"

    if kaan_here() and not renpy.showing("kaan"):
        "bg_beach_firepit_people_kaan"
    if mateo_here() and not renpy.showing("mateo"):
        "bg_beach_firepit_people_mateo"
    if sandy_here() and not renpy.showing("sandy"):
        "bg_beach_firepit_people_sandy_layered"
    if zahra_here() and not renpy.showing("zahra"):
        "bg_beach_firepit_people_zahra_layered"
    if robin_here() and not renpy.showing("robin"):
        "bg_beach_firepit_people_robin"
    if erika_here() and not renpy.showing("erika"):
        "bg_beach_firepit_people_erika_layered"

image bg_beach_fire_people_layer:
    "bg_beach_fire_people"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
