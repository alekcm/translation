image bg_boardwalk_scene:
    get_background_filename("boardwalk", True, False)
    bg_tint_transform()

layeredimage bg_boardwalk_people_sandy:
    always "bg_boardwalk_people_sandy_base"
    if sandy.showing:
        "bg_boardwalk_people_sandy_preg"

layeredimage bg_boardwalk_people_customer:
    always "bg_boardwalk_people_customer_base"
    if girl_dummy_1.showing:
        "bg_boardwalk_people_customer_preg"

layeredimage bg_boardwalk_people_vendor:
    always "bg_boardwalk_people_vendor_base"
    if girl_dummy_2.showing:
        "bg_boardwalk_people_vendor_preg"

layeredimage bg_boardwalk_people_walk:
    always "bg_boardwalk_people_walk_base"
    if girl_dummy_3.showing:
        "bg_boardwalk_people_walk_preg"

layeredimage bg_boardwalk_people:
    if not renpy.showing("sandy") and sandy_here():
        "bg_boardwalk_people_sandy"
    if sandy_here() and girl_dummy_1.hour_number > 3:
        "bg_boardwalk_people_customer"
    if not t.timeofday == "night" and girl_dummy_2.hour_number > 3:
        "bg_boardwalk_people_walk"
    if t.time_from_to(08.00,19.59):
        "bg_boardwalk_people_vendor"
    if girl_dummy_4.hour_number > 5 and not t.timeofday == "night":
        "bg_boardwalk_people_close"
    if t.hour in workhours and weather_var <= 2:
        "bg_boardwalk_people_manclose"
    if t.hour in workhours and weather_var <= 2:
        "bg_boardwalk_people_manfar"

layeredimage bg_boardwalk_layer:
    always "bg_boardwalk_scene"
    always "bg_boardwalk_people"

image bg_boardwalk:
    "bg_boardwalk_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
