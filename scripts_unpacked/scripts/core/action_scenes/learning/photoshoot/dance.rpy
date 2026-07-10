image ps_dance_body_base_layer:
    "ps_dance_body_base"
    skin_base_colour_transform()
image ps_dance_body_shad_layer:
    "ps_dance_body_shad"
    skin_shad_colour_transform()
image ps_dance_body_shad_skirt_layer:
    "ps_dance_body_shad_skirt"
    skin_shad_colour_transform()

image ps_dance_body_phair_layer:
    "ps_dance_body_phair"
    phair_colour_transform()
image ps_dance_body_navring_layer:
    get_skin_filename("ps_dance_body_navring", False)
    accessories_secondary_colour_transform("navelring")

image ps_dance_breasts_base_layer:
    get_skin_filename("ps_dance_breasts_base", breasts=True)
    skin_base_colour_transform()
image ps_dance_breasts_shad_layer:
    get_skin_filename("ps_dance_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image ps_dance_breasts_nips_layer:
    get_skin_filename("ps_dance_breasts_nips", breasts=True)
    nipple_colour_transform()
image ps_dance_breasts_nipring_layer:
    get_skin_filename("ps_dance_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image ps_dance_breasts_tattoo_layer:
    get_skin_filename("ps_dance_breasts_tattoo", breasts=True)

image ps_dance_belly_base_layer:
    "ps_dance_belly_base"
    skin_base_colour_transform()
image ps_dance_belly_shad_layer:
    "ps_dance_belly_shad"
    skin_shad_colour_transform()

image ps_dance_armdown_base_layer:
    "ps_dance_armdown_base"
    skin_base_colour_transform()
image ps_dance_armdown_shad_layer:
    "ps_dance_armdown_shad"
    skin_shad_colour_transform()
image ps_dance_armup_base_layer:
    "ps_dance_armup_base"
    skin_base_colour_transform()
image ps_dance_armup_shad_layer:
    "ps_dance_armup_shad"
    skin_shad_colour_transform()

image ps_dance_writing_chest_layer:
    "ps_dance_writing_chest"
    writing_transform("chest")
image ps_dance_writing_belly_layer:
    "ps_dance_writing_belly_0"
    writing_transform("belly")
image ps_dance_writing_belly_preg_layer:
    "ps_dance_writing_belly_3"
    writing_transform("belly")
image ps_dance_writing_pubic_layer:
    "ps_dance_writing_pubic"
    writing_transform("pubic")
image ps_dance_writing_face_layer:
    "ps_dance_writing_face"
    writing_transform("face")
image ps_dance_writing_forehead_layer:
    "ps_dance_writing_forehead"
    writing_transform("forehead")
image ps_dance_writing_lleg_layer:
    "ps_dance_writing_lleg"
    writing_transform("lleg")

image ps_dance_face_eyeshad_layer:
    "ps_dance_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", 0.8)
image ps_dance_face_mouth_happy_lipstick_layer:
    "ps_dance_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_dance_face_mouth_vhappy_lipstick_layer:
    "ps_dance_face_mouth_vhappy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_dance_face_mouth_ag_lipstick_layer:
    "ps_dance_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_dance_face_mouth_pout_lipstick_layer:
    "ps_dance_face_mouth_pout_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))
image ps_dance_face_mouth_tounge_lipstick_layer:
    "ps_dance_face_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on,1,0))


image ps_dance_hair_front_layer:
    "ps_dance_hair_front_" + str(player.hair_fringe)
    hair_colour_transform()

image ps_dance_hair_back_3 = "ps_dance_hair_back_2"
image ps_dance_hair_back_4 = "ps_dance_hair_back_2"

image ps_dance_hair_back_layer:
    "ps_dance_hair_back_" + str(player.hair_neck)
    hair_colour_transform()
image ps_dance_face_brow_straight_layer:
    "ps_dance_face_brow_straight"
    hair_colour_transform()
image ps_dance_face_brow_worried_layer:
    "ps_dance_face_brow_worried"
    hair_colour_transform()
image ps_dance_face_brow_cheeky_layer:
    "ps_dance_face_brow_cheeky"
    hair_colour_transform()

image ps_dance_face_eyeliner_layer:
    "ps_dance_face_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image ps_dance_face_eye_iris_layer:
    "ps_dance_face_eye_iris"
    eye_colour_transform()

image ps_dance_pants_small_layer:
    "ps_dance_pants_small"
    pants_primary_colour_transform()
image ps_dance_pants_big_layer:
    "ps_dance_pants_big"
    pants_primary_colour_transform()
image ps_dance_pants_big_preg_layer:
    "ps_dance_pants_big_preg"
    pants_primary_colour_transform()

image ps_dance_top_crop_layer:
    "ps_dance_top_crop_" + str(player.breasts)
    top_primary_colour_transform()

image ps_dance_top_knot_layer:
    "ps_dance_top_knot"
    top_primary_colour_transform()
image ps_dance_top_knot_preg_layer:
    "ps_dance_top_knot_preg"
    top_primary_colour_transform()
image ps_dance_top_knot_preg_front_layer:
    "ps_dance_top_knot_preg_front"
    top_primary_colour_transform()
image ps_dance_top_knot_breasts_layer:
    "ps_dance_top_knot_breasts_" + str(player.breasts)
    top_primary_colour_transform()

image ps_dance_skirt_layer:
    "ps_dance_skirt"
    bottom_primary_colour_transform()
image ps_dance_skirt_preg_layer:
    "ps_dance_skirt_preg"
    bottom_primary_colour_transform()

image ps_dance_tights_layer:
    "ps_dance_tights"
    socks_primary_colour_transform()

layeredimage ps_dance:

    if loc(loc_school_gym):
        "ps_dance_bg_gym"
    else:
        "ps_dance_bg"

    always "ps_dance_hair_back_layer"

    always "ps_dance_body_base_layer"
    if c.bottom:
        "ps_dance_body_shad_skirt_layer"
    always "ps_dance_body_shad_layer"

    if player.phair:
        "ps_dance_body_phair_layer"
    if acc.navelring:
        "ps_dance_body_navring_layer"

    if writing.chest:
        "ps_dance_writing_chest_layer"
    if writing.belly and player.pregnancy >= 2:
        "ps_dance_writing_belly_layer"
    elif writing.belly:
        "ps_dance_writing_belly_layer"
    if writing.pubic:
        "ps_dance_writing_pubic_layer"
    if writing.face:
        "ps_dance_writing_face_layer"
    if writing.forehead:
        "ps_dance_writing_forehead_layer"
    if writing.lleg:
        "ps_dance_writing_lleg_layer"

    if not c.top == 20:
        "ps_dance_breasts"

    if player.pregnancy >= 2:
        "ps_dance_belly_base_layer"
    if player.pregnancy >= 2:
        "ps_dance_belly_shad_layer"

    if c.top == 19:
        "ps_dance_top_crop_layer"

    group arms:
        attribute armdown default "ps_dance_armdown_base_layer"
        attribute armdown default "ps_dance_armdown_shad_layer"

        attribute armup "ps_dance_armup_base_layer"
        attribute armup "ps_dance_armup_shad_layer"

    if acc.eyeshadow and acc.makeup_on:
        "ps_dance_face_eyeshad_layer"


    group mouth:
        attribute happy default "ps_dance_face_mouth_happy_lipstick_layer"
        attribute happy default "ps_dance_face_mouth_happy"

        attribute ag "ps_dance_face_mouth_ag_lipstick_layer"
        attribute ag "ps_dance_face_mouth_ag"

        attribute vhappy "ps_dance_face_mouth_vhappy_lipstick_layer"
        attribute vhappy "ps_dance_face_mouth_vhappy"

        attribute pout "ps_dance_face_mouth_pout_lipstick_layer"
        attribute pout "ps_dance_face_mouth_pout"

        attribute tounge "ps_dance_face_mouth_tounge_lipstick_layer"
        attribute tounge "ps_dance_face_mouth_tounge"

    always "ps_dance_face_eye_iris_layer"
    always "ps_dance_face_eye_eye"
    always "ps_dance_face_eyeliner_layer"

    group brows:
        attribute straight default "ps_dance_face_brow_straight_layer"
        attribute worried "ps_dance_face_brow_worried_layer"
        attribute cheeky "ps_dance_face_brow_cheeky_layer"


    always "ps_dance_hair_front_layer"


    if c.thong:
        "ps_dance_pants_small_layer"
    elif c.pants and player.pregnancy >= 2:
        "ps_dance_pants_big_preg_layer"
    elif c.pants:
        "ps_dance_pants_big_layer"

    if c.socks:
        "ps_dance_tights_layer"

    if c.bottom and player.pregnancy >= 2:
        "ps_dance_skirt_preg_layer"
    elif c.bottom:
        "ps_dance_skirt_layer"
    if c.top == 20:
        "ps_dance_top_knot_layerd"

    always "ps_dance_frame"

layeredimage ps_dance_breasts:
    always "ps_dance_breasts_base_layer"
    always "ps_dance_breasts_shad_layer"
    always "ps_dance_breasts_nips_layer"
    if tattoo.chest:
        "ps_dance_breasts_tattoo_layer"
    if acc.nipring:
        "ps_dance_breasts_nipring_layer"

layeredimage ps_dance_top_knot_layerd:
    if player.pregnancy >= 2:
        "ps_dance_top_knot_preg_layer"
    else:
        "ps_dance_top_knot_layer"
    always "ps_dance_top_knot_breasts_layer"
    if player.pregnancy >= 2:
        "ps_dance_top_knot_preg_front_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
