image bg_bus_interior_scene_layer:
    get_background_filename("bus_interior_scene", False, False)
    bg_tint_transform()





layeredimage bg_bus_interior_people_leftsit_layer:
    if girl_dummy_3.hour_number == 5 and global_random_hour_number > 8 and t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_leftsit_sex"
    elif t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_leftsit_panties"
    else:
        "bg_bus_interior_people_leftsit_hoodie"
    if global_random_hour_number > 5:
        "bg_bus_interior_people_leftsit_manuni"

layeredimage bg_bus_interior_people_middlesit_layer:
    if t.time_from_to(22.00, 04.00) and girl_dummy_1.hour_number > 7 and global_random_number % 2 == 0:
        "bg_bus_interior_people_middlesit_sleep_layer"
    else:
        "bg_bus_interior_people_middlesit_man_layer"

layeredimage bg_bus_interior_people_middlesit_man_layer:
    if global_random_hour_number % 2 == 0 and global_random_hour_number > 7:
        "bg_bus_interior_people_middlesit_manarm"
    elif global_random_hour_number > 3:
        "bg_bus_interior_people_middlesit_manlean"
    always "bg_bus_interior_people_middlesit_girl_layer"

layeredimage bg_bus_interior_people_middlesit_girl_layer:
    if global_random_hour_number > 3 and global_random_number == 10 and girl_dummy_2.hour_number == 10:
        "bg_bus_interior_people_middlesit_jeansblow"
    elif t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_middlesit_unisit"
    elif t.hour in (6,7,22,23,0,1,2):
        "bg_bus_interior_people_middlesit_whoreshorts"

layeredimage bg_bus_interior_people_middlesit_sleep_layer:
    always "bg_bus_interior_people_middlesit_sleep"
    if girl_dummy_1.hour_number == 10 and global_random_number:
        "bg_bus_interior_people_middlesit_sleep_clothes"

layeredimage bg_bus_interior_people_rightsit_layer:
    if girl_dummy_3.hour_number == 1 and global_random_hour_number == 3 and t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_rightsit_sex"
    elif t.time_from_to(22.00, 04.00) and girl_dummy_2.hour_number == 10 and global_random_number % 2 == 0:
        "bg_bus_interior_people_rightsit_nude"
    elif t.hour in (6,7,22,23,0,1,2):
        "bg_bus_interior_people_rightsit_whore"
    else:
        "bg_bus_interior_people_rightsit_hoodie"
    if not (t.time_from_to(22.00, 04.00) and girl_dummy_2.hour_number == 10 and global_random_number % 2 == 0) and global_random_hour_number > 4:
        "bg_bus_interior_people_rightsit_man"

layeredimage bg_bus_interior_people_rightstand_grope_layer:
    if girl_dummy_3.hour_number == 7 and global_random_hour_number > 8 and t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_rightstand_blow2"
    elif girl_dummy_3.hour_number == 7 and global_random_hour_number == 6 and t.time_from_to(08.00, 14.00):
        "bg_bus_interior_people_rightstand_blow1"
    elif girl_dummy_3.hour_number == 7 and global_random_hour_number == 6 and t.hour in night:
        "bg_bus_interior_people_rightstand_blow3"
    elif t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_rightstand_skirt"
    elif t.time_from_to(08.00, 14.00):
        "bg_bus_interior_people_rightstand_sport"
    elif t.hour in night and global_random_hour_number % 2 == 0:
        "bg_bus_interior_people_rightstand_whoredress"
    elif t.hour in night:
        "bg_bus_interior_people_rightstand_whorepants"
    else:
        "bg_bus_interior_people_rightstand_shorts"

    if girl_dummy_3.hour_number == 0:
        "bg_bus_interior_people_rightstand_mantee"
    elif girl_dummy_3.hour_number == 1:
        "bg_bus_interior_people_rightstand_manvest"

image bg_bus_interior_people_rightstand_image:
    "bg_bus_interior_people_rightstand_grope_layer"
    anchor (global_random_hour_number*30, 0)

