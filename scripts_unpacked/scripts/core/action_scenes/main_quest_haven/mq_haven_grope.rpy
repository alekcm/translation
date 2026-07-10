image haven_grope_pc_spank_layer:
    "haven_grope_pc_spank"
    opacity_transform(bruise.ass)

image haven_grope_pc_writing_belly_layer:
    "haven_grope_pc_writing_belly"
    writing_transform("belly")
image haven_grope_pc_writing_pubic_layer:
    "haven_grope_pc_writing_pubic"
    writing_transform("pubic")
image haven_grope_pc_writing_milk_layer:
    "haven_grope_pc_writing_milk"
    writing_transform("chest")
image haven_grope_pc_writing_whore_avoid_layer:
    "haven_grope_pc_writing_whore_avoid"
    writing_transform("forehead")
image haven_grope_pc_writing_whore_look_layer:
    "haven_grope_pc_writing_whore_look"
    writing_transform("forehead")
image haven_grope_pc_writing_slut_avoid_layer:
    "haven_grope_pc_writing_slut_avoid"
    writing_transform("face")
image haven_grope_pc_writing_slut_look_layer:
    "haven_grope_pc_writing_slut_look"
    writing_transform("face")

layeredimage haven_grope:

    always:
        "haven_grope_base"
    always:
        "haven_grope_pc_spank_layer"
    if writing.belly:
        "haven_grope_pc_writing_belly_layer"
    if writing.pubic:
        "haven_grope_pc_writing_pubic_layer"
    if writing.chest:
        "haven_grope_pc_writing_milk_layer"


    if c.bottom:
        "haven_grope_pc_shorts"

    group head:
        attribute forward default:
            "haven_grope_pc_head_look"
        attribute avoid:
            "haven_grope_pc_head_avoid"
    group face:
        attribute neutral default if_all "forward":
            "haven_grope_pc_face_look_neutral"
        attribute neutral default if_all "avoid":
            "haven_grope_pc_face_avoid_neutral"

        attribute happy if_all "forward":
            "haven_grope_pc_face_look_happy"
        attribute happy if_all "avoid":
            "haven_grope_pc_face_avoid_happy"

        attribute down if_all "forward":
            "haven_grope_pc_face_look_down"
        attribute down if_all "avoid":
            "haven_grope_pc_face_avoid_down"

        attribute stern if_all "forward":
            "haven_grope_pc_face_look_stern"
        attribute stern if_all "avoid":
            "haven_grope_pc_face_avoid_stern"

    if writing.forehead:
        if_any "forward" "haven_grope_pc_writing_whore_look_layer"
    if writing.forehead:
        if_any "avoid" "haven_grope_pc_writing_whore_avoid_layer"

    if writing.face:
        if_any "forward" "haven_grope_pc_writing_slut_look_layer"
    if writing.face:
        if_any "avoid" "haven_grope_pc_writing_slut_avoid_layer"


    group hair:
        attribute forward:
            "haven_grope_pc_hair_look"
        attribute avoid:
            "haven_grope_pc_hair_avoid"

    group manarm:
        attribute waist default:
            "haven_grope_man_arm_waist"
        attribute grope:
            "haven_grope_man_arm_grope"

    group penis:
        attribute nopenis default:
            null
        attribute penis:
            "haven_grope_man_penis"

    if c.top:
        if_any "waist" "haven_grope_pc_top"
    if c.top:
        if_any "grope" "haven_grope_pc_topgrope"

    group arm:
        attribute up default:
            "haven_grope_pc_arm_up"
        attribute mast:
            "haven_grope_pc_arm_mast"
        attribute hold:
            "haven_grope_pc_arm_hold"

    if c.top:
        if_any "mast" "haven_grope_pc_top_mast"
    if c.top:
        if_any "hold" "haven_grope_pc_top_hold"
    if c.top:
        if_any "up" "haven_grope_pc_top_up"






    always:
        "haven_grope_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
