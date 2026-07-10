image dance_front_bg_layer:
    "dance_front_bg"
    desire_colour_transform()

image dance_front_body_base_layer:
    "dance_front_body_base"
    skin_base_colour_transform()
image dance_front_body_shad_layer:
    "dance_front_body_shad"
    skin_shad_colour_transform()
image dance_front_body_shad_top2_layer:
    "dance_front_body_shad_top2"
    skin_shad_colour_transform()
image dance_front_body_shad_skirt_layer:
    "dance_front_body_shad_skirt"
    skin_shad_colour_transform()
image dance_front_body_shad_hair_layer:
    "dance_front_body_shad_hair" + str(player.hair_fringe)
    skin_shad_colour_transform()

image dance_front_body_nips_layer:
    "dance_front_body_nips"
    nipple_colour_transform()
image dance_front_body_phair_layer:
    "dance_front_body_phair"
    phair_colour_transform()

image dance_front_hair_front_layer:
    "dance_front_hair_front_" + str(player.hair_fringe)
    hair_colour_transform()
image dance_front_hair_back_layer:
    "dance_front_hair_back"
    hair_colour_transform()
image dance_front_brow_happy_layer:
    "dance_front_brow_happy"
    hair_colour_transform()

image dance_front_eye_iris_layer:
    "dance_front_eye_iris"
    eye_colour_transform()
image dance_front_eye_eyeliner_layer:
    "dance_front_eye_eyeliner" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image dance_front_makeup_eyeshadow_layer:
    "dance_front_makeup_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", 0.8)
image dance_front_makeup_lipstick_layer:
    "dance_front_makeup_lipstick"
    accessories_primary_colour_transform("lipstick")
image dance_front_makeup_nails_layer:
    "dance_front_makeup_nails"
    accessories_primary_colour_transform("nails")

image dance_front_pants1_layer:
    "dance_front_pants1"
    pants_primary_colour_transform()
image dance_front_pants2_layer:
    "dance_front_pants2"
    pants_primary_colour_transform()
image dance_front_top1_layer:
    "dance_front_top1"
    top_primary_colour_transform()
image dance_front_top2_layer:
    "dance_front_top2"
    top_primary_colour_transform()
image dance_front_skirt_layer:
    "dance_front_skirt"
    bottom_primary_colour_transform()
image dance_front_tights_layer:
    "dance_front_tights"
    socks_primary_colour_transform()

layeredimage dance_front:

    group dani: 
        attribute dani default:
            "dance_front_bg_layer"
    always:
        "dance_front_dani_body"

    if c.socks:
        "dance_front_dani_tights"

    if c.top == 19:
        "dance_front_dani_top2"
    elif c.top == 20:
        "dance_front_dani_top1"

    if c.bottom == 13:
        "dance_front_dani_skirt"

    group dani: 
        attribute nodani:
            "dance_front_bg_layer"


    always:
        "dance_front_body_base_layer"

    always:
        "dance_front_body_nips_layer"
    always:
        "dance_front_body_mouth"

    if c.bottom == 13:
        "dance_front_body_shad_skirt_layer"
    if c.top == 19:
        "dance_front_body_shad_top2_layer"
    always:
        "dance_front_body_shad_hair_layer"

    always:
        "dance_front_body_shad_layer"

    if player.phair > 0:
        "dance_front_body_phair_layer"

    always:
        "dance_front_hair_back_layer"

    if acc.eyeshadow and acc.makeup_on:
        "dance_front_makeup_eyeshadow_layer"
    if acc.nails:
        "dance_front_makeup_nails_layer"
    if acc.lipstick and acc.makeup_on:
        "dance_front_makeup_lipstick_layer"


    always:
        "dance_front_brow_happy_layer"

    always:
        "dance_front_eye_iris_layer"
    always:
        "dance_front_eye_eye"
    always:
        "dance_front_eye_eyeliner_layer"


    always:
        "dance_front_hair_front_layer"

    if c.pants and c.thong:
        "dance_front_pants2_layer"
    elif c.pants:
        "dance_front_pants1_layer"

    if c.socks:
        "dance_front_tights_layer"

    if c.top == 19:
        "dance_front_top2_layer"
    elif c.top == 20:
        "dance_front_top1_layer"

    if c.bottom == 13:
        "dance_front_skirt_layer"


    always:
        "dance_front_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
