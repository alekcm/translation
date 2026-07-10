image pub_serving_clevage_pc_body_base_layer:
    "pub_serving_clevage_pc_body_base"
    skin_base_colour_transform()
image pub_serving_clevage_pc_body_shad_layer:
    "pub_serving_clevage_pc_body_shad"
    skin_shad_colour_transform()

image pub_serving_clevage_pc_dress_breasts_layer:
    get_skin_filename("pub_serving_clevage_pc_dress_breasts", breasts=True)
image pub_serving_clevage_pc_dress_breasts_tattoo_layer:
    get_skin_filename("pub_serving_clevage_pc_dress_breasts_tattoo", breasts=True)
image pub_serving_clevage_pc_dress_breasts_shad_layer:
    get_skin_filename("pub_serving_clevage_pc_dress_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image pub_serving_clevage_pc_writing_chest_layer:
    "pub_serving_clevage_pc_writing_chest"
    writing_transform("chest")

image pub_serving_clevage_man_grope_layer:
    "pub_serving_clevage_man_grope"
    npc_skin_shad_colour_transform()

image pub_serve_clevage = LayeredImageProxy("pub_serve_clevage_layered", Transform(align=(0.9, 0.0)))

layeredimage pub_serve_clevage_layered:

    always:
        "pub_serving_clevage_bg"

    group groper:
        attribute grope:
            "pub_serving_clevage_man_grope_layer"
        attribute nogrope default:
            null

    always:
        "pub_serving_clevage_pc_body_base_layer"
    always:
        "pub_serving_clevage_pc_body_shad_layer"

    if c.socks:
        "pub_serving_clevage_pc_socks"
    always:
        "pub_serving_clevage_pc_dress"
    if player.pregnancy >= 2:
        "pub_serving_clevage_pc_dress_belly"
    always:
        "pub_serving_clevage_pc_dress_breasts_shad_layer"
    if tattoo.chest:
        "pub_serving_clevage_pc_dress_breasts_tattoo_layer"
    if writing.chest:
        "pub_serving_clevage_pc_writing_chest_layer"
    always:
        "pub_serving_clevage_pc_dress_breasts_layer"

    always:
        "pub_serving_clevage_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