layeredimage bg_bus_interior_people_rightstand_face_layer:

    if t.hour in (8, 14,15) and t.wkday in weekdays and not global_random_hour_number > 8:
        "bg_bus_interior_people_rightstand_uni"
    elif not t.hour in night and not global_random_hour_number < 2:
        "bg_bus_interior_people_rightstand_baggy"

image bg_bus_interior_people_rightstand_face_image:
    "bg_bus_interior_people_rightstand_face_layer"
    anchor (-global_random_hour_number*50, 0)

layeredimage bg_bus_interior_people_leftstand_layer:
    if t.hour in (8, 14,15) and t.wkday in weekdays and not global_random_hour_number > 8:
        "bg_bus_interior_people_leftstand_uni"
    elif not t.hour in night and global_random_hour_number % 2 == 0:
        "bg_bus_interior_people_leftstand_black_layer"
    elif not t.hour in night:
        "bg_bus_interior_people_leftstand_dress_layer"
    elif global_random_hour_number % 2 == 0:
        "bg_bus_interior_people_leftstand_sport"

layeredimage bg_bus_interior_people_leftstand_man_layer:
    if girl_dummy_2.hour_number == 10:
        "bg_bus_interior_people_leftstand_manmastsuit"
    elif girl_dummy_2.hour_number == 9:
        "bg_bus_interior_people_leftstand_manmastshorts"

layeredimage bg_bus_interior_people_leftstand_black_layer:
    always "bg_bus_interior_people_leftstand_black"
    if girl_dummy_3.showing:
        "bg_bus_interior_people_leftstand_black_preg"

layeredimage bg_bus_interior_people_leftstand_dress_layer:
    always "bg_bus_interior_people_leftstand_dress"
    if girl_dummy_1.showing:
        "bg_bus_interior_people_leftstand_dress_preg"

layeredimage bg_bus_interior_people_middlestand_layer:
    if t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_midlestand_uni"
    elif t.time_from_to(09.00, 18.00) and global_random_hour_number % 2 == 0:
        "bg_bus_interior_people_midlestand_jeans"
    elif t.time_from_to(09.00, 18.00):
        "bg_bus_interior_people_midlestand_sport"
    elif global_random_hour_number > 7:
        "bg_bus_interior_people_midlestand_jeanshorts"
    elif global_random_hour_number < 4:
        "bg_bus_interior_people_midlestand_whorepink"
    else:
        "bg_bus_interior_people_midlestand_teeshorts"

    if global_random_hour_number == 10:
        "bg_bus_interior_people_midlestand_manshirt"

image bg_bus_interior_people_middlestand_image:
    "bg_bus_interior_people_middlestand_layer"
    anchor (global_random_hour_number*10, 0)

layeredimage bg_bus_interior_people_all_test:
    always "bg_bus_interior_people_leftsit_layer"
    always "bg_bus_interior_people_middlesit_layer"
    always "bg_bus_interior_people_rightsit_layer"
    always "bg_bus_interior_people_leftstand_layer"
    always "bg_bus_interior_people_middlestand_image"
    always "bg_bus_interior_people_leftstand_man_layer"
    always "bg_bus_interior_people_rightstand_image"
    always "bg_bus_interior_people_rightstand_face_image"


layeredimage bg_bus_interior_people_academy_layer:

    if girl_dummy_4.hour_number > 3: 
        "bg_bus_interior_people_leftsit_layer"
    if girl_dummy_5.hour_number > 3: 
        "bg_bus_interior_people_middlesit_layer"
    if girl_dummy_6.hour_number > 3: 
        "bg_bus_interior_people_rightsit_layer"

    if global_random_number > 8 and global_random_hour_number == 10 and t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_rightstand_sex"
    elif global_random_hour_number < 7:
        "bg_bus_interior_people_rightfarstan_manhood"

    if girl_dummy_6.hour_number < 8:   
        "bg_bus_interior_people_leftstand_layer"
    if girl_dummy_5.hour_number < 8: 
        "bg_bus_interior_people_middlestand_image"
    if girl_dummy_6.hour_number < 8:   
        "bg_bus_interior_people_leftstand_man_layer"

    if girl_dummy_4.hour_number < 8:
        "bg_bus_interior_people_rightstand_image"
    if girl_dummy_5.hour_number % 2 == 0:
        "bg_bus_interior_people_rightstand_face_image"




