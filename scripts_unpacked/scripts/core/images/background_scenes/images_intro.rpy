image bg_residential_area_shadow_dawn:
    get_background_filename("residential_area")
    matrixcolor TintMatrix(weather_colours["shadow_dawn"])
image bg_bedroom_shadow_dawn:
    get_background_filename("bedroom")
    matrixcolor TintMatrix(weather_colours["shadow_dawn"])
image bg_bedroom_noshad_night:
    get_background_filename("bedroom")
    matrixcolor TintMatrix(weather_colours["noshad_night"])

layeredimage bg_residential_area_dawn:
    always "bg_sky_dawn_sunny"
    always "bg_residential_area_shadow_dawn"
    always "bg_residential_area_people"

layeredimage bg_bedroom_dawn:
    always "bg_sky_dawn_sunny"
    always "bg_bedroom_shadow_dawn"

layeredimage bg_bedroom_night:
    always "bg_sky_night_sunny"
    always "bg_bedroom_noshad_night"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
