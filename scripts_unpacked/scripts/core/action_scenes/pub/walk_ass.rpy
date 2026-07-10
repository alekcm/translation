image pub_walking_skirt_body_base_layer:
    "pub_walking_skirt_body_base"
    skin_base_colour_transform()
image pub_walking_skirt_body_shad_layer:
    "pub_walking_skirt_body_shad"
    skin_shad_colour_transform()
image pub_walking_skirt_body_vag_layer:
    "pub_walking_skirt_body_vag"
    vagina_colour_transform()

image pub_walk_ass = LayeredImageProxy("pub_walk_ass_layered", Transform(align=(0.6, 0.0)))

layeredimage pub_walk_ass_layered:

    always:
        "pub_walking_skirt_bg"

    always:
        "pub_walking_skirt_body_base_layer"
    always:
        "pub_walking_skirt_body_shad_layer"
    always:
        "pub_walking_skirt_body_vag_layer"
    if acc.anus:
        "pub_walking_skirt_plug"
    if c.pants:
        "pub_walking_skirt_pants"
    if c.socks:
        "pub_walking_skirt_socks"
    always:
        "pub_walking_skirt_dress"
    if player.pregnancy >= 2:
        "pub_walking_skirt_belly"

    always:
        "pub_walking_skirt_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
