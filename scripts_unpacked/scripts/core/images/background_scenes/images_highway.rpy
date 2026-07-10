image bg_highway_image:
    get_background_filename("highway_local")


layeredimage bg_highway_layered:
    always "bg_highway_image"

    if t.hour in irange(17,23):
        "bg_highway_local_people_mantunnel"
    if t.hour in irange(14,21):
        "bg_highway_local_people_menfar"
    if t.hour in night:
        "bg_highway_local_people_bgwhore"

    if kitty_here() and kitty.showing and not renpy.showing("kitty"):
        "bg_highway_local_people_kitty_preg"
    elif kitty_here() and not renpy.showing("kitty"):
        "bg_highway_local_people_kitty"

    if rose_here() and rose.showing and not renpy.showing("rose"):
        "bg_highway_local_people_rose_preg"
    elif rose_here() and not renpy.showing("rose"):
        "bg_highway_local_people_rose"

    if charity_here() and charity.showing and not renpy.showing("charity"):
        "bg_highway_local_people_charity_preg"
    elif charity_here() and not renpy.showing("charity"):
        "bg_highway_local_people_charity"

    if pursy_here() and pursy.showing and not renpy.showing("pursy"):
        "bg_highway_local_people_pursy_preg"
    elif pursy_here() and not renpy.showing("pursy"):
        "bg_highway_local_people_pursy"

    if cass_here() and cass.showing and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_highway_local_people_cass_skirt_preg"
    elif cass_here() and cass.iswhore and (cass.noon_number % 2) and not renpy.showing("cass"):
        "bg_highway_local_people_cass_skirt"
    elif cass_here() and cass.showing and cass.iswhore and not renpy.showing("cass"):
        "bg_highway_local_people_cass_dress_preg"
    elif cass_here() and cass.iswhore and not renpy.showing("cass"):
        "bg_highway_local_people_cass_dress"

    if mira_here() and mira.showing and not renpy.showing("mira"):
        "bg_highway_local_people_mira_preg"
    elif mira_here() and not renpy.showing("mira"):
        "bg_highway_local_people_mira"

    if not (cass_here() or mira_here()) and t.time_from_to(17.00, 04.00):
        "bg_highway_local_people_girlstalk"

    if neighbour_here():
        "bg_highway_local_people_neigh"


image bg_highway:
    "bg_highway_layered"
    bg_tint_transform()





image bg_haven_exterior:
    get_background_filename("haven_exterior", True, False)
    bg_tint_transform()


image bg_haven_bed:
    "bg_haven_bed_scene"
    bg_tint_transform(True)


image bg_haven_bedroom_layer:
    "bg_haven_bedroom_scene"
    bg_tint_transform(True)

image bg_haven_bedroom_safe_layer:
    "bg_haven_bedroom_safe"
    bg_tint_transform(True)
image bg_haven_bedroom_danger_layer:
    "bg_haven_bedroom_danger"
    bg_tint_transform(True)
image bg_haven_bedroom_normal_layer:
    "bg_haven_bedroom_normal"
    bg_tint_transform(True)

layeredimage bg_haven_bedroom:

    always:
        "bg_haven_bedroom_layer"

    if haven_time_safe():
        "bg_haven_bedroom_safe_layer"
    elif haven_time_danger():
        "bg_haven_bedroom_danger_layer"
    elif haven_time_normal():
        "bg_haven_bedroom_normal_layer"

    if not t.timeofday == "night" and weather_var == 1:
        "bg_haven_bedroom_light"


image bg_haven_hallway_1f_layer:
    "bg_haven_hallway_1f_scene"
    bg_tint_transform(True)

layeredimage bg_haven_hallway_1f:
    always:
        "bg_haven_hallway_1f_layer"
    if not t.timeofday == "night" and weather_var == 1:
        "bg_haven_hallway_1f_light"


image bg_haven_hallway_2f_layer:
    "bg_haven_hallway_2f_scene"
    bg_tint_transform(True)

layeredimage bg_haven_hallway_2f:
    always:
        "bg_haven_hallway_2f_layer"
    if not t.hour in dark and weather_var == 1:
        "bg_haven_hallway_2f_light"


image bg_haven_hallway_3f:
    "bg_haven_hallway_3f_scene"
    bg_tint_transform(True)


