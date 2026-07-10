
image sb_standbehind_bg_room = "sb_standbehind_bg_plaster"
image sb_standbehind_bg_layer:
    "sb_standbehind_bg_" + loc_cur.loc_type


image sb_standbehind_pc_body_base_layer:
    "sb_standbehind_pc_body_base"
    skin_base_colour_transform()
image sb_standbehind_pc_body_shad_layer:
    "sb_standbehind_pc_body_shad"
    skin_shad_colour_transform()
image sb_standbehind_pc_body_nails_layer:
    "sb_standbehind_pc_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))


image sb_standbehind_pc_belly_base_2 = "sb_standbehind_pc_belly_base_3"
image sb_standbehind_pc_belly_shad_2 = "sb_standbehind_pc_belly_shad_3"
image sb_standbehind_pc_belly_base_layer:
    get_skin_filename("sb_standbehind_pc_belly_base", preg=True)
    skin_base_colour_transform()
image sb_standbehind_pc_belly_shad_layer:
    get_skin_filename("sb_standbehind_pc_belly_shad", preg=True)
    skin_shad_colour_transform()


image sb_standbehind_breasts_man_base_layer:
    get_skin_filename("sb_standbehind_breasts_man_base", breasts=True)
    npc_skin_base_colour_transform()
image sb_standbehind_breasts_man_shad_layer:
    get_skin_filename("sb_standbehind_breasts_man_shad", breasts=True)
    npc_skin_shad_colour_transform()
image sb_standbehind_breasts_pc_base_layer:
    get_skin_filename("sb_standbehind_breasts_pc_base", breasts=True)
    skin_base_colour_transform()
image sb_standbehind_breasts_pc_shad_layer:
    get_skin_filename("sb_standbehind_breasts_pc_shad", breasts=True)
    skin_shad_colour_transform()
