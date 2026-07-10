image bg_residential_area_layer:
    get_background_filename("residential_area", winter=False)
    bg_tint_transform()
image bg_residential_area_people_layer:
    "bg_residential_area_people"
    bg_tint_transform()

layeredimage bg_residential:
    always:
        "bg_residential_area_layer"



image bg_stairwell_scene:
    get_background_filename("stairwell")
layeredimage bg_stairwell_layered:
    always "bg_stairwell_scene"
    if dani_here() and dani.showing and not renpy.showing("dani"):
        "bg_stairwell_people_dani_preg"
    elif dani_here() and not renpy.showing("dani"):
        "bg_stairwell_people_dani"
image bg_stairwell:
    "bg_stairwell_layered"
    bg_tint_transform()

layeredimage bg_office_ll:
    if t.hour in loc_office_ll.opening_hours:
        "bg_office_ll_light"
    else:
        "bg_office_ll_dark"
    if oskar_here() and robin_here():
        "bg_office_ll_oskar_sex_robin"
    elif oskar_here() and not renpy.showing("oskar"):
        "bg_office_ll_oskar_sit"

image bg_bedroom_dani_bg:
    get_background_filename("bedroom_dani")

layeredimage bg_bedroom_dani_person_dani_stand_sleep_layer:
    always "bg_bedroom_dani_people_dani_stand_sleep"
    if dani.heavy_preg:
        "bg_bedroom_dani_people_dani_stand_sleep_preg2"
    elif dani.showing:
        "bg_bedroom_dani_people_dani_stand_sleep_preg1"

layeredimage bg_bedroom_dani_person_dani_stand_casual_layer:
    always "bg_bedroom_dani_people_dani_stand_casual"
    if dani.heavy_preg:
        "bg_bedroom_dani_people_dani_stand_casual_preg2"
    elif dani.showing:
        "bg_bedroom_dani_people_dani_stand_casual_preg1"

layeredimage bg_bedroom_dani_person_dani_sit_layer:
    if dani.showing:
        "bg_bedroom_dani_people_dani_sit_preg"
    else:
        "bg_bedroom_dani_people_dani_sit"

layeredimage bg_bedroom_dani_person_dani_sleepwear_layer:
    if dani.hour_number / 2 == 0:
        "bg_bedroom_dani_person_dani_stand_sleep_layer"
    else:
        "bg_bedroom_dani_person_dani_sit_layer"

layeredimage bg_bedroom_dani_person_dani_layer:
    if t.hour in (23,0, 1,2,3,4,5):
        "bg_bedroom_dani_people_dani_lay"
    elif t.hour in (21,22,23,0,1,2,3,4,5,6,7,8,9):
        "bg_bedroom_dani_person_dani_sleepwear_layer"
    else:
        "bg_bedroom_dani_person_dani_stand_casual_layer"

layeredimage bg_bedroom_dani_layer:
    always "bg_bedroom_dani_bg"
    if dani_here() and not renpy.showing("dani"):
        "bg_bedroom_dani_person_dani_layer"

image bg_bedroom_dani:
    "bg_bedroom_dani_layer"
    bg_tint_transform(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
