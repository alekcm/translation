init python:
    def people_beach():
        if weather_var in (1,2) and not t.month == "Winter":
            return True
        else:
            return False
    def people_beach_vball():
        if t.hour in irange(9, 17) and people_beach():
            return True
        else:
            return False

    def people_nude_beach_vball_canplay():
        if "nude_vball" in loc_beach_hangout.list and t.hour in (21,22,23,0,1,2) and not weather_var >= 3:
            return True
        else:
            return False

    def people_nude_beach_vball():
        if people_nude_beach_vball_canplay() and any([mason_here(loc_beach_gym), erika_here(loc_beach_gym), zahra_here(loc_beach_gym), robin_here(loc_beach_gym), rachel_here(loc_beach_gym)]):
            return True
        else:
            return False

    def people_beach_girls_vball():
        for person in diary_people_list:
            if person.is_female and person._original_name.lower() + "_here" in globals() and globals()[person._original_name.lower() + "_here"](loc_beach_fire) and people_beach():
                return True
        else:
            return False

    def people_beach_firepit():
        for person in diary_people_list:
            if person._original_name.lower() + "_here" in globals() and globals()[person._original_name.lower() + "_here"](loc_beach_fire):
                return True
        else:
            return False

image bg_lake_image:
    get_background_filename("lake", True, False)

layeredimage bg_lake_layered:
    always "bg_lake_image"
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_1.hour_number > 4:
        "bg_lake_people_stand"
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_2.hour_number > 4:
        "bg_lake_people_butt"
    if t.hour_from_to(8,17) and weather_var == 1 and girl_dummy_3.hour_number > 4:
        "bg_lake_people_dance"
    if t.hour_from_to(8,19) and weather_var == 1 and girl_dummy_4.hour_number > 4:
        "bg_lake_people_water"
image bg_lake:
    "bg_lake_layered"
    bg_tint_transform()


image bg_beach_hangout_image:
    get_background_filename("beach", True, False)
    bg_tint_transform()
layeredimage bg_beach_hangout_people_layer:
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_2.hour_number > 3:
        "bg_beach_hangout_people_girl_water"
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_1.hour_number > 4:
        "bg_beach_hangout_people_girl_ball"
    if t.hour_from_to(10,19) and weather_var == 1 and girl_dummy_4.hour_number < 6:
        "bg_beach_hangout_people_man_water"
    if t.hour_from_to(9,20) and weather_var <= 2 and not t.month == "Winter" and girl_dummy_6.hour_number < 6:
        "bg_beach_hangout_people_girl_towel"
    if t.hour_from_to(8,17) and weather_var == 1 and global_random_hour_number < 6:
        "bg_beach_hangout_people_girl_cream"
    if t.hour_from_to(10,19) and weather_var <= 2 and not t.month == "Winter" and girl_dummy_5.hour_number < 8:
        "bg_beach_hangout_people_man_stand"
    if t.hour_from_to(10,19) and weather_var <= 2 and not t.month == "Winter" and global_random_hour_number < 8:
        "bg_beach_hangout_people_girl_close"

image bg_beach_hangout_people_layer_image:
    "bg_beach_hangout_people_layer"
    bg_tint_transform()

layeredimage bg_beach_hangout:
    always "bg_beach_hangout_image"
    always "bg_beach_hangout_people_layer_image"

image bg_beach_gym_layer:
    get_background_filename("beach_hangout", True, False)
    bg_tint_transform()

image bg_beach_pier_image:
    get_background_filename("beach_pier_under", True, False)


layeredimage bg_beach_pier_layered:
    always "bg_beach_pier_image"
    if t.hour_from_to(8,17) and weather_var == 1 and global_random_hour_number > 8:
        "bg_beach_pier_under_people_stand"
    if t.hour_from_to(11,23) and weather_var <= 2 and global_random_hour_number == 1 and girl_dummy_6.hour_number == 1:
        "bg_beach_pier_under_people_blow"

image bg_beach_pier:
    "bg_beach_pier_layered"
    bg_tint_transform()

image bg_beach_rocks_image:
    get_background_filename("beach_rocks", True, False)
    bg_tint_transform()
image bg_beach_rocks_people_dealer_image:
    "bg_beach_rocks_people_dealer"
    bg_tint_transform()
layeredimage bg_beach_rocks:
    always "bg_beach_rocks_image"
    if lake_dealer_here() and not renpy.showing("lake_dealer"):
        "bg_beach_rocks_people_dealer_image"

image bg_pier_layer:
    get_background_filename("pier", True, False)
    bg_tint_transform()
layeredimage bg_pier_people_sandy_layer:
    always "bg_pier_people_sandy"
    if sandy.days_pregnant > (global_pregnancy_length * 0.75):
        "bg_pier_people_sandy_2"
    elif sandy.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_pier_people_sandy_1"
layeredimage bg_pier_people_erika_layer:
    always "bg_pier_people_erika"
    if erika.days_pregnant > (global_pregnancy_length * 0.75):
        "bg_pier_people_erika_2"
    elif erika.days_pregnant > (global_pregnancy_length * 0.3):
        "bg_pier_people_erika_1"
image bg_pier_people_erika_image:
    "bg_pier_people_erika_layer"
    bg_tint_transform()
image bg_pier_people_sandy_image:
    "bg_pier_people_sandy_layer"
    bg_tint_transform()
layeredimage bg_pier:
    always "bg_pier_layer"
    if sandy_here():
        "bg_pier_people_sandy_image"
    if erika_here():
        "bg_pier_people_erika_image"

image bg_walk_lake_shrubs:
    get_background_filename("lake_shrubs", True, False)
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