image sb_standbehind_breasts_nips_layer:
    get_skin_filename("sb_standbehind_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_standbehind_breasts_nipring_layer:
    get_skin_filename("sb_standbehind_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_standbehind_breasts_tattoo_layer:
    get_skin_filename("sb_standbehind_breasts_tattoo", breasts=True)


image sb_standbehind_face_eyeshadow_layer:
    "sb_standbehind_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If(acc.eyeshadow and acc.makeup_on,0.6,0))
image sb_standbehind_face_blush_layer:
    "sb_standbehind_face_blush"
    blush_opacity_transform()
image sb_standbehind_face_freck_layer:
    "sb_standbehind_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))

image sb_standbehind_face_mouth_happy_lipstick_layer:
    "sb_standbehind_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_standbehind_face_mouth_ah_lipstick_layer:
    "sb_standbehind_face_mouth_ah_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_standbehind_face_mouth_oh_lipstick_layer:
    "sb_standbehind_face_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_standbehind_face_mouth_ag_lipstick_layer:
    "sb_standbehind_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_standbehind_face_mouth_gag_base_layer:
    "sb_standbehind_face_mouth_gag_base"
    gag_colour_transform()
image sb_standbehind_face_mouth_gag_metal_layer:
    "sb_standbehind_face_mouth_gag_metal"
    gag_metal_transform()
image sb_standbehind_face_mouth_gag_lipstick_layer:
    "sb_standbehind_face_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_standbehind_face_brow_slant_layer:
    "sb_standbehind_face_brow_slant"
    hair_colour_transform()
image sb_standbehind_face_brow_worried_layer:
    "sb_standbehind_face_brow_worried"
    hair_colour_transform()
image sb_standbehind_face_brow_angry_layer:
    "sb_standbehind_face_brow_angry"
    hair_colour_transform()
image sb_standbehind_face_brow_happy_layer:
    "sb_standbehind_face_brow_happy"
    hair_colour_transform()

image sb_standbehind_face_eye_back_iris_layer:
    "sb_standbehind_face_eye_back_iris"
    eye_colour_transform()
image sb_standbehind_face_eye_down_iris_layer:
    "sb_standbehind_face_eye_down_iris"
    eye_colour_transform()

image sb_standbehind_face_eye_back_eyeliner_layer:
    "sb_standbehind_face_eye_back_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_standbehind_face_eye_down_eyeliner_layer:
    "sb_standbehind_face_eye_down_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_standbehind_face_eye_closed_eyeliner_layer:
    "sb_standbehind_face_eye_closed_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")


image sb_standbehind_pc_hair_back_bun_2 = "sb_standbehind_pc_hair_back_bun"
image sb_standbehind_pc_hair_back_bun_3 = "sb_standbehind_pc_hair_back_bun"
image sb_standbehind_pc_hair_back_bun_4 = "sb_standbehind_pc_hair_back_bun"
image sb_standbehind_pc_hair_back_pony_4 = "sb_standbehind_pc_hair_back_pony_3"

image sb_standbehind_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_standbehind_hair_back")
    hair_colour_transform()

image sb_standbehind_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_standbehind_hair_front")
    hair_colour_transform()


image sb_standbehind_pc_writing_chest_layer:
    "sb_standbehind_pc_writing_chest"
    writing_transform("chest")
image sb_standbehind_pc_writing_belly_0_layer:
    "sb_standbehind_pc_writing_belly_0"
    writing_transform("belly")
image sb_standbehind_pc_writing_belly_1_layer:
    "sb_standbehind_pc_writing_belly_1"
    writing_transform("belly")
image sb_standbehind_pc_writing_pubic_layer:
    "sb_standbehind_pc_writing_pubic"
    writing_transform("pubic")
image sb_standbehind_pc_writing_face_layer:
    "sb_standbehind_pc_writing_face"
    writing_transform("face")
image sb_standbehind_pc_writing_forehead_layer:
    "sb_standbehind_pc_writing_forehead"
    writing_transform("forehead")


image sb_standbehind_man_base_layer:
    "sb_standbehind_man_base"
    npc_skin_base_colour_transform()
image sb_standbehind_man_shad_layer:
    "sb_standbehind_man_shad"
    npc_skin_shad_colour_transform()


image sb_standbehind_pc_outfit_pub_breasts_layer:
    get_skin_filename("sb_standbehind_pc_outfit_pub_breasts", breasts=True)

image sb_standbehind_effect_rain_loop:
    "sb_standbehind_effect_rain1"
    .03
    "sb_standbehind_effect_rain2"
    .03
    "sb_standbehind_effect_rain3"
    .03
    repeat

layeredimage sb_standbehind_shower_layered:
    always "sb_standbehind_effect_rain_loop"
    always "sb_standbehind_effect_steam"

layeredimage sb_standbehind_gag_layered:
    always "sb_standbehind_face_mouth_gag_lipstick_layer"
    always "sb_standbehind_face_mouth_gag_base_layer"
    always "sb_standbehind_face_mouth_gag_metal_layer"

layeredimage sb_standbehind:
    if not loc_cur == loc_pub:
        "sb_standbehind_bg_layer"
    else:
        "sb_standbehind_bg_pub"

    always "sb_standbehind_man_base_layer"
    always "sb_standbehind_man_shad_layer"

    always "sb_standbehind_pc_body_base_layer"
    always "sb_standbehind_pc_body_shad_layer"
    always "sb_standbehind_pc_body_nails_layer"

    if writing.pubic:
        "sb_standbehind_pc_writing_pubic_layer"

    if player.pregnancy:
        "sb_standbehind_pc_belly_base_layer"
    if player.pregnancy:
        "sb_standbehind_pc_belly_shad_layer"
    always "sb_standbehind_breasts_pc_base_layer"
    always "sb_standbehind_breasts_pc_shad_layer"
    always "sb_standbehind_breasts_nips_layer"
    always "sb_standbehind_breasts_man_base_layer"
    always "sb_standbehind_breasts_man_shad_layer"

    if acc.nipring:
        "sb_standbehind_breasts_nipring_layer"
    if tattoo.chest:
        "sb_standbehind_breasts_tattoo_layer"

    if writing.chest:
        "sb_standbehind_pc_writing_chest_layer"
    if writing.belly and player.pregnancy == 1:
        "sb_standbehind_pc_writing_belly_1_layer"
    elif writing.belly and player.pregnancy == 0:
        "sb_standbehind_pc_writing_belly_0_layer"

    if writing.forehead:
        "sb_standbehind_pc_writing_forehead_layer"
    if writing.face:
        "sb_standbehind_pc_writing_face_layer"

    always "sb_standbehind_face_eyeshadow_layer"
    always "sb_standbehind_face_blush_layer"
    always "sb_standbehind_face_freck_layer"

    if c.outfit == 6:
        "sb_standbehind_pc_outfit_pub_breasts_layer"
    if c.outfit == 6:
        "sb_standbehind_pc_outfit_pub_base"
    if c.outfit == 6 and player.showing:
        "sb_standbehind_pc_outfit_pub_belly_3"

    group face:
        attribute oh default "sb_standbehind_face_brow_slant_layer"
        attribute oh default "sb_standbehind_face_mouth_oh_lipstick_layer"
        attribute oh default "sb_standbehind_face_mouth_oh"

        attribute ah "sb_standbehind_face_brow_worried_layer"
        attribute ah "sb_standbehind_face_mouth_ah_lipstick_layer"
        attribute ah "sb_standbehind_face_mouth_ah"

        attribute ag "sb_standbehind_face_brow_worried_layer"
        attribute ag "sb_standbehind_face_mouth_ag_lipstick_layer"
        attribute ag "sb_standbehind_face_mouth_ag"

        attribute happy "sb_standbehind_face_brow_happy_layer"
        attribute happy "sb_standbehind_face_mouth_happy_lipstick_layer"
        attribute happy "sb_standbehind_face_mouth_happy"

    if player.gagged:
        "sb_standbehind_gag_layered"

    always "sb_standbehind_face_eye_back_iris_layer"
    always "sb_standbehind_face_eye_back_eye"
    always "sb_standbehind_face_eye_back_eyeliner_layer"

    if player.blind:
        "sb_standbehind_face_blind"

    always "sb_standbehind_pc_hair_back_layer"
    always "sb_standbehind_pc_hair_front_layer"

    if "shower" in loc_cur.name:
        "sb_standbehind_shower_layered"

    always "sb_standbehind_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
