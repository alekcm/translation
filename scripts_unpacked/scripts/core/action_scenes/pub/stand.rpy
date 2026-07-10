image pub_stand_pc_body_base_layer:
    "pub_stand_pc_body_base"
    skin_base_colour_transform()
image pub_stand_pc_body_shad_layer:
    "pub_stand_pc_body_shad"
    skin_shad_colour_transform()

image pub_stand_pc_rarm_down_layer:
    "pub_stand_pc_rarm_down"
    skin_shad_colour_transform()
image pub_stand_pc_rarm_beer_layer:
    "pub_stand_pc_rarm_beer"
    skin_shad_colour_transform()

image pub_stand_pc_larm_beer_base_layer:
    "pub_stand_pc_larm_beer_base"
    skin_base_colour_transform()
image pub_stand_pc_larm_beer_shad_layer:
    "pub_stand_pc_larm_beer_shad"
    skin_shad_colour_transform()
image pub_stand_pc_larm_down_base_layer:
    "pub_stand_pc_larm_down_base"
    skin_base_colour_transform()
image pub_stand_pc_larm_down_shad_layer:
    "pub_stand_pc_larm_down_shad"
    skin_shad_colour_transform()

image pub_stand_pc_breasts_col_layer:
    get_skin_filename("pub_stand_pc_breasts_col", breasts=True)
image pub_stand_pc_breasts_base_layer:
    get_skin_filename("pub_stand_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image pub_stand_pc_breasts_shad_layer:
    get_skin_filename("pub_stand_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image pub_stand_pc_writing_chest_layer:
    "pub_stand_pc_writing_chest"
    writing_transform("chest")


image pub_stand_man_hold_base_layer:
    "pub_stand_man_hold_base"
    npc_skin_base_colour_transform()
image pub_stand_man_hold_shad_layer:
    "pub_stand_man_hold_shad"
    npc_skin_shad_colour_transform()

image pub_stand_man_mast_base_layer:
    "pub_stand_man_mast_base"
    npc_skin_base_colour_transform()
image pub_stand_man_mast_shad_layer:
    "pub_stand_man_mast_shad"
    npc_skin_shad_colour_transform()

image pub_stand = LayeredImageProxy("pub_stand_layered", Transform(align=(0.75, 0.0)))

layeredimage pub_stand_layered:

    always:
        "pub_stand_bg"

    if player.right_hand == "beer":
        "pub_stand_pc_rarm_beer_layer"

    else:
        "pub_stand_pc_rarm_down_layer"

    always:
        "pub_stand_pc_body_base_layer"
    always:
        "pub_stand_pc_body_shad_layer"
    always:
        "pub_stand_pc_dress"
    if player.pregnancy >= 2:
        "pub_stand_pc_belly"

    always:
        "pub_stand_pc_breasts_base_layer"
    always:
        "pub_stand_pc_breasts_shad_layer"
    if writing.chest:
        "pub_stand_pc_writing_chest_layer"
    always:
        "pub_stand_pc_breasts_col_layer"

    group man:
        attribute hold default:
            "pub_stand_man_hold_base_layer"
        attribute hold default:
            "pub_stand_man_hold_shad_layer"
        attribute hold default:
            "pub_stand_man_hold_col"

        attribute mast:
            "pub_stand_man_mast_base_layer"
        attribute mast:
            "pub_stand_man_mast_shad_layer"
        attribute mast:
            "pub_stand_man_mast_col"

    if player.left_hand == "beer":
        "pub_stand_pc_larm_beer_base_layer"
    else:
        "pub_stand_pc_larm_down_base_layer"
    if player.left_hand == "beer":
        "pub_stand_pc_larm_beer_shad_layer"
    else:
        "pub_stand_pc_larm_down_shad_layer"
    if player.left_hand == "beer":
        "pub_stand_pc_larm_beer_col"

    always:
        "pub_stand_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
