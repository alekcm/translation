image dance_upskirt_bg_layer:
    "dance_upskirt_bg"
    desire_colour_transform()

image dance_upskirt_body_base_layer:
    "dance_upskirt_body_base"
    skin_base_colour_transform()
image dance_upskirt_body_shad_layer:
    "dance_upskirt_body_shad"
    skin_shad_colour_transform()
image dance_upskirt_body_shadskirt_layer:
    "dance_upskirt_body_shadskirt"
    skin_shad_colour_transform()

image dance_upskirt_pants1_layer:
    "dance_upskirt_pants1"
    pants_primary_colour_transform()
image dance_upskirt_pants2_layer:
    "dance_upskirt_pants2"
    pants_primary_colour_transform()

image dance_upskirt_tights_layer:
    "dance_upskirt_tights"
    socks_primary_colour_transform()

image dance_upskirt_skirt_layer:
    "dance_upskirt_skirt"
    socks_primary_colour_transform()


layeredimage dance_upskirt:

    always:
        "dance_upskirt_bg_layer"

    always:
        "dance_upskirt_body_base_layer"

    if c.bottom > 0:
        "dance_upskirt_body_shadskirt_layer"

    always:
        "dance_upskirt_body_shad_layer"


    if c.pants > 0 and c.thong:
        "dance_upskirt_pants2_layer"
    elif c.pants > 0:
        "dance_upskirt_pants1_layer"

    if c.socks > 0:
        "dance_upskirt_tights_layer"

    if c.bottom > 0:
        "dance_upskirt_skirt_layer"

    always:
        "dance_upskirt_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