layeredimage bg_bus_interior_people_rushhour_layer:

    if girl_dummy_4.hour_number > 3: 
        "bg_bus_interior_people_leftsit_layer"
    if girl_dummy_5.hour_number > 3: 
        "bg_bus_interior_people_middlesit_layer"
    if girl_dummy_6.hour_number > 3: 
        "bg_bus_interior_people_rightsit_layer"

    if girl_dummy_6.hour_number < 8:   
        "bg_bus_interior_people_leftstand_layer"
    if girl_dummy_5.hour_number < 8: 
        "bg_bus_interior_people_middlestand_image"
    if girl_dummy_6.hour_number < 8:   
        "bg_bus_interior_people_leftstand_man_layer"

    if girl_dummy_4.hour_number < 8:
        "bg_bus_interior_people_rightstand_image"
    if girl_dummy_5.hour_number % 2 == 0:
        "bg_bus_interior_people_rightstand_face_image"

    elif global_random_hour_number < 8:
        "bg_bus_interior_people_rightfarstan_manhood"

layeredimage bg_bus_interior_people_daytime_layer:

    if girl_dummy_4.hour_number > 4: 
        "bg_bus_interior_people_leftsit_layer"
    if girl_dummy_5.hour_number > 4: 
        "bg_bus_interior_people_middlesit_layer"
    if girl_dummy_6.hour_number > 4: 
        "bg_bus_interior_people_rightsit_layer"

    if global_random_hour_number < 7:
        "bg_bus_interior_people_rightfarstan_manhood"

    if girl_dummy_6.hour_number < 7:   
        "bg_bus_interior_people_leftstand_layer"
    if girl_dummy_5.hour_number < 7: 
        "bg_bus_interior_people_middlestand_image"
    if girl_dummy_6.hour_number < 7:   
        "bg_bus_interior_people_leftstand_man_layer"

    if girl_dummy_4.hour_number < 7:
        "bg_bus_interior_people_rightstand_image"
    if girl_dummy_5.hour_number % 2 == 0:
        "bg_bus_interior_people_rightstand_face_image"



layeredimage bg_bus_interior_people_nighttime_layer:

    if girl_dummy_4.hour_number > 5: 
        "bg_bus_interior_people_leftsit_layer"
    if girl_dummy_5.hour_number > 5: 
        "bg_bus_interior_people_middlesit_layer"
    if girl_dummy_6.hour_number > 5: 
        "bg_bus_interior_people_rightsit_layer"

    if global_random_hour_number < 5:
        "bg_bus_interior_people_rightfarstan_manhood"

    if girl_dummy_6.hour_number < 6:   
        "bg_bus_interior_people_leftstand_layer"
    if girl_dummy_5.hour_number < 6: 
        "bg_bus_interior_people_middlestand_image"
    if girl_dummy_6.hour_number < 6:   
        "bg_bus_interior_people_leftstand_man_layer"

    if girl_dummy_4.hour_number < 6:
        "bg_bus_interior_people_rightstand_image"
    if girl_dummy_5.hour_number % 2 == 0:
        "bg_bus_interior_people_rightstand_face_image"

layeredimage bg_bus_interior_people_graveyard_layer:

    if girl_dummy_4.hour_number < 3: 
        "bg_bus_interior_people_leftsit_layer"
    if girl_dummy_5.hour_number < 3: 
        "bg_bus_interior_people_middlesit_layer"
    if girl_dummy_6.hour_number < 3: 
        "bg_bus_interior_people_rightsit_layer"

    if global_random_hour_number < 5:
        "bg_bus_interior_people_rightfarstan_manhood"

    if girl_dummy_6.hour_number > 8:   
        "bg_bus_interior_people_leftstand_layer"
    if girl_dummy_5.hour_number > 8: 
        "bg_bus_interior_people_middlestand_image"
    if girl_dummy_6.hour_number > 8:   
        "bg_bus_interior_people_leftstand_man_layer"

    if girl_dummy_4.hour_number > 8:
        "bg_bus_interior_people_rightstand_image"


