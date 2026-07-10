image haven_blow_spank_1h_layer:
    "haven_blow_spank_1h"
    opacity_transform(bruise.ass)
image haven_blow_spank_2h_layer:
    "haven_blow_spank_2h"
    opacity_transform(bruise.ass)
image haven_blow_spank_ballrub_layer:
    "haven_blow_spank_ballrub"
    opacity_transform(bruise.ass)
image haven_blow_spank_ballsuck_layer:
    "haven_blow_spank_ballsuck"
    opacity_transform(bruise.ass)
image haven_blow_spank_knees_layer:
    "haven_blow_spank_knees"
    opacity_transform(bruise.ass)

image haven_blow_writing_milk_1h_layer:
    "haven_blow_writing_milk_1h"
    writing_transform("chest")
image haven_blow_writing_milk_ballrub_layer:
    "haven_blow_writing_milk_ballrub"
    writing_transform("chest")
image haven_blow_writing_milk_ballsuck_layer:
    "haven_blow_writing_milk_ballsuck"
    writing_transform("chest")
image haven_blow_writing_milk_knees_layer:
    "haven_blow_writing_milk_knees"
    writing_transform("chest")





layeredimage haven_blow wait:

    always:
        "haven_blow_bg"

    always:
        "haven_blow_knees_pc_base"
    always:
        "haven_blow_spank_knees_layer"
    if writing.chest:
        "haven_blow_writing_milk_knees_layer"

    if c.top:
        "haven_blow_knees_pc_top"
    if c.bottom:
        "haven_blow_knees_pc_shorts"

    always:
        "haven_blow_knees_pc_wait"

    always:
        "haven_blow_knees_man"

    group mouth:
        attribute ah:
            "haven_blow_knees_pc_wait_ah"
        attribute neutral default:
            "haven_blow_knees_pc_wait_neutral"
        attribute ub:
            "haven_blow_knees_pc_wait_ub"
        attribute happy:
            "haven_blow_knees_pc_wait_happy"
    always:
        "haven_blow_frame"

layeredimage haven_blow cum:

    always:
        "haven_blow_bg"

    always:
        "haven_blow_knees_pc_base"
    always:
        "haven_blow_spank_knees_layer"
    if writing.chest:
        "haven_blow_writing_milk_knees_layer"

    if c.top:
        "haven_blow_knees_pc_top"
    if c.bottom:
        "haven_blow_knees_pc_shorts"

    always:
        "haven_blow_knees_pc_tounge"
    always:
        "haven_blow_knees_man"

    group eyes:
        attribute lookup:
            "haven_blow_knees_pc_tounge_lookup"
        attribute lookdown default:
            "haven_blow_knees_pc_tounge_lookdown"
    always:
        "haven_blow_frame"



layeredimage haven_blow ballsuck:

    always:
        "haven_blow_bg"

    always:
        "haven_blow_ballsuck_base"

    always:
        "haven_blow_spank_ballsuck_layer"
    if writing.chest:
        "haven_blow_writing_milk_ballsuck_layer"

    if c.top:
        "haven_blow_ballsuck_top"
    if c.bottom:
        "haven_blow_ballsuck_shorts"


    always:
        "haven_blow_frame"

layeredimage haven_blow ballrub:

    always:
        "haven_blow_bg"

    always:
        "haven_blow_ballrub_base"


    always:
        "haven_blow_spank_ballrub_layer"
    if writing.chest:
        "haven_blow_writing_milk_ballrub_layer"

    if c.top:
        "haven_blow_ballrub_top"
    if c.bottom:
        "haven_blow_ballrub_shorts"


    always:
        "haven_blow_frame"

layeredimage haven_blow 1h:

    always:
        "haven_blow_bg"

    always:
        "haven_blow_1h_base"

    always:
        "haven_blow_spank_1h_layer"
    if writing.chest:
        "haven_blow_writing_milk_1h_layer"

    if c.top:
        "haven_blow_1h_top"
    if c.bottom:
        "haven_blow_1h_shorts"

    always:
        "haven_blow_frame"

layeredimage haven_blow 2h:

    always:
        "haven_blow_bg"

    always:
        "haven_blow_2h_base"


    always:
        "haven_blow_spank_2h_layer"
    if writing.chest:
        "haven_blow_writing_milk_1h_layer"

    if c.top:
        "haven_blow_2h_top"
    if c.bottom:
        "haven_blow_2h_shorts"


    always:
        "haven_blow_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
