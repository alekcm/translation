image bg_market_scene:
    get_background_filename("market")

layeredimage bg_market_layer:

    always:
        "bg_market_scene"
    if not t.hour in workhours:
        "bg_market_closed"

    if t.hour in workhours:
        "bg_market_people_manfar"
    if t.hour in workhours:
        "bg_market_people_manright"
    if t.hour in workhours:
        "bg_market_people_stallclose"
    if t.hour in workhours:
        "bg_market_people_stallfar"
    if flyergirl_here() and not renpy.showing("flyergirl"):
        "bg_market_people_flier"
    if flyergirl_here() and flyergirl.showing and not renpy.showing("flyergirl"):
        "bg_market_people_flier_preg"
    if t.hour in workhours and girl_dummy_4.hour_number > 3:
        "bg_market_people_walk"
    if t.hour in workhours and girl_dummy_1.hour_number > 3:
        "bg_market_people_jeans"
    if t.hour in workhours and girl_dummy_2.hour_number > 3:
        "bg_market_people_browse"

image bg_market:
    "bg_market_layer"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