layeredimage bg_bus_interior_people_layer:
    if t.hour in (8, 14,15) and t.wkday in weekdays:
        "bg_bus_interior_people_academy_layer" 
    elif t.hour in (7,8,9, 16,17,18,19):
        "bg_bus_interior_people_rushhour_layer"
    elif t.hour in irange(9,21):
        "bg_bus_interior_people_daytime_layer"
    elif t.hour in (6,7,22,23,0,1,2):
        "bg_bus_interior_people_nighttime_layer"
    else:
        "bg_bus_interior_people_graveyard_layer"

image bg_bus_interior_people_image:
    "bg_bus_interior_people_layer"
    bg_tint_transform()

layeredimage bg_bus_interior:
    always "bg_bus_interior_scene_layer"
    always "bg_bus_interior_people_image"

















layeredimage fg_bus_interior_people_rightgrope_layer:
    if girl_dummy_2.hour_number == 10:
        "bg_bus_interior_people_fg_right_mangrope"

    if global_random_hour_number > 5:
        "bg_bus_interior_people_fg_right_hoodie"
    else:
        "bg_bus_interior_people_fg_right_sportg"

    if girl_dummy_2.hour_number == 10:
        "bg_bus_interior_people_fg_right_manhand"

layeredimage fg_bus_interior_people_rightsex_layer:
    if girl_dummy_2.hour_number == 3:
        "bg_bus_interior_people_fg_right_camisex"
    else:
        "bg_bus_interior_people_fg_right_camistand"

layeredimage fg_bus_interior_people_rightmisc_layer:
    if girl_dummy_5.hour_number > 5:
        "bg_bus_interior_people_fg_middle_shirt"
    else:
        "bg_bus_interior_people_fg_right_sport"

layeredimage fg_bus_interior_people_academy_layer:
    if girl_dummy_2.hour_number == 10:
        "bg_bus_interior_people_fg_right_manwank"
    else: 
        "bg_bus_interior_people_fg_left_uni"

    if global_random_hour_number == 1:
        "bg_bus_interior_people_fg_right_manwank"
    elif global_random_hour_number < 9:
        "bg_bus_interior_people_fg_right_uni"

layeredimage fg_bus_interior_people_rushhour_layer:
    if global_random_hour_number == 10:
        "bg_bus_interior_people_fg_left_manwank"
    if girl_dummy_5.hour_number > 5 and global_random_hour_number in (3,4,5,6,7):
        "fg_bus_interior_people_rightgrope_layer"

layeredimage fg_bus_interior_people_daytime_layer:
    if global_random_hour_number == 10:
        "bg_bus_interior_people_fg_left_manwank"

    if girl_dummy_5.hour_number > 5 and global_random_hour_number in (3,4,5,6,7):
        "fg_bus_interior_people_rightsex_layer"

layeredimage fg_bus_interior_people_graveyard_layer:
    if global_random_hour_number == 10:
        "bg_bus_interior_people_fg_left_manwank"
    if girl_dummy_5.hour_number > 8:
        "fg_bus_interior_people_rightmisc_layer"

layeredimage fg_bus_interior_layer:
    if t.hour in (8, 14,15) and t.wkday in weekdays:
        "fg_bus_interior_people_academy_layer" 
    elif t.hour in (7,8,9, 16,17,18,19):
        "fg_bus_interior_people_rushhour_layer"
    elif t.hour in irange(9,21):
        "fg_bus_interior_people_daytime_layer"
    else:
        "fg_bus_interior_people_graveyard_layer"

image fg_bus_interior:
    "fg_bus_interior_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