image bg_haven_landing_scene_layer:
    "bg_haven_landing_scene"
    bg_tint_transform(True)
image bg_haven_landing_guard_layer:
    "bg_haven_landing_guard"
    bg_tint_transform(True)

image bg_haven_landing_gatelocked_layer:
    "bg_haven_landing_gatelocked"
    bg_tint_transform(True)
image bg_haven_landing_gateopen_layer:
    "bg_haven_landing_gateopen"
    bg_tint_transform(True)

layeredimage bg_haven_landing:
    always:
        "bg_haven_landing_scene_layer"
    if not t.timeofday == "night" and weather_var == 1:
        "bg_haven_landing_light"

    if not haven_guard_smoking() or loc_haven_landing.dict.get("gate_open") or not havengateguard.active: 
        "bg_haven_landing_guard_layer"

    if loc_haven_landing.dict.get("gate_open"):
        "bg_haven_landing_gateopen_layer"
    else:
        "bg_haven_landing_gatelocked_layer"


image bg_haven_lobby_scene_layer:
    "bg_haven_lobby_scene"
    bg_tint_transform(True)

layeredimage bg_haven_lobby:
    always:
        "bg_haven_lobby_scene_layer"
    if not t.timeofday == "night" and weather_var == 1:
        "bg_haven_lobby_light"


image bg_haven_lounge_sun_layer:
    "bg_haven_lounge_sun"
    bg_tint_transform(True)
image bg_haven_lounge_nosun_layer:
    "bg_haven_lounge_nosun"
    bg_tint_transform(True)
image bg_haven_lounge_people1_layer:
    "bg_haven_lounge_people1"
    bg_tint_transform(True)
image bg_haven_lounge_people2_layer:
    "bg_haven_lounge_people2"
    bg_tint_transform(True)
image bg_haven_lounge_people3_layer:
    "bg_haven_lounge_people3"
    bg_tint_transform(True)

layeredimage bg_haven_lounge:

    if t.timeofday == "night":
        "bg_haven_lounge_night"
    elif weather_var == 1:
        "bg_haven_lounge_sun_layer"
    else:
        "bg_haven_lounge_nosun_layer"

    if haven_time_safe():
        "bg_haven_lounge_people1_layer"
    elif haven_time_danger():
        "bg_haven_lounge_people2_layer"
    elif haven_time_normal():
        "bg_haven_lounge_people3_layer"


image bg_haven_office:
    "bg_haven_office_base"
    bg_tint_transform(True)


image bg_haven_room1_layer:
    "bg_haven_room1_scene"
    bg_tint_transform(True)

layeredimage bg_haven_room1:
    always:
        "bg_haven_room1_layer"
    if t.timeofday == "night":
        "bg_haven_room1_peepholelight"


image bg_haven_room2:
    "bg_haven_room2_scene"
    bg_tint_transform(True)


image bg_haven_room3:
    "bg_haven_room3_scene"
    bg_tint_transform(True)


image bg_haven_shower_stall:
    "bg_haven_shower_stall_scene"
    bg_tint_transform(True)


image bg_haven_shower_layer:
    "bg_haven_shower_scene"
    bg_tint_transform(True)

image bg_haven_shower_girls_layer:
    "bg_haven_shower_girls"
    bg_tint_transform(True)
image bg_haven_shower_men1_layer:
    "bg_haven_shower_men1"
    bg_tint_transform(True)
image bg_haven_shower_men2_layer:
    "bg_haven_shower_men2"
    bg_tint_transform(True)
layeredimage bg_haven_shower:

    always:
        "bg_haven_shower_layer"

    if not t.timeofday == "night" and weather_var == 1:
        "bg_haven_shower_light"

    if haven_time_safe():
        "bg_haven_shower_girls_layer"
    elif haven_time_danger():
        "bg_haven_shower_men1_layer"
    elif haven_time_normal():
        "bg_haven_shower_men2_layer"


layeredimage bg_haven_storage:

    always:
        "bg_haven_storage_scene"
    if not "vent_open" in loc_haven_storage.list:
        "bg_haven_storage_vent_idle"

image bg_haven_toplanding:
    "bg_haven_toplanding_scene"
    bg_tint_transform(True)


image bg_haven_utilities:
    "bg_haven_utilities_scene"
    bg_tint_transform(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
