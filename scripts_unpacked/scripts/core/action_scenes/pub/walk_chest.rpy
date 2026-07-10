image pub_walking_chest_body_base_layer:
    "pub_walking_chest_body_base"
    skin_base_colour_transform()
image pub_walking_chest_body_shad_layer:
    "pub_walking_chest_body_shad"
    skin_shad_colour_transform()

image pub_walking_chest_breasts_dress_layer:
    get_skin_filename("pub_walking_chest_breasts_dress", breasts=True)
image pub_walking_chest_breasts_tattoo_layer:
    get_skin_filename("pub_walking_chest_breasts_tattoo", breasts=True)
image pub_walking_chest_breasts_shad_layer:
    get_skin_filename("pub_walking_chest_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image pub_walking_chest_writing_chest_layer:
    "pub_walking_chest_writing_chest"
    writing_transform("chest")

image pub_walk_chest = LayeredImageProxy("pub_walk_chest_layered", Transform(align=(0.6, 0.0)))

layeredimage pub_walk_chest_layered:

    always:
        "pub_walking_chest_bg"

    always:
        "pub_walking_chest_body_base_layer"
    always:
        "pub_walking_chest_body_shad_layer"
    always:
        "pub_walking_chest_dress"
    if player.pregnancy >= 2:
        "pub_walking_chest_belly"

    always:
        "pub_walking_chest_breasts_shad_layer"
    if tattoo.chest:
        "pub_walking_chest_breasts_tattoo_layer"
    if writing.chest:
        "pub_walking_chest_writing_chest_layer"
    always:
        "pub_walking_chest_breasts_dress_layer"

    always:
        "pub_walking_chest_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
