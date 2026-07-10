image bg_busstop:
    get_background_filename("busstop")
    bg_tint_transform()

image bg_busstop_highway_local_layer:
    get_background_filename("busstop_highway")
    bg_tint_transform()
image bg_busstop_trainstation_layer:
    get_background_filename("busstop_trainstation", True, False)
    bg_tint_transform()
image bg_busstop_school_layer:
    get_background_filename("busstop_school", True, False)
    bg_tint_transform()
image bg_busstop_residential_layer:
    get_background_filename("busstop_residential", True, False)
    bg_tint_transform()

layeredimage bg_busstop_shelter:
    always:
        "bg_busstop"
    if t.hour in (6,7,8,9,16,17,18,19):
        "bg_busstop_people1"
    if t.hour in (9,10,11,14,16,17,18,19,20,21,22,23):
        "bg_busstop_people2"

layeredimage bg_busstop_highway:
    always:
        "bg_busstop_highway_local_layer"
    always:
        "bg_busstop_shelter"

layeredimage bg_busstop_revel:
    always:
        "bg_busstop_trainstation_layer"
    always:
        "bg_busstop_shelter"

layeredimage bg_busstop_school:
    always:
        "bg_busstop_school_layer"
    always:
        "bg_busstop_shelter"

layeredimage bg_busstop_residential:
    always:
        "bg_busstop_residential_layer"
    always:
        "bg_busstop_shelter"

image bg_busstop_truckstop:
    ("bg_busstop_residential")
image bg_busstop_lake:
    ("bg_busstop_residential")
image bg_busstop_industrial:
    ("bg_busstop_revel")
image bg_busstop_commercial:
    ("bg_busstop_revel")
image bg_busstop_checkpoint:
    ("bg_busstop_highway")
image bg_busstop_park:
    ("bg_busstop_residential")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
