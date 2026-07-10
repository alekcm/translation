image bg_park:
    get_background_filename("park_local")
    bg_tint_transform()

image bg_park_toilet:
    get_background_filename("park_toilet", winter=False)
    bg_tint_transform()

image bg_park_path:
    get_background_filename("park_path", winter=False)
    bg_tint_transform()

image bg_park_field:
    "bg_park_field_base"
    bg_tint_transform()

image bg_park_gazebo:
    get_background_filename("park_gazebo", winter=False)
    bg_tint_transform()

image bg_walk_park_forest:
    "bg_park_mud_base"
    bg_tint_transform()

image bg_walk_park_shrubs:
    "bg_park_shrubs_base"
    bg_tint_transform()


image bg_park_toilet_boys = "bg_park_toilet_boys_base"

layeredimage bg_park_toilet_girls:
    always "bg_park_toilet_girls_base"
    if t.hour in (6, 17, 18, 0, 1):
        "bg_toilet_girls_people_whores" xpos (-0.2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
